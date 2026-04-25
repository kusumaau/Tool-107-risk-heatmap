import os
import time
import logging
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_groq(messages, temperature=0.3, max_tokens=1000, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            logger.info(f"Calling Groq API — attempt {attempt + 1}")
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            content = response.choices[0].message.content
            logger.info("Groq API call successful")
            return {
                "success": True,
                "content": content,
                "is_fallback": False
            }

        except Exception as e:
            attempt += 1
            wait_time = 2 ** attempt
            logger.error(f"Groq API error on attempt {attempt}: {str(e)}")
            if attempt < retries:
                logger.info(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                logger.error("All retries failed. Returning fallback response.")
                return {
                    "success": False,
                    "content": "AI service is temporarily unavailable. Please try again later.",
                    "is_fallback": True
                }