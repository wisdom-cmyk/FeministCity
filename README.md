# 젠더와 도시계획 · 2주차 발표 대시보드

피피티처럼 한 페이지씩 넘기는 Streamlit 발표 자료입니다. 표지 → 클릭 가능한 목차 → 두 책의 도입 페이지와 본문 → 토론 순서로 구성됩니다.

## 실행

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## 내용을 수정하는 곳

모든 발표 내용은 `content.py`에 있습니다.

- 본문 수정: `SLIDES` 안의 해당 페이지 `blocks` 내용을 바꿉니다.
- 페이지 추가: `SLIDES` 맨 끝에 `s(...)` 항목을 추가합니다. 목차와 페이지 번호는 자동으로 바뀝니다.
- 토론 주제 추가: `DISCUSSION_TOPICS`에 아래 항목을 추가합니다.

```python
{"status":"ready", "heading":"토론 대주제 2", "body":"토론할 내용"},
```

- 표지 변경: `assets/`에 새 이미지를 넣고 `BOOKS`의 `cover` 경로를 바꿉니다.

## GitHub와 Streamlit 배포

1. GitHub에서 새 저장소를 만듭니다.
2. 이 폴더의 `app.py`, `content.py`, `requirements.txt`, `assets/`를 올립니다.
3. [Streamlit Community Cloud](https://share.streamlit.io/)에서 저장소와 `app.py`를 선택해 배포합니다.
