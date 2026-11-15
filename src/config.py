
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)

def get_client():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing.")

    return OpenAI(
        timeout=30.0,
        max_retries=1
    )

