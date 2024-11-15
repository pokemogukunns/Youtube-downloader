import os
import yt_dlp
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORSを許可

@app.route('/download/<video_id>/mp3', methods=['GET'])
def download_mp3(video_id):
    file_path = f'downloads/{video_id}.mp3'

    if not os.path.exists(file_path):
        try:
            # MP3形式でダウンロード
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': file_path,  # ダウンロード先
                'quiet': True
            }
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            return f"Error downloading video: {str(e)}", 500

    return send_from_directory(directory='downloads', path=f'{video_id}.mp3')

@app.route('/download/<video_id>/mp4', methods=['GET'])
def download_mp4(video_id):
    file_path = f'downloads/{video_id}.mp4'

    if not os.path.exists(file_path):
        try:
            # MP4形式でダウンロード
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',  # 動画と音声の最良品質でダウンロード
                'outtmpl': file_path,  # ダウンロード先
                'quiet': True
            }
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except Exception as e:
            return f"Error downloading video: {str(e)}", 500

    return send_from_directory(directory='downloads', path=f'{video_id}.mp4')

if __name__ == '__main__':
    app.run(debug=True)
