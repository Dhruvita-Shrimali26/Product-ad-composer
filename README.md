# 🚀 AI Product Ad Composer

An AI-powered product advertisement generator that creates personalized ad copy and high-fidelity visuals from a real ecommerce product dataset.

## ✨ Features

- **Smart Product Selection** — Browse thousands of real products from a cleaned Flipkart dataset
- **High-Performance Copy Generation** — Instant ad copy using persona-matched deterministic templates
- **High-Fidelity Visuals** — Integrates Hugging Face's FLUX.1 Schnell model to generate photorealistic product images
- **Demographic Targeting** — Custom creative strategies for Teenagers, Professionals, and Seniors
- **Simplified Setup** — No configuration needed for text generation logic

## 🏗️ Project Structure

```
project-ad-composer/
├── app.py                        ← Main Streamlit application
├── requirements.txt              ← Python dependencies
├── .env.example                  ← API key template (safe to commit)
├── .env                          ← Your real API keys (in .gitignore)
├── .gitignore                    ← Protects secrets and large files
├── README.md                     ← This file
│
├── notebooks/
│   └── Personalized_Ad_Composer.ipynb  ← Data exploration & cleaning
│
├── scripts/
│   ├── test_api.py               ← NVIDIA API connectivity test
│   ├── read_nb.py                ← Notebook cell inspector
│   └── update_nb_script.py      ← One-off notebook path fixer
│
└── tests/
    └── test_app.py               ← Unit tests (run with pytest)
```

## ⚙️ Setup

### 1. Clone & Install Dependencies
```bash
git clone <your-repo-url>
cd project-ad-composer
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
# Copy the template
cp .env.example .env

# Edit .env and add your real keys
# HUGGINGFACE_API_KEY=hf_...
```

- Get a **Hugging Face API key** from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (free)

### 3. Add the Dataset
Place `cleaned_product_data.csv` in the project root directory. This file is excluded from git due to its large size.

### 4. Run the Application
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

## 🧪 Running Tests
```bash
pytest tests/ -v
```

## 🔑 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `HUGGINGFACE_API_KEY` | Required | Enables FLUX.1 image generation |

> **Note:** The ad copy logic is now local and instant, requiring no external LLM API key.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Web Framework | Streamlit |
| Data Processing | Pandas |
| Copy Generation | Deterministic Template Engine (Persona-based) |
| Image Generation | Hugging Face — FLUX.1 Schnell |
| Secrets Management | python-dotenv |
