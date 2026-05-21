import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>GCP Flask App</title>
            <style>
                body { font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9; }
                .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #4285F4; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>✨ Hello Deam team!</h1>
                <p>Your Flask application is running on <b>Google Cloud Run</b>.</p>
                <p>Deployed via Cloud Build without a Dockerfile.</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Cloud Run sets the PORT environment variable. 
    # If running locally, it defaults to 8080.
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
