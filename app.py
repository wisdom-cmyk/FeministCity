from pathlib import Path

import streamlit as st

from content import BOOKS, DISCUSSION_TOPICS, SESSION, SLIDES

st.set_page_config(page_title="젠더와 도시계획 · 2주차", page_icon="◒", layout="wide")
KERN_COUNT = sum(slide["book"] == "kern" for slide in SLIDES)
BOOK2_INTRO = KERN_COUNT + 3
URBAN_INDEX = len(SLIDES) + 4
DISCUSSION_INDEX = len(SLIDES) + 5

STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
:root { --ink:#152827; --paper:#f5f1e9; --orange:#c8553d; --blue:#294d68; --muted:#61706d; --line:#d5cdbf; }
.stApp { background:var(--paper); color:var(--ink); } html,body,[class*="css"] { font-family:'Noto Sans KR',sans-serif; }
#MainMenu,footer,header { visibility:hidden; }.block-container { max-width:1180px; padding:2.5rem 3rem 1rem; }
.eyebrow { font-family:'DM Mono',monospace;color:var(--orange);font-size:.78rem;letter-spacing:.1em;text-transform:uppercase; }
.slide-title { font-family:'Playfair Display','Noto Sans KR',serif;font-size:clamp(2.1rem,4.5vw,4.25rem);letter-spacing:-.045em;line-height:1.12;margin:.45rem 0 .7rem; }
.deck-title { font-family:'Playfair Display','Noto Sans KR',serif;font-size:clamp(3.6rem,8vw,7.4rem);letter-spacing:-.06em;line-height:.92;margin:.5rem 0 1.2rem; }
.subtitle,.meta { color:var(--muted);line-height:1.7; }.subtitle { font-size:1.15rem;max-width:700px; }.rule { border:0;border-top:1px solid var(--line);margin:1.5rem 0 1.7rem; }
.panel { background:#fffdf9;border:1px solid var(--line);border-radius:13px;padding:1.3rem 1.45rem;min-height:235px; }.panel h3 { font-size:.83rem;color:var(--orange);letter-spacing:.04em;margin:0 0 .7rem; }.panel p,.panel li { color:#354642;font-size:1rem;line-height:1.72; }
.lead { font-size:1.2rem;line-height:1.72;color:#29413d;max-width:960px; }.quote { border-left:4px solid var(--orange);padding:.85rem 1.2rem;background:#ece6d9;color:#33433f;font-size:1.08rem;line-height:1.65; }.keyline { font-family:'DM Mono',monospace;color:var(--blue);letter-spacing:.02em;padding:1rem 0 .2rem; }
.toc-group { color:var(--blue);font-size:.85rem;font-weight:700;letter-spacing:.04em;margin:1.4rem 0 .4rem; }.placeholder { border:1px dashed #ae9d84;border-radius:13px;color:#7b7164;padding:1.4rem;min-height:175px;display:flex;align-items:center;justify-content:center;text-align:center; }.slide-count { color:#7a867f;font-family:'DM Mono',monospace;font-size:.78rem;text-align:center;padding-top:.7rem; }.cover-mark { font-size:4.2rem;color:var(--orange);line-height:1;margin-bottom:1rem; }
div.stButton>button { background:transparent;color:var(--ink);border:1px solid var(--ink);border-radius:999px;padding:.4rem 1.05rem; }div.stButton>button:hover { background:var(--ink);color:white;border-color:var(--ink); }.toc-button div.stButton>button { width:100%;text-align:left;border-radius:9px;border-color:var(--line);background:#fffdf9;padding:.7rem .9rem;margin:.1rem 0; }
</style>
"""

def set_slide(index): st.session_state.slide = max(0, min(index, DISCUSSION_INDEX))

def show_image(relative_path, **options):
    """Cloud 배포에서도 프로젝트 폴더 안의 이미지를 안전하게 읽는다."""
    image_path = Path(__file__).parent / relative_path
    if image_path.is_file():
        st.image(image_path.read_bytes(), **options)
    else:
        st.info(f"이미지 파일이 없습니다: {relative_path}")

def header(slide, index):
    st.markdown(f"<div class='eyebrow'>{slide['section']} · {index:02d}</div><div class='slide-title'>{slide['title']}</div>", unsafe_allow_html=True)
    if slide.get("subtitle"): st.markdown(f"<div class='subtitle'>{slide['subtitle']}</div>", unsafe_allow_html=True)
    st.markdown("<hr class='rule'>", unsafe_allow_html=True)

def blocks(items, cols=2):
    for start in range(0, len(items), cols):
        row = st.columns(cols)
        for col, item in zip(row, items[start:start+cols]):
            with col: st.markdown(f"<div class='panel'><h3>{item['heading']}</h3>{item['body']}</div>", unsafe_allow_html=True)

def body_slide(slide, index):
    header(slide, index); layout = slide.get("layout", "split")
    if layout == "quote":
        st.markdown(f"<div class='quote'>“{slide['quote']}”</div><br><div class='lead'>{slide['lead']}</div>", unsafe_allow_html=True)
    elif layout in ("stack", "flow"):
        if slide.get("lead"): st.markdown(f"<div class='lead'>{slide['lead']}</div>", unsafe_allow_html=True)
        if layout == "flow": st.markdown(f"<div class='keyline'>{slide['flow']}</div>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    blocks(slide["blocks"], 1 if layout == "stack" else 2)
    if slide.get("takeaway"): st.markdown(f"<br><div class='quote'>{slide['takeaway']}</div>", unsafe_allow_html=True)

def cover():
    left, right = st.columns([1.45, .55], gap="large")
    with left:
        st.markdown(f"<div style='min-height:66vh;display:flex;flex-direction:column;justify-content:center'><div class='eyebrow'>{SESSION['course']} · {SESSION['week']}</div><div class='deck-title'>{SESSION['title']}</div><div class='subtitle'>{SESSION['subtitle']}</div><br><div class='meta'>{SESSION['date']} · {SESSION['presenters']}</div></div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div style='padding-top:4rem'>", unsafe_allow_html=True)
        show_image("assets/rose-hero.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

def toc():
    st.markdown("<div class='eyebrow'>Contents</div><div class='slide-title'>목차</div><hr class='rule'>", unsafe_allow_html=True)
    left, middle, right = st.columns(3, gap="large")
    with left:
        if st.button("1. 레슬리 컨 지음, 황가한 역, 2022, 여자를 위한 도시는 없다, 열린책들, (5장 제외) (Kern, Leslie, 2020, Feminist City, Verso).", key="toc-kern", use_container_width=True): set_slide(2); st.rerun()
        st.markdown("<p>– 1장, 엄마들의 도시</p><p>– 2장, 친구들의 도시</p><p>– 3장, 혼자만의 도시</p><p>– 4장, 시위의 도시</p>", unsafe_allow_html=True)
    with middle:
        if st.button("2. Leslie Weisman, 1992, Discrimination by Design, University of Illinois Press. (1–3장)", key="toc-weisman", use_container_width=True): set_slide(BOOK2_INTRO); st.rerun()
        st.markdown("<p>– 1장, The Spatial Caste System: Design for Social Inequality</p><p>– 2장, Public Architecture and Social Status</p><p>– 3장, The Private Use of Public Space</p>", unsafe_allow_html=True)
    with right:
        if st.button("3. 토론", key="toc-discussion", use_container_width=True): set_slide(DISCUSSION_INDEX); st.rerun()
        st.markdown("<p>Feminisms for our time! - Urban Matters Journal 읽고 토론하기</p>", unsafe_allow_html=True)

def intro(book, index):
    left,middle,right = st.columns([.75,.75,1.5], gap="large")
    with left: show_image(book["cover"], use_container_width=True)
    with middle: show_image(book["portrait"], use_container_width=True)
    with right: st.markdown(f"<div class='eyebrow'>{book['label']} · {index:02d}</div><div class='slide-title'>{book['title']}</div><div class='subtitle'>{book['citation']}</div><hr class='rule'><div class='lead'>{book['author']}</div><br>{book['bio']}", unsafe_allow_html=True)

def discussion():
    st.markdown("<div class='eyebrow'>Discussion · last</div><div class='slide-title'>토론</div><hr class='rule'>", unsafe_allow_html=True)
    for topic in DISCUSSION_TOPICS:
        if topic["status"] == "ready": st.markdown(f"<div class='panel' style='margin-bottom:1rem'><h3>{topic['heading']}</h3><p>{topic['body']}</p></div>", unsafe_allow_html=True)
        else: st.markdown(f"<div class='placeholder'>{topic['body']}</div><br>", unsafe_allow_html=True)

def urban_matters():
    st.markdown("<div class='eyebrow'>Urban Matters Journal</div><div class='slide-title'>Feminisms for our time!</div><hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<div class='panel'><h3>Urban Matters Journal · 2025년 8월호</h3><p>Feminisms for our time!</p></div>", unsafe_allow_html=True)
    st.link_button("Urban Matters Journal 특집호 열기", "https://urbanmattersjournal.com/issue/feminisms-forourtimes/")

def navigation(current):
    st.markdown("<hr class='rule' style='margin-top:1.6rem;margin-bottom:.4rem'>", unsafe_allow_html=True); a,b,c=st.columns([1,4,1])
    with a:
        if current>0 and st.button("← 이전", key=f"back-{current}"): set_slide(current-1); st.rerun()
    with b:
        if st.button("목차", key=f"toc-return-{current}"): set_slide(1); st.rerun()
        st.markdown(f"<div class='slide-count'>{current+1} / {DISCUSSION_INDEX+1}</div>", unsafe_allow_html=True)
    with c:
        if current<DISCUSSION_INDEX and st.button("다음 →", key=f"next-{current}"): set_slide(current+1); st.rerun()

st.markdown(STYLE, unsafe_allow_html=True)
if "slide" not in st.session_state: st.session_state.slide=0
current=st.session_state.slide
if current==0: cover()
elif current==1: toc()
elif current in (2,BOOK2_INTRO): intro(BOOKS[0] if current==2 else BOOKS[1],current)
elif current==URBAN_INDEX: urban_matters()
elif current==DISCUSSION_INDEX: discussion()
else:
    item_index=current-3 if current<BOOK2_INTRO else current-4
    body_slide(SLIDES[item_index],current)
navigation(current)
