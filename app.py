"""
app.py — xG/Lab · "¿Puede la IA entender el fútbol?"
TP Integrador — Introducción a las Redes Neuronales — Opción B: MLP
"""

import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from mlp import MLP
import ref_model
import styles
import lineup_model
import injury_model


# ===================================================================
# CONFIG
# ===================================================================
st.set_page_config(
    page_title="xG/Lab · ¿Puede la IA entender el fútbol?",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)
styles.inject_css()


# ===================================================================
# COLORES
# ===================================================================
BG     = "#0F1923"
TEXT_1 = "#FFFFFF"
TEXT_2 = "#8A9BB0"
ACC_G  = "#00D4AA"
ACC_Y  = "#FFD700"
ACC_R  = "#FF4655"
BORDER = "rgba(255,255,255,0.08)"

PLOTLY_DARK = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="JetBrains Mono, monospace", size=12, color=TEXT_2),
    xaxis=dict(gridcolor="rgba(255,255,255,0.05)", zerolinecolor="rgba(255,255,255,0.08)"),
    yaxis=dict(gridcolor="rgba(255,255,255,0.05)", zerolinecolor="rgba(255,255,255,0.08)"),
    margin=dict(l=40, r=20, t=40, b=40),
)


# ===================================================================
# DATOS SINTÉTICOS
# ===================================================================
@st.cache_data
def generar_tiros(n: int = 600, seed: int = 42) -> tuple:
    rng = np.random.default_rng(seed)
    distancia = rng.uniform(4, 36, n)
    angulo    = rng.uniform(3, 87, n)
    # Tuned formula → ~22-25% goals (≈130-140 out of 600); close shots reach >50% xG
    raw = 1.25 * np.exp(-distancia / 11.5) * (angulo / 90.0) ** 0.30
    xg  = np.clip(raw, 0.04, 0.92)
    gol = (rng.uniform(0, 1, n) < xg).astype(float)
    return distancia, angulo, gol, xg


# ===================================================================
# CANCHA
# ===================================================================
def cancha_base(height: int = 420) -> go.Figure:
    fig = go.Figure()
    fig.add_shape(type="rect", x0=0, y0=0, x1=52.5, y1=68,
                  fillcolor=BG, line=dict(color="rgba(255,255,255,0.18)", width=1.2))
    fig.add_shape(type="rect", x0=0, y0=13.84, x1=16.5, y1=54.16,
                  line=dict(color="rgba(255,255,255,0.25)", width=1.2),
                  fillcolor="rgba(0,0,0,0)")
    fig.add_shape(type="rect", x0=0, y0=24.84, x1=5.5, y1=43.16,
                  line=dict(color="rgba(255,255,255,0.3)", width=1.2),
                  fillcolor="rgba(0,0,0,0)")
    fig.add_shape(type="rect", x0=-1.5, y0=30.34, x1=0, y1=37.66,
                  line=dict(color="rgba(255,255,255,0.5)", width=2),
                  fillcolor="rgba(255,255,255,0.12)")
    fig.add_trace(go.Scatter(x=[11], y=[34], mode="markers",
                             marker=dict(color="rgba(255,255,255,0.6)", size=5),
                             showlegend=False, hoverinfo="skip"))
    theta = np.linspace(np.radians(-53), np.radians(53), 60)
    arc_x = 11 + 9.15 * np.cos(theta)
    arc_y = 34 + 9.15 * np.sin(theta)
    mask = arc_x > 16.5
    fig.add_trace(go.Scatter(x=arc_x[mask], y=arc_y[mask], mode="lines",
                             line=dict(color="rgba(255,255,255,0.25)", width=1.2),
                             showlegend=False, hoverinfo="skip"))
    fig.update_layout(
        xaxis=dict(range=[-3, 54], visible=False, scaleanchor="y"),
        yaxis=dict(range=[-2, 70], visible=False),
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False, height=height,
    )
    return fig


def tiros_a_xy(distancia, angulo):
    x = distancia * np.cos(np.radians(90 - angulo * 0.4))
    y = 34 + (angulo - 45) * distancia * 0.012
    return np.clip(x, 0.5, 52), np.clip(y, 1, 67)


def heatmap_xg(mlp: MLP, height: int = 440) -> go.Figure:
    fig = cancha_base(height=height)
    xs = np.linspace(1, 50, 80)
    ys = np.linspace(2, 66, 60)
    XX, YY = np.meshgrid(xs, ys)
    dist_grid = np.clip(np.sqrt(XX**2 + (YY - 34)**2), 4, 36)
    ang_grid  = np.clip(np.degrees(np.arctan2(XX, np.abs(YY - 34) + 0.1)), 3, 87)
    X_grid = np.column_stack([dist_grid.flatten() / 36.0, ang_grid.flatten() / 90.0])
    proba = mlp.predict_proba(X_grid).reshape(XX.shape)
    fig.add_trace(go.Contour(
        x=xs, y=ys, z=proba,
        colorscale=[
            [0.0,  "rgba(255,70,85,0.00)"],
            [0.15, "rgba(255,70,85,0.35)"],
            [0.35, "rgba(255,215,0,0.30)"],
            [0.55, "rgba(0,212,170,0.40)"],
            [1.0,  "rgba(0,212,170,0.65)"],
        ],
        contours=dict(start=0, end=1, size=0.08, showlines=False, coloring="heatmap"),
        showscale=True,
        colorbar=dict(
            title=dict(text="P(gol)", font=dict(color=TEXT_2, family="JetBrains Mono")),
            tickfont=dict(color=TEXT_2, family="JetBrains Mono", size=10),
            len=0.55, x=1.02, thickness=10, outlinewidth=0, tickformat=".0%",
        ),
        hovertemplate="P(gol): %{z:.1%}<extra></extra>",
    ))
    return fig


def scatter_tiros(distancia, angulo, gol, height: int = 500) -> go.Figure:
    fig = cancha_base(height=height)
    x_g,  y_g  = tiros_a_xy(distancia[gol == 1], angulo[gol == 1])
    x_ng, y_ng = tiros_a_xy(distancia[gol == 0], angulo[gol == 0])
    fig.add_trace(go.Scatter(
        x=x_ng, y=y_ng, mode="markers", name="No gol",
        marker=dict(color="rgba(255,70,85,0.55)", size=6, symbol="x"),
    ))
    fig.add_trace(go.Scatter(
        x=x_g, y=y_g, mode="markers", name="Gol ⚽",
        marker=dict(color="rgba(0,212,170,0.9)", size=8,
                    line=dict(color="white", width=1)),
    ))
    fig.update_layout(showlegend=True, legend=dict(
        bgcolor="rgba(0,0,0,0.4)", bordercolor=BORDER, borderwidth=1,
        font=dict(color=TEXT_1, family="Inter"),
        x=0.02, y=0.98,
    ))
    return fig


# ===================================================================
# GLOSARIO
# ===================================================================
GLOSARIO = [
    dict(name="Expected Goals", sym="xG",
         definicion="Probabilidad de que un tiro entre. xG = 0.30 significa que ese tiro entraría 3 de cada 10 veces.",
         formula="xG ≈ f(distancia, ángulo, presión, …)",
         bajo="xG < 0.05 → tiro muy difícil, desde lejos o ángulo cerrado.",
         alto="xG > 0.50 → situación de gol claro, mano a mano o pelota parada.",
         analogia="Como el pronóstico del clima: \"30% de chance de lluvia\" no garantiza lluvia, pero informa la decisión.",
         tip="Un jugador que mete más goles que su xG es clínico. Uno que mete menos, desperdicia chances."),
    dict(name="Neurona", sym="n_j",
         definicion="Una mini-decisión que combina sus inputs con pesos, los suma, y aplica una función no lineal.",
         formula="a_j = σ( Σ w_ij · x_i + b_j )",
         bajo="Si todas las neuronas son lineales, la red se reduce a una sola línea.",
         alto="Demasiadas neuronas → la red memoriza los datos (overfitting).",
         analogia="Como un panel de jueces deportivos: cada uno opina con un peso distinto y se promedia la decisión.",
         tip="Empezá con 8–16 neuronas por capa. Subí solo si la red no aprende."),
    dict(name="Peso", sym="w_ij",
         definicion="Cuánto le importa a una neurona el valor que viene de otra. Es lo único que la red ajusta.",
         formula="w ← w − α · ∂L/∂w",
         bajo="Pesos cercanos a 0 → esa conexión no aporta.",
         alto="Pesos enormes → la red está confiada de más, suele sobreajustar.",
         analogia="Como el volumen de cada parlante en una consola: la red los gira hasta que el mix suena bien.",
         tip="Inicializá los pesos con Xavier/Glorot. Evita gradientes que explotan o desaparecen."),
    dict(name="Sesgo", sym="b_j",
         definicion="Número que se suma a la salida de la neurona antes de la activación. Le da libertad para correr la curva.",
         formula="z_j = Σ w_ij · x_i + b_j",
         bajo="Sin sesgo, todas las neuronas pasan por el origen.",
         alto="Sesgo dominante → la neurona ignora sus inputs.",
         analogia="Como el handicap en el golf: te ajusta el punto de partida antes de empezar el hoyo.",
         tip="Inicializalo en 0. Se aprende solo con el gradiente."),
    dict(name="Tasa de aprendizaje", sym="α",
         definicion="Controla cuánto ajustan los pesos en cada paso. Si es muy alta, la red oscila y no aprende.",
         formula="w ← w − α · ∂L/∂w",
         bajo="Converge muy lento. Necesita muchos epochs.",
         alto="Los pesos oscilan o explotan. La pérdida sube en lugar de bajar.",
         analogia="Como ajustar un volumen: giros chicos y tardás, giros grandes y te pasás.",
         tip="Empezá con 0.05. Si la pérdida oscila, bajala a 0.01."),
    dict(name="Epoch", sym="e",
         definicion="Una pasada completa por todos los tiros del dataset de entrenamiento.",
         formula="epoch e → actualiza pesos con todos los tiros",
         bajo="Pocos epochs → underfitting: la red no aprendió suficiente.",
         alto="Demasiados epochs → overfitting: memoriza casos en lugar de patrones.",
         analogia="Como ver partidos para aprender: con 5 sabés algo, con 10.000 sos un experto.",
         tip="Mirá la curva de pérdida. Cuando se aplana, seguir entrenando no ayuda."),
    dict(name="Backpropagation", sym="∂L/∂w",
         definicion="Algoritmo que calcula cuánto contribuyó cada peso al error final y los ajusta proporcionalmente.",
         formula="δˡ = (Wˡ⁺¹)ᵀ · δˡ⁺¹ ⊙ σ′(zˡ)",
         bajo="Vanishing gradient → las primeras capas no aprenden.",
         alto="Exploding gradient → los pesos divergen, la pérdida sube.",
         analogia="Como revisar la jugada del gol al revés: ¿dónde empezó el error? Cada uno recibe su cuota de culpa.",
         tip="Si los gradientes desaparecen, probá inicialización Xavier y activación tanh."),
    dict(name="Sigmoid", sym="σ(z)",
         definicion="Aplasta cualquier número entre 0 y 1. Perfecta para la última capa de un clasificador binario.",
         formula="σ(z) = 1 / (1 + e⁻ᶻ)",
         bajo="σ(−5) ≈ 0.007 → casi cero probabilidad.",
         alto="σ(+5) ≈ 0.993 → casi certeza.",
         analogia="El traductor a porcentaje: convierte cualquier puntaje en algo legible.",
         tip="Usá sigmoid solo en la última capa. En capas ocultas preferí tanh o ReLU."),
    dict(name="Binary Cross-Entropy", sym="L",
         definicion="Función de pérdida para clasificación binaria. Penaliza más cuando la red está segura y se equivoca.",
         formula="L = −[ y·log(ŷ) + (1−y)·log(1−ŷ) ]",
         bajo="L ≈ 0 → predicciones muy acertadas.",
         alto="L > 1 → la red está muy equivocada y confiada.",
         analogia="Penalizás más a un periodista que dijo \"99% gana Argentina\" y perdió.",
         tip="Para regresión usá MSE. Para clasificación binaria usá BCE."),
    dict(name="Accuracy", sym="acc",
         definicion="Porcentaje de tiros clasificados correctamente por la red.",
         formula="acc = tiros correctos / total de tiros",
         bajo="acc < 60% → peor que tirar una moneda. La red no aprendió.",
         alto="acc > 80% → la red clasifica bien. En fútbol ~75–80% es excelente.",
         analogia="Si un analista predice bien 8 de cada 10 tiros, tiene 80% de accuracy.",
         tip="El accuracy puede ser engañoso si hay desbalance de clases. Mirá también la pérdida BCE."),
]


# ===================================================================
# ESTADO
# ===================================================================
def _init_state():
    for k, v in dict(mlp_xg=None, epoch_xg=0, x_train=None, y_train=None,
                     x_val=None, y_val=None, net_ref=None, net_lineup=None,
                     net_injury=None).items():
        if k not in st.session_state:
            st.session_state[k] = v
_init_state()

dist_all, ang_all, gol_all, xg_all = generar_tiros(600)


# ===================================================================
# HERO
# ===================================================================
st.markdown(styles.hero(n_tiros=600, target_acc=78), unsafe_allow_html=True)
# Inject scroll+tab JS functions into parent window via isolated iframe
components.html(styles.hero_js(), height=0)


# ===================================================================
# TABS
# ===================================================================
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Cómo funciona", "Los datos", "Entrenar la red",
    "Simulador xG", "Árbitro IA", "Titular o Suplente", "¿Se lesiona?", "Glosario",
])


# ----------------------------------------------------------------
# TAB 1 — CÓMO FUNCIONA
# ----------------------------------------------------------------
with tab1:
    st.markdown(styles.section_head(
        kicker="01 · Fundamentos",
        title="Una red neuronal, en 4 pasos.",
        lead="Olvidate del jerga. Una red neuronal es una máquina que mira ejemplos, "
             "adivina, se equivoca, y se corrige. Una y otra vez. Hasta que adivina bien."
    ), unsafe_allow_html=True)

    st.markdown(styles.steps_explainer(), unsafe_allow_html=True)

    st.markdown(styles.section_head(
        kicker="02 · El problema",
        title="¿Qué es xG?",
        lead="Los clubes de élite usan redes neuronales para evaluar la calidad de cada "
             "tiro. A ese número se le llama Expected Goals."
    ), unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown("""
En el fútbol moderno, cada tiro tiene una **probabilidad de ser gol**.
A ese número se le llama **Expected Goals (xG)**.

- Un tiro desde **5 m, frente al arco** tiene xG ≈ 0.70 (70% de chance)
- Un tiro desde **30 m, en diagonal** tiene xG ≈ 0.03 (3% de chance)

Los clubes lo usan para:
- Evaluar si un delantero es clínico o desperdicia chances.
- Decidir si un gol fue suerte o mérito real.
- Comparar jugadores de distintas ligas.

**¿Cómo se construye?** Con una red neuronal entrenada con miles de tiros
históricos donde se sabe el resultado. Exactamente lo que vas a hacer acá.

> 🔑 La red aprende que ciertos *patrones* (cerca + buen ángulo) son más
> peligrosos que otros, **sin que nadie le explique las reglas del fútbol**.
        """)
    with c2:
        st.markdown("**Tabla de referencia xG**")
        st.dataframe(pd.DataFrame({
            "Situación": ["Penal (11 m)", "Mano a mano (6 m)", "Cabezazo área chica",
                          "Remate lejano (25 m)", "Tiro lejano (35 m)", "Ángulo cerrado"],
            "xG típico": ["0.79", "0.65", "0.40", "0.12", "0.04", "0.02"],
            "Interpretación": ["Muy probable", "Probable", "Moderado",
                               "Difícil", "Muy difícil", "Casi imposible"],
        }), use_container_width=True, hide_index=True)


# ----------------------------------------------------------------
# TAB 2 — LOS DATOS  (stats bar + full-width pitch)
# ----------------------------------------------------------------
with tab2:
    st.markdown(styles.section_head(
        kicker="03 · Dataset",
        title="600 tiros sintéticos.",
        lead="Características basadas en estadísticas reales de Premier League "
             "y Champions League. Cada tiro tiene distancia + ángulo + resultado."
    ), unsafe_allow_html=True)

    n_goles = int(gol_all.sum())
    n_total  = len(gol_all)

    # Big numbers stats bar
    st.markdown(styles.dataset_stats(n_total, n_goles), unsafe_allow_html=True)

    # Full-width pitch scatter
    fig_sc = scatter_tiros(dist_all, ang_all, gol_all, height=520)
    fig_sc.update_layout(
        title=dict(text="Distribución de tiros en la cancha",
                   font=dict(color=TEXT_1, family="Outfit", size=16))
    )
    st.plotly_chart(fig_sc, use_container_width=True)

    # Feature notes
    col_a, col_b, col_c = st.columns(3)
    col_a.markdown("**Entrada 1** `distancia` · metros al arco (4–36 m)")
    col_b.markdown("**Entrada 2** `angulo` · grados del tiro (3–87°)")
    col_c.markdown("**Salida** `gol` · 1 si entró, 0 si no")

    st.markdown("---")
    st.markdown("### Distribución de las variables")
    fig_h = make_subplots(rows=1, cols=3,
                          subplot_titles=("Distancia (m)", "Ángulo (°)", "xG verdadero"))
    fig_h.add_trace(go.Histogram(x=dist_all, nbinsx=25, marker_color=ACC_G,
                                 marker_line_color=BG, marker_line_width=1), row=1, col=1)
    fig_h.add_trace(go.Histogram(x=ang_all, nbinsx=25, marker_color=ACC_Y,
                                 marker_line_color=BG, marker_line_width=1), row=1, col=2)
    fig_h.add_trace(go.Histogram(x=xg_all, nbinsx=25, marker_color=ACC_R,
                                 marker_line_color=BG, marker_line_width=1), row=1, col=3)
    fig_h.update_layout(showlegend=False, height=260, **PLOTLY_DARK)
    for i in range(1, 4):
        fig_h.update_xaxes(gridcolor="rgba(255,255,255,0.05)", row=1, col=i)
        fig_h.update_yaxes(gridcolor="rgba(255,255,255,0.05)", row=1, col=i)
    st.plotly_chart(fig_h, use_container_width=True)


# ----------------------------------------------------------------
# TAB 3 — ENTRENAR LA RED  (+ NN diagram + progress bar)
# ----------------------------------------------------------------
with tab3:
    st.markdown(styles.section_head(
        kicker="04 · Módulo",
        title="Entrenamiento en vivo.",
        lead="Mirá cómo la red aprende. Cada epoch es una pasada por los 600 tiros, "
             "y los pesos se ajustan con backpropagation."
    ), unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        lr = st.select_slider("Tasa de aprendizaje (α)",
                              options=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5],
                              value=0.05, format_func=lambda x: f"{x}")
        n_ocultas = st.slider("Capas ocultas", 1, 4, 2)
    with c2:
        n_neu = st.slider("Neuronas por capa", 4, 64, 16)
        epochs_step = st.select_slider("Epochs por paso",
                                       options=[50, 100, 250, 500, 1000], value=250)
    with c3:
        train_pct = st.slider("% datos para entrenamiento", 60, 90, 80)
        st.caption(f"Entrenamiento: **{int(600 * train_pct/100)}** tiros · "
                   f"Validación: **{int(600 * (1-train_pct/100))}** tiros")

    arch = [2] + [n_neu] * n_ocultas + [1]
    n_params = sum(arch[i]*arch[i+1] + arch[i+1] for i in range(len(arch)-1))
    st.markdown(f"**Arquitectura:** `{' → '.join(map(str, arch))}` · **{n_params}** parámetros")

    # Neural network diagram (always visible)
    is_trained = st.session_state.mlp_xg is not None and st.session_state.epoch_xg > 0
    st.markdown(styles.nn_diagram(arch, is_training=is_trained), unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("🔄 Inicializar red", use_container_width=True):
            idx = int(600 * train_pct / 100)
            X = np.column_stack([dist_all / 36.0, ang_all / 90.0])
            st.session_state.x_train  = X[:idx]
            st.session_state.y_train  = gol_all[:idx]
            st.session_state.x_val    = X[idx:]
            st.session_state.y_val    = gol_all[idx:]
            st.session_state.mlp_xg   = MLP(arch, lr=lr)
            st.session_state.epoch_xg = 0
            st.rerun()
    with b2:
        if st.button(f"▶ Entrenar {epochs_step} epochs", use_container_width=True):
            if st.session_state.mlp_xg is None:
                st.warning("Primero inicializá la red.")
            else:
                for _ in range(epochs_step):
                    st.session_state.mlp_xg.train_step(
                        st.session_state.x_train, st.session_state.y_train)
                st.session_state.epoch_xg += epochs_step
                st.rerun()
    with b3:
        if st.button("🚀 Entrenar hasta 3000", use_container_width=True):
            if st.session_state.mlp_xg is None:
                st.warning("Primero inicializá la red.")
            else:
                faltan = max(0, 3000 - st.session_state.epoch_xg)
                for _ in range(faltan):
                    st.session_state.mlp_xg.train_step(
                        st.session_state.x_train, st.session_state.y_train)
                st.session_state.epoch_xg += faltan
                st.rerun()

    st.markdown("---")

    if st.session_state.mlp_xg is not None:
        mlp = st.session_state.mlp_xg
        Xv, yv = st.session_state.x_val, st.session_state.y_val
        acc_t = mlp.acc_history[-1]  if mlp.acc_history else 0
        acc_v = mlp.accuracy(Xv, yv)
        loss  = mlp.loss_history[-1] if mlp.loss_history else 1

        # Epoch progress bar
        progress = min(1.0, st.session_state.epoch_xg / 3000)
        st.progress(progress,
                    text=f"Progreso: **{st.session_state.epoch_xg:,} / 3000** epochs "
                         f"({progress:.0%})")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Epoch",          f"{st.session_state.epoch_xg:,}")
        m2.metric("Pérdida (BCE)",  f"{loss:.4f}")
        m3.metric("Accuracy entr.", f"{acc_t:.1%}")
        m4.metric("Accuracy valid.", f"{acc_v:.1%}")

        cA, cB = st.columns([3, 2])
        with cA:
            fig_hm = heatmap_xg(mlp, height=440)
            xp_g,  yp_g  = tiros_a_xy(dist_all[gol_all == 1], ang_all[gol_all == 1])
            xp_ng, yp_ng = tiros_a_xy(dist_all[gol_all == 0], ang_all[gol_all == 0])
            fig_hm.add_trace(go.Scatter(x=xp_ng[:80], y=yp_ng[:80], mode="markers",
                                        marker=dict(color="rgba(255,70,85,0.45)", size=5, symbol="x"),
                                        showlegend=False, hoverinfo="skip"))
            fig_hm.add_trace(go.Scatter(x=xp_g[:80], y=yp_g[:80], mode="markers",
                                        marker=dict(color="rgba(0,212,170,0.95)", size=7,
                                                    line=dict(color="white", width=1)),
                                        showlegend=False, hoverinfo="skip"))
            fig_hm.update_layout(title=dict(text="Mapa de peligro · P(gol) por zona",
                                            font=dict(color=TEXT_1, family="Outfit", size=16)))
            st.plotly_chart(fig_hm, use_container_width=True)

        with cB:
            # Loss curve — green + spline for smooth look
            fig_l = go.Figure()
            fig_l.add_trace(go.Scatter(
                y=mlp.loss_history, mode="lines",
                line=dict(color=ACC_G, width=2, shape="spline", smoothing=1.1),
                fill="tozeroy", fillcolor="rgba(0,212,170,0.08)",
            ))
            fig_l.update_layout(
                title=dict(text="Curva de pérdida (BCE)",
                           font=dict(color=TEXT_1, family="Outfit", size=14)),
                height=215, **PLOTLY_DARK,
            )
            st.plotly_chart(fig_l, use_container_width=True)

            # Accuracy curve
            fig_a = go.Figure()
            fig_a.add_trace(go.Scatter(
                y=mlp.acc_history, mode="lines",
                line=dict(color=ACC_Y, width=2, shape="spline", smoothing=1.1),
                fill="tozeroy", fillcolor="rgba(255,215,0,0.08)",
            ))
            fig_a.update_layout(
                title=dict(text="Accuracy por epoch",
                           font=dict(color=TEXT_1, family="Outfit", size=14)),
                yaxis=dict(range=[0, 1], gridcolor="rgba(255,255,255,0.05)"),
                height=215,
                **{k: v for k, v in PLOTLY_DARK.items() if k != "yaxis"},
            )
            st.plotly_chart(fig_a, use_container_width=True)

        if acc_v >= 0.75:
            st.success(f"✅ La red predice bien: **{acc_v:.1%}** de los tiros clasificados correctamente.")
        elif acc_v >= 0.65:
            st.info(f"📊 La red está aprendiendo: **{acc_v:.1%}** de accuracy. Seguí entrenando.")
        else:
            st.warning("⚠️ La red todavía no aprendió bien. Probá más epochs o ajustá la arquitectura.")
    else:
        st.info("👆 Hacé clic en **🔄 Inicializar red** para empezar.")


# ----------------------------------------------------------------
# TAB 4 — SIMULADOR xG  (pitch LEFT, controls RIGHT)
# ----------------------------------------------------------------
with tab4:
    st.markdown(styles.section_head(
        kicker="05 · Módulo",
        title="¿Es gol?",
        lead="Movés la pelota por la cancha. La red, ya entrenada, te dice "
             "qué probabilidad hay de que termine adentro."
    ), unsafe_allow_html=True)

    if st.session_state.mlp_xg is None:
        st.warning("⚠️ Primero entrenás la red en la pestaña **Entrenar la red**.")
    else:
        mlp = st.session_state.mlp_xg

        # Layout: pitch LEFT (wider), controls RIGHT
        c_pitch, c_ctrl = st.columns([3, 2])

        with c_ctrl:
            st.markdown("#### Configurá tu tiro")
            dist_sim = st.slider("📏 Distancia al arco (m)", 4, 36, 12)
            ang_sim  = st.slider("📐 Ángulo del tiro (°)", 5, 85, 45,
                                 help="90° = de frente · 5° = ángulo muy cerrado")

            X_sim = np.array([[dist_sim / 36.0, ang_sim / 90.0]])
            proba = float(mlp.predict_proba(X_sim)[0])

            st.markdown(styles.result_box(proba), unsafe_allow_html=True)
            st.markdown("")
            if proba > 0.5:
                st.success("⚽ **¡Tirá! Es una buena chance.**")
            elif proba > 0.25:
                st.warning("🤔 **Chance moderada — depende de la presión.**")
            else:
                st.error("🔴 **Chance baja — buscá mejor posición.**")

            # Goal celebration animation
            st.markdown(styles.goal_celebration(proba), unsafe_allow_html=True)

        with c_pitch:
            fig_sim = heatmap_xg(mlp, height=500)
            x_t, y_t = tiros_a_xy(np.array([dist_sim]), np.array([ang_sim]))
            cx, cy = float(x_t[0]), float(y_t[0])

            # Green glowing dot — layered circles for glow effect
            for sz, alpha in [(54, 0.07), (38, 0.14), (24, 0.28)]:
                fig_sim.add_trace(go.Scatter(
                    x=[cx], y=[cy], mode="markers",
                    marker=dict(color=f"rgba(0,212,170,{alpha})", size=sz, symbol="circle"),
                    showlegend=False, hoverinfo="skip",
                ))
            fig_sim.add_trace(go.Scatter(
                x=[cx], y=[cy], mode="markers+text",
                marker=dict(color=ACC_G, size=13, symbol="circle",
                            line=dict(color="white", width=2.5)),
                text=[f" {dist_sim}m · {ang_sim}°"],
                textposition="middle right",
                textfont=dict(color=TEXT_1, size=12, family="JetBrains Mono"),
                showlegend=False,
                hovertemplate=f"Distancia: {dist_sim} m<br>Ángulo: {ang_sim}°<br>xG: {proba:.1%}<extra></extra>",
            ))
            fig_sim.update_layout(title=dict(text="Tu posición en la cancha",
                                             font=dict(color=TEXT_1, family="Outfit", size=16)))
            st.plotly_chart(fig_sim, use_container_width=True)

        st.markdown("---")
        st.markdown("### Comparación de posiciones")
        st.caption("¿Cómo cambia el xG según te movés por la cancha?")
        rows = []
        for d in [8, 15, 25, 35]:
            for a in [20, 45, 75]:
                xg_p = float(mlp.predict_proba(np.array([[d / 36.0, a / 90.0]]))[0])
                cal = "🟢 Alta" if xg_p > 0.4 else ("🟡 Media" if xg_p > 0.15 else "🔴 Baja")
                rows.append({"Distancia": f"{d} m", "Ángulo": f"{a}°",
                             "xG predicho": f"{xg_p:.3f}", "Calidad": cal})
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


# ----------------------------------------------------------------
# TAB 5 — ÁRBITRO IA  (yellow card animation retrriggers each change)
# ----------------------------------------------------------------
with tab5:
    st.markdown(styles.section_head(
        kicker="06 · Módulo",
        title="¿Tarjeta amarilla?",
        lead="Misma idea, otra decisión. Cinco variables entran. Una red neuronal "
             "decide si el árbitro saca la cartulina."
    ), unsafe_allow_html=True)

    if st.session_state.net_ref is None:
        with st.spinner("Entrenando árbitro virtual…"):
            st.session_state.net_ref = ref_model.entrenar_modelo_arbitro(epochs=1500, lr=0.08)

    net = st.session_state.net_ref

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("#### Factores del foul")
        vel    = st.slider("Velocidad del impacto", 1, 10, 7)
        ball   = st.radio("¿Fue por la pelota?", ["No", "Sí"], horizontal=True) == "Sí"
        zona   = st.radio("Zona de la cancha", ["propia", "medio", "rival"],
                          horizontal=True, index=1)
        minuto = st.slider("Minuto del partido", 1, 90, 72)
        score  = st.slider("Diferencia en el marcador", -3, 3, -1,
                           help="Negativo = equipo del foul perdiendo")

    p = ref_model.predecir(net, vel, ball, zona, minuto, score)
    is_yellow = p >= 0.55

    with c2:
        st.markdown("#### Escena")
        # render_key encodes all inputs so DOM changes on every slider move → animation replays
        render_key = f"{vel}{int(ball)}{zona}{minuto}{score}{p:.4f}"
        st.markdown(
            styles.referee_scene(vel, ball, zona, minuto, score, is_yellow,
                                 render_key=render_key),
            unsafe_allow_html=True,
        )

    st.markdown("---")

    c3, c4 = st.columns([1, 2])
    with c3:
        st.markdown(styles.result_box(
            p,
            verdict_high="🟡 La red saca amarilla",
            verdict_mid="Decisión dudosa",
            verdict_low="✅ Sigue el juego",
            label="P(tarjeta amarilla)",
        ), unsafe_allow_html=True)

    with c4:
        factor = ref_model.factor_dominante(vel, ball, zona, minuto, score)
        st.info(f"📊 El factor que más empuja la decisión hacia la amarilla es **{factor}**.")
        rows = []
        for v_test in [2, 4, 6, 8, 10]:
            pt = ref_model.predecir(net, v_test, ball, zona, minuto, score)
            cal = "🟡 Amarilla" if pt >= 0.55 else ("🤔 Dudoso" if pt > 0.30 else "✅ Sin tarjeta")
            rows.append({"Velocidad": v_test, "P(amarilla)": f"{pt:.0%}", "Decisión": cal})
        st.markdown("**¿Y si solo cambia la velocidad?**")
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


# ----------------------------------------------------------------
# TAB 6 — TITULAR O SUPLENTE
# ----------------------------------------------------------------
with tab6:
    st.markdown(styles.section_head(
        kicker="07 · Módulo",
        title="¿Titular o suplente?",
        lead="El DT también usa datos. Esta red analiza el rendimiento reciente de un "
             "jugador y decide si arranca desde el primer minuto o se queda en el banco."
    ), unsafe_allow_html=True)

    if st.session_state.net_lineup is None:
        with st.spinner("Entrenando modelo de alineación…"):
            st.session_state.net_lineup = lineup_model.entrenar_modelo_lineup(
                epochs=2000, lr=0.06)

    net_lu = st.session_state.net_lineup

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("#### Stats del jugador")
        goals_in   = st.slider("⚽ Goles por 90 min",        0.0, 1.5, 0.6, step=0.05)
        assists_in = st.slider("🎯 Asistencias por 90 min",  0.0, 1.0, 0.3, step=0.05)
        pct_in     = st.slider("🎯 Precisión de pases (%)",  50,  100, 82)
        mins_in    = st.slider("⏱ Minutos últimos 3 partidos", 0, 270, 200)
        cond_in    = st.slider("💪 Condición física (1–10)",  1,  10,  7)
        edad_in    = st.slider("📅 Edad del jugador",        17,  38,  24)

    p_tit = lineup_model.predecir_lineup(
        net_lu, goals_in, assists_in, pct_in, mins_in, cond_in, edad_in)
    is_tit = p_tit >= 0.5

    with c2:
        st.markdown("#### Decisión del DT")
        lu_key = f"{goals_in}{assists_in}{pct_in}{mins_in}{cond_in}{edad_in}{p_tit:.4f}"
        components.html(
            styles.lineup_scene(is_tit, render_key=lu_key),
            height=400,
        )

    st.markdown("---")

    c3, c4 = st.columns([1, 2])
    with c3:
        st.markdown(styles.result_box(
            p_tit,
            verdict_high="🟢 Sale de titular",
            verdict_mid="Decisión pareja",
            verdict_low="🟠 Al banco",
            label="P(titular)",
        ), unsafe_allow_html=True)

    with c4:
        factor = lineup_model.factor_lineup(
            goals_in, assists_in, pct_in, mins_in, cond_in, edad_in)
        st.info(f"📊 Lo que más define la decisión es **{factor}**.")
        st.markdown(
            styles.lineup_feature_table(
                goals_in, assists_in, pct_in, mins_in, cond_in, edad_in),
            unsafe_allow_html=True,
        )


# ----------------------------------------------------------------
# TAB 7 — ¿SE LESIONA?
# ----------------------------------------------------------------
with tab7:
    st.markdown(styles.section_head(
        kicker="08 · Módulo",
        title="¿Se va a lesionar?",
        lead="La sobrecarga no se ve en el marcador, pero la red la detecta. "
             "Cinco variables de carga y recuperación definen el riesgo muscular de un jugador."
    ), unsafe_allow_html=True)

    if st.session_state.net_injury is None:
        with st.spinner("Entrenando modelo de lesiones…"):
            st.session_state.net_injury = injury_model.entrenar_modelo_injury(
                epochs=2000, lr=0.06)

    net_inj = st.session_state.net_injury

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("#### Carga del jugador")
        mins_inj   = st.slider("⏱ Minutos en los últimos 3 partidos",  0, 270, 210)
        dias_inj   = st.slider("🩹 Días desde la última lesión",        0, 365, 45,
                               help="0 = lesionado ayer · 365 = hace un año sin lesiones")
        edad_inj   = st.slider("📅 Edad del jugador",                  17,  38,  28)
        inten_inj  = st.slider("🏋 Intensidad de entrenamiento (1–10)", 1,  10,   7)
        part_inj   = st.slider("📅 Partidos en los últimos 30 días",    0,  12,   6)

    p_les = injury_model.predecir_lesion(
        net_inj, mins_inj, dias_inj, edad_inj, inten_inj, part_inj)
    is_inj = p_les >= 0.5

    with c2:
        st.markdown("#### Estado físico")
        inj_key = f"{mins_inj}{dias_inj}{edad_inj}{inten_inj}{part_inj}{p_les:.4f}"
        components.html(
            styles.injury_scene(is_inj, render_key=inj_key),
            height=400,
        )

    st.markdown("---")

    c3, c4 = st.columns([1, 2])
    with c3:
        st.markdown(styles.result_box(
            p_les,
            verdict_high="🔴 Alto riesgo de lesión",
            verdict_mid="⚠️ Zona de precaución",
            verdict_low="🟢 Baja probabilidad",
            label="P(lesión)",
        ), unsafe_allow_html=True)

    with c4:
        factor = injury_model.factor_lesion(
            mins_inj, dias_inj, edad_inj, inten_inj, part_inj)
        st.info(f"📊 El factor que más eleva el riesgo es **{factor}**.")
        st.markdown(
            styles.injury_feature_table(
                mins_inj, dias_inj, edad_inj, inten_inj, part_inj),
            unsafe_allow_html=True,
        )


# ----------------------------------------------------------------
# TAB 8 — GLOSARIO
# ----------------------------------------------------------------
with tab8:
    st.markdown(styles.section_head(
        kicker="07 · Glosario",
        title="Las palabras importantes.",
        lead="Cada concepto, con su fórmula, una analogía cotidiana y un ejemplo "
             "del proyecto. Hacé clic para expandir."
    ), unsafe_allow_html=True)

    for g in GLOSARIO:
        with st.expander(f"{g['name']}  ·  {g['sym']}", expanded=False):
            st.markdown(styles.glosario_card(**g), unsafe_allow_html=True)


# ===================================================================
# FOOTER
# ===================================================================
st.markdown(styles.footer(), unsafe_allow_html=True)
