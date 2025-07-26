words = {
    'cat':'кошка',
    'car':'машина',
    'dog':'собака'
}

def translate(words):
    while True:
        text = input("введите слово: ")
        if text in words:
            print('перевод ', words[text])
        elif text == 'exit':
                break
        else:
            print('слово не найдено')

def add(words):
    eng = input('введите слово на английском: ')
    ru = input('введите перевод на русском: ')
    words[eng] = ru
    print('слово добавленно! ')

def delete(words):
     text = input('введите слово на английском для удаления: ')
     if text in words:
          del words[text]
          print('слово удалено')
     else:
          print('такого слова нет')

