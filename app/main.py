from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from converter import Converter
from ui import Ui

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

converter = Converter(tokenizer=tokenizer, model=model)

Ui(converter)
