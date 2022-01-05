from translate import Translator


with open('./texto.txt') as text:
    root_text = text.read()

translator= Translator(to_lang="ja")
translation = translator.translate(root_text)

print(translation)