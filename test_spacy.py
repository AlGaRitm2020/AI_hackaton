
import spacy
from spacy import displacy
nlp = spacy.load("ru_core_news_sm")
# Text with nlp
doc = nlp("Николай приехал в Лондон")
# Display Entities
displacy.render(doc, style="ent")
print(doc)