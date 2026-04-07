import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
# OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

class LLMModel:
    def __init__(self, model_name="llama-3.3-70b-versatile"):
        if not model_name:
            raise ValueError("Model is not defined.")
        self.model_name = model_name
        self.groq_api=ChatGroq(model=self.model_name)
        
    def get_model(self):
        return self.groq_api

if __name__ == "__main__":
    llm_instance = LLMModel()  
    llm_model = llm_instance.get_model()
    response=llm_model.invoke("hi")

    print(response)