"""
lineup_model.py — MLP para predecir Titular o Suplente.
6 features: goles_p90 (0-1.5), asistencias_p90 (0-1.0),
            pases_pct (50-100), minutos (0-270),
            condicion (1-10), edad (17-38)
"""
import numpy as np
from mlp import MLP


def generar_jugadores(n: int = 1000, seed: int = 99) -> tuple:
    rng = np.random.default_rng(seed)
    goals   = rng.uniform(0.0, 1.5, n)
    assists = rng.uniform(0.0, 1.0, n)
    pct     = rng.uniform(50.0, 100.0, n)
    mins    = rng.uniform(0.0, 270.0, n)
    cond    = rng.uniform(1.0, 10.0, n)
    edad    = rng.uniform(17.0, 38.0, n)

    # Strict AND-style criteria: ALL thresholds must be met to qualify as titular.
    # Scoring 6/6 criteria = strongly titular; fewer = suplente.
    ok_goals   = (goals   > 0.4).astype(float)
    ok_assists = (assists  > 0.3).astype(float)
    ok_pct     = (pct      > 72.0).astype(float)
    ok_mins    = (mins     > 160.0).astype(float)
    ok_cond    = (cond     > 6.0).astype(float)
    ok_age     = ((edad >= 22.0) & (edad <= 32.0)).astype(float)
    n_ok = ok_goals + ok_assists + ok_pct + ok_mins + ok_cond + ok_age

    # Need 5-6 criteria for a positive logit; < 4 → firmly suplente
    logits  = -12.0 + 2.5 * n_ok + rng.normal(0, 0.25, n)
    proba   = 1.0 / (1.0 + np.exp(-logits))
    titular = (rng.uniform(0, 1, n) < proba).astype(float)
    return goals, assists, pct, mins, cond, edad, titular


def normalizar(goals, assists, pct, mins, cond, edad) -> np.ndarray:
    return np.column_stack([
        np.asarray(goals)   / 1.5,
        np.asarray(assists) / 1.0,
        (np.asarray(pct) - 50.0) / 50.0,
        np.asarray(mins)    / 270.0,
        (np.asarray(cond) - 1.0) / 9.0,
        (np.asarray(edad) - 17.0) / 21.0,
    ])


def entrenar_modelo_lineup(epochs: int = 2000, lr: float = 0.03) -> MLP:
    g, a, p, m, c, e, tit = generar_jugadores(1000)
    X   = normalizar(g, a, p, m, c, e)
    net = MLP([6, 32, 16, 1], lr=lr, seed=42)
    for _ in range(epochs):
        net.train_epoch(X, tit, batch_size=64)
    return net


def predecir_lineup(net: MLP, goals: float, assists: float, pct: float,
                    mins: float, cond: float, edad: float) -> float:
    X = normalizar([goals], [assists], [pct], [mins], [cond], [edad])
    return float(net.predict_proba(X)[0])


def factor_lineup(goals: float, assists: float, pct: float,
                  mins: float, cond: float, edad: float) -> str:
    scores = [
        ("los goles por 90 min",               goals / 1.5),
        ("las asistencias",                    assists / 1.0),
        ("la precisión de pases",              (pct - 50) / 50),
        ("los minutos jugados últimamente",    mins / 270),
        ("la condición física",                (cond - 1) / 9),
        ("la edad (pico 22-32 años)",          max(0.0, 1 - abs(edad - 27) / 10)),
    ]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]
