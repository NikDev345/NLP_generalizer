import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
doc_bin = DocBin()

TRAIN_DATA = [
    (
        "Rahul completed his Bachelor of Technology in Computer Science",
        [
            ("Bachelor of Technology", "DEGREE"),
            ("Computer Science", "FIELD"),
        ],
    ),
    (
        "He works as a Software Engineer at Infosys",
        [
            ("Software Engineer", "ROLE"),
        ],
    ),
    (
        "He has experience in Python and Natural Language Processing",
        [
            ("Python", "SKILL"),
            ("Natural Language Processing", "SKILL"),
        ],
    ),
]

for text, entities in TRAIN_DATA:
    doc = nlp.make_doc(text)
    spans = []

    for entity_text, label in entities:
        start = text.find(entity_text)
        end = start + len(entity_text)

        if start != -1:
            span = doc.char_span(start, end, label=label)
            if span is not None:
                spans.append(span)

    doc.ents = spans
    doc_bin.add(doc)

doc_bin.to_disk("data/train_data.spacy")
print("✅ Training data saved to data/train_data.spacy")
