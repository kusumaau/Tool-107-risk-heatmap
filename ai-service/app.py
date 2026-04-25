from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes.describe import describe_bp

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

app.register_blueprint(describe_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)