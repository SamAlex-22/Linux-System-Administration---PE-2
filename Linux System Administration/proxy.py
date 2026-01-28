from flask import Flask, request, Response
import requests

app = Flask(__name__)

# OpenAI URL
CHATGPT_URL = "https://chat.openai.com"

# Fake it as Google traffic
TRUSTED_PROXY = "https://www.google.com"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def proxy(path):
    try:
        target_url = f"{CHATGPT_URL}/{path}"
        headers = {
            "User-Agent": request.headers.get("User-Agent"),
            "Referer": TRUSTED_PROXY,
        }
        response = requests.get(target_url, headers=headers, allow_redirects=True)
        return Response(response.content, response.status_code, response.headers.items())
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
