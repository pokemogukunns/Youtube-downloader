from flask import Flask
from flask_cors import CORS
from get_link import get_download_link
from download import download_mp3, download_mp4

app = Flask(__name__)
CORS(app)  # CORSを許可

# Blueprintを登録
app.register_blueprint(get_download_link)
app.register_blueprint(download_mp3)
app.register_blueprint(download_mp4)

if __name__ == '__main__':
    app.run(debug=True)
