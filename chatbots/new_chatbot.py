from dotenv import load_dotenv
import numpy as np
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash")

chat_history = []

# Since 
while True:
    user_input = input('You:')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content[0]['text'])
    print('AI:', result.content[0]['text'])

print(chat_history)

# here we have the chathistory and thats why we can communciate with the chatbot easily
# but the new problem, we have no idea who is the user or ai