from translate import Translator

trn_ru_to_en = Translator(from_lang='ru', to_lang='en')
text = ''

with open('russian.txt', 'r+', encoding='unf-8') as file:
    for i in file:
        text += i

with open("english.txt", mode='a') as file:
    total = trn_ru_to_en.translate(text)
    file.write(total)

print(total)