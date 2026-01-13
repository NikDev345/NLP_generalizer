import streamlit as st
import spacy
import re
import pandas as pd

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# -------------------------
# Streamlit setup
# -------------------------
st.set_page_config(page_title="NLP Data Generalizer", layout="centered")
st.title("🧠 NLP Data Generalization Tool")
st.write("Upload text data and generalize it using a principled NLP pipeline.")

uploaded_file = st.file_uploader("Upload a .txt or .csv file", type=["txt", "csv"])

# -------------------------
# Rule-based masking (things NER should NOT guess)
# -------------------------
def mask_structured_data(text: str) -> str:
    # Email
    text = re.sub(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "EMAIL",
        text
    )

    # Phone numbers
    text = re.sub(
        r"\+?\d[\d\s\-]{8,}\d",
        "PHONE_NUMBER",
        text
    )

    # Age (e.g., 24-year-old)
    text = re.sub(
        r"\b\d{1,3}[- ]?year[- ]?old\b",
        "AGE",
        text,
        flags=re.IGNORECASE
    )

    # Year (e.g., 2023)
    text = re.sub(
        r"\b(19|20)\d{2}\b",
        "YEAR",
        text
    )

    # Degree (NER is bad at this → rules are correct)
    text = re.sub(
        r"\b(bachelor of technology|bachelor|b\.?tech|master|degree)\b",
        "DEGREE",
        text,
        flags=re.IGNORECASE
    )

    return text


# -------------------------
# NER-based generalization (ONLY where reliable)
# -------------------------
ALLOWED_ENTITIES = {"PERSON", "ORG", "GPE", "LOC"}

def generalize_text(text: str) -> str:
    doc = nlp(text)
    result = text

    # Replace longer spans first to avoid overlap
    for ent in sorted(doc.ents, key=lambda e: -len(e.text)):
        if ent.label_ in ALLOWED_ENTITIES:
            result = result.replace(ent.text, ent.label_)

    return result


# -------------------------
# App logic
# -------------------------
if uploaded_file:

    if uploaded_file.type == "text/plain":
        raw_text = uploaded_file.read().decode("utf-8")
    else:
        df = pd.read_csv(uploaded_file)
        raw_text = " ".join(df.iloc[:, 0].astype(str).tolist())

    st.subheader("📄 Original Text")
    st.text_area("", raw_text, height=220)

    # Step 1: Deterministic masking
    masked_text = mask_structured_data(raw_text)

    # Step 2: Controlled NER generalization
    generalized_text = generalize_text(masked_text)

    st.subheader("✨ Generalized Output")
    st.text_area("", generalized_text, height=220)

    st.download_button(
        "Download Generalized Text",
        generalized_text,
        file_name="generalized_output.txt"
    )
