🧠 NLP Generalizer

A principled NLP web application that generalizes and anonymizes user-uploaded text data using a hybrid, real-world approach.

This project is designed with system correctness and generalization in mind — not cosmetic or forced outputs.

✨ What This Project Does

Accepts user-uploaded .txt or .csv files

Generalizes sensitive and identifying information

Produces privacy-preserving text output

Allows users to download the generalized text

🧠 Core Design Philosophy
<div style=" border: 2px solid #7c3aed; border-radius: 10px; padding: 16px; background-color: #0f172a; color: #e5e7eb; ">

<strong>Principles Followed</strong>

<br><br>

• Use NLP only where it is reliable
• Use rule-based logic where structure is deterministic
• Do NOT guess semantic meaning
• Do NOT overfit to one dataset
• Do NOT force output to look perfect

</div>

This mirrors how real NLP systems are designed in production environments.

🏗️ System Architecture
User Upload
   ↓
Rule-based Masking
(Email, Phone, Age, Year, Degree)
   ↓
NLP Named Entity Recognition
(PERSON, ORG, GPE, LOC)
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
<div style=" border: 2px solid #7c3aed; border-radius: 10px; padding: 16px; background-color: #0f172a; color: #e5e7eb; font-family: monospace; ">

<strong>GENERALIZED OUTPUT</strong>

<br><br>

PERSON is a AGE software engineer living in GPE, GPE.
He works at ORG and previously interned at ORG.

<br><br>

His email address is EMAIL and his phone number is PHONE_NUMBER.

<br><br>

PERSON completed his DEGREE in Computer Science from ORG in YEAR.
PERSON traveled from GPE to GPE for an office conference organized by ORG.

</div>

⚠️ Minor imperfections are expected and accepted by design.
The goal is correctness and generalization — not forced perfection.

🛠️ Tech Stack

Python 3.10+

spaCy

Transformer-based NER (en_core_web_trf)

Streamlit

Pandas

Regex (deterministic masking)

🚀 Installation & Usage
git clone https://github.com/NikDev345/NLP_generalizer.git
cd NLP_generalizer
pip install -r requirements.txt
python -m spacy download en_core_web_trf
streamlit run main.py


Open in browser:

http://localhost:8501

📌 Use Cases

Resume anonymization

Privacy-preserving data preprocessing

AI training data sanitization

NLP experimentation

Academic & portfolio projects

🔮 Future Improvements
<div style=" border: 2px solid #22c55e; border-radius: 10px; padding: 16px; background-color: #052e16; color: #dcfce7; ">

• Custom NER training (Degree, Skill, Role)
• FastAPI backend
• React frontend
• Batch file processing
• Evaluation metrics (precision / recall)
• Privacy levels (light / medium / strong)

</div>
🧠 Key Takeaway
<div style=" border: 2px solid #f59e0b; border-radius: 10px; padding: 16px; background-color: #3b2f05; color: #fef3c7; ">

This project demonstrates engineering maturity.

Instead of forcing outputs to look perfect,
it builds a system that is honest, explainable, and extensible.

</div>
📄 License

Open-source and available for educational and personal use.
