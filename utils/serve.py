from flask import Flask, send_from_directory
import os
import platform

app = Flask(__name__)

# templates 폴더의 절대 경로를 설정합니다.
TEMPLATE_DIR = os.path.abspath("./templates/")

@app.route('/')
def index():
    # 루트 접속 시 index.html 반환
    return send_from_directory(TEMPLATE_DIR, 'index.html')

@app.route('/poweroffapi/')
def power_off():
    print("전원 종료를 시작합니다..")
    print("운영체제를 확인합니다...")
    # 현재 운영체제 확인 (Windows, Linux 등)
    system_os = platform.system()
    print(f"운영체제: {system_os}")
    try:
        if system_os == "Windows":
            # 윈도우 종료 명령어 (/s: 종료, /t 0: 0초 후 실행)
            os.system("shutdown /s /t 0")
        elif system_os == "Linux" or system_os == "Darwin": # Darwin은 macOS
            # 리눅스/맥 종료 명령어 (-h now: 지금 즉시 종료)
            os.system("sudo shutdown -h now")
        else:
            return f"지원하지 않는 OS입니다: {system_os}", 400
            
        return "시스템을 종료합니다...", 200
    except Exception as e:
        return f"오류 발생: {str(e)}", 500
@app.route('/<path:filename>')
def serve_static(filename):
    # 정적 파일 서빙
    return send_from_directory(TEMPLATE_DIR, filename)

if __name__ == '__main__':
    # Flask 서버 실행
    app.run(host='0.0.0.0', port=5000)
