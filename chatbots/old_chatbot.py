from dotenv import load_dotenv
import numpy as np
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash")

# Since 
while True:
    user_input = input('You:')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print('AI:', result.content[0]['text'])

# the problem is it doesnt has the chat history , every chat is new 