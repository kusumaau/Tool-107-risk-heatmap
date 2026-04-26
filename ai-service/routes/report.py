from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from services.sanitiser import sanitise_input
from groq_client import call_groq

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing field: text"}), 400

    clean_text, error = sanitise_input(data["text"])
    if error:
        return jsonify({"error": error}), 400

    prompt = open("prompts/report_prompt.txt").read().replace("{text}", clean_text)
    messages = [{"role": "user", "content": prompt}]
    result = call_groq(messages)

    return jsonify({
        "success": result["success"],
        "report": result["content"],
        "is_fallback": result["is_fallback"],
        "generated_at": datetime.now(timezone.utc).isoformat()
    }), 200