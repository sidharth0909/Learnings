from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimension = 300)
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers.",
    "My name is Sidharth , currently I am pursuing my MS in Data Science.",
    "Sidharth is a MS student at UB who is working as a data scientist, Sidharth is a basketball player."
 ]

query = "Who is Sidharth?"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)
# print(type(doc_embeddings))
# print(np.array(doc_embeddings).shape)

# print(type(query_embedding))
# print(np.array(query_embedding).shape)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]
# since we want 1 D list thats why we used [0] to get 1D list
# print(scores)

# print(sorted(list(enumerate(scores)), key=lambda x:x[1])[-1])
# Why does sorting help , [(0, np.float64(0.5915738078151087)), (1, np.float64(0.5968681453074994)), (2, np.float64(0.6093320880592841)), (3, np.float64(0.58747521296889)), (4, np.float64(0.5884268184041108)), (5, np.float64(0.7689494262008167))]
# To get the ascending order, easier for use to know why has the highest similarity score
# when we do -1 then we get the highest similarity score

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print('similarity score is:', score)