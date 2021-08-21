import spacy

nlp = spacy.load("zh_core_web_md")
doc = nlp('合肥明天天气如何')
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)