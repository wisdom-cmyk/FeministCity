# 젠더와 도시계획 · 2주차 발제 대시보드

Streamlit으로 만든 발표용 대시보드입니다. 문서에 정리된 읽기 13개를 각각 독립 화면으로 구성했습니다.

## 실행

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

브라우저에서 열린 화면의 `이전`·`다음` 버튼으로 발표를 진행합니다.

## 내용 넣기

`content.py`만 편집하면 됩니다. 각 읽기 항목의 다음 네 칸을 실제 발제문으로 바꾸세요.

- `claim`: 핵심 주장
- `urban_link`: 젠더·도시계획 연결점
- `notes`: 사례·개념·인용 메모
- `draft`: 긴 요약 또는 인용문 초안

읽기를 추가하거나 순서를 바꾸려면 `READINGS` 목록의 항목을 수정하세요. 목차와 발표 페이지 번호는 자동으로 업데이트됩니다.

## GitHub 및 Streamlit Community Cloud 배포

1. GitHub에서 새 저장소를 만든 뒤 이 폴더의 파일을 올립니다.
2. [Streamlit Community Cloud](https://share.streamlit.io/)에서 저장소를 선택합니다.
3. 시작 파일로 `app.py`를 지정해 배포합니다.

저장소 이름 예시: `feminist-city-week2`.
