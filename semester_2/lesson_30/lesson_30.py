from translate import Translator

trn_ru_to_en = Translator(from_lang='ru', to_lang='en')
text = ''

with open('russian.txt', mode='r+', encoding='utf-8') as file:
    for i in file:
        text += i

with open("english.txt", mode='w', encoding='utf-8') as file:
    total = trn_ru_to_en.translate(text)
    file.write(total)

print(total)