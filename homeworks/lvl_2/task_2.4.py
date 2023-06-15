# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    while s.find('!') != -1:
        ns = ''
        for j in range(0, len(s)):
            # string = ''
            # print(s.find('!'))
            if j != s.find('!'):  
                ns = ns+ s[j]
                # print(ns)
        s=ns
    # print(s)    
    return s 
        
# string = str(input('Введите текст: '))
# print('Исправленный текст: ', remove_exclamation_marks(string))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!':
        ns = ''
        for j in range(0, len(s) -1):
            ns = ns + s[j] 
    return ns 

# text = str(input('Введите текст: '))
# print('Исправленный текст: ', remove_last_em(text))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    arr = []
    arr =s.split()
    ns = ''
    for i in arr:
        c = 0
        ni = ''
        p=i
        while i.find('!') != -1:
            c += 1
            ni = ''
            for j in range(0, len(i)):
                if j != i.find('!'): 
                    ni = ni+ i[j]
            i = ni
        if c != 1:
            ns = ns + p + ' '
    return ns


words = str(input('Введите текст: '))
# words = ('Hi Hi! Hi! !Hi!')
print('Исправленный текст: ', remove_word_with_one_em(words))