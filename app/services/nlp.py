import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities_and_actions(prompt):
    doc = nlp(prompt)
    actions = [token.text.lower() for token in doc if token.pos_ == "VERB"]
    entities = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "ADJ", "PROPN"]]
    return entities, actions
