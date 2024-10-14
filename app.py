import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

# ログ設定
logging.basicConfig(filename='alert_logs.log', level=logging.INFO)


# Webhookエンドポイントの作成
@app.route('/')
def webhook():
    if request.method == 'POST':
        try:
            # リクエストボディのパース
            data = request.get_json()
            logging.info(f"Received alert: {data}")

            # レスポンスを返す
            return jsonify({"status": "success"}), 200
        except Exception as e:
            logging.error(f"Error: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

# アプリの実行
if __name__ == '__main__':
   app.run()

