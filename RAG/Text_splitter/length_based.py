from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
doc = loader.load()

# text = """
# Heyy Kashyap,
# Myself Sidharth, I applied for Pricing and Offer Strategy – Artificial Intelligence (AI) Intern role at Vistra Corp and wanted to reach out to you regarding any referral you might provide. On the Application it ask for the name and email address, if possible can you please share me.

# Heyy Kashyap,
# Myself Sidharth, I applied for Pricing and Offer Strategy – Artificial Intelligence (AI) Intern role at Vistra Corp and wanted to reach out to you regarding any referral you might provide. Happy to share my resume or any other details you might require.
# Thank you

# Hii Amber,
# Myself Sidharth, I applied for Pricing & Offer Strategy Artificial Intelligence (AI) Intern role at Vistra Corp and wanted to reach out to you regarding how i am a great fit for this role, I am ready for a quick screening call and explain what currently i am working on, my projects etc.
# """
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator='',
)

# result = splitter.split_text(text)
# print(result)

result = splitter.split_documents(doc)
print(result[0])