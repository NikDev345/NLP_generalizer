🧠 NLP Data Generalization Tool

A principled Natural Language Processing (NLP) web application that generalizes and anonymizes user-uploaded text data using a hybrid approach:

Deterministic rules for structured personal data

Transformer-based Named Entity Recognition (NER) for reliable entities

This project focuses on correct system design, not forced output manipulation.

🚀 Features

Upload .txt or .csv files from the user end

Automatically anonymizes sensitive information:

Names

Organizations

Locations

Email addresses

Phone numbers

Age

Year

Academic degrees

Uses Transformer-based spaCy model (en_core_web_trf)

Stable and generalizable (not tuned for a single sample)

Clean web interface built with Streamlit

Download generalized output as a text file

🧠 Design Philosophy (Important)

This project intentionally does not force perfect-looking output.

Instead, it follows these principles:

✅ Use NLP only where it is reliable

✅ Use rule-based methods where structure is known

❌ Do NOT guess semantic meaning

❌ Do NOT overfit to one dataset

❌ Do NOT patch errors just to make output “look good”

This mirrors real-world NLP system design used in production.

🏗️ Architecture Overview
User Upload
    ↓
Rule-based Masking (Email, Phone, Age, Year, Degree)
    ↓
Transformer NER (PERSON, ORG, GPE, LOC only)
    ↓
Generalized Output
    ↓
Downloadable Text File

🧪 Example
📄 Input Text
Rahul Sharma is a 24-year-old software engineer living in Bengaluru, India.
He works at Infosys and previously interned at Google.

His email address is rahul@gmail.com and his phone number is +91 9876543210.

Rahul completed his Bachelor of Technology in Computer Science from IIT Bombay in 2023.
Last month, Rahul traveled from Bengaluru to Mumbai for an office conference organized by Infosys.

✨ Generalized Output
PERSON is a AGE software engineer living in GPE, GPE.
He works at ORG and previously interned at ORG.

His email address is EMAIL and his phone number is PHONE_NUMBER.

PERSON completed his DEGREE in Computer Science from ORG in YEAR.
PERSON traveled from GPE to GPE for an office conference organized by ORG.


⚠️ Note:
Minor imperfections are expected and accepted by design.
The system prioritizes correctness and generalization over cosmetic perfection.

🛠️ Tech Stack

Python 3.10+

spaCy

Transformer model: en_core_web_trf

Streamlit

Pandas

Regex (for deterministic masking)

📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/nlp-data-generalizer.git
cd nlp-data-generalizer

2️⃣ Install dependencies
pip install streamlit spacy pandas

3️⃣ Download the transformer model
python -m spacy download en_core_web_trf

4️⃣ Run the application
streamlit run main.py


Open in browser:

http://localhost:8501

📁 Project Structure
nlp-data-generalizer/
│
├── main.py
├── README.md
└── requirements.txt

📌 Use Cases

Resume anonymization

Privacy-preserving data preprocessing

AI training data sanitization

NLP experimentation & learning

Academic and portfolio projects

🔮 Future Improvements

Custom NER training (Degree, Skill, Role)

FastAPI backend

React frontend

Batch file processing

Evaluation metrics (precision / recall)

GDPR-style anonymization modes

🧠 Key Takeaway

This project demonstrates engineering maturity:

Instead of forcing outputs to look perfect,
it builds a system that is honest, explainable, and extensible.

📄 License

This project is open-source and available for educational and personal use.
