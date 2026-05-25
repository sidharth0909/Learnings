from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash")

# schema
# so lets say the model doesnt understand what to sen in summary then we can simply add annotated which is kind of a one line explanation to llm what to send

class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: str


structured_model= model.with_structured_output(Review)

result = structured_model.invoke("""
This is a very nice upscale looking shirt. It has great styling that is not over-sized. My husband normally wears a medium or large depending on the cut/style. He got a medium in this size and it is a perfect, comfortable fit. It arrived with some creases in the material from being folded in the packaging but it came out beautifully from the dryer. I'm happy he has a casual but nice shirt to wear when he takes me out to dinner!
""")

print(result)
print(result['summary'])
print(result['sentiment'])
