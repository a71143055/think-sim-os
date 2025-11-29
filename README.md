# ThinkSimOS (Web OS for Thought Simulation)

- Python: 3.11

## Run (Dev)
1. `python -m venv .venv && source .venv/bin/activate` (Windows: `.venv\Scripts\activate`)
2. `pip install -r requirements.txt`
3. `python -m app.init_db`
4. `uvicorn app.main:app --reload`
5. 브라우저에서 `http://localhost:8000` 접속

## Flow
- `/chat/new`: 생각 입력 → 세션 생성
- 세션 페이지: 규칙(JSON) 적용 → 시뮬레이션 Run → 스냅샷 저장 + 워크스페이스 파일 생성
- Windows 패키지: 버튼 클릭으로 ZIP 생성(`/data/exports`) 후 다운로드
- Web OS: `/os/env`에서 워크스페이스 디렉터리 탐색

## Artifacts
- Workspace (per session): `/workspace/session_{id}`
    - `config.json`, `snapshot.json`, `README.txt`, `synthesis_brief.md`
- Windows ZIP: `/data/exports/session_{id}_windows.zip`
    - 포함: `README.txt`, `config.json`, `snapshot.json`, `run.bat`, `synthesis_brief.md`

## Notes
- 이는 MVP입니다. 시뮬레이션 규칙(가치/전이/감정)을 확장하면 더 정밀한 사고 흐름을 재현할 수 있습니다.
