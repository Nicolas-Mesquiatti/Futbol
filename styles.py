"""
styles.py — CSS + componentes HTML custom para la app Streamlit.
"""

import streamlit as st


CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
  --bg-primary:   #0F1923;
  --bg-deeper:    #0A1018;
  --bg-card:      #1A1A2E;
  --bg-card-2:    #16213E;
  --acc-green:    #00D4AA;
  --acc-green-2:  #5EE8C7;
  --acc-yellow:   #FFD700;
  --acc-red:      #FF4655;
  --text-1:       #FFFFFF;
  --text-2:       #8A9BB0;
  --text-3:       #5B6B7F;
  --border:       rgba(255,255,255,0.08);
  --border-2:     rgba(255,255,255,0.14);
  --font-ui:      'Inter', system-ui, sans-serif;
  --font-disp:    'Outfit', 'Inter', sans-serif;
  --font-mono:    'JetBrains Mono', ui-monospace, monospace;
}

html, body, .stApp {
  background: var(--bg-primary) !important;
  color: var(--text-1) !important;
  font-family: var(--font-ui) !important;
}
.stApp { background: var(--bg-primary) !important; }
.main .block-container {
  max-width: 1280px;
  padding-top: 1rem;
  padding-bottom: 4rem;
}
#MainMenu, header[data-testid="stHeader"], footer { visibility: hidden; height: 0; }

[data-testid="stSidebar"] {
  background: var(--bg-deeper) !important;
  border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text-1) !important; }

h1, h2, h3, h4 { font-family: var(--font-disp); letter-spacing: -0.02em; color: var(--text-1); }
.main p, .main li, .main span, .main label { color: var(--text-1); }
code, pre, .mono { font-family: var(--font-mono) !important; font-variant-numeric: tabular-nums; }
code {
  background: rgba(0,212,170,0.08) !important;
  color: var(--acc-green-2) !important;
  padding: 1px 6px; border-radius: 4px;
}

/* ===== Tabs ===== */
.stTabs [data-baseweb="tab-list"] {
  gap: 4px; background: transparent;
  border-bottom: 1px solid var(--border); padding: 0;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important; color: var(--text-2) !important;
  border: none !important; padding: 14px 22px !important;
  font-family: var(--font-ui); font-weight: 500; font-size: 14px;
  border-radius: 0 !important; border-bottom: 2px solid transparent !important;
  transition: color .2s, border-color .2s;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
  color: var(--acc-green) !important;
  border-bottom-color: var(--acc-green) !important;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--text-1) !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 30px; }

/* ===== Buttons ===== */
.stButton > button {
  background: transparent !important; color: var(--text-1) !important;
  border: 1px solid var(--border-2) !important; border-radius: 999px !important;
  padding: 10px 22px !important; font-family: var(--font-ui) !important;
  font-weight: 600 !important; font-size: 14px !important;
  transition: all .2s ease !important; box-shadow: none !important;
}
.stButton > button:hover {
  border-color: var(--acc-green) !important; color: var(--acc-green) !important;
  background: rgba(0,212,170,0.05) !important; transform: translateY(-1px);
}
.stButton > button:focus { outline: none !important; }

/* ===== Sliders ===== */
.stSlider label { color: var(--text-1) !important; font-weight: 500; font-size: 14px; }
.stSlider [data-baseweb="slider"] > div { background: rgba(255,255,255,0.06) !important; }
.stSlider [data-baseweb="slider"] [role="slider"] {
  background: var(--text-1) !important; border: 3px solid var(--acc-green) !important;
  box-shadow: 0 4px 14px rgba(0,212,170,0.35) !important;
  height: 22px !important; width: 22px !important;
}
.stSlider [data-baseweb="slider"] > div > div > div { background: var(--acc-green) !important; }
.stSlider [data-testid="stTickBar"] { color: var(--text-3) !important; font-family: var(--font-mono); font-size: 11px; }
.stSlider [data-baseweb="slider"] [role="slider"] + div {
  background: var(--bg-card-2) !important; color: var(--acc-green) !important;
  font-family: var(--font-mono) !important; font-weight: 600 !important;
}

/* ===== Radio ===== */
.stSelectbox label, .stRadio label, .stCheckbox label { color: var(--text-1) !important; font-weight: 500; }
.stSelectbox > div > div {
  background: var(--bg-card) !important; border: 1px solid var(--border) !important;
  border-radius: 10px !important; color: var(--text-1) !important;
}
.stRadio [role="radiogroup"] { gap: 8px; }
.stRadio [role="radiogroup"] label {
  background: transparent !important; border: 1px solid var(--border);
  border-radius: 999px; padding: 8px 16px !important;
  color: var(--text-2) !important; cursor: pointer; transition: all .2s;
}
.stRadio [role="radiogroup"] label[data-checked="true"],
.stRadio [role="radiogroup"] label:has(input:checked) {
  background: rgba(0,212,170,0.12) !important;
  border-color: var(--acc-green); color: var(--acc-green) !important;
}

/* ===== Metrics ===== */
[data-testid="stMetric"] {
  background: var(--bg-card) !important; border: 1px solid var(--border) !important;
  border-radius: 16px; padding: 20px 22px !important;
  box-shadow: 0 20px 50px -30px rgba(0,0,0,0.6);
}
[data-testid="stMetricLabel"] {
  font-family: var(--font-mono) !important; font-size: 11px !important;
  letter-spacing: 0.15em; text-transform: uppercase; color: var(--text-2) !important;
}
[data-testid="stMetricValue"] {
  font-family: var(--font-disp) !important; font-weight: 700 !important;
  font-size: 36px !important; letter-spacing: -0.02em; color: var(--text-1) !important;
}
[data-testid="stMetricDelta"] {
  font-family: var(--font-mono) !important; font-size: 12px !important;
  color: var(--acc-green) !important;
}

/* ===== Alerts ===== */
.stAlert {
  border-radius: 12px !important; border: 1px solid var(--border) !important;
  background: rgba(0,0,0,0.18) !important; color: var(--text-1) !important;
}
.stAlert [data-testid="stMarkdownContainer"] p { color: var(--text-1) !important; }

/* ===== Progress bar ===== */
.stProgress > div > div > div > div { background: var(--acc-green) !important; }
.stProgress > div > div > div { background: rgba(255,255,255,0.06) !important; border-radius: 999px !important; }

/* ===== DataFrame ===== */
[data-testid="stDataFrame"] {
  background: var(--bg-card) !important; border-radius: 14px;
  border: 1px solid var(--border); padding: 6px;
}
[data-testid="stDataFrame"] * { color: var(--text-1) !important; font-family: var(--font-mono) !important; }

/* ===== Plotly ===== */
.js-plotly-plot, .plot-container, .stPlotlyChart { background: transparent !important; }

/* ===========================================================
   HERO
   =========================================================== */
.xg-hero {
  position: relative;
  padding: 72px 0 60px;
  margin-bottom: 18px;
  overflow: hidden;
  isolation: isolate;
  border-bottom: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}
.xg-hero__pitch {
  position: absolute; inset: 0; z-index: -1;
  width: 100%; height: 100%; opacity: 0.35;
}
.xg-hero__pitch .pl {
  stroke-dasharray: 100; stroke-dashoffset: 100;
  animation: draw 2.4s cubic-bezier(.5,.05,.25,1) forwards;
}
.xg-hero__pitch .pl:nth-child(2) { animation-delay: .1s; }
.xg-hero__pitch .pl:nth-child(3) { animation-delay: .2s; }
.xg-hero__pitch .pl:nth-child(4) { animation-delay: .3s; }
.xg-hero__pitch .pl:nth-child(5) { animation-delay: .4s; }
.xg-hero__pitch .pl:nth-child(6) { animation-delay: .5s; }
.xg-hero__pitch .pl:nth-child(7) { animation-delay: .55s; }
.xg-hero__pitch .pl:nth-child(8) { animation-delay: .6s; }
.xg-hero__pitch .pl:nth-child(9) { animation-delay: .65s; }
.xg-hero__pitch .pl:nth-child(10){ animation-delay: .7s; }
@keyframes draw { to { stroke-dashoffset: 0; } }

.xg-hero__tag {
  display: inline-flex; align-items: center; gap: 10px;
  padding: 6px 14px; border: 1px solid var(--border);
  border-radius: 999px; background: rgba(255,255,255,0.02);
  font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--text-2); font-family: var(--font-mono); margin-bottom: 28px;
}
.xg-hero__tag i {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--acc-green); box-shadow: 0 0 0 3px rgba(0,212,170,0.18);
  animation: pulseDot 2s ease-in-out infinite;
}
@keyframes pulseDot {
  0%, 100% { box-shadow: 0 0 0 3px rgba(0,212,170,0.18); }
  50%      { box-shadow: 0 0 0 6px rgba(0,212,170,0.05); }
}

.xg-hero__title {
  font-family: var(--font-disp);
  font-weight: 800;
  font-size: clamp(52px, 7.5vw, 96px);
  line-height: 0.94;
  letter-spacing: -0.04em;
  margin: 0 0 24px 0;
  color: var(--text-1);
}
.xg-hero__title em {
  font-style: italic; font-weight: 900;
  background: linear-gradient(120deg, #00D4AA 0%, #5EE8C7 50%, #FFD700 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.xg-hero__sub {
  font-size: 19px; color: var(--text-2);
  max-width: 580px; margin: 0 auto 36px; line-height: 1.6;
}

/* CTA buttons */
.xg-hero__cta {
  display: flex; gap: 14px; margin-bottom: 44px; flex-wrap: wrap;
  justify-content: center;
}
.xg-cta {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 14px 30px; border-radius: 999px;
  font-family: var(--font-ui); font-weight: 600; font-size: 15px;
  text-decoration: none; transition: all .22s ease; cursor: pointer;
  letter-spacing: 0.01em;
}
.xg-cta--primary {
  background: var(--acc-green); color: #0A1018 !important;
  box-shadow: 0 14px 32px -10px rgba(0,212,170,0.6);
}
.xg-cta--primary:hover {
  background: var(--acc-green-2); transform: translateY(-2px);
  box-shadow: 0 18px 38px -10px rgba(0,212,170,0.7);
  color: #0A1018 !important;
}
.xg-cta--ghost {
  background: transparent; color: var(--text-1);
  border: 1px solid var(--border-2);
}
.xg-cta--ghost:hover {
  border-color: var(--acc-green); color: var(--acc-green);
  background: rgba(0,212,170,0.05); transform: translateY(-2px);
}

.xg-hero__stats {
  display: grid; grid-template-columns: repeat(4, 1fr);
  border-top: 1px solid var(--border); padding-top: 24px;
}
.xg-hero__stat { padding-right: 28px; border-right: 1px solid var(--border); }
.xg-hero__stat:last-child { border-right: none; }
.xg-hero__stat .v {
  font-family: var(--font-disp); font-weight: 700;
  font-size: 34px; letter-spacing: -0.02em; line-height: 1;
}
.xg-hero__stat .v .suf {
  font-family: var(--font-mono); font-size: 13px;
  color: var(--text-2); font-weight: 500; margin-left: 4px;
}
.xg-hero__stat .l {
  font-family: var(--font-mono); font-size: 11px;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--text-2); margin-top: 8px;
}
@media (max-width: 720px) { .xg-hero__stats { grid-template-columns: repeat(2, 1fr); } }

/* ===========================================================
   SECTION HEAD
   =========================================================== */
.xg-shead { margin: 50px 0 28px; }
.xg-shead .kk {
  font-family: var(--font-mono); font-size: 12px;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--acc-green); margin-bottom: 10px;
}
.xg-shead .tt {
  font-family: var(--font-disp); font-weight: 700;
  font-size: clamp(28px, 4vw, 48px); letter-spacing: -0.025em;
  margin: 0 0 10px 0; line-height: 1.02;
}
.xg-shead .ll {
  color: var(--text-2); font-size: 16px;
  max-width: 640px; margin: 0; line-height: 1.55;
}

/* ===========================================================
   STEP CARDS
   =========================================================== */
.xg-steps {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 14px; margin: 30px 0 10px;
}
@media (max-width: 980px) { .xg-steps { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 560px) { .xg-steps { grid-template-columns: 1fr; } }
.xg-step {
  padding: 24px;
  background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent), var(--bg-card);
  border: 1px solid var(--border); border-radius: 14px;
  min-height: 240px; display: flex; flex-direction: column;
  transition: border-color .25s, transform .25s;
}
.xg-step:hover { border-color: var(--border-2); transform: translateY(-2px); }
.xg-step .n {
  font-family: var(--font-mono); font-size: 12px;
  color: var(--text-3); letter-spacing: 0.1em; margin-bottom: 14px;
}
.xg-step .ic { width: 44px; height: 44px; color: var(--acc-green); margin-bottom: 18px; }
.xg-step .ic svg { width: 100%; height: 100%; }
.xg-step h3 {
  font-family: var(--font-disp); font-weight: 600; font-size: 19px;
  margin: 0 0 8px; letter-spacing: -0.015em;
}
.xg-step p { color: var(--text-2); font-size: 14px; margin: 0; line-height: 1.55; }
.n-pulse { animation: nodePulse 1.6s ease-in-out infinite; }
.n-pulse--d1 { animation-delay: .3s; } .n-pulse--d2 { animation-delay: .6s; }
@keyframes nodePulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; filter: drop-shadow(0 0 6px currentColor); }
}

/* ===========================================================
   DATASET STATS BAR
   =========================================================== */
.xg-ds-stats {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 14px; margin: 0 0 28px;
}
.xg-ds-stat {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 14px; padding: 22px 24px;
}
.xg-ds-stat .v {
  font-family: var(--font-disp); font-weight: 800;
  font-size: 44px; line-height: 1; letter-spacing: -0.03em;
}
.xg-ds-stat .l {
  font-family: var(--font-mono); font-size: 11px;
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--text-2); margin-top: 8px;
}
@media (max-width: 720px) { .xg-ds-stats { grid-template-columns: repeat(2, 1fr); } }

/* ===========================================================
   RESULT BOX
   =========================================================== */
.xg-result {
  padding: 28px; border-radius: 16px;
  background: rgba(0,0,0,0.22); border: 1px solid var(--border);
  margin-top: 8px;
}
.xg-result .lbl {
  font-family: var(--font-mono); font-size: 11px;
  letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--text-2); margin-bottom: 8px;
}
.xg-result .num {
  font-family: var(--font-disp); font-weight: 800;
  font-size: 72px; line-height: 1; letter-spacing: -0.03em; margin: 6px 0 16px;
}
.xg-result .num .pct { font-size: 30px; color: var(--text-2); font-weight: 600; margin-left: 4px; }
.xg-result.is-high { border-color: rgba(0,212,170,0.35); }
.xg-result.is-high .num { color: var(--acc-green); }
.xg-result.is-mid  { border-color: rgba(255,215,0,0.35); }
.xg-result.is-mid  .num { color: var(--acc-yellow); }
.xg-result.is-low  { border-color: rgba(255,70,85,0.35); }
.xg-result.is-low  .num { color: var(--acc-red); }
.xg-result .bar {
  height: 4px; background: rgba(255,255,255,0.08);
  border-radius: 999px; overflow: hidden; margin-bottom: 14px;
}
.xg-result .bar .fill {
  height: 100%;
  background: linear-gradient(90deg, var(--acc-red) 0%, var(--acc-yellow) 50%, var(--acc-green) 100%);
  transition: width .35s cubic-bezier(.4,0,.2,1);
}
.xg-result .verdict {
  display: flex; align-items: center; gap: 10px;
  font-size: 14px; color: var(--text-2);
}
.xg-result .verdict i { width: 8px; height: 8px; border-radius: 50%; display: inline-block; }
.xg-result.is-high .verdict i { background: var(--acc-green); box-shadow: 0 0 0 4px rgba(0,212,170,0.18); }
.xg-result.is-mid  .verdict i { background: var(--acc-yellow); box-shadow: 0 0 0 4px rgba(255,215,0,0.18); }
.xg-result.is-low  .verdict i { background: var(--acc-red); box-shadow: 0 0 0 4px rgba(255,70,85,0.18); }
.xg-result.is-high.is-goal .num { animation: bump .35s ease; }
@keyframes bump {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.08); }
}

/* ===========================================================
   NEURAL NETWORK DIAGRAM
   =========================================================== */
.xg-nn-wrap {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 14px; padding: 20px 24px; margin-bottom: 20px;
}
.xg-nn-header {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 14px;
}
.xg-nn-title {
  font-family: var(--font-mono); font-size: 11px;
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--text-2);
}
.xg-nn-live {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 3px 10px; border-radius: 999px;
  background: rgba(0,212,170,0.1); border: 1px solid rgba(0,212,170,0.25);
  font-family: var(--font-mono); font-size: 10px; color: var(--acc-green);
  letter-spacing: 0.1em;
}
.xg-nn-live::before {
  content: ''; width: 6px; height: 6px; border-radius: 50%;
  background: var(--acc-green); animation: pulseDot 1.2s ease-in-out infinite;
}

/* ===========================================================
   REFEREE SCENE
   =========================================================== */
.xg-ref {
  position: relative; height: 380px;
  display: flex; align-items: center; justify-content: center;
  background: radial-gradient(ellipse at center, rgba(255,215,0,0.03) 0%, transparent 60%);
  border: 1px solid var(--border); border-radius: 16px; overflow: hidden;
  transition: background 0.5s ease, box-shadow 0.5s ease;
}
.xg-ref.is-yellow {
  background: radial-gradient(ellipse at center, rgba(255,215,0,0.18) 0%, transparent 65%);
  box-shadow: 0 0 60px -20px rgba(255,215,0,0.25), inset 0 0 40px -20px rgba(255,215,0,0.08);
  border-color: rgba(255,215,0,0.2);
  animation: yellowGlow 0.7s ease forwards;
}
@keyframes yellowGlow {
  0%   { box-shadow: 0 0 0 0 rgba(255,215,0,0); }
  40%  { box-shadow: 0 0 80px -10px rgba(255,215,0,0.4), inset 0 0 40px -15px rgba(255,215,0,0.12); }
  100% { box-shadow: 0 0 60px -20px rgba(255,215,0,0.25), inset 0 0 40px -20px rgba(255,215,0,0.08); }
}
.xg-ref svg.fig { height: 90%; filter: drop-shadow(0 8px 30px rgba(0,0,0,0.4)); }
.xg-ref .arm {
  transform-origin: 130px 80px;
  transform: rotate(40deg);
  transition: transform 0.55s cubic-bezier(.5,1.6,.5,1);
}
.xg-ref.is-yellow .arm { transform: rotate(-50deg); }
.xg-ref .chip {
  position: absolute; top: 50%; left: 50%;
  transform: translate(calc(-50% + var(--ox)), calc(-50% + var(--oy)));
  background: var(--bg-card-2); border: 1px solid var(--border);
  border-radius: 8px; padding: 8px 14px;
  display: flex; align-items: center; gap: 10px;
  font-size: 12px; box-shadow: 0 8px 24px -10px rgba(0,0,0,0.5); z-index: 2;
  animation: chipFloat 4s ease-in-out infinite;
}
.xg-ref .chip .k { font-family: var(--font-mono); font-size: 10px; letter-spacing: 0.1em; color: var(--text-2); }
.xg-ref .chip .v { color: var(--text-1); font-weight: 600; font-family: var(--font-mono); }
@keyframes chipFloat {
  0%, 100% { transform: translate(calc(-50% + var(--ox)), calc(-50% + var(--oy))); }
  50%      { transform: translate(calc(-50% + var(--ox)), calc(-50% + var(--oy) - 8px)); }
}

/* ===========================================================
   GLOSARIO CARD
   =========================================================== */
.xg-glos {
  border: 1px solid var(--border); background: var(--bg-card);
  border-radius: 14px; padding: 22px; margin-bottom: 12px;
}
.xg-glos .hd {
  display: flex; align-items: baseline; justify-content: space-between;
  gap: 14px; margin-bottom: 14px;
}
.xg-glos .name { font-family: var(--font-disp); font-weight: 600; font-size: 20px; letter-spacing: -0.015em; }
.xg-glos .sym { font-family: var(--font-mono); font-size: 12px; color: var(--acc-green); letter-spacing: 0.05em; }
.xg-glos .def { font-size: 15px; color: var(--text-1); margin: 0 0 12px; line-height: 1.55; }
.xg-glos .formula {
  padding: 10px 14px; background: rgba(0,0,0,0.3);
  border: 1px solid var(--border); border-radius: 8px;
  font-family: var(--font-mono); font-size: 13px;
  color: var(--acc-green-2); margin-bottom: 12px;
}
.xg-glos .row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 12px; }
.xg-glos .row .cell {
  padding: 10px 12px; background: rgba(255,255,255,0.02);
  border: 1px solid var(--border); border-radius: 8px;
}
.xg-glos .row .cell .h {
  font-family: var(--font-mono); font-size: 10px;
  letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--text-2); margin-bottom: 4px;
  display: flex; align-items: center; gap: 6px;
}
.xg-glos .row .cell .h .dot { width: 6px; height: 6px; border-radius: 50%; }
.xg-glos .row .cell .h.lo .dot { background: var(--acc-red); }
.xg-glos .row .cell .h.hi .dot { background: var(--acc-green); }
.xg-glos .row .cell .b { font-size: 13px; color: var(--text-1); }
.xg-glos .analogy {
  border-left: 2px solid var(--acc-green); padding: 4px 0 4px 12px;
  font-style: italic; color: var(--text-2); font-size: 14px; margin-bottom: 12px;
}
.xg-glos .tip {
  padding: 10px 14px; background: rgba(0,212,170,0.06);
  border: 1px solid rgba(0,212,170,0.2); border-radius: 8px;
  font-size: 13px; color: var(--text-1);
}
.xg-glos .tip strong { color: var(--acc-green); }

/* ===========================================================
   FOOTER
   =========================================================== */
.xg-foot {
  border-top: 1px solid var(--border); padding: 36px 0 12px; margin-top: 50px;
  display: flex; flex-wrap: wrap; gap: 40px;
  justify-content: space-between; color: var(--text-2); font-size: 13px;
}
.xg-foot .brand { display: flex; align-items: center; gap: 10px; }
.xg-foot .brand .dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--acc-green);
  box-shadow: 0 0 0 4px rgba(0,212,170,0.18), 0 0 20px var(--acc-green);
}
.xg-foot .brand b { color: var(--text-1); font-family: var(--font-disp); font-weight: 800; letter-spacing: -0.01em; }

hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 30px 0 !important; }
.stMarkdown a { color: var(--acc-green); }

/* ===========================================================
   LINEUP & INJURY TABLES (rendered via st.markdown)
   =========================================================== */
.xg-lineup-table, .xg-injury-table {
  background: #1A1A2E; border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; padding: 18px; margin-top: 16px;
}
.xg-lineup-table .lt-row, .xg-injury-table .lt-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 9px 0; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 14px;
}
.xg-lineup-table .lt-row:last-child,
.xg-injury-table  .lt-row:last-child { border-bottom: none; }
.xg-lineup-table .lt-feat, .xg-injury-table .lt-feat {
  color: #8A9BB0; font-family: 'JetBrains Mono', monospace; font-size: 12px;
}
.xg-lineup-table .lt-val, .xg-injury-table .lt-val {
  color: #FFFFFF; font-family: 'JetBrains Mono', monospace; font-weight: 600;
}
.xg-lineup-table .lt-imp, .xg-injury-table .lt-imp { font-size: 13px; }
</style>
"""


def inject_css() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


# ===================================================================
# HERO
# ===================================================================
def hero_js() -> str:
    """Navega via query params para que Python active el tab correcto.
    Render via: st.components.v1.html(styles.hero_js(), height=0)
    """
    return """<script>
// "Empezar →": navega a ?tab=intro → Python lee el param y activa el tab
parent.xgEmpezar = function() {
  parent.location.search = '?tab=intro';
};
// "Ir directo al simulador": navega a ?tab=simulador → activa Entrenar la red
parent.xgSimulador = function() {
  parent.location.search = '?tab=simulador';
};
</script>"""


def hero(n_tiros: int, target_acc: int = 78) -> str:
    return f"""
<div class="xg-hero">
  <svg class="xg-hero__pitch" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <g fill="none" stroke="#00D4AA" stroke-width="1.4" stroke-opacity="0.5">
      <rect class="pl" x="80" y="80" width="1440" height="740" pathLength="100"/>
      <line class="pl" x1="800" y1="80" x2="800" y2="820" pathLength="100"/>
      <circle class="pl" cx="800" cy="450" r="110" pathLength="100"/>
      <rect class="pl" x="80" y="225" width="220" height="450" pathLength="100"/>
      <rect class="pl" x="80" y="335" width="80" height="230" pathLength="100"/>
      <rect class="pl" x="1300" y="225" width="220" height="450" pathLength="100"/>
      <rect class="pl" x="1440" y="335" width="80" height="230" pathLength="100"/>
      <path class="pl" d="M 300 360 A 80 80 0 0 1 300 540" pathLength="100"/>
      <path class="pl" d="M 1300 360 A 80 80 0 0 0 1300 540" pathLength="100"/>
      <circle class="pl" cx="245" cy="450" r="3" fill="#00D4AA" pathLength="100"/>
    </g>
  </svg>
  <div class="xg-hero__tag"><i></i><span>Red neuronal entrenada en vivo</span></div>
  <h1 class="xg-hero__title">¿Puede la IA<br/><em>entender</em> el fútbol?</h1>
  <p class="xg-hero__sub">
    Una red neuronal mira miles de tiros y aprende, sola, qué hace que una pelota
    termine en el fondo del arco. Sin reglas. Sin fórmulas. Solo patrones.
  </p>
  <div class="xg-hero__cta">
    <a class="xg-cta xg-cta--primary" href="#" onclick="xgEmpezar();return false;">
      Empezar
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
    </a>
    <a class="xg-cta xg-cta--ghost" href="#" onclick="xgSimulador();return false;">
      Ir directo al simulador
    </a>
  </div>
  <div class="xg-hero__stats">
    <div class="xg-hero__stat">
      <div class="v">{n_tiros}</div><div class="l">tiros analizados</div>
    </div>
    <div class="xg-hero__stat">
      <div class="v">2<span class="suf">capas</span></div><div class="l">ocultas tanh</div>
    </div>
    <div class="xg-hero__stat">
      <div class="v">{target_acc}<span class="suf">%</span></div><div class="l">accuracy objetivo</div>
    </div>
    <div class="xg-hero__stat">
      <div class="v">0<span class="suf">deps ML</span></div><div class="l">sin TF · sin sklearn</div>
    </div>
  </div>
</div>
"""


# ===================================================================
# INTRO TAB CONTENT
# ===================================================================
def intro_tab_content() -> str:
    """HTML doc completo para components.html(height=960).
    SVG 2→2→1 + explicación en español. Sin st.markdown para evitar sanitización."""
    return """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #0F1923;
  color: #FFFFFF;
  font-family: 'Inter', system-ui, sans-serif;
  padding: 8px 12px 32px;
  overflow-x: hidden;
}
.kicker {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
  color: #00D4AA; margin-bottom: 10px;
}
.title {
  font-family: 'Outfit', sans-serif;
  font-weight: 700; font-size: 36px; letter-spacing: -0.025em;
  color: #FFFFFF; margin: 0 0 10px;
}
.lead { color: #8A9BB0; font-size: 15px; line-height: 1.6; max-width: 640px; margin-bottom: 28px; }
.diagram-box {
  background: #1A1A2E; border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px; padding: 28px 24px; margin-bottom: 24px; text-align: center;
}
.diagram-label {
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  letter-spacing: 0.15em; text-transform: uppercase;
  color: #8A9BB0; margin-bottom: 18px;
}
.cards {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-bottom: 24px;
}
@media (max-width: 600px) { .cards { grid-template-columns: 1fr; } }
.card {
  background: #1A1A2E; border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; padding: 20px;
}
.card-kicker {
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 10px;
}
.card p { font-size: 14px; color: #FFFFFF; line-height: 1.6; margin: 0 0 12px; }
.formula {
  font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #5EE8C7;
  background: rgba(0,0,0,0.3); padding: 8px 12px; border-radius: 6px;
}
.football-box {
  background: linear-gradient(135deg, rgba(0,212,170,0.06), transparent);
  border: 1px solid rgba(0,212,170,0.2); border-radius: 16px; padding: 28px 32px;
}
.football-box .kicker { margin-bottom: 14px; }
.football-box p { font-size: 15px; line-height: 1.65; color: #FFFFFF; margin-bottom: 12px; }
.football-box p:last-child { color: #8A9BB0; font-size: 14px; margin-bottom: 0; }
</style>
</head>
<body>
  <div class="kicker">00 · Introducción</div>
  <h2 class="title">¿Qué es una red neuronal?</h2>
  <p class="lead">Sin matemáticas complejas. Sin jerga innecesaria. Solo la intuición detrás
  de la tecnología que usa el fútbol moderno para tomar decisiones.</p>

  <!-- SVG diagram -->
  <div class="diagram-box">
    <div class="diagram-label">Arquitectura MLP · 2 → 2 → 1</div>
    <svg viewBox="0 0 560 210" width="100%" style="max-width:540px;display:block;margin:0 auto;overflow:visible;">
      <!-- connections input→hidden -->
      <line x1="100" y1="70"  x2="280" y2="70"  stroke="rgba(255,255,255,0.10)" stroke-width="1.5"/>
      <line x1="100" y1="70"  x2="280" y2="140" stroke="rgba(255,255,255,0.10)" stroke-width="1.5"/>
      <line x1="100" y1="140" x2="280" y2="70"  stroke="rgba(255,255,255,0.10)" stroke-width="1.5"/>
      <line x1="100" y1="140" x2="280" y2="140" stroke="rgba(255,255,255,0.10)" stroke-width="1.5"/>
      <!-- connections hidden→output -->
      <line x1="280" y1="70"  x2="460" y2="105" stroke="rgba(94,232,199,0.25)" stroke-width="1.5"/>
      <line x1="280" y1="140" x2="460" y2="105" stroke="rgba(94,232,199,0.25)" stroke-width="1.5"/>

      <!-- input nodes -->
      <circle cx="100" cy="70"  r="20" fill="#00D4AA" opacity="0.88"/>
      <circle cx="100" cy="140" r="20" fill="#00D4AA" opacity="0.88"/>
      <text x="100" y="75"  text-anchor="middle" fill="#0A1018" font-size="10" font-weight="700" font-family="JetBrains Mono, monospace">dist</text>
      <text x="100" y="145" text-anchor="middle" fill="#0A1018" font-size="10" font-weight="700" font-family="JetBrains Mono, monospace">ang</text>

      <!-- hidden nodes -->
      <circle cx="280" cy="70"  r="20" fill="#5EE8C7" opacity="0.88"/>
      <circle cx="280" cy="140" r="20" fill="#5EE8C7" opacity="0.88"/>
      <text x="280" y="75"  text-anchor="middle" fill="#0A1018" font-size="10" font-weight="700" font-family="JetBrains Mono, monospace">tanh</text>
      <text x="280" y="145" text-anchor="middle" fill="#0A1018" font-size="10" font-weight="700" font-family="JetBrains Mono, monospace">tanh</text>

      <!-- output node -->
      <circle cx="460" cy="105" r="24" fill="#FFD700" opacity="0.92"/>
      <text x="460" y="102" text-anchor="middle" fill="#0A1018" font-size="13" font-weight="700" font-family="JetBrains Mono, monospace">σ</text>
      <text x="460" y="116" text-anchor="middle" fill="#0A1018" font-size="9"  font-weight="600" font-family="JetBrains Mono, monospace">xG</text>

      <!-- weight labels -->
      <text x="188" y="55"  text-anchor="middle" fill="rgba(255,255,255,0.38)" font-size="10" font-family="JetBrains Mono, monospace">w₁</text>
      <text x="188" y="162" text-anchor="middle" fill="rgba(255,255,255,0.38)" font-size="10" font-family="JetBrains Mono, monospace">w₄</text>
      <text x="372" y="86"  text-anchor="middle" fill="rgba(94,232,199,0.55)"  font-size="10" font-family="JetBrains Mono, monospace">w₅</text>

      <!-- arrows at edges -->
      <polygon points="258,66 272,70 258,74" fill="rgba(255,255,255,0.18)"/>
      <polygon points="258,136 272,140 258,144" fill="rgba(255,255,255,0.18)"/>
      <polygon points="436,102 450,105 436,108" fill="rgba(94,232,199,0.45)"/>

      <!-- layer labels below -->
      <text x="100" y="178" text-anchor="middle" fill="rgba(255,255,255,0.32)" font-size="10" font-family="JetBrains Mono, monospace">Entrada</text>
      <text x="100" y="192" text-anchor="middle" fill="#00D4AA"                font-size="9"  font-family="JetBrains Mono, monospace">2 features</text>
      <text x="280" y="178" text-anchor="middle" fill="rgba(255,255,255,0.32)" font-size="10" font-family="JetBrains Mono, monospace">Capa oculta</text>
      <text x="280" y="192" text-anchor="middle" fill="#5EE8C7"                font-size="9"  font-family="JetBrains Mono, monospace">2 neuronas · tanh</text>
      <text x="460" y="178" text-anchor="middle" fill="rgba(255,255,255,0.32)" font-size="10" font-family="JetBrains Mono, monospace">Salida</text>
      <text x="460" y="192" text-anchor="middle" fill="#FFD700"                font-size="9"  font-family="JetBrains Mono, monospace">1 neurona · σ</text>
    </svg>
  </div>

  <!-- Concept cards -->
  <div class="cards">
    <div class="card">
      <div class="card-kicker" style="color:#00D4AA;">Neurona</div>
      <p>Cada neurona recibe números, los combina con sus <strong>pesos</strong> y los pasa por una función no lineal. Sola no hace gran cosa. Junto a otras, reconoce patrones.</p>
      <div class="formula">a = tanh(w₁·x₁ + w₂·x₂ + b)</div>
    </div>
    <div class="card">
      <div class="card-kicker" style="color:#FFD700;">Backpropagation</div>
      <p>La red adivina. Si se equivoca, el error viaja hacia atrás y cada peso recibe su cuota de culpa. Así aprende: ajustando un poquito a la vez, epoch tras epoch.</p>
      <div class="formula">w ← w − α · ∂L/∂w</div>
    </div>
    <div class="card">
      <div class="card-kicker" style="color:#FF4655;">Sigmoid σ</div>
      <p>La última capa usa sigmoid: aplasta cualquier número al rango [0, 1]. Perfecto para decir "hay un 73% de probabilidad de gol" en lugar de un número sin escala.</p>
      <div class="formula">σ(z) = 1 / (1 + e⁻ᶻ)</div>
    </div>
  </div>

  <!-- Football application -->
  <div class="football-box">
    <div class="kicker">¿Por qué el fútbol?</div>
    <p>El fútbol genera millones de eventos medibles por temporada. Cada tiro tiene dos coordenadas —distancia y ángulo— y un resultado binario: gol o no gol. Es el dataset ideal para entrenar un MLP desde cero.</p>
    <p>Clubes como Liverpool, Bayern o Brighton usan redes neuronales para evaluar jugadores, anticipar lesiones y diseñar esquemas tácticos. Esta app replica esa lógica en pequeño — con la diferencia de que acá podés ver cada peso ajustarse en tiempo real.</p>
  </div>
</body></html>"""


# ===================================================================
# SECTION HEAD
# ===================================================================
def section_head(kicker: str, title: str, lead: str = "") -> str:
    return f"""
<div class="xg-shead">
  <div class="kk">{kicker}</div>
  <h2 class="tt">{title}</h2>
  {('<p class="ll">' + lead + '</p>') if lead else ''}
</div>
"""


# ===================================================================
# STEPS EXPLAINER
# ===================================================================
def steps_explainer() -> str:
    icon1 = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6">
      <rect x="6" y="14" width="22" height="6" rx="1"/>
      <rect x="6" y="26" width="34" height="6" rx="1"/>
      <rect x="6" y="38" width="18" height="6" rx="1"/>
      <path d="M44 17h14M44 29h14M44 41h14" stroke-dasharray="2 3"/>
      <circle cx="58" cy="17" r="2.5" fill="currentColor" stroke="none"/>
      <circle cx="58" cy="29" r="2.5" fill="currentColor" stroke="none"/>
      <circle cx="58" cy="41" r="2.5" fill="currentColor" stroke="none"/>
    </svg>"""
    icon2 = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.4">
      <g stroke-opacity="0.5">
        <line x1="10" y1="20" x2="32" y2="14"/><line x1="10" y1="20" x2="32" y2="32"/>
        <line x1="10" y1="20" x2="32" y2="50"/><line x1="10" y1="44" x2="32" y2="14"/>
        <line x1="10" y1="44" x2="32" y2="32"/><line x1="10" y1="44" x2="32" y2="50"/>
        <line x1="32" y1="14" x2="54" y2="32"/><line x1="32" y1="32" x2="54" y2="32"/>
        <line x1="32" y1="50" x2="54" y2="32"/>
      </g>
      <circle cx="10" cy="20" r="3.5" fill="currentColor"/>
      <circle cx="10" cy="44" r="3.5" fill="currentColor"/>
      <circle cx="32" cy="14" r="4" class="n-pulse" fill="currentColor"/>
      <circle cx="32" cy="32" r="4" class="n-pulse n-pulse--d1" fill="currentColor"/>
      <circle cx="32" cy="50" r="4" class="n-pulse n-pulse--d2" fill="currentColor"/>
      <circle cx="54" cy="32" r="4.5" fill="currentColor"/>
    </svg>"""
    icon3 = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6">
      <circle cx="32" cy="32" r="20"/>
      <path d="M32 12v20l12 8" stroke-linecap="round"/>
    </svg>"""
    icon4 = """<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.6">
      <path d="M14 32a18 18 0 1 1 6 13.5" stroke-linecap="round"/>
      <path d="M14 32V20M14 32h12" stroke-linecap="round"/>
    </svg>"""
    return f"""
<div class="xg-steps">
  <div class="xg-step"><div class="n">01</div><div class="ic">{icon1}</div>
    <h3>Le damos datos</h3>
    <p>Para cada tiro, dos números: <code>distancia al arco</code> y <code>ángulo</code>. Nada más.</p></div>
  <div class="xg-step"><div class="n">02</div><div class="ic">{icon2}</div>
    <h3>La red piensa</h3>
    <p>Decenas de mini-decisiones (neuronas) combinan esos números. Cada conexión tiene un <code>peso</code> que dice cuánto importa.</p></div>
  <div class="xg-step"><div class="n">03</div><div class="ic">{icon3}</div>
    <h3>Da una respuesta</h3>
    <p>Un número entre 0 y 1. <code>0.73</code> = "73% de probabilidad de gol". Eso es xG.</p></div>
  <div class="xg-step"><div class="n">04</div><div class="ic">{icon4}</div>
    <h3>Aprende del error</h3>
    <p>Si se equivocó, retropropaga el error y ajusta los pesos. <em>Backpropagation</em>: culpa repartida hacia atrás.</p></div>
</div>
"""


# ===================================================================
# DATASET STATS BAR
# ===================================================================
def dataset_stats(n_total: int, n_goles: int) -> str:
    n_no_gol = n_total - n_goles
    pct = n_goles / n_total * 100
    return f"""
<div class="xg-ds-stats">
  <div class="xg-ds-stat">
    <div class="v" style="color:var(--text-1)">{n_total}</div>
    <div class="l">tiros totales</div>
  </div>
  <div class="xg-ds-stat">
    <div class="v" style="color:var(--acc-green)">{n_goles}</div>
    <div class="l">goles ⚽</div>
  </div>
  <div class="xg-ds-stat">
    <div class="v" style="color:var(--acc-red)">{n_no_gol}</div>
    <div class="l">no goles</div>
  </div>
  <div class="xg-ds-stat">
    <div class="v" style="color:var(--acc-yellow)">{pct:.1f}<span style="font-size:22px;color:var(--text-2);font-weight:600">%</span></div>
    <div class="l">conversión</div>
  </div>
</div>
"""


# ===================================================================
# NEURAL NETWORK DIAGRAM
# ===================================================================
def nn_diagram(arch: list, is_training: bool = False) -> str:
    """SVG diagram of the MLP architecture. Max 6 nodes shown per layer."""
    MAX_SHOW = 6
    W, H = 620, 240
    pad_x, pad_y = 70, 28
    n_layers = len(arch)
    xs = [pad_x + i * (W - 2 * pad_x) / max(n_layers - 1, 1) for i in range(n_layers)]

    node_r = 9
    lines_svg = ""
    nodes_svg = ""
    labels_svg = ""

    layer_ys = []
    for li, n in enumerate(arch):
        show = min(n, MAX_SHOW)
        layer_h = H - 2 * pad_y
        if show == 1:
            ys = [H / 2]
        else:
            ys = [pad_y + j * layer_h / (show - 1) for j in range(show)]
        layer_ys.append(ys)

    # Draw connections
    for li in range(n_layers - 1):
        for y0 in layer_ys[li]:
            for y1 in layer_ys[li + 1]:
                lines_svg += (
                    f'<line x1="{xs[li]:.1f}" y1="{y0:.1f}" '
                    f'x2="{xs[li+1]:.1f}" y2="{y1:.1f}" '
                    f'stroke="rgba(255,255,255,0.07)" stroke-width="1"/>'
                )

    # Draw nodes
    pulse_css = ""
    if is_training:
        pulse_css = """
        @keyframes nnP {
          0%,100%{opacity:.65;transform:scale(1);}
          50%{opacity:1;transform:scale(1.35);filter:drop-shadow(0 0 7px currentColor);}
        }
        .nnp{animation:nnP 1.1s ease-in-out infinite;transform-box:fill-box;transform-origin:center;}
        """

    node_colors = {0: "#00D4AA", -1: "#FFD700"}
    for li, (x, ys) in enumerate(zip(xs, layer_ys)):
        n = arch[li]
        show = min(n, MAX_SHOW)
        color = node_colors.get(li if li == 0 else (li - n_layers + 1 if li == n_layers - 1 else None), "#5EE8C7")
        cls = "nnp" if is_training else ""
        for ji, y in enumerate(ys):
            delay = f"{(li * 0.15 + ji * 0.08) % 1.4:.2f}s"
            style = f'animation-delay:{delay}' if is_training else ""
            nodes_svg += (
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{node_r}" '
                f'fill="{color}" fill-opacity="0.9" class="{cls}" style="{style}"/>'
            )
        if n > MAX_SHOW:
            nodes_svg += (
                f'<text x="{x:.1f}" y="{H - pad_y + 6:.1f}" text-anchor="middle" '
                f'fill="rgba(255,255,255,0.35)" font-family="JetBrains Mono" font-size="10">+{n-MAX_SHOW}</text>'
            )
        # Layer label
        lbl = "Input" if li == 0 else ("Output" if li == n_layers - 1 else f"Oculta {li}")
        count = f"{n}n" if 0 < li < n_layers - 1 else ("2 feat" if li == 0 else "1 out")
        labels_svg += (
            f'<text x="{x:.1f}" y="{H + 16:.0f}" text-anchor="middle" '
            f'fill="rgba(255,255,255,0.35)" font-family="JetBrains Mono" font-size="10">{lbl}</text>'
            f'<text x="{x:.1f}" y="{H + 30:.0f}" text-anchor="middle" '
            f'fill="{color}" font-family="JetBrains Mono" font-size="9" opacity="0.8">{count}</text>'
        )

    live_badge = '<span class="xg-nn-live">entrenando</span>' if is_training else ""
    return f"""
<div class="xg-nn-wrap">
  <div class="xg-nn-header">
    <span class="xg-nn-title">Arquitectura de la red</span>
    {live_badge}
  </div>
  <svg viewBox="0 0 {W} {H+36}" width="100%" style="overflow:visible;max-height:300px;">
    <style>{pulse_css}</style>
    {lines_svg}
    {nodes_svg}
    {labels_svg}
  </svg>
</div>
"""


# ===================================================================
# RESULT BOX
# ===================================================================
def result_box(proba: float, verdict_high: str = "⚽ Chance clara",
               verdict_mid: str = "Chance moderada",
               verdict_low: str = "🔴 Muy difícil",
               label: str = "Probabilidad de gol") -> str:
    pct = int(round(proba * 100))
    if proba >= 0.5:
        tier, verdict = "is-high", verdict_high
        goal_class = "is-goal" if proba > 0.7 else ""
    elif proba >= 0.2:
        tier, verdict, goal_class = "is-mid", verdict_mid, ""
    else:
        tier, verdict, goal_class = "is-low", verdict_low, ""
    return f"""
<div class="xg-result {tier} {goal_class}">
  <div class="lbl">{label}</div>
  <div class="num">{pct}<span class="pct">%</span></div>
  <div class="bar"><div class="fill" style="width:{max(2,pct)}%"></div></div>
  <div class="verdict"><i></i><span>{verdict}</span></div>
</div>
"""


# ===================================================================
# REFEREE SCENE  — animation retrriggers via unique anim name per render
# ===================================================================
def referee_scene(vel: int, ball: bool, zona: str, minuto: int, score: int,
                  is_yellow: bool, render_key: str = "") -> str:
    yellow_cls = "is-yellow" if is_yellow else ""
    ball_txt = "Sí" if ball else "No"
    zona_txt = zona.capitalize()
    score_txt = f"+{score}" if score > 0 else f"{score}"

    # Unique animation name so the browser always replays it
    anim_id = render_key or f"{vel}{int(ball)}{zona}{minuto}{score}"
    card_anim_name = f"cardFly_{abs(hash(anim_id)) % 99999}"

    card_anim_css = f"""
    @keyframes {card_anim_name} {{
      0%   {{ transform: translateY(28px) scale(0.3) rotate(-22deg); opacity: 0; }}
      50%  {{ transform: translateY(-14px) scale(1.18) rotate(9deg); opacity: 1; }}
      78%  {{ transform: translateY(5px) scale(0.96) rotate(-3deg); }}
      100% {{ transform: translateY(0) scale(1) rotate(0deg); opacity: 1; }}
    }}
    """ if is_yellow else ""

    card_style = (
        f"opacity:1; animation:{card_anim_name} 0.62s cubic-bezier(0.34,1.56,0.64,1) 0.08s both;"
        " transform-box:fill-box; transform-origin:161px 121px;"
    ) if is_yellow else "opacity:0;"

    return f"""
<style>{card_anim_css}</style>
<div class="xg-ref {yellow_cls}">
  <div class="chip" style="--ox:-220px; --oy:-100px;">
    <span class="k">VEL</span><span class="v">{vel}</span>
  </div>
  <div class="chip" style="--ox:200px; --oy:-120px;">
    <span class="k">PELOTA</span><span class="v">{ball_txt}</span>
  </div>
  <div class="chip" style="--ox:-240px; --oy:80px;">
    <span class="k">ZONA</span><span class="v">{zona_txt}</span>
  </div>
  <div class="chip" style="--ox:220px; --oy:100px;">
    <span class="k">MIN</span><span class="v">{minuto}'</span>
  </div>
  <div class="chip" style="--ox:0px; --oy:-160px;">
    <span class="k">MARCADOR</span><span class="v">{score_txt}</span>
  </div>
  <svg class="fig" viewBox="0 0 200 280">
    <circle cx="100" cy="42" r="20" fill="none" stroke="#fff" stroke-width="1.6"/>
    <path d="M 70 70 L 130 70 L 138 180 L 62 180 Z" fill="none" stroke="#fff" stroke-width="1.6"/>
    <line x1="64" y1="140" x2="136" y2="140" stroke="#fff" stroke-width="1.2" stroke-dasharray="3 3"/>
    <rect x="105" y="100" width="14" height="20" fill="none" stroke="#FFD700" stroke-width="1.4" stroke-opacity="0.5"/>
    <line x1="80" y1="180" x2="76" y2="260" stroke="#fff" stroke-width="1.6"/>
    <line x1="120" y1="180" x2="124" y2="260" stroke="#fff" stroke-width="1.6"/>
    <line x1="70" y1="80" x2="40" y2="130" stroke="#fff" stroke-width="1.6"/>
    <g class="arm">
      <line x1="130" y1="80" x2="160" y2="130" stroke="#fff" stroke-width="1.6"/>
      <g style="{card_style}">
        <rect x="152" y="108" width="18" height="26" rx="1.5" fill="#FFD700" stroke="#fff" stroke-width="1"/>
      </g>
    </g>
  </svg>
</div>
"""


# ===================================================================
# GOAL CELEBRATION
# ===================================================================
def goal_celebration(proba: float) -> str:
    """Confetti + GOOOL banner. Unique keyframe names per proba value so it always replays."""
    if proba <= 0.5:
        return ""
    n = abs(hash(f"{proba:.5f}")) % 999983
    rng_c = [
        ("#00D4AA", "5", "50"),  ("FFD700", "8", "30"),  ("#FF4655", "6", "50"),
        ("#5EE8C7", "7", "50"),  ("#FFFFFF", "5", "30"),  ("#00D4AA", "9", "50"),
        ("#FFD700", "6", "30"),  ("#FF4655", "5", "50"),  ("#5EE8C7", "8", "30"),
        ("#00D4AA", "7", "50"),  ("#FFD700", "5", "50"),  ("#FF4655", "9", "30"),
        ("#5EE8C7", "6", "50"),  ("#FFFFFF", "8", "30"),  ("#00D4AA", "5", "50"),
        ("#FFD700", "7", "50"),  ("#FF4655", "6", "30"),  ("#5EE8C7", "5", "50"),
        ("#FFFFFF", "9", "30"),  ("#00D4AA", "6", "50"),
    ]
    positions = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,93,97]
    delays    = [0,.08,.16,.24,.32,.1,.18,.26,.34,.05,.13,.21,.29,.37,.03,.11,.19,.27,.35,.07]
    confetti  = "".join(
        f'<div style="position:absolute;left:{pos}%;top:-12px;width:{w}px;height:{w}px;'
        f'background:{col};border-radius:{br}%;opacity:1;'
        f'animation:cFall{n} {1.4+d:.2f}s cubic-bezier(.25,1,.4,1) {d:.2f}s both;"></div>'
        for (col, w, br), pos, d in zip(rng_c, positions, delays)
    )
    return f"""
<style>
@keyframes cFall{n}{{0%{{transform:translateY(0) rotate(0deg);opacity:1;}}100%{{transform:translateY(280px) rotate(540deg);opacity:0;}}}}
@keyframes gPop{n}{{0%{{transform:scale(0) rotate(-12deg);opacity:0;}}55%{{transform:scale(1.22) rotate(4deg);opacity:1;}}78%{{transform:scale(.95);}}100%{{transform:scale(1) rotate(0deg);opacity:1;}}}}
@keyframes gFlash{n}{{0%{{box-shadow:inset 0 0 0 0 rgba(0,212,170,0);}}35%{{box-shadow:inset 0 0 80px 0 rgba(0,212,170,0.45);}}100%{{box-shadow:inset 0 0 0 0 rgba(0,212,170,0);}}}}
</style>
<div style="position:relative;overflow:hidden;text-align:center;padding:28px 20px;border-radius:16px;
background:rgba(0,212,170,0.07);border:1px solid rgba(0,212,170,0.3);margin:16px 0;
animation:gFlash{n} 0.9s ease forwards;">
  {confetti}
  <div style="font-family:'Outfit',sans-serif;font-weight:900;font-size:54px;color:#00D4AA;
    letter-spacing:-0.02em;line-height:1;text-shadow:0 0 40px rgba(0,212,170,0.9);
    animation:gPop{n} 0.65s cubic-bezier(0.34,1.56,0.64,1) 0.08s both;">
    ⚽ ¡¡GOOOL!!
  </div>
  <div style="font-family:'JetBrains Mono',monospace;font-size:13px;
    color:rgba(0,212,170,0.7);margin-top:10px;letter-spacing:0.1em;">
    {int(proba*100)}% · La red lo vio venir
  </div>
</div>
"""


# ===================================================================
# LINEUP SCENE  — self-contained HTML for st.components.v1.html()
# ===================================================================
def lineup_scene(is_titular: bool, render_key: str = "") -> str:
    """Returns a complete HTML document for st.components.v1.html(height=400).
    Standing green figure = TITULAR; sitting orange figure on bench = SUPLENTE.
    Animation keyframe name is unique per render_key so it always replays."""
    n = abs(hash(render_key or str(is_titular))) % 999983
    color  = "#00D4AA" if is_titular else "#FF8C42"
    badge  = "TITULAR"  if is_titular else "SUPLENTE"
    bg_col = "rgba(0,212,170,0.14)" if is_titular else "rgba(255,140,66,0.14)"
    glow   = "rgba(0,212,170,0.18)" if is_titular else "rgba(255,140,66,0.14)"
    dy     = "-22px"   if is_titular else "22px"

    if is_titular:
        # Standing figure — upright with jersey number
        figure_svg = f"""
<circle cx="100" cy="42" r="22" fill="none" stroke="{color}" stroke-width="2"/>
<path d="M76 64 L60 94 L78 92 L100 185 L122 92 L140 94 L124 64 Z"
      fill="{bg_col}" stroke="{color}" stroke-width="1.8"/>
<text x="100" y="138" text-anchor="middle" fill="{color}"
      font-size="30" font-weight="900" font-family="sans-serif">11</text>
<line x1="76" y1="78" x2="44" y2="116" stroke="{color}" stroke-width="2"/>
<line x1="124" y1="78" x2="156" y2="116" stroke="{color}" stroke-width="2"/>
<line x1="90" y1="185" x2="82" y2="262" stroke="{color}" stroke-width="2.2"/>
<line x1="110" y1="185" x2="118" y2="262" stroke="{color}" stroke-width="2.2"/>"""
    else:
        # Sitting on bench — bent knees, orange bib, bench below
        figure_svg = f"""
<circle cx="94" cy="46" r="22" fill="none" stroke="{color}" stroke-width="2"/>
<path d="M72 68 L60 94 L76 92 L94 162 L112 92 L128 94 L116 68 Z"
      fill="{bg_col}" stroke="{color}" stroke-width="1.8"/>
<text x="94" y="128" text-anchor="middle" fill="{color}"
      font-size="11" font-family="monospace" letter-spacing="1">VEST</text>
<line x1="72" y1="80" x2="50" y2="106" stroke="{color}" stroke-width="2"/>
<line x1="50" y1="106" x2="54" y2="162" stroke="{color}" stroke-width="2"/>
<line x1="116" y1="80" x2="138" y2="106" stroke="{color}" stroke-width="2"/>
<line x1="138" y1="106" x2="134" y2="162" stroke="{color}" stroke-width="2"/>
<line x1="87" y1="162" x2="72" y2="210" stroke="{color}" stroke-width="2.2"/>
<line x1="72" y1="210" x2="96" y2="214" stroke="{color}" stroke-width="2.2"/>
<line x1="101" y1="162" x2="116" y2="210" stroke="{color}" stroke-width="2.2"/>
<line x1="116" y1="210" x2="140" y2="214" stroke="{color}" stroke-width="2.2"/>
<line x1="28" y1="218" x2="168" y2="218" stroke="{color}" stroke-width="3.5" stroke-opacity="0.5"/>
<line x1="42" y1="218" x2="42" y2="248" stroke="{color}" stroke-width="2.5" stroke-opacity="0.4"/>
<line x1="154" y1="218" x2="154" y2="248" stroke="{color}" stroke-width="2.5" stroke-opacity="0.4"/>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #0F1923; font-family: -apple-system, system-ui, sans-serif; overflow: hidden; }}
  @keyframes pEnter{n} {{
    0%   {{ opacity: 0; transform: translateY({dy}) scale(0.88); }}
    100% {{ opacity: 1; transform: translateY(0)   scale(1);    }}
  }}
  .scene {{
    height: 390px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; overflow: hidden;
    background: radial-gradient(ellipse at center, {glow} 0%, transparent 65%);
  }}
  .fig-wrap {{
    animation: pEnter{n} 0.55s cubic-bezier(0.34,1.56,0.64,1) both;
    display: flex; align-items: center; justify-content: center;
  }}
  .fig-wrap svg {{ width: 170px; height: 290px; }}
  .badge {{
    margin-top: 14px; padding: 5px 22px; border-radius: 999px;
    font-size: 12px; letter-spacing: 0.14em; font-weight: 700;
    text-transform: uppercase; border: 1px solid {color};
    background: {bg_col}; color: {color};
  }}
</style>
</head><body>
<div class="scene">
  <div class="fig-wrap">
    <svg viewBox="0 0 200 270" xmlns="http://www.w3.org/2000/svg">
      {figure_svg}
    </svg>
  </div>
  <div class="badge">{badge}</div>
</div>
</body></html>"""


def lineup_feature_table(goals: float, assists: float, pct: float,
                         mins: float, cond: float, edad: float) -> str:
    """Table showing each feature value and its rough impact on the titular decision."""
    def imp(score: float) -> str:
        if score > 0.65: return "🟢 Alto"
        if score > 0.35: return "🟡 Medio"
        return "🔴 Bajo"

    rows = [
        ("Goles / 90 min",           f"{goals:.2f}",    imp(goals / 1.5)),
        ("Asistencias / 90 min",     f"{assists:.2f}",  imp(assists / 1.0)),
        ("Precisión de pases",       f"{pct:.0f}%",     imp((pct-50)/50)),
        ("Minutos últimos 3 partidos", f"{int(mins)}'", imp(mins/270)),
        ("Condición física (1–10)",  f"{cond:.1f}",     imp((cond-1)/9)),
        ("Edad",                     f"{int(edad)} años", imp(max(0.0, 1-abs(edad-26)/10))),
    ]
    rows_html = "".join(
        f'<div class="lt-row">'
        f'<span class="lt-feat">{feat}</span>'
        f'<span class="lt-val">{val}</span>'
        f'<span class="lt-imp">{imp_txt}</span>'
        f'</div>'
        for feat, val, imp_txt in rows
    )
    return f'<div class="xg-lineup-table">{rows_html}</div>'


# ===================================================================
# INJURY SCENE  — self-contained HTML for st.components.v1.html()
# ===================================================================
def injury_scene(is_injured: bool, render_key: str = "") -> str:
    """Returns a complete HTML document for st.components.v1.html(height=400).
    Standing figure with pulsing green cross = no injury.
    Lying figure on stretcher with red cross = injury risk."""
    n = abs(hash(render_key or str(is_injured))) % 999983
    color  = "#FF4655" if is_injured else "#00D4AA"
    badge  = "EN RIESGO"  if is_injured else "SIN RIESGO"
    bg_col = "rgba(255,70,85,0.14)"  if is_injured else "rgba(0,212,170,0.14)"
    glow   = "rgba(255,70,85,0.20)"  if is_injured else "rgba(0,212,170,0.18)"
    dy     = "22px" if is_injured else "-22px"

    if is_injured:
        # Lying down on a stretcher, red medical cross above
        figure_svg = f"""
<rect x="88" y="8" width="14" height="42" rx="3" fill="{color}" opacity="0.9"/>
<rect x="76" y="20" width="38" height="14" rx="3" fill="{color}" opacity="0.9"/>
<rect x="12" y="188" width="176" height="16" rx="5"
      fill="rgba(255,70,85,0.10)" stroke="{color}" stroke-width="1.5" stroke-opacity="0.55"/>
<line x1="30"  y1="204" x2="30"  y2="232" stroke="{color}" stroke-width="2.5" stroke-opacity="0.4"/>
<line x1="170" y1="204" x2="170" y2="232" stroke="{color}" stroke-width="2.5" stroke-opacity="0.4"/>
<circle cx="158" cy="196" r="17" fill="none" stroke="{color}" stroke-width="2"/>
<line x1="141" y1="196" x2="66"  y2="196" stroke="{color}" stroke-width="2.8"/>
<line x1="66"  y1="196" x2="22"  y2="196" stroke="{color}" stroke-width="2.2"/>
<line x1="102" y1="196" x2="92"  y2="175" stroke="{color}" stroke-width="2"/>
<line x1="102" y1="196" x2="89"  y2="217" stroke="{color}" stroke-width="2"/>"""
    else:
        # Standing figure with pulsing green cross floating above head
        cross_anim = f"crossPulse{n}"
        figure_svg = f"""
<g style="animation:{cross_anim} 2s ease-in-out infinite; transform-origin:100px 30px;">
  <rect x="93" y="8"  width="14" height="44" rx="3" fill="{color}" opacity="0.9"/>
  <rect x="80" y="20" width="40" height="14" rx="3" fill="{color}" opacity="0.9"/>
</g>
<circle cx="100" cy="84" r="21" fill="none" stroke="{color}" stroke-width="2"/>
<line x1="100" y1="105" x2="100" y2="175" stroke="{color}" stroke-width="2.8"/>
<line x1="100" y1="128" x2="64"  y2="155" stroke="{color}" stroke-width="2"/>
<line x1="100" y1="128" x2="136" y2="155" stroke="{color}" stroke-width="2"/>
<line x1="100" y1="175" x2="82"  y2="250" stroke="{color}" stroke-width="2.2"/>
<line x1="100" y1="175" x2="118" y2="250" stroke="{color}" stroke-width="2.2"/>"""

    cross_css = (
        f"@keyframes crossPulse{n} {{"
        "0%,100%{opacity:0.9;filter:drop-shadow(0 0 4px currentColor);}"
        "50%{opacity:1;filter:drop-shadow(0 0 14px currentColor);}}"
    ) if not is_injured else ""

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #0F1923; font-family: -apple-system, system-ui, sans-serif; overflow: hidden; }}
  {cross_css}
  @keyframes injEnter{n} {{
    0%   {{ opacity: 0; transform: translateY({dy}) scale(0.88); }}
    100% {{ opacity: 1; transform: translateY(0)   scale(1);    }}
  }}
  @keyframes redGlow{n} {{
    0%,100% {{ box-shadow: inset 0 0 0 0 rgba(255,70,85,0); }}
    50%     {{ box-shadow: inset 0 0 60px 0 rgba(255,70,85,0.3); }}
  }}
  .scene {{
    height: 390px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; overflow: hidden;
    background: radial-gradient(ellipse at center, {glow} 0%, transparent 65%);
    {"animation: redGlow" + str(n) + " 2.5s ease-in-out infinite;" if is_injured else ""}
  }}
  .fig-wrap {{
    animation: injEnter{n} 0.55s cubic-bezier(0.34,1.56,0.64,1) both;
    display: flex; align-items: center; justify-content: center;
  }}
  .fig-wrap svg {{ width: 170px; height: 290px; }}
  .badge {{
    margin-top: 14px; padding: 5px 22px; border-radius: 999px;
    font-size: 12px; letter-spacing: 0.14em; font-weight: 700;
    text-transform: uppercase; border: 1px solid {color};
    background: {bg_col}; color: {color};
  }}
</style>
</head><body>
<div class="scene">
  <div class="fig-wrap">
    <svg viewBox="0 0 200 270" xmlns="http://www.w3.org/2000/svg">
      {figure_svg}
    </svg>
  </div>
  <div class="badge">{badge}</div>
</div>
</body></html>"""


def injury_feature_table(minutos: float, dias: float, edad: float,
                         inten: float, partidos: float) -> str:
    """Table showing each injury feature value and its risk level."""
    def risk(score: float) -> str:
        if score > 0.65: return "🔴 Alto"
        if score > 0.35: return "🟡 Medio"
        return "🟢 Bajo"

    rows = [
        ("Minutos últimos 3 partidos",        f"{int(minutos)}'", risk(minutos / 270)),
        ("Días desde última lesión",          f"{int(dias)} días", risk(1.0 - min(dias, 365) / 365)),
        ("Edad del jugador",                  f"{int(edad)} años", risk(max(0.0, (edad - 24) / 14))),
        ("Intensidad de entrenamiento (1–10)", f"{inten:.1f}",     risk((inten - 1) / 9)),
        ("Partidos en últimos 30 días",        f"{int(partidos)}",  risk(partidos / 12)),
    ]
    rows_html = "".join(
        f'<div class="lt-row">'
        f'<span class="lt-feat">{feat}</span>'
        f'<span class="lt-val">{val}</span>'
        f'<span class="lt-imp">{risk_txt}</span>'
        f'</div>'
        for feat, val, risk_txt in rows
    )
    return f'<div class="xg-injury-table">{rows_html}</div>'


# ===================================================================
# SABÍAS QUE... CARDS  (curiosidades reales del fútbol + analytics)
# ===================================================================
def sabias_que_dinamico(items: list) -> str:
    """Grid de cards generadas con datos calculados al vuelo.
    items: lista de tuplas (titulo, color, html_text, big_stat, small_label)."""
    cards_html = ""
    for title, color, text, big, small in items:
        cards_html += f"""
<div class="sq-card">
  <div class="sq-head" style="color:{color};">{title}</div>
  <p class="sq-text">{text}</p>
  <div class="sq-stat">
    <div class="sq-big" style="color:{color};">{big}</div>
    <div class="sq-small">{small}</div>
  </div>
</div>"""
    return f"""
<style>
.sq-grid {{
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;
  margin: 8px 0 12px;
}}
@media (max-width: 980px) {{ .sq-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (max-width: 560px) {{ .sq-grid {{ grid-template-columns: 1fr; }} }}
.sq-card {{
  background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent), #1A1A2E;
  border: 1px solid rgba(255,255,255,0.08); border-radius: 14px;
  padding: 22px 22px 18px; display: flex; flex-direction: column;
  transition: border-color .25s, transform .25s;
}}
.sq-card:hover {{ border-color: rgba(255,255,255,0.16); transform: translateY(-2px); }}
.sq-head {{
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 12px;
}}
.sq-text {{
  color: #FFFFFF; font-size: 14px; line-height: 1.6; margin: 0 0 16px; flex: 1;
}}
.sq-stat {{
  border-top: 1px solid rgba(255,255,255,0.08); padding-top: 12px;
  display: flex; align-items: baseline; gap: 12px;
}}
.sq-big {{
  font-family: 'Outfit', sans-serif; font-weight: 800;
  font-size: 30px; line-height: 1; letter-spacing: -0.02em;
}}
.sq-small {{
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  color: #8A9BB0; letter-spacing: 0.06em;
}}
</style>
<div class="sq-grid">{cards_html}</div>
"""


def sabias_que_tab() -> str:
    """6 cards sobre casos reales de IA en el fútbol. Layout full-width con imagen + texto."""
    cards = [
        (
            "Liverpool fichó a Salah con un algoritmo",
            "#00D4AA",
            "El departamento de analytics de Liverpool, liderado por Ian Graham (doctor "
            "en física teórica), identificó a Mohamed Salah y Andy Robertson mediante "
            "modelos estadísticos de calidad de tiro y presión. Con un presupuesto de "
            "analytics de solo £1-2M anuales, Liverpool ganó la Champions League 2019 y "
            "la Premier League 2020 — su primera liga en 30 años.",
            "2 Champions",
            "ganadas con analytics",
            "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
        ),
        (
            "Brentford ascendió sin ojeadores tradicionales",
            "#FFD700",
            "El Brentford FC prescindió de los scouts tradicionales y apostó por un "
            "modelo de datos puro. Su sistema detecta jugadores subvalorados en mercados "
            "como Escandinavia y las ligas menores inglesas usando expected assists (xA) "
            "y datos físicos. Resultado: ascenso a la Premier League en 2021.",
            "£0.5M",
            "presupuesto analytics",
            "https://upload.wikimedia.org/wikipedia/en/2/2a/Brentford_FC_crest.svg",
        ),
        (
            "Arsenal diseñó sus córners con datos",
            "#FF4655",
            "Arteta y su equipo de analytics analizaron miles de situaciones de pelota "
            "parada para diseñar rutinas específicas. La temporada 2023/24, Arsenal fue "
            "el equipo con más goles de córner de toda la Premier League. Cada movimiento "
            "en el área estaba calculado de antemano.",
            "#1 PL",
            "goles de córner 2023/24",
            "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
        ),
        (
            "Messi convertía 35% más de lo esperado",
            "#5EE8C7",
            "En su mejor temporada (2011/12), Messi anotó 50 goles en La Liga. Su xG "
            "promedio por tiro era 0.31, pero convertía a un ritmo de 0.42 — un 35% "
            "por encima de lo que cualquier modelo esperaría. Es la diferencia entre "
            "un buen jugador y el mejor de la historia.",
            "0.42 g/tiro",
            "vs 0.31 xG esperado",
            "https://upload.wikimedia.org/wikipedia/commons/1/1a/24701-soccer-ball-icon.png",
        ),
        (
            "Brighton usó xG para llegar a Europa",
            "#00D4AA",
            "Brighton & Hove Albion, bajo Tony Bloom (jugador profesional de poker y "
            "experto en datos), usó modelos xG para fichar a Moisés Caicedo y Alexis "
            "Mac Allister cuando nadie los quería. Ambos fueron vendidos luego por más "
            "de £250M en total. El xG les dijo que generaban chances de altísima calidad "
            "antes de que sus goles lo demostraran.",
            "+£250M",
            "en ventas con xG",
            "https://upload.wikimedia.org/wikipedia/en/f/fd/Brighton_%26_Hove_Albion_FC.svg",
        ),
        (
            "Midtjylland ganó su primera liga con xG",
            "#FFD700",
            "El FC Midtjylland danés fue uno de los primeros clubes del mundo en "
            "implementar modelos xG de forma sistemática. Usaron el modelo para optimizar "
            "tiros libres y córners, identificar jugadores subvalorados y tomar decisiones "
            "de juego en tiempo real. Resultado: ganaron su primer título de la liga danesa. "
            "El mismo dueño luego replicó el modelo en Brighton.",
            "1er título",
            "en su historia",
            "https://upload.wikimedia.org/wikipedia/en/7/79/FC_Midtjylland_logo.svg",
        ),
    ]

    cards_html = ""
    for title, color, text, big, small, img_url in cards:
        cards_html += f"""
<div class="sq-card">
  <div class="sq-img-wrap">
    <img src="{img_url}" alt="" onerror="this.style.display='none'" />
  </div>
  <div class="sq-content">
    <div class="sq-head" style="color:{color};">{title}</div>
    <p class="sq-text">{text}</p>
    <div class="sq-stat">
      <span class="sq-big" style="color:{color};">{big}</span>
      <span class="sq-small">{small}</span>
    </div>
  </div>
</div>"""

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@400;700;800&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: transparent;
  padding: 4px 2px 12px;
  font-family: 'Outfit', system-ui, sans-serif;
}}
.sq-container {{
  display: flex; flex-direction: column; gap: 14px;
}}
.sq-card {{
  background: linear-gradient(180deg, rgba(255,255,255,0.025), transparent), #1A1A2E;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 18px 22px;
  display: flex;
  flex-direction: row;
  gap: 20px;
  align-items: center;
  transition: border-color .25s, transform .2s;
}}
.sq-card:hover {{
  border-color: rgba(255,255,255,0.20);
  transform: translateY(-2px);
}}
.sq-img-wrap {{
  flex-shrink: 0;
  width: 100px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.03);
  border-radius: 10px;
  padding: 8px;
}}
.sq-img-wrap img {{
  width: 84px;
  height: 84px;
  object-fit: contain;
}}
.sq-content {{
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0;
}}
.sq-head {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 8px;
}}
.sq-text {{
  color: #FFFFFF;
  font-size: 13.5px;
  line-height: 1.65;
  margin-bottom: 14px;
  flex: 1;
}}
.sq-stat {{
  border-top: 1px solid rgba(255,255,255,0.08);
  padding-top: 10px;
  display: flex;
  align-items: baseline;
  gap: 10px;
}}
.sq-big {{
  font-family: 'Outfit', sans-serif;
  font-weight: 800;
  font-size: 26px;
  line-height: 1;
  letter-spacing: -0.02em;
}}
.sq-small {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: #8A9BB0;
  letter-spacing: 0.06em;
}}
</style>
</head>
<body>
<div class="sq-container">
{cards_html}
</div>
</body>
</html>"""


def sabias_que_cards() -> str:
    """Grid de cards con curiosidades reales sobre analytics en clubes top."""
    cards = [
        ("Liverpool",      "#00D4AA",
         "El Liverpool de Klopp pasó de ignorar el xG a basar todas sus contrataciones "
         "en él. Firmaron a Salah cuando su xG indicaba que era el mejor extremo "
         "disponible en Europa.",
         "Salah", "2017 · 0.62 xG/90"),
        ("Arsenal",        "#FFD700",
         "El Arsenal 2023/24 fue el equipo con más goles de corner de la Premier "
         "League. Arteta diseñó cada rutina con modelos de datos.",
         "16", "goles de corner · 2023/24"),
        ("Messi · Barça",  "#FF4655",
         "En su mejor temporada (2011/12), Messi convertía un 42% de sus tiros "
         "esperados. El promedio de la liga era 28%.",
         "42%", "conversión · liga: 28%"),
        ("Bayern Munich",  "#5EE8C7",
         "El Bayern Munich usa modelos de lesiones similares al de esta app para "
         "gestionar la carga de sus jugadores semana a semana.",
         "−27%", "lesiones musculares · 5 temporadas"),
        ("Brentford FC",   "#00D4AA",
         "El Brentford FC ascendió a la Premier League basándose casi exclusivamente "
         "en analytics. No tienen ojeadores tradicionales.",
         "0", "scouts tradicionales en plantilla"),
    ]
    items = ""
    for title, color, text, big, small in cards:
        items += f"""
<div class="sq-card">
  <div class="sq-head" style="color:{color};">{title}</div>
  <p class="sq-text">{text}</p>
  <div class="sq-stat">
    <div class="sq-big" style="color:{color};">{big}</div>
    <div class="sq-small">{small}</div>
  </div>
</div>
"""
    return f"""
<style>
.sq-grid {{
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;
  margin: 8px 0 12px;
}}
@media (max-width: 980px) {{ .sq-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
@media (max-width: 560px) {{ .sq-grid {{ grid-template-columns: 1fr; }} }}
.sq-card {{
  background: linear-gradient(180deg, rgba(255,255,255,0.02), transparent), #1A1A2E;
  border: 1px solid rgba(255,255,255,0.08); border-radius: 14px;
  padding: 22px 22px 18px; display: flex; flex-direction: column;
  transition: border-color .25s, transform .25s;
}}
.sq-card:hover {{ border-color: rgba(255,255,255,0.16); transform: translateY(-2px); }}
.sq-head {{
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 12px;
}}
.sq-text {{
  color: #FFFFFF; font-size: 14px; line-height: 1.6; margin: 0 0 16px; flex: 1;
}}
.sq-stat {{
  border-top: 1px solid rgba(255,255,255,0.08); padding-top: 12px;
  display: flex; align-items: baseline; gap: 12px;
}}
.sq-big {{
  font-family: 'Outfit', sans-serif; font-weight: 800;
  font-size: 32px; line-height: 1; letter-spacing: -0.02em;
}}
.sq-small {{
  font-family: 'JetBrains Mono', monospace; font-size: 11px;
  color: #8A9BB0; letter-spacing: 0.06em;
}}
</style>
<div class="sq-grid">{items}</div>
"""


# ===================================================================
# GLOSARIO CARD
# ===================================================================
def glosario_card(name: str, sym: str, definicion: str, formula: str,
                  bajo: str, alto: str, analogia: str, tip: str) -> str:
    return f"""
<div class="xg-glos">
  <div class="hd"><span class="name">{name}</span><span class="sym">{sym}</span></div>
  <p class="def">{definicion}</p>
  <div class="formula">{formula}</div>
  <div class="row">
    <div class="cell"><div class="h lo"><span class="dot"></span>Valor bajo</div><div class="b">{bajo}</div></div>
    <div class="cell"><div class="h hi"><span class="dot"></span>Valor alto</div><div class="b">{alto}</div></div>
  </div>
  <div class="analogy">{analogia}</div>
  <div class="tip"><strong>Tip:</strong> {tip}</div>
</div>
"""


# ===================================================================
# FOOTER
# ===================================================================
def footer() -> str:
    return """
<div class="xg-foot">
  <div>
    <div class="brand"><span class="dot"></span><b>xG/Lab</b></div>
    <p style="margin:10px 0 0; max-width: 380px;">
      Implementado con <strong style="color:#fff">NumPy puro</strong> — sin TensorFlow ni scikit-learn.<br/>
      Stack: Streamlit ≥ 1.30 · Python ≥ 3.10 · Plotly · Pandas.
    </p>
  </div>
  <div>
    <div style="font-family:var(--font-mono); font-size:11px; letter-spacing:0.15em; text-transform:uppercase; color:var(--text-2); margin-bottom:10px;">TP Integrador</div>
    <div>Introducción a las Redes Neuronales</div>
    <div>Opción B — MLP con backpropagation · 2026</div>
  </div>
</div>
"""
