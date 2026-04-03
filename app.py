import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Zomato Sentiment Analyzer",
    page_icon="🍽️",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
}

/* Force override Streamlit default button styles */
button {
    background-color: #1A1A1A !important;
    color: #FFFFFF !important;
    border: 1.5px solid rgba(255,255,255,0.12) !important;
}

button p { color: #FFFFFF !important; }

.stApp {
    background: #0D0D0D;
    color: #F1FAEE !important;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding: 0rem 2rem 4rem !important;
    max-width: 800px !important;
}

/* ── TEXTAREA ── */
.stTextArea textarea {
    background: #1A1A1A !important;
    border: 1.5px solid rgba(230,57,70,0.25) !important;
    border-radius: 14px !important;
    color: #F1FAEE !important;
    font-size: 15px !important;
    font-family: 'DM Sans', sans-serif !important;
    line-height: 1.7 !important;
    padding: 16px !important;
    transition: border-color 0.3s !important;
}

.stTextArea textarea:focus {
    border-color: rgba(230,57,70,0.7) !important;
    box-shadow: 0 0 0 3px rgba(230,57,70,0.1) !important;
}

.stTextArea textarea::placeholder {
    color: rgba(255,255,255,0.2) !important;
}

.stTextArea label {
    color: #A8DADC !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── BUTTONS ── */
.stButton > button,
.stButton > button:focus,
.stButton > button:active,
button[kind="secondary"],
button[kind="primary"] {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 12px !important;
    transition: all 0.25s ease !important;
    width: 100% !important;
    background-color: #1A1A1A !important;
    background-image: none !important;
    color: #FFFFFF !important;
    border: 1.5px solid rgba(255,255,255,0.12) !important;
    font-size: 13px !important;
    height: 44px !important;
}

.stButton > button:hover {
    background-color: #2A1A1A !important;
    border-color: rgba(230,57,70,0.5) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
}

div[data-testid="column"] .stButton > button {
    background-color: #1A1A1A !important;
    background-image: none !important;
    border: 1.5px solid rgba(255,255,255,0.12) !important;
    color: #FFFFFF !important;
    font-size: 13px !important;
    height: 44px !important;
}

div[data-testid="column"] .stButton > button:hover {
    background-color: rgba(230,57,70,0.15) !important;
    border-color: rgba(230,57,70,0.5) !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
}

div[data-testid="column"] .stButton > button p,
div[data-testid="column"] .stButton > button span {
    color: #FFFFFF !important;
}

/* ── METRICS ── */
[data-testid="metric-container"] {
    background: #1A1A1A !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 16px !important;
    padding: 18px 14px !important;
    text-align: center !important;
}

[data-testid="metric-container"] label {
    color: #A8DADC !important;
    font-size: 10px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 600 !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #F1FAEE !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    font-family: 'Playfair Display', serif !important;
}

.stSuccess > div, .stError > div {
    border-radius: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}

.stSpinner > div { border-top-color: #E63946 !important; }

/* ── CUSTOM HTML ELEMENTS ── */
.hero-wrap {
    text-align: center;
    padding: 3.5rem 1rem 2rem;
}

.hero-badge {
    display: inline-block;
    background: rgba(230,57,70,0.1);
    border: 1px solid rgba(230,57,70,0.3);
    color: #F4A261;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    padding: 7px 20px;
    border-radius: 100px;
    margin-bottom: 22px;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(42px, 7vw, 66px);
    font-weight: 900;
    color: #F1FAEE;
    line-height: 1.05;
    margin-bottom: 14px;
}

.hero-title em {
    font-style: italic;
    color: #E63946;
}

.hero-sub {
    font-size: 12px;
    color: rgba(255,255,255,0.25);
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

.hero-line {
    display: flex;
    align-items: center;
    gap: 16px;
    margin: 0 auto 2.5rem;
    max-width: 280px;
}

.hero-line-bar { flex: 1; height: 1px; background: rgba(255,255,255,0.08); }

.hero-line-dot {
    width: 8px; height: 8px;
    background: #E63946;
    border-radius: 50%;
    box-shadow: 0 0 14px rgba(230,57,70,0.9);
}

.section-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.22);
    text-align: center;
    margin-bottom: 14px;
}

.analyse-btn-wrap {
    margin-top: 16px;
}

.analyse-btn-wrap .stButton > button {
    background: linear-gradient(135deg, #B71C1C 0%, #7F0000 100%) !important;
    color: white !important;
    height: 56px !important;
    font-size: 17px !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 8px 30px rgba(230,57,70,0.4) !important;
    border-radius: 14px !important;
}

.analyse-btn-wrap .stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 14px 40px rgba(230,57,70,0.55) !important;
}

.analyse-btn-wrap .stButton > button:disabled {
    background: #1A1A1A !important;
    color: rgba(255,255,255,0.2) !important;
    box-shadow: none !important;
    transform: none !important;
}

.tip {
    font-size: 11px;
    color: rgba(255,255,255,0.16);
    text-align: center;
    margin-top: 10px;
    font-style: italic;
}

.result-emoji {
    font-size: 68px;
    text-align: center;
    display: block;
    margin: 1rem 0 0.5rem;
    animation: popIn 0.5s cubic-bezier(0.34,1.56,0.64,1) both;
}

@keyframes popIn {
    from { transform: scale(0.3); opacity: 0; }
    to   { transform: scale(1);   opacity: 1; }
}

.result-title-pos {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 900;
    color: #06D6A0;
    text-align: center;
    margin-bottom: 6px;
}

.result-title-neg {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 900;
    color: #E63946;
    text-align: center;
    margin-bottom: 6px;
}

.result-desc {
    text-align: center;
    font-size: 14px;
    color: rgba(255,255,255,0.3);
    margin-bottom: 1.4rem;
}

.quote-box {
    background: linear-gradient(135deg, rgba(230,57,70,0.06), rgba(244,162,97,0.03));
    border: 1px solid rgba(230,57,70,0.18);
    border-radius: 14px;
    padding: 20px 22px 16px 36px;
    font-size: 15px;
    color: rgba(255,255,255,0.5);
    font-style: italic;
    line-height: 1.75;
    margin: 0 0 1.4rem;
    position: relative;
}

.quote-box::before {
    content: '"';
    font-family: 'Playfair Display', serif;
    font-size: 72px;
    color: rgba(230,57,70,0.18);
    position: absolute;
    top: -14px;
    left: 12px;
    line-height: 1;
}

.conf-label {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.2);
    margin-bottom: 8px;
}

.conf-track {
    background: rgba(255,255,255,0.06);
    border-radius: 100px;
    height: 5px;
    margin-bottom: 1.6rem;
    overflow: hidden;
}

.conf-fill-pos {
    height: 100%;
    width: 88%;
    background: linear-gradient(90deg, #06D6A0, #00B4D8);
    border-radius: 100px;
}

.conf-fill-neg {
    height: 100%;
    width: 22%;
    background: linear-gradient(90deg, #E63946, #F4A261);
    border-radius: 100px;
}

.divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin: 2rem 0;
}

/* ── FOOTER ── */
.footer-wrap {
    text-align: center;
    margin-top: 4rem;
    padding-top: 2.5rem;
    border-top: 1px solid rgba(255,255,255,0.06);
}

.footer-name {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 900;
    color: #F1FAEE;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
}

.footer-name span {
    color: #E63946;
    font-style: italic;
}

.footer-role {
    font-size: 11px;
    color: rgba(255,255,255,0.2);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 18px;
}

.footer-stack {
    display: flex;
    justify-content: center;
    gap: 8px;
    flex-wrap: wrap;
}

.stack-pill {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 11px;
    color: rgba(255,255,255,0.25);
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">🍽️ AI Powered Review Intelligence</div>
    <div class="hero-title">Zomato<br><em>Sentiment</em> Analyzer</div>
    <div class="hero-sub">Word2Vec &nbsp;·&nbsp; Linear SVM &nbsp;·&nbsp; FastAPI &nbsp;·&nbsp; Streamlit</div>
    <div class="hero-line">
        <div class="hero-line-bar"></div>
        <div class="hero-line-dot"></div>
        <div class="hero-line-bar"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── EXAMPLES ──
st.markdown('<div class="section-label">✦ Quick Examples</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

if col1.button("👍 Try Positive Review"):
    st.session_state.review = "The biryani was absolutely amazing! Delivery was super fast and food was piping hot. Will definitely order again!"

if col2.button("👎 Try Negative Review"):
    st.session_state.review = "Worst experience ever. Food arrived cold and 2 hours late. Completely inedible. Never ordering again."

# ── TEXT AREA ──
st.write("")
review = st.text_area(
    "📝 YOUR REVIEW",
    value       = st.session_state.get("review", ""),
    placeholder = "e.g. The paneer butter masala was rich, creamy and absolutely delicious...",
    height      = 150
)

# ── ANALYSE BUTTON ──
st.markdown('<div class="analyse-btn-wrap">', unsafe_allow_html=True)
button_clicked = st.button(
    "🔍 Analyse Sentiment",
    disabled = (review.strip() == "")
)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="tip">✦ Works best with English reviews · Short or detailed both work!</div>', unsafe_allow_html=True)

# ── RESULT ──
if button_clicked:
    with st.spinner("Analysing your review..."):
        try:
            response = requests.post(
                API_URL,
                json    = {"review": review},
                timeout = 5
            )

            if response.status_code == 200:
                result    = response.json()
                sentiment = result.get("sentiment", "Positive")

                st.markdown('<hr class="divider">', unsafe_allow_html=True)

                if sentiment == "Positive":
                    st.markdown('<span class="result-emoji">😊</span>', unsafe_allow_html=True)
                    st.markdown('<div class="result-title-pos">Positive Sentiment</div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-desc">Customers loved this experience — keep it up!</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="quote-box">{review}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="conf-label">Confidence Score</div>', unsafe_allow_html=True)
                    st.markdown('<div class="conf-track"><div class="conf-fill-pos"></div></div>', unsafe_allow_html=True)
                    st.success("🎉 Great review! This restaurant is winning customers.")
                    st.balloons()

                else:
                    st.markdown('<span class="result-emoji">😞</span>', unsafe_allow_html=True)
                    st.markdown('<div class="result-title-neg">Negative Sentiment</div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-desc">This review highlights areas that need improvement.</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="quote-box">{review}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="conf-label">Confidence Score</div>', unsafe_allow_html=True)
                    st.markdown('<div class="conf-track"><div class="conf-fill-neg"></div></div>', unsafe_allow_html=True)
                    st.error("⚠️ Negative feedback detected — attention needed!")

                # ── METRICS ──
                st.write("")
                word_count = len(review.split())
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Prediction",  sentiment)
                m2.metric("Words",       word_count)
                m3.metric("Model",       "Linear SVM")
                m4.metric("Embeddings",  "Word2Vec")

            else:
                st.error("🚨 Server error! Please try again.")

        except Exception:
            st.error("🚨 Backend not running! Start FastAPI server first.")
            st.code("uvicorn api:app --reload", language="bash")

# ── FOOTER ──
st.markdown('<div class="footer-wrap"><div class="footer-name">Developed by <span>Leela Krishna</span></div><div class="footer-role">Major Project &nbsp;·&nbsp; NLP &nbsp;·&nbsp; 2025</div><div class="footer-stack"><span class="stack-pill">Word2Vec</span><span class="stack-pill">Linear SVM</span><span class="stack-pill">FastAPI</span><span class="stack-pill">Streamlit</span><span class="stack-pill">Scikit-Learn</span></div></div>', unsafe_allow_html=True)
