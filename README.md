
```markdown
# 🎬 CineSage - Movie Metadata Extraction & JSON Parsing

An AI-powered web application built with **Streamlit**, **LangChain**, **Mistral AI**, and **Pydantic**. CineSage converts unstructured movie synopses or plots into structured metadata and displays it both as clean UI metrics and validated JSON.

🚀 **Live Demo**: [CineSage Web App](https://cinesage-metadata-extraction-json-parsing-duttefb8bqe4327z6xbu.streamlit.app/)

---

## ✨ Features

- **Structured Data Extraction**: Automatically extracts title, genres, setting, director, composer, scientific advisors, and executive summaries from plain movie text.
- **Strict Pydantic Validation**: Guarantees output structure using `PydanticOutputParser` to prevent malformed responses.
- **Interactive Streamlit UI**: Styled layout featuring a dual-column dashboard to view both formatted overview cards and interactive raw JSON.
- **Powered by Mistral AI**: Leverages the `open-mistral-7b` LLM via LangChain integration.

---

## 🛠️ Tech Stack

- **Frontend / Framework**: [Streamlit](https://streamlit.io/)
- **LLM Orchestration**: [LangChain](https://www.langchain.com/) / `langchain-mistralai`
- **LLM Provider**: [Mistral AI](https://mistral.ai/) (`open-mistral-7b`)
- **Data Validation**: [Pydantic](https://docs.pydantic.dev/)
- **Environment Management**: `python-dotenv`

---

## 🚀 Local Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Clone the Repository
```bash
git clone [https://github.com/Rayyan-Rizwan/CineSage-Metadata-Extraction-JSON-Parsing.git](https://github.com/Rayyan-Rizwan/CineSage-Metadata-Extraction-JSON-Parsing.git)
cd CineSage-Metadata-Extraction-JSON-Parsing

```

### 3. Set Up Virtual Environment & Dependencies

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Mistral API Key:

```env
MISTRAL_API_KEY=your_actual_mistral_api_key_here

```

### 5. Run the App

```bash
streamlit run uicore.py

```

---

## ☁️ Deployment on Streamlit Community Cloud

1. Fork or push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New app** and select your repository.
4. Set **Main file path** to `uicore.py`.
5. Under **Advanced Settings > Secrets**, add your API key:
```toml
MISTRAL_API_KEY = "your_actual_mistral_api_key_here"

```


6. Click **Deploy!**

```

```
