from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash")

prompt = input("user input")

Ai_msg = model.invoke(prompt)
print(Ai_msg.content)