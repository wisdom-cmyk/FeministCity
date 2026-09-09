from pathlib import Path
import re

import streamlit as st

from content import BOOKS, DISCUSSION_TOPICS, SESSION, SLIDES

st.set_page_config(page_title="젠더와 도시계획 · 2주차", page_icon="◒", layout="wide")
KERN_COUNT = sum(slide["book"] == "kern" for slide in SLIDES)
BOOK2_INTRO = KERN_COUNT + 3
URBAN_INDEX = len(SLIDES) + 4
DISCUSSION_INDEX = len(SLIDES) + 5
THANKS_INDEX = len(SLIDES) + 6

STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Nanum+Gothic:wght@400;700;800&family=Playfair+Display:wght@600;700&display=swap');
:root { --ink:#2b1635; --paper:#f7eef9; --purple:#a85fc1; --purple-dark:#6f3c82; --pink:#f5cee9; --orange:#c8553d; --blue:#294d68; --muted:#685c6e; --line:#b984c5; }
.stApp { background:radial-gradient(circle at 95% 5%,#ead6ee 0,transparent 25%),radial-gradient(circle at 4% 94%,#f4d7d0 0,transparent 21%),var(--paper); color:var(--ink); } html,body,[class*="css"] { font-family:'Nanum Gothic',sans-serif; }
#MainMenu,footer,header { visibility:hidden; }.block-container { max-width:1180px; padding:2.5rem 3rem 1rem; }
.eyebrow { font-family:'DM Mono',monospace;color:var(--purple-dark);font-size:.78rem;letter-spacing:.1em;text-transform:uppercase; }
.slide-title { font-family:'Nanum Gothic',sans-serif;font-weight:800;font-size:clamp(2.1rem,4.5vw,4.25rem);letter-spacing:-.055em;line-height:1.18;margin:.45rem 0 .7rem; }
.deck-title { font-family:'Nanum Gothic',sans-serif;font-weight:800;font-size:clamp(3.6rem,8vw,7.4rem);letter-spacing:-.06em;line-height:1;margin:.5rem 0 1.2rem; }
.subtitle,.meta { color:var(--muted);line-height:1.7; }.subtitle { font-size:1.15rem;max-width:700px; }.rule { border:0;border-top:1px solid var(--line);margin:1.5rem 0 1.7rem; }
.panel { background:#fffdf9;border:2px solid var(--purple-dark);border-radius:20px;padding:.82rem 1.45rem;min-height:120px;box-shadow:7px 7px 0 #e1bde7; }.panel h3 { font-size:1.22rem;color:var(--purple-dark);font-weight:800;letter-spacing:-.02em;margin:0 0 .5rem; }.panel p,.panel li { color:#332b37;font-size:1rem;line-height:1.72; }.body-point { position:relative;padding-left:1.1rem; }.body-point:before { content:'•';position:absolute;left:0;color:var(--purple);font-weight:700; }
.lead { font-size:1.2rem;line-height:1.72;color:#29413d;max-width:960px; }.quote { border-left:5px solid var(--purple-dark);padding:.85rem 1.2rem;background:#f1ddf5;color:#332b37;font-size:1.08rem;line-height:1.65; }.keyline { font-family:'DM Mono',monospace;color:var(--blue);letter-spacing:.02em;padding:1rem 0 .2rem; }
.toc-group { color:var(--blue);font-size:.85rem;font-weight:700;letter-spacing:.04em;margin:1.4rem 0 .4rem; }.placeholder { border:1px dashed #ae9d84;border-radius:13px;color:#7b7164;padding:1.4rem;min-height:175px;display:flex;align-items:center;justify-content:center;text-align:center; }.slide-count { color:#7a867f;font-family:'DM Mono',monospace;font-size:.78rem;text-align:center;padding-top:.7rem; }.cover-mark { font-size:4.2rem;color:var(--orange);line-height:1;margin-bottom:1rem; }
div.stButton>button { background:#fffdf9;color:var(--ink);border:2px solid var(--purple-dark);border-radius:999px;padding:.4rem 1.05rem;white-space:normal;height:auto; }div.stButton>button:hover { background:var(--purple-dark);color:white;border-color:var(--purple-dark); }.toc-title div.stButton>button { font-size:1.55rem;font-weight:800;text-align:left;border-radius:14px;background:#f5dff5;padding:1rem; }.toc-detail { padding:.7rem 1rem;border-left:4px solid var(--purple);line-height:1.65;color:#42534f; }.toc-list { padding-left:1.1rem;text-indent:-1.1rem;margin:.42rem 0; }.middle-title { font-size:1.62rem;font-weight:800;line-height:1.35;margin:0 0 1.1rem;color:var(--purple-dark); }.highlight { font-size:1.18rem;font-weight:700;line-height:1.68;color:#332b37;border-left:5px solid var(--purple-dark);padding:.85rem 1.15rem;margin:0 0 1.35rem;background:#f1ddf5; }.bilingual-ko { color:var(--muted);font-size:1.16rem;margin:-.35rem 0 1rem; }.data-table { width:100%;border-collapse:collapse;margin-top:.7rem; }.data-table th,.data-table td { border:1px solid var(--line);padding:.75rem;vertical-align:top;text-align:left;line-height:1.55; }.data-table th { background:#ead3ef;color:var(--purple-dark);width:28%; }.discussion-question { font-size:1.36rem;font-weight:800;line-height:1.65;color:var(--purple-dark);padding:.8rem 0; }
</style>
"""

def set_slide(index): st.session_state.slide = max(0, min(index, THANKS_INDEX))

def show_image(relative_path, **options):
    """assets 폴더 또는 저장소 최상위에 둔 이미지를 모두 지원한다."""
    project_root = Path(__file__).parent
    image_path = project_root / relative_path
    root_level_path = project_root / Path(relative_path).name
    if image_path.is_file():
        st.image(image_path.read_bytes(), **options)
    elif root_level_path.is_file():
        st.image(root_level_path.read_bytes(), **options)
    else:
        st.info(f"이미지 파일이 없습니다: {Path(relative_path).name}")

def header(slide, index):
    st.markdown(f"<div class='eyebrow'>{slide['section']} · {index:02d}</div>", unsafe_allow_html=True)
    bilingual = re.match(r"(.+) \((.+)\)$", slide["title"])
    if bilingual:
        st.markdown(f"<div class='slide-title'>{bilingual.group(1)}</div><div class='bilingual-ko'>({bilingual.group(2)})</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='slide-title'>{slide['title']}</div>", unsafe_allow_html=True)
    middle_titles = {3:"임산부의 도시 경험",4:"도시는 어떻게 성역할을 강화하는가?",5:"여성의 우정은 도시 생존의 인프라",6:"여성친화적 도시 - 친구와 함께",7:"도시에서 홀로 존재하기",8:"공적인 여성 공간",9:"화장실",10:"시위는 도시를 찾는 페미니스트 실천",11:"‘여성의 시위’는 누구를 포함하는가",12:"운동 내부의 성별화된 노동과 연대",14:"공간은 사회적 위계를 ‘설계’한다",15:"이분법적 공간 질서 / 영역성",16:"성별화된 건축 비판 / 도시계획적 함의",17:"사무용 고층건물 (office tower)",18:"백화점 (department store) / 쇼핑 몰 (shopping mall)",19:"산과 병원 (Maternity hospital)",20:"도시의 공공공간은 모든 사람에게 같은 공간이 아니다",21:"페미니즘 관점에서 도시 바라보기"}
    if index in middle_titles: st.markdown(f"<div class='middle-title'>{middle_titles[index]}</div>", unsafe_allow_html=True)
    if slide.get("subtitle"): st.markdown(f"<div class='subtitle'>{slide['subtitle']}</div>", unsafe_allow_html=True)
    st.markdown("<hr class='rule'>", unsafe_allow_html=True)

def blocks(items, cols=2):
    if len(items) == 1:
        cols = 1
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
    highlights_top = {5:"“여성의 우정은 연애와 결혼의 부차적 관계가 아니라, 도시에서 살아가고 독립하며 정체성을 형성하게 하는 핵심적 관계망이다.”",7:"공적인 것으로 여겨지는 도시 공간의 점유는 권력과 밀접한 관계를 맺는다. 공간에 누가 있을 수 있는지, 누가 공간과 어울리지 않는지는 사회에 존재하는 차별의 구조를 드러낸다.",10:"“시위는 여성이 도시에 속할 권리, 안전할 권리, 생계를 유지할 권리, 지역사회를 대표할 권리를 집단적으로 요구하는 공간이다.”"}
    if index in highlights_top: st.markdown(f"<div class='highlight'>{highlights_top[index]}</div>", unsafe_allow_html=True)
    wide_pages = {5,6,7,8,9,11,12,14,15,16,17,19,21}
    items = slide["blocks"]
    if index == 5:
        # 핵심 문장은 상단 강조로 두고, 설명은 하나의 넓은 카드로 합친다.
        quote = "<p class='body-point'>“여성의 우정은 연애와 결혼의 부차적 관계가 아니라, 도시에서 살아가고 독립하며 정체성을 형성하게 하는 핵심적 관계망이다.”</p>"
        items = [{"heading":"", "body":"".join(block["body"] for block in slide["blocks"]).replace(quote, "")}]
    if index == 6:
        # 비교표는 카드 안에서 별도로 그린다.
        items = slide["blocks"][:1]
    if index == 7:
        items = [{"heading":block["heading"], "body":block["body"].replace("<p class='body-point'>공적인 것으로 여겨지는 도시 공간의 점유는 권력과 밀접한 관계를 맺는다. 공간에 누가 있을 수 있는지, 누가 공간과 어울리지 않는지는 사회에 존재하는 차별의 구조를 드러낸다.</p>", "")} for block in slide["blocks"]]
    if index == 10:
        items = [{"heading":block["heading"], "body":block["body"].replace("<p class='body-point'>“시위는 여성이 도시에 속할 권리, 안전할 권리, 생계를 유지할 권리, 지역사회를 대표할 권리를 집단적으로 요구하는 공간이다.”</p>", "")} for block in slide["blocks"]]
    if index == 14:
        items = [{"heading":"", "body":"".join(block["body"] for block in slide["blocks"]).replace("<p class='body-point'>누가 설계하는가 → 누가 접근하는가 → 누가 통제하는가 → 누가 배제되는가</p>", "")}]
    if index in {17, 19}:
        items = [{"heading":"", "body":"".join(block["body"] for block in slide["blocks"])}]
    if index == 12:
        conclusion = "<p class='body-point'>=> 여성 친화적 도시는 도시는 저절로 만들어지지 않는다. 도시의 변화는 저항과 집단행동에서 시작되며, 그 운동은 동시에 더 포용적이고 돌봄을 고려하며 교차적인 방식으로 조직되어야 한다.</p>"
        items = [{"heading":"", "body":"".join(block["body"] for block in slide["blocks"][1:]).replace(conclusion, "")}]
    if index == 12:
        st.markdown("<table class='data-table'><tr><th>남성 역할</th><th>여성 역할</th></tr><tr><td>공식 지도자, 대변인, 비전 제시자<br>의사결정과 언론 노출<br>정치적 ‘주체’로 인정</td><td>가가호호 조직, 전단 제작, 음식 준비<br>감정노동, 관계 조정, 돌봄과 내무<br>보이지 않는 실무, 지원 인력</td></tr></table><br>", unsafe_allow_html=True)
        items = slide["blocks"][1:]
    if index == 16:
        items = slide["blocks"][:1]
    blocks(items, 1 if layout == "stack" or index in wide_pages else 2)
    highlights_bottom = {6:"✦ 여성 친화적 도시는 여성들이 친구와 함께 안전하게 머물고, 서로 돌보며, 결혼 여부와 무관하게 삶을 조직할 수 있도록 지원하는 도시여야 한다.",11:"✦ 페미니스트 시위는 단지 ‘여성을 위한’ 공간이어서는 안 되며, 서로 다른 위험과 조건을 지닌 사람들의 참여를 보장하는 교차적 공간이어야 한다.",12:"✦ 여성 친화적 도시는 도시는 저절로 만들어지지 않는다. 도시의 변화는 저항과 집단행동에서 시작되며, 그 운동은 동시에 더 포용적이고 돌봄을 고려하며 교차적인 방식으로 조직되어야 한다.",14:"누가 설계하는가 → 누가 접근하는가 → 누가 통제하는가 → 누가 배제되는가"}
    if index in highlights_bottom: st.markdown(f"<div class='highlight'>{highlights_bottom[index]}</div>", unsafe_allow_html=True)
    if index == 6:
        st.markdown("<table class='data-table'><tr><th>기존 도시의 전제</th><th>여성주의적 도시</th></tr><tr><td>부부, 핵가족 중심 주거<br>사적 가정이 돌봄의 중심<br>소비 공간 중심의 만남<br>결혼을 성인의 정상 경로로 상정</td><td>친구와 비혈연 공동체를 위한 다양한 주거<br>친구 관계망을 지지하는 공공 돌봄<br>무료, 안전, 접근 가능한 공공 만남의 공간<br>다양한 친밀 관계와 독립적 삶의 경로 인정</td></tr></table>", unsafe_allow_html=True)
    if index == 15:
        st.markdown("<table class='data-table'><tr><th>권력과 우월성</th><th>종속과 열등성</th></tr><tr><td>남성</td><td>여성</td></tr><tr><td>공적 공간·일터</td><td>사적 공간·가정</td></tr><tr><td>도시·문명</td><td>자연·황야</td></tr><tr><td>위·앞·오른쪽</td><td>아래·뒤·왼쪽</td></tr><tr><td>이성·생산·통제</td><td>감정·돌봄·의존</td></tr></table>", unsafe_allow_html=True)
    if index == 16:
        st.markdown("<table class='data-table'><tr><th>질문</th><th>도시계획적 고려</th></tr><tr><td>누가 이 공간을 이용하는가?</td><td>성별, 연령, 장애, 계급, 이주 지위에 따른 서로 다른 경험을 고려</td></tr><tr><td>주거와 일터는 어떻게 분리되는가?</td><td>돌봄·노동·휴식·이 양립 가능한 근린 및 주거 환경 마련</td></tr><tr><td>공공공간은 안전한가?</td><td>이동 경로, 조명, 화장실, 대중교통, 체류 공간의 접근성 개선</td></tr><tr><td>누가 계획을 결정하는가?</td><td>설계·계획·정책의 의사결정에 다양한 이용자의 참여 보장</td></tr></table><div class='highlight'>✦ 여성주의 도시계획의 과제는 ‘여성을 위한 별도 공간’을 덧붙이는 것이 아니라, 도시의 설계·이용·통제를 조직하는 권력관계 자체를 바꾸는 데 있다.</div>", unsafe_allow_html=True)
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
        st.markdown("<div class='toc-title'>", unsafe_allow_html=True)
        if st.button("1. 여자를 위한 도시는 없다", key="toc-kern", use_container_width=True): set_slide(2); st.rerun()
        st.markdown("</div><div class='toc-detail'>레슬리 컨 지음, 황가한 역, 2022, 여자를 위한 도시는 없다, 열린책들, (5장 제외) (Kern, Leslie, 2020, <em>Feminist City</em>, Verso).<br><br><div class='toc-list'>– 1장, 엄마들의 도시</div><div class='toc-list'>– 2장, 친구들의 도시</div><div class='toc-list'>– 3장, 혼자만의 도시</div><div class='toc-list'>– 4장, 시위의 도시</div></div>", unsafe_allow_html=True)
    with middle:
        st.markdown("<div class='toc-title'>", unsafe_allow_html=True)
        if st.button("2. Discrimination by Design", key="toc-weisman", use_container_width=True): set_slide(BOOK2_INTRO); st.rerun()
        st.markdown("</div><div class='toc-detail'>Leslie Weisman, 1992, <em>Discrimination by Design</em>, University of Illinois Press. (1–3장)<br><br><div class='toc-list'>– 1장, The Spatial Caste System: Design for Social Inequality</div><div class='toc-list'>– 2장, Public Architecture and Social Status</div><div class='toc-list'>– 3장, The Private Use of Public Space</div></div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div class='toc-title'>", unsafe_allow_html=True)
        if st.button("3. 토론", key="toc-discussion", use_container_width=True): set_slide(DISCUSSION_INDEX); st.rerun()
        st.markdown("</div><div class='toc-detail'>Feminisms for our time! - Urban Matters Journal</div>", unsafe_allow_html=True)

def intro(book, index):
    left,right = st.columns([1.05,1.15], gap="large")
    with left: show_image(book["cover"], use_container_width=True)
    with right:
        st.markdown(f"<div class='eyebrow'>{book['label']} · {index:02d}</div><div class='slide-title'>{book['title']}</div><div class='subtitle'>{book['citation']}</div><hr class='rule'>", unsafe_allow_html=True)
        with st.container(border=True):
            photo, bio = st.columns([.38, .62])
            with photo: show_image(book["portrait"], width=180)
            with bio: st.markdown(f"<div class='lead'>{book['author']}</div>{book['bio']}", unsafe_allow_html=True)

def discussion():
    st.markdown("<div class='eyebrow'>Discussion · last</div><div class='slide-title'>토론</div><hr class='rule'>", unsafe_allow_html=True)
    for topic in DISCUSSION_TOPICS[1:]:
        if topic["status"] == "ready" and topic["heading"] == "토론 대주제 1":
            st.markdown("<div class='middle-title'>토론 대주제 1</div>", unsafe_allow_html=True)
            left, right = st.columns(2)
            with left: st.markdown("<div class='panel'><div class='discussion-question'>• 페미니즘 관점으로 도시를 연구한다는 것은 무엇인가?</div></div>", unsafe_allow_html=True)
            with right: st.markdown("<div class='panel'><div class='discussion-question'>• 그 사회적·학술적 장점은 무엇인가?</div></div>", unsafe_allow_html=True)
        elif topic["status"] == "ready": st.markdown(f"<div class='panel' style='margin-bottom:1rem'><h3>{topic['heading']}</h3><div class='discussion-question'>{topic['body']}</div></div>", unsafe_allow_html=True)
        else: st.markdown(f"<div class='placeholder'>{topic['body']}</div><br>", unsafe_allow_html=True)

def urban_matters():
    st.markdown("<div class='eyebrow'>Urban Matters Journal · 2025년 8월호</div><div class='slide-title'>Feminisms for our time!</div><hr class='rule'>", unsafe_allow_html=True)
    cols = st.columns(3)
    for column, image_name in zip(cols, ("assets/urban-matters-articles-1.png", "assets/urban-matters-articles-2.png", "assets/urban-matters-articles-3.png")):
        with column: show_image(image_name, use_container_width=True)

def thanks():
    st.markdown("<div style='min-height:66vh;display:flex;align-items:center;justify-content:center'><div style='text-align:center'><div class='cover-mark'>✦</div><div class='deck-title'>감사합니다.</div></div></div>", unsafe_allow_html=True)

def navigation(current):
    st.markdown("<hr class='rule' style='margin-top:1.6rem;margin-bottom:.4rem'>", unsafe_allow_html=True); a,b,c=st.columns([1,4,1])
    with a:
        if current>0 and st.button("← 이전", key=f"back-{current}"): set_slide(current-1); st.rerun()
    with b:
        if st.button("목차", key=f"toc-return-{current}"): set_slide(1); st.rerun()
        st.markdown(f"<div class='slide-count'>{current+1} / {THANKS_INDEX+1}</div>", unsafe_allow_html=True)
    with c:
        if current<THANKS_INDEX and st.button("다음 →", key=f"next-{current}"): set_slide(current+1); st.rerun()

st.markdown(STYLE, unsafe_allow_html=True)
if "slide" not in st.session_state: st.session_state.slide=0
current=st.session_state.slide
if current==0: cover()
elif current==1: toc()
elif current in (2,BOOK2_INTRO): intro(BOOKS[0] if current==2 else BOOKS[1],current)
elif current==URBAN_INDEX: urban_matters()
elif current==DISCUSSION_INDEX: discussion()
elif current==THANKS_INDEX: thanks()
else:
    item_index=current-3 if current<BOOK2_INTRO else current-4
    body_slide(SLIDES[item_index],current)
navigation(current)
