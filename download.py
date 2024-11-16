from flask import Blueprint, send_from_directory, jsonify
import os

# Blueprintを作成
download_mp3 = Blueprint('download_mp3', __name__)
download_mp4 = Blueprint('download_mp4', __name__)

DOWNLOAD_FOLDER = './downloads'  # ダウンロードフォルダを設定

# MP3ダウンロード用エンドポイント
@download_mp3.route('/download/<video_id>/mp3', methods=['GET'])
def download_audio(video_id):
    try:
        file_path = os.path.join(DOWNLOAD_FOLDER, f"{video_id}.mp3")
        if os.path.exists(file_path):
            return send_from_directory(DOWNLOAD_FOLDER, f"{video_id}.mp3", as_attachment=True)
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# MP4ダウンロード用エンドポイント
@download_mp4.route('/download/<video_id>/mp4', methods=['GET'])
def download_video(video_id):
    try:
        file_path = os.path.join(DOWNLOAD_FOLDER, f"{video_id}.mp4")
        if os.path.exists(file_path):
            return send_from_directory(DOWNLOAD_FOLDER, f"{video_id}.mp4", as_attachment=True)
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
