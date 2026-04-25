from groq_client import call_groq

messages = [
    {"role": "user", "content": "Give me a one sentence summary of what a risk heatmap is."}
]

result = call_groq(messages)

print("Success:", result["success"])
print("Is Fallback:", result["is_fallback"])
print("Response:", result["content"])