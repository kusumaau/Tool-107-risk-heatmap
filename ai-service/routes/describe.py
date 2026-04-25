from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from services.sanitiser import sanitise_input
from groq_client import call_groq

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing field: text"}), 400

    clean_text, error = sanitise_input(data["text"])
    if error:
        return jsonify({"error": error}), 400

    messages = [
        {"role": "user", "content": f"Describe this risk in a structured way: {clean_text}"}
    ]

    result = call_groq(messages)

    return jsonify({
        "success": result["success"],
        "description": result["content"],
        "is_fallback": result["is_fallback"],
        "generated_at": datetime.now(timezone.utc).isoformat()
    }), 200