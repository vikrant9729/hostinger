import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")