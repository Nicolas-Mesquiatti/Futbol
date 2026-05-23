"""
mlp.py — MLP para clasificación binaria
Implementado desde cero con NumPy. Sin scikit-learn ni frameworks de ML.

Entrada: 2 números (distancia al arco, ángulo del tiro)
Salida:  1 número entre 0 y 1 (probabilidad de gol)
"""

import numpy as np


class MLP:
    """
    Perceptrón Multicapa para clasificación binaria.

    - Capas ocultas:   activación tanh
    - Capa de salida:  activación sigmoid  → salida entre 0 y 1
    - Pérdida:         Binary Cross-Entropy (BCE)
    - Optimizador:     Descenso por gradiente (SGD)
    - Inicialización:  Xavier/Glorot
    """

    def __init__(self, layer_sizes: list, lr: float = 0.05, seed: int = 42):
        """
        layer_sizes: tamaño de cada capa, ej. [2, 16, 16, 1]
                     primer elemento = nº features, último = 1 (salida binaria)
        """
        self.layer_sizes = layer_sizes
        self.lr = lr
        self.loss_history: list = []
        self.acc_history: list = []
        self._init_weights(seed)

    # ------------------------------------------------------------------
    # Inicialización
    # ------------------------------------------------------------------
    def _init_weights(self, seed: int):
        """Xavier: scale = sqrt(2 / (n_in + n_out)). Evita gradientes que explotan."""
        rng = np.random.default_rng(seed)
        self.W, self.b = [], []
        for i in range(len(self.layer_sizes) - 1):
            n_in, n_out = self.layer_sizes[i], self.layer_sizes[i + 1]
            self.W.append(rng.standard_normal((n_in, n_out)) * np.sqrt(2 / (n_in + n_out)))
            self.b.append(np.zeros((1, n_out)))

    # ------------------------------------------------------------------
    # Funciones de activación
    # ------------------------------------------------------------------
    @staticmethod
    def _sigmoid(z):
        return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

    @staticmethod
    def _tanh(z):
        return np.tanh(z)

    @staticmethod
    def _tanh_d(z):
        return 1.0 - np.tanh(z) ** 2

    # ------------------------------------------------------------------
    # Forward pass
    # ------------------------------------------------------------------
    def forward(self, X: np.ndarray) -> np.ndarray:
        """
        Propaga X hacia adelante.
        Capas ocultas: tanh  |  Capa final: sigmoid
        """
        self._a = [X]
        self._z = []
        a = X
        for i, (W, b) in enumerate(zip(self.W, self.b)):
            z = a @ W + b
            self._z.append(z)
            a = self._sigmoid(z) if i == len(self.W) - 1 else self._tanh(z)
            self._a.append(a)
        return self._a[-1]

    # ------------------------------------------------------------------
    # Backward pass
    # ------------------------------------------------------------------
    def backward(self, y: np.ndarray):
        """
        Backpropagation con BCE + sigmoid:
        El gradiente inicial es simplemente (ŷ - y) / m
        (la cancelación matemática entre BCE' y sigmoid' da esta forma limpia)
        """
        m = y.shape[0]
        delta = (self._a[-1] - y.reshape(-1, 1)) / m
        for i in reversed(range(len(self.W))):
            dW = self._a[i].T @ delta
            db = delta.sum(axis=0, keepdims=True)
            if i > 0:
                delta = (delta @ self.W[i].T) * self._tanh_d(self._z[i - 1])
            self.W[i] -= self.lr * dW
            self.b[i] -= self.lr * db

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------
    def train_step(self, X: np.ndarray, y: np.ndarray) -> float:
        """Un epoch de entrenamiento. Retorna la pérdida BCE."""
        self.forward(X)
        self.backward(y)
        proba = self.predict_proba(X)
        eps = 1e-9
        loss = float(-np.mean(y * np.log(proba + eps) + (1 - y) * np.log(1 - proba + eps)))
        acc = float(np.mean((proba >= 0.5).astype(int) == y))
        self.loss_history.append(loss)
        self.acc_history.append(acc)
        return loss

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Probabilidad de gol para cada tiro (valor entre 0 y 1)."""
        return self.forward(X).flatten()

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """Clasificación binaria: 1 = gol predicho, 0 = no gol."""
        return (self.predict_proba(X) >= threshold).astype(int)

    def accuracy(self, X: np.ndarray, y: np.ndarray) -> float:
        return float(np.mean(self.predict(X) == y))

    def total_params(self) -> int:
        return sum(W.size + b.size for W, b in zip(self.W, self.b))

    def reset(self, seed: int = 42):
        self.loss_history, self.acc_history = [], []
        self._init_weights(seed)
