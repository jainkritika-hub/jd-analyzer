from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

from models import JobPosting

load_dotenv()

MODEL_NAME = "groq:openai/gpt-oss-120b"

model = init_chat_model(MODEL_NAME)
structured_model = model.with_structured_output(JobPosting)

SYSTEM_PROMPT = SystemMessage("""
You extract structured data from job descriptions.
Only use information that is in the text.
If a detail is missing, leave it empty. Do not guess.
""")


def analyze_jd(jd_text: str) -> JobPosting:
    messages = [SYSTEM_PROMPT, HumanMessage(jd_text)]
    return structured_model.invoke(messages)