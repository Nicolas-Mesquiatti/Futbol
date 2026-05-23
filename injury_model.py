"""
injury_model.py — MLP para predecir riesgo de lesión muscular.
5 features: minutos_ultimos3 (0-270), dias_desde_lesion (0-365),
            edad (17-38), intensidad_entreno (1-10), partidos_ultimos30 (0-12)
"""
import numpy as np
from mlp import MLP


def generar_lesiones(n: int = 800, seed: int = 77) -> tuple:
    rng = np.random.default_rng(seed)
    minutos  = rng.uniform(0.0, 270.0, n)
    dias     = rng.uniform(0.0, 365.0, n)
    edad     = rng.uniform(17.0, 38.0, n)
    inten    = rng.uniform(1.0, 10.0, n)
    partidos = rng.uniform(0.0, 12.0, n)

    # Realistic injury logic:
    # - More minutes → fatigue → higher risk
    # - Fewer days since last injury → still recovering → higher risk
    # - Older age (peaks above 30) → higher risk
    # - Higher training intensity → higher risk
    # - More matches in 30 days → overload → higher risk
    logits = (
        -2.8
        + 0.010 * minutos
        - 0.004 * dias
        + 0.085 * (edad - 24)
        + 0.28  * inten
        + 0.22  * partidos
    )
    proba  = 1.0 / (1.0 + np.exp(-logits))
    lesion = (rng.uniform(0, 1, n) < proba).astype(float)
    return minutos, dias, edad, inten, partidos, lesion


def normalizar(minutos, dias, edad, inten, partidos) -> np.ndarray:
    return np.column_stack([
        np.asarray(minutos)  / 270.0,
        np.asarray(dias)     / 365.0,
        (np.asarray(edad) - 17.0) / 21.0,
        (np.asarray(inten) - 1.0) / 9.0,
        np.asarray(partidos) / 12.0,
    ])


def entrenar_modelo_injury(epochs: int = 2000, lr: float = 0.06) -> MLP:
    m, d, e, i, p, l = generar_lesiones(800)
    X   = normalizar(m, d, e, i, p)
    net = MLP([5, 16, 10, 1], lr=lr, seed=77)
    for _ in range(epochs):
        net.train_step(X, l)
    return net


def predecir_lesion(net: MLP, minutos: float, dias: float, edad: float,
                    inten: float, partidos: float) -> float:
    X = normalizar([minutos], [dias], [edad], [inten], [partidos])
    return float(net.predict_proba(X)[0])


def factor_lesion(minutos: float, dias: float, edad: float,
                  inten: float, partidos: float) -> str:
    scores = [
        ("los minutos acumulados en los últimos 3 partidos", minutos / 270),
        ("el poco tiempo desde la última lesión",            1.0 - min(dias, 365) / 365),
        ("la edad del jugador",                              max(0.0, (edad - 24) / 14)),
        ("la intensidad de entrenamiento",                   (inten - 1) / 9),
        ("los partidos jugados en los últimos 30 días",      partidos / 12),
    ]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0]
