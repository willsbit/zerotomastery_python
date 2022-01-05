from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('./texto.txt') as text:
        root_text = text.read()
        translation = translator.translate(root_text)
        print(translation) 
except FileNotFoundError as err:
    print('Incorrect file path.')


