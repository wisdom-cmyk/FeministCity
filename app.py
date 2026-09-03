import streamlit as st

from content import DISCUSSION, READINGS, SESSION


st.set_page_config(
    page_title=SESSION["title"],
    page_icon="◒",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def inject_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
        html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif; }
        .stApp { background: #f7f4ee; color: #1d2a28; }
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { max-width: 1180px; padding-top: 4.1rem; padding-bottom: 2rem; }
        .eyebrow { color: #c05034; font-family: 'DM Mono', monospace; font-size: .78rem; letter-spacing: .09em; text-transform: uppercase; }
        .hero { min-height: 64vh; display:flex; flex-direction:column; justify-content:center; }
        .hero h1 { font-family:'Playfair Display','Noto Sans KR',serif; font-size: clamp(3rem, 8vw, 6.8rem); line-height: .98; margin: .5rem 0 1.4rem; letter-spacing:-.045em; }
        .hero p { max-width: 680px; font-size: 1.2rem; line-height: 1.8; color:#52615d; }
        .page-title { font-family:'Playfair Display','Noto Sans KR',serif; font-size:clamp(2.2rem,5vw,4.2rem); line-height:1.1; letter-spacing:-.035em; margin:.6rem 0 1rem; }
        .meta { color:#64716d; font-size:.92rem; }
        .rule { border:0; border-top:1px solid #cfc9bc; margin:2rem 0; }
        .card { background:#fffdfa; border:1px solid #e3ddd1; border-radius:14px; padding:1.35rem 1.45rem; min-height: 170px; }
        .card h3 { margin-top:0; color:#c05034; font-size:.9rem; letter-spacing:.03em; }
        .card p, .card li { color:#43514e; line-height:1.65; }
        .toc-item { border-top:1px solid #d9d2c5; padding:1rem .1rem; font-size:1.05rem; }
        .toc-num { font-family:'DM Mono',monospace; color:#c05034; display:inline-block; width:3.2rem; }
        .quote { border-left:4px solid #c05034; padding:.8rem 1.2rem; background:#f0ebe0; color:#3d4b47; font-size:1.05rem; line-height:1.7; }
        div.stButton > button { border-radius:99px; border:1px solid #1d2a28; background:transparent; color:#1d2a28; padding:.45rem 1rem; }
        div.stButton > button:hover { background:#1d2a28; color:#fffdfa; border-color:#1d2a28; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def go_to(index: int):
    st.session_state.page_index = max(0, min(index, len(READINGS) + 2))


def nav(current: int):
    left, center, right = st.columns([1, 5, 1])
    with left:
        if current and st.button("← 이전", key=f"prev-{current}"):
            go_to(current - 1)
            st.rerun()
    with center:
        st.markdown(f"<p style='text-align:center' class='meta'>{current + 1} / {len(READINGS) + 3}</p>", unsafe_allow_html=True)
    with right:
        if current < len(READINGS) + 2 and st.button("다음 →", key=f"next-{current}"):
            go_to(current + 1)
            st.rerun()


def cover():
    st.markdown("<section class='hero'>", unsafe_allow_html=True)
    st.markdown(f"<div class='eyebrow'>{SESSION['course']} · {SESSION['week']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h1>{SESSION['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p>{SESSION['subtitle']}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='meta'>{SESSION['date']} &nbsp;·&nbsp; {SESSION['presenters']}</p>", unsafe_allow_html=True)
    st.markdown("</section>", unsafe_allow_html=True)


def toc():
    st.markdown("<div class='eyebrow'>00 / Table of contents</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='page-title'>오늘의 읽기</h1>", unsafe_allow_html=True)
    grouped = {}
    for number, reading in enumerate(READINGS, 1):
        grouped.setdefault(reading["source"], []).append((number, reading))
    for source, items in grouped.items():
        st.markdown(f"<p class='meta' style='margin-top:1.6rem'>{source}</p>", unsafe_allow_html=True)
        for number, reading in items:
            st.markdown(f"<div class='toc-item'><span class='toc-num'>{number:02d}</span>{reading['title']} <span class='meta'>— {reading['presenter']}</span></div>", unsafe_allow_html=True)


def reading_page(reading: dict, number: int):
    st.markdown(f"<div class='eyebrow'>{number:02d} / {reading['kind']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='page-title'>{reading['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='meta'>{reading['citation']} &nbsp;·&nbsp; 발제: {reading['presenter']}</p>", unsafe_allow_html=True)
    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    a, b, c = st.columns(3)
    cards = [
        ("핵심 주장", reading["claim"]),
        ("젠더·도시 연결점", reading["urban_link"]),
        ("발제 메모", reading["notes"]),
    ]
    for column, (heading, body) in zip((a, b, c), cards):
        with column:
            st.markdown(f"<div class='card'><h3>{heading}</h3><p>{body}</p></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<div class='quote'><strong>발제 질문</strong><br>{reading['question']}</div>", unsafe_allow_html=True)
    with st.expander("요약·인용문을 채우는 곳", expanded=False):
        st.markdown("이 영역은 발표 준비용입니다. 아래 내용을 `content.py`의 해당 읽기 항목에 붙여 넣으면 화면이 갱신됩니다.")
        st.text_area("요약 초안", value=reading["draft"], height=170, key=f"draft-{number}")


def discussion():
    st.markdown("<div class='eyebrow'>Last / Discussion</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='page-title'>토론: 페미니즘은 도시를 어떻게 다시 읽는가?</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='meta'>{DISCUSSION['context']}</p>", unsafe_allow_html=True)
    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    for index, prompt in enumerate(DISCUSSION["questions"], 1):
        st.markdown(f"<div class='card' style='margin-bottom:1rem'><h3>질문 {index:02d}</h3><p>{prompt}</p></div>", unsafe_allow_html=True)
    st.markdown("<br><div class='quote'><strong>마무리</strong><br>각 읽기에서 포착한 도시의 규칙·배제·돌봄·저항을 연결해, ‘누구를 위한 도시인가’를 함께 다시 묻습니다.</div>", unsafe_allow_html=True)


inject_style()
if "page_index" not in st.session_state:
    st.session_state.page_index = 0

page = st.session_state.page_index
if page == 0:
    cover()
elif page == 1:
    toc()
elif page <= len(READINGS) + 1:
    reading_page(READINGS[page - 2], page - 1)
else:
    discussion()
nav(page)
