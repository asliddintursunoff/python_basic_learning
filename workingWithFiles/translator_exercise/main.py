from os import write

from translate import Translator
translator= Translator(to_lang="uz")
try:
    with  open("from.txt" , mode= "r") as text:
        word = text.read()
        translation = translator.translate(word)
        after_text = open("translated_text.txt",mode="w")
        after_text.write(translation)
except FileNotFoundError:
    print("file not found error")
    



    
    
# translation = translator.translate("This is a pen.")
# print(translation)