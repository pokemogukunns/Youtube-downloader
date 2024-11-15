import os
import random
import string
from googleapiclient.discovery import build
from flask import Flask, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)  # CORSを許可

# YouTube Data APIのAPIキーを設定
API_KEY = os.getenv("YOUTUBE_API_KEY")  # 環境変数からAPIキーを取得

# YouTube APIクライアントの作成
youtube = build('youtube', 'v3', developerKey=API_KEY)

@app.route('/api/<video_id>', methods=['GET'])
def get_download_link(video_id):
    try:
        # YouTube Data APIで動画情報を取得
        request = youtube.videos().list(part='snippet,contentDetails', id=video_id)
        response = request.execute()

        if 'items' not in response or len(response['items']) == 0:
            return jsonify({"error": "Video not found"}), 404

        video_info = response['items'][0]['snippet']
        video_title = video_info['title']
        thumbnail_url = video_info['thumbnails']['high']['url']  # 高解像度サムネイル

        # yt-dlpでMP3とMP4のダウンロードリンクを取得
        ydl_opts = {
            'format': 'bestaudio/best',  # 音声の最良品質で
            'outtmpl': f'downloads/{video_id}.mp3',
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 音声のダウンロードリンクを取得
            info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            mp3_link = f"/download/{video_id}/mp3"  # MP3ダウンロードリンク

        ydl_opts['format'] = 'bestvideo+bestaudio/best'  # 動画+音声の最良品質
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 動画のダウンロードリンクを取得
            info_dict = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            mp4_link = f"/download/{video_id}/mp4"  # MP4ダウンロードリンク

        # ダウンロードリンクと動画情報を返す
        return jsonify({
            "video_title": video_title,
            "thumbnail_url": thumbnail_url,
            "mp3_download_url": mp3_link,
            "mp4_download_url": mp4_link
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
