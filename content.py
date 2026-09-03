"""발표 내용 데이터. 각 항목의 대괄호 문구를 실제 요약으로 바꿔 사용하세요."""

SESSION = {
    "course": "젠더와 도시계획",
    "week": "Week 2 · 페미니스트 도시 비평",
    "title": "Feminist City",
    "subtitle": "젠더의 관점으로 도시의 공간, 일상, 권력과 가능성을 다시 읽기",
    "date": "2026. 09. 10",
    "presenters": "이지혜 · 장윤정 · 장준하",
}

KERN = "Leslie Kern, Feminist City / 『여자를 위한 도시는 없다』 (2022, 황가한 옮김)"
WEISMAN = "Leslie Weisman, Discrimination by Design (1992)"
URBAN = "Urban Matters Journal, ‘Feminisms for our time!’ (2025.08)"

def reading(title, presenter, source, citation, kind="읽기", question="이 글이 전제하는 ‘도시의 사용자’는 누구인가?"):
    return {
        "title": title, "presenter": presenter, "source": source, "citation": citation,
        "kind": kind,
        "claim": "[저자의 핵심 주장 1–2문장을 입력하세요.]",
        "urban_link": "[공간·이동·주거·안전·돌봄 등 도시계획과의 연결점을 입력하세요.]",
        "notes": "[발표에서 강조할 사례, 개념, 인용문을 입력하세요.]",
        "question": question,
        "draft": "[요약 초안 또는 인용문을 여기에 붙여 넣으세요.]",
    }


READINGS = [
    reading("1장. 엄마들의 도시", "장윤정", KERN, "Leslie Kern, ‘City of Moms’", "장", "돌봄 노동과 이동의 관점에서 도시는 어떻게 다르게 경험되는가?"),
    reading("2장. 친구들의 도시", "이지혜", KERN, "Leslie Kern, ‘City of Friends’", "장", "친구 관계와 상호돌봄은 도시 생활의 어떤 인프라가 될 수 있는가?"),
    reading("3장. 혼자만의 도시", "장준하", KERN, "Leslie Kern, ‘City of One’", "장", "혼자 걷고, 살고, 머무를 권리는 누구에게 동등하게 주어지는가?"),
    reading("4장. 시위의 도시", "이지혜", KERN, "Leslie Kern, ‘City of Protest’", "장", "시위와 집회는 도시 공간의 공적 성격을 어떻게 재구성하는가?"),
    reading("1장. The Spatial Caste System: Design for Social Inequality", "이지혜", WEISMAN, "Leslie Weisman, Discrimination by Design, ch. 1", "장", "공간 설계는 사회적 위계를 어떻게 자연스러운 것으로 보이게 하는가?"),
    reading("2장. Public Architecture and Social Status", "장준하", WEISMAN, "Leslie Weisman, Discrimination by Design, ch. 2", "장", "공공건축은 누구의 지위와 경험을 중심에 놓는가?"),
    reading("3장. The Private Use of Public Space", "장윤정", WEISMAN, "Leslie Weisman, Discrimination by Design, ch. 3", "장", "공공 공간의 사적 점유는 젠더화된 접근성을 어떻게 만들고 있는가?"),
    reading("The Safety Premium: Gendered Costs and Control in Student Housing in Dehradun", "장윤정", URBAN, "Dikchha Tiwari · Uttam Kumar Roy", "논문", "안전을 이유로 한 비용과 통제는 누구에게, 어떤 방식으로 배분되는가?"),
    reading("Urban Invisibles: Feminist perspectives on marginalization and resistance in Nairobi and Addis Ababa through the lens of embodied research practices", "장윤정", URBAN, "Annapia Debarry · Valentine Opanga", "논문", "체화된 연구 실천은 ‘보이지 않는’ 도시 경험을 어떻게 드러내는가?"),
    reading("Beyond the shelter, one finds care: Queer kinship and communality in Dutch squats", "장준하", URBAN, "Maya Borean", "논문", "퀴어 친족성과 공동체는 주거를 ‘돌봄’의 공간으로 어떻게 바꾸는가?"),
    reading("Reclaiming the City. Feminist and Queer Resistance to ‘Anti-gender’ Mobilisations", "장준하", URBAN, "Marianne Blidon", "논문", "반(反)젠더 동원에 대한 저항은 도시의 공공성을 어떻게 되찾는가?"),
    reading("The Flâneuse in Turkish and Indian Fiction: Urban Inequality and Female Migrants", "이지혜", URBAN, "Pallavi Narayan", "논문", "여성 이주자의 도시 보행과 서사는 어떤 불평등을 드러내는가?"),
    reading("Straddling and resisting the scholar-community action boundaries", "이지혜", URBAN, "Sinead D’Silva", "논문", "연구자와 지역사회 사이의 경계를 넘나드는 실천은 무엇을 가능하게 하는가?"),
]

DISCUSSION = {
    "context": "Urban Matters의 특집 ‘Feminisms for our time!’ 수록 6편을 함께 읽고 토론합니다.",
    "questions": [
        "페미니즘 관점으로 도시를 연구한다는 것은, 연구 대상·방법·질문을 어떻게 바꾸는가?",
        "이 관점이 사회적으로 제공하는 장점은 무엇이며, 어떤 정책·설계의 변화를 요청하는가?",
        "학문적으로 무엇을 더 보이게 하고, 반대로 어떤 한계나 긴장을 남기는가?",
        "오늘 읽기들 가운데 한국의 도시계획 현장에 가장 시급히 연결할 수 있는 문제는 무엇인가?",
    ],
}
