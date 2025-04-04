from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from dotenv import load_dotenv
import os 

load_dotenv()  # Load environment variables from .env file

llm = HuggingFaceInferenceAPI(
    model_name="Qwen/Qwen2.5-Coder-32B-Instruct",
    temperature=0.7,
    max_tokens=100,
    token=os.getenv("HUGGINGFACE_TOKEN")
)

print(llm.complete("Hello, how are you?"))