from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# templates 폴더의 절대 경로를 가져옵니다.
TEMPLATE_DIR = os.path.abspath("./templates/")

@app.route('/')
def index():
    # 루트 접속 시 기본적으로 index.html을 보여줍니다.
    return send_from_directory(TEMPLATE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # 사용자가 요청한 경로(<path:filename>)에 있는 파일을 폴더에서 찾아 반환합니다.
    return send_from_directory(TEMPLATE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
