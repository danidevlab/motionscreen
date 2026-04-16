import subprocess
import time
import sys

def run_scripts():
    # 1. ./utils/serve.py 실행 (백그라운드)
    print("Starting serve.py...")
    # 윈도우/리눅스 호환성을 위해 sys.executable (현재 파이썬 인터프리터) 사용
    serve_proc = subprocess.Popen([sys.executable, "./utils/serve.py"])

    # 2. 3초 대기
    print("Waiting for 3 seconds...")
    time.sleep(3)

    # 3. ./utils/gui.py 실행
    print("Starting gui.py...")
    gui_proc = subprocess.Popen([sys.executable, "./utils/gui.py"])

    # 필요시 gui_proc.wait()를 사용하여 gui가 종료될 때까지 대기 가능

if __name__ == "__main__":
    run_scripts()
