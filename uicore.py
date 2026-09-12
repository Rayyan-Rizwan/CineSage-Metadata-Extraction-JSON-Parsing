import os
from typing import List, Optional
import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from pydantic import BaseModel

load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="CineSage - Movie Metadata Extractor",
    page_icon="🎬",
    layout="wide",
)

# Custom CSS Styling
st.markdown(
    """
    <style>
    /* Gradient Background Header */
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8F00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0rem;
    }
    .sub-title {
        color: #888888;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    /* Card Container Styling */
    .metric-card {
        background-color: #1E1E1E;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #333;
        margin-bottom: 10px;
    }
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF2B2B;
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.4);
    }
    </style>
""",
    unsafe_allow_html=True,
)


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
    (
        "system",
        """You are an expert film analyst and data extraction assistant. Analyze the provided movie text and extract key metadata into a structured layout, followed by a concise executive summary.
{format_instructions}""",
    ),
    (
        "human",
        """Extract information from the following movie text:

{text}""",
    ),
])

# Header Section
st.markdown('<p class="main-title">🎬 CineSage</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">AI-Powered Movie Metadata Extraction & JSON Parsing</p>',
    unsafe_allow_html=True,
)

# Input UI Component
txt = st.text_area(
    "Enter Movie Plot or Summary:",
    height=180,
    placeholder="Paste a movie synopsis here...",
)

submit_btn = st.button("⚡ Extract Metadata")

if submit_btn:
    if txt.strip():
        with st.spinner("Analyzing text and generating JSON..."):
            final_prompt = prompt.invoke({
                "text": txt,
                "format_instructions": parser.get_format_instructions(),
            })
            response = model.invoke(final_prompt)
            parsed_movie: Movie = parser.parse(response.content)

            st.divider()

            # Structured Output Section
            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("📋 Parsed Overview")
                st.markdown(f"**🎬 Title:** {parsed_movie.title}")
                st.markdown(
                    f"**🏷️ Genre:** {', '.join(parsed_movie.genre) if parsed_movie.genre else 'N/A'}"
                )
                st.markdown(
                    f"**🎬 Director:** {parsed_movie.director or 'N/A'}"
                )
                st.markdown(
                    f"**🎵 Composer:** {parsed_movie.composer or 'N/A'}"
                )
                st.markdown(
                    f"**🔬 Scientific Advisors:** {', '.join(parsed_movie.scientific_advisors) if parsed_movie.scientific_advisors else 'N/A'}"
                )
                st.markdown(
                    f"**🌍 Setting:** {parsed_movie.setting or 'N/A'}"
                )

                st.info(f"**Summary:** {parsed_movie.summary}")

            with col2:
                st.subheader("📄 Raw JSON Output")
                st.json(parsed_movie.model_dump())

    else:
        st.warning("Please provide some movie text before running the extraction.")