from flask import Flask
from get_link import get_download_link  # Blueprintのインポート
from download import download_mp3, download_mp4
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORSを許可

# YouTube動画の情報とダウンロードリンクを取得するエンドポイント
app.register_blueprint(get_download_link)

# 動画のMP3をダウンロードするエンドポイント
app.register_blueprint(download_mp3)

# 動画のMP4をダウンロードするエンドポイント
app.register_blueprint(download_mp4)

if __name__ == '__main__':
    app.run(debug=True)
