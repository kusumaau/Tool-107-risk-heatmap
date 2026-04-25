import re

INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "disregard your instructions",
    "you are now",
    "act as",
    "pretend you are",
    "forget everything",
    "new instructions",
    "system prompt",
]

def strip_html(text):
    clean = re.sub(r'<[^>]+>', '', text)
    return clean.strip()

def detect_prompt_injection(text):
    text_lower = text.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in text_lower:
            return True
    return False

def sanitise_input(text):
    if not text or not isinstance(text, str):
        return None, "Input must be a non-empty string"
    
    text = strip_html(text)
    
    if detect_prompt_injection(text):
        return None, "Potentially harmful input detected"
    
    if len(text) > 2000:
        return None, "Input too long — maximum 2000 characters"
    
    return text, None