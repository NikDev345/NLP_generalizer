import spacy

nlp = spacy.load("model/model-best")

doc = nlp("Rahul completed his Bachelor of Technology in Computer Science")

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
