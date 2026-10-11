import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class CFG:
    model = 'gpt-4o-mini'
    openai_api_key = os.getenv('OPENAI_API_KEY')

    use_retrieved = True

    max_ret = 25
    task = '13B'
