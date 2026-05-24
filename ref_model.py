"""
ref_model.py — MLP del árbitro virtual
Predice si un foul recibe tarjeta amarilla a partir de 5 features:
  - velocidad del impacto (1..10)
  - fue por la pelota (0 / 1)
  - zona de la cancha (0=propia, 1=medio, 2=rival)
  - minuto del partido (1..90)
  - diferencia en el marcador (-3..+3)

Reutiliza la implementación MLP genérica de mlp.py.
"""

import numpy as np
from mlp import MLP


# ---------------------------------------------------------------
# Datos sintéticos
# ---------------------------------------------------------------
def generar_fouls(n: int = 800, seed: int = 7) -> tuple:
    """
    Genera fouls sintéticos con una regla "verdadera" + ruido.
    P(amarilla) sube con velocidad alta, contacto sin pelota,
    zona rival, minuto avanzado y estar perdiendo.
    """
    rng = np.random.default_rng(seed)
    vel    = rng.integers(1, 11, n)                # 1..10
    ball   = rng.integers(0, 2, n)                 # 0 o 1
    zona   = rng.integers(0, 3, n)                 # 0, 1, 2
    minuto = rng.integers(1, 91, n)                # 1..90
    score  = rng.integers(-3, 4, n)                # -3..3

    # Reglas blandas (ground truth probabilístico)
    logits = (
        -3.0
        + 0.55 * vel
        + np.where(ball == 1, -1.2, 1.0)
        + (zona - 1) * 1.0
        + 0.018 * minuto
        + 0.25 * (-score)
    )
    proba = 1.0 / (1.0 + np.exp(-logits))
    amarilla = (rng.uniform(0, 1, n) < proba).astype(float)
    return vel, ball, zona, minuto, score, amarilla


def normalizar(vel, ball, zona, minuto, score) -> np.ndarray:
    """
    Normaliza las features al rango ~[0, 1] (zona y score centrados en 0).
    """
    return np.column_stack([
        np.asarray(vel)    / 10.0,
        np.asarray(ball).astype(float),
        np.asarray(zona)   / 2.0,
        np.asarray(minuto) / 90.0,
        (np.asarray(score) + 3.0) / 6.0,
    ])


# ---------------------------------------------------------------
# Construcción / entrenamiento rápido
# ---------------------------------------------------------------
def entrenar_modelo_arbitro(epochs: int = 2000, lr: float = 0.05) -> MLP:
    """
    Entrena un MLP 5-32-16-1 con mini-batch SGD sobre los datos sintéticos.
    Devuelve la red lista para usar.
    """
    vel, ball, zona, minuto, score, amarilla = generar_fouls(1000)
    X = normalizar(vel, ball, zona, minuto, score)
    net = MLP([5, 32, 16, 1], lr=lr, seed=11)
    for _ in range(epochs):
        net.train_epoch(X, amarilla, batch_size=64)
    return net


def predecir(net: MLP, vel: int, ball: bool, zona: str,
             minuto: int, score: int) -> float:
    """
    Convierte inputs humanos a vector normalizado y devuelve P(amarilla).
    """
    zona_idx = {"propia": 0, "medio": 1, "rival": 2}[zona]
    X = normalizar([vel], [1 if ball else 0], [zona_idx], [minuto], [score])
    return float(net.predict_proba(X)[0])


def factor_dominante(vel: int, ball: bool, zona: str,
                     minuto: int, score: int) -> str:
    """
    Explicación heurística — qué variable empujó más la decisión hacia la amarilla.
    """
    z = {"propia": 0.0, "medio": 0.2, "rival": 0.7}[zona]
    factores = [
        ("la velocidad del impacto",   vel / 10.0),
        ("el contacto sin la pelota",  0.0 if ball else 0.6),
        ("la zona donde ocurrió",      z),
        ("el minuto del partido",      minuto / 90.0 * 0.5),
        ("estar perdiendo",            max(0.0, -score / 3.0) * 0.6),
    ]
    factores.sort(key=lambda x: x[1], reverse=True)
    return factores[0][0]
