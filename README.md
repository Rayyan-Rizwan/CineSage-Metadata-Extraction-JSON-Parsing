
```markdown
# 🎬 CineSage - Movie Metadata Extraction & JSON Parsing

An AI-powered web application built with **Streamlit**, **LangChain**, **Mistral AI**, and **Pydantic**. CineSage converts unstructured movie synopses or plots into structured, validated JSON metadata while providing a custom, responsive dual-column user interface.

🚀 **Live Application**: [CineSage on Streamlit Cloud](https://cinesage-metadata-extraction-json-parsing-duttefb8bqe4327z6xbu.streamlit.app/)

---

## ✨ Features

- **Structured Metadata Extraction**: Extracts title, genres, setting, director, composer, scientific advisors, and executive summaries from plain movie text.
- **Strict Data Validation**: Uses LangChain's `PydanticOutputParser` to enforce schema validation and prevent malformed responses.
- **Dual-View Dashboard**: Displays formatted overview cards on the left and an interactive, collapsible raw JSON tree on the right side-by-side.
- **Powered by Mistral AI**: Leverages the `open-mistral-7b` LLM model.

---

## 🛠️ Tech Stack

- **Frontend & App Framework**: [Streamlit](https://streamlit.io/)
- **LLM Orchestration**: [LangChain](https://www.langchain.com/) (`langchain-mistralai`, `langchain-core`)
- **Model**: [Mistral AI](https://mistral.ai/) (`open-mistral-7b`)
- **Schema Validation**: [Pydantic](https://docs.pydantic.dev/)
- **Environment Management**: `python-dotenv`

---

## 📁 Repository Structure

```text
├── uicore.py           # Main Streamlit application file
├── core.py             # CLI extraction script
├── requirements.txt    # Application dependencies
├── .gitignore          # Excluded files (virtual environment, secrets)
└── README.md           # Project documentation

```

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/Rayyan-Rizwan/CineSage-Metadata-Extraction-JSON-Parsing.git](https://github.com/Rayyan-Rizwan/CineSage-Metadata-Extraction-JSON-Parsing.git)
cd CineSage-Metadata-Extraction-JSON-Parsing

```

### 2. Set Up Virtual Environment & Dependencies

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your Mistral API Key:

```env
MISTRAL_API_KEY=YOUR_MISTRAL_API_KEY

```

### 4. Run the Streamlit Application

```bash
streamlit run uicore.py

```

---

## ☁️ Deployment Settings (Streamlit Cloud)

To deploy your own instance on Streamlit Community Cloud:

1. Connect your repository (`Rayyan-Rizwan/CineSage-Metadata-Extraction-JSON-Parsing`).
2. Set the **Main file path** to `uicore.py`.
3. Add your API Key under **Advanced Settings > Secrets**:
```toml
MISTRAL_API_KEY = "YOUR_MISTRAL_API_KEY"

```



```

```
