from dotenv import load_dotenv
    
load_dotenv()

import os
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

class Movie(BaseModel):
    title: str
    genre: Optional[List[str]] = None
    setting: Optional[str] = None
    director: Optional[str] = None
    scientific_advisors: Optional[List[str]] = None
    composer: Optional[str] = None
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)


# Initialize the model
model = ChatMistralAI(model="open-mistral-7b")
prompt = ChatPromptTemplate.from_messages([
    ('system', """You are an expert film analyst and data extraction assistant. Analyze the provided movie text and extract key metadata into a structured layout, followed by a concise executive summary.
{format_instructions}"""),
    ("human",
     """Extract information from the following movie text:

{text}""")
])


txt = input("Please provide the movie text for analysis: ")
final_prompt = prompt.invoke(
    {
    "text": txt,
    "format_instructions": parser.get_format_instructions()
    }
    )
response = model.invoke(final_prompt)
print(response.content)