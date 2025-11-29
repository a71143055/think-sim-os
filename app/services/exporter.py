import os
import zipfile
from typing import Dict
from app.config import settings

WINDOWS_README = """\
Windows 실행 자료
=================

이 패키지는 ThinkSimOS에서 생성된 사고 시뮬레이션 결과를 포함합니다.

- config.json: 설정 값
- snapshot.json: 시뮬레이션 스냅샷
- run.bat: Windows에서 간단 실행/검증 예시
"""

RUN_BAT = """@echo off
echo Running Thought Simulation Artifact
type README.txt
echo Showing config.json:
type config.json
echo Showing snapshot.json (head):
more +1 snapshot.json
echo Done.
pause
"""

def create_windows_artifact(session_id: int, workspace_paths: Dict) -> str:
    export_dir = settings.EXPORT_DIR
    os.makedirs(export_dir, exist_ok=True)
    zip_path = os.path.join(export_dir, f"session_{session_id}_windows.zip")

    base = workspace_paths["base"]
    # 준비 파일: README.txt, config.json, snapshot.json, run.bat
    readme = os.path.join(base, "README.txt")
    with open(readme, "w", encoding="utf-8") as f:
        f.write(WINDOWS_README)

    runbat = os.path.join(base, "run.bat")
    with open(runbat, "w", encoding="cp949", newline="\r\n") as f:
        f.write(RUN_BAT)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for fname in ["README.txt", "config.json", "snapshot.json", "run.bat", "synthesis_brief.md"]:
            z.write(os.path.join(base, fname), arcname=fname)

    return zip_path
