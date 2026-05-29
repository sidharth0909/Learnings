from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.5-flash')

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.com/COOFANDY-Casual-Shirts-Button-Summer/dp/B0BV241H3F?ref=dlx_memor_dg_dcl_B0BV241H3F_dt_sl14_a2_pi&pf_rd_r=BKK8E6GZWX6QRSTBJTP6&pf_rd_p=ca04a489-97ef-4134-986c-9687e00659a2&th=1&psc=1'

loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))