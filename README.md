# 🎓 SAT Oman Prep Project

This project helps Omani students prepare for the **SAT** with bilingual (English & Arabic) support.  
It includes:
- 📌 A **Streamlit app** for quizzes, dataset management, and translations.  
- 🤖 A **Discord bot** for quizzes in chat.  
- 🌐 Automatic translation (Google Cloud Translate API if configured, or `googletrans` fallback).  

---

## 📂 Project Structure
sat_prep/
├── bot.py # Discord bot
├── streamlit_app.py # Streamlit app
├── utils.py # Dataset helpers
├── translator.py # Translator (Google Cloud or fallback)
├── requirements.txt # Python dependencies
├── README.md # Documentation
└── data/
├── pyqs.json # Main dataset (created/managed in app)
└── sample_pyqs.json # Example dataset

yaml
Copy code

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run the Streamlit app
```

bash
```
streamlit run streamlit_app.py
```

### Go to the sidebar → Quiz to practice questions.
### Use Dataset Manager to upload, merge, reset, or preview datasets.
### You can toggle English / Arabic when answering questions.

### 3. Run the Discord bot

Create a bot on the Discord Developer Portal.
Copy your bot token.
Replace YOUR_DISCORD_TOKEN in bot.py (or set it as an environment variable).
Run the bot:

```
python bot.py
```

### Commands:
!quiz → Sends a random SAT-style question in English.

### 🌍 Translation
By default, the app uses googletrans.
To use Google Cloud Translate API:
Enable Cloud Translation API in Google Cloud Console.
Create a service account & download its JSON key.
Set the environment variable:

```
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account.json"
The app will automatically switch to Google Cloud Translate.
```

### 📊 Dataset Management

All datasets are stored in data/pyqs.json.
You can:
Upload a full dataset (replace).
Add new questions (merge).
Reset to empty or sample dataset.
Preview questions inside the app.
Dataset schema:

```
{
  "id": "unique-id",
  "question_en": "English question",
  "question_ar": "Arabic translation",
  "choices_en": ["opt1", "opt2", "opt3", "opt4"],
  "choices_ar": ["خيار١", "خيار٢", "خيار٣", "خيار٤"],
  "answer_index": 0
}
```

### ⚡ Notes
data/pyqs.json will be created automatically if missing.
You can expand sample_pyqs.json with real SAT-style practice questions.
Both the bot and the Streamlit app read from the same dataset.

### 📌 Next Steps
Add real SAT practice questions.
Deploy the Streamlit app to Streamlit Cloud / Heroku / Docker.
Deploy the bot to Replit or a VPS.
Optionally integrate leaderboards and progress tracking.
