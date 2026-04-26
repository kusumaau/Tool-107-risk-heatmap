from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "model": "llama-3.3-70b-versatile",
        "uptime": "running"
    }), 200