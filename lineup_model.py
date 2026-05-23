"""
lineup_model.py — MLP para predecir Titular o Suplente.
6 features: goles_p90 (0-1.5), asistencias_p90 (0-1.0),
            pases_pct (50-100), minutos (0-270),
            condicion (1-10), edad (17-38)
"""
import numpy as np
from mlp import MLP


def generar_jugadores(n: int = 800, seed: int = 99) -> tuple:
    rng = np.random.default_rng(seed)
    goals   = rng.uniform(0.0, 1.5, n)
    assists = rng.uniform(0.0, 1.0, n)
    pct     = rng.uniform(50.0, 100.0, n)
    mins    = rng.uniform(0.0, 270.0, n)
    cond    = rng.uniform(1.0, 10.0, n)
    edad    = rng.uniform(17.0, 38.0, n)

    # Ground-truth logit: more goals/assists/mins/fitness → starter
    logits = (
        -1.8
        + 3.0  * goals
        + 2.0  * assists
        + 0.04 * (pct - 70)
        + 0.012 * mins
        + 0.30  * cond
        - 0.06  * np.abs(edad - 26)   # peak age 26
    )
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


def entrenar_modelo_lineup(epochs: int = 2000, lr: float = 0.06) -> MLP:
    g, a, p, m, c, e, tit = generar_jugadores(800)
    X   = normalizar(g, a, p, m, c, e)
    net = MLP([6, 16, 10, 1], lr=lr, seed=42)
    for _ in range(epochs):
        net.train_step(X, tit)
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
        ("la edad (pico ~26 años)",            max(0.0, 1 - abs(edad - 26) / 10)),
    ]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]
