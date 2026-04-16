import subprocess
import time
import sys

def run_scripts():
    print("Starting serve.py...")
    serve_proc = subprocess.Popen([sys.executable, "./utils/serve.py"])

    print("Waiting for 3 seconds...")
    time.sleep(3)

    print("Starting mouse.py...")
    mouse_proc = subprocess.Popen([sys.executable, "./utils/mouse.py"])

    print("Starting gui.py...")
    gui_proc = subprocess.Popen([sys.executable, "./utils/gui.py"])

    # gui.py 종료될 때까지 대기
    gui_proc.wait()

    print("gui.py has exited. Cleaning up...")

    # 필요하면 다른 프로세스 종료
    serve_proc.terminate()
    mouse_proc.terminate()

if __name__ == "__main__":
    run_scripts()
