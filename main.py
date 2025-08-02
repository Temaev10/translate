from my_project.translator import translate, add, delete, words

while True:
    print('\nВыберите действие:')
    print('1 - перевести слово')
    print('2 - добавить слово')
    print('3 - удалить слово')
    print('4 - выйти')

    a = int(input("введите цифру: "))

    if a == 1:
        translate(words)

    elif a == 2:
        add(words)

    elif a == 3:
        delete(words)
        
    elif a == 4:
        break

    else:
        print('не правильная команда ')




# git clone 
