import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    OPENAI_MODEL = 'gpt-4o-mini'
    OPENAI_TEMPERATURE = 0.5
    OPENAI_MAX_TOKENS = 100
    TIKTOKEN_ENCODING = 'o200k_base'