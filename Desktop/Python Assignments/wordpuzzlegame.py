def shuffle_word(word):
    import random
    lst = list(word)
    random.shuffle(lst)
    return ''.join(lst)

word_list = ['FATHER', 'COUNTRY', 'BREAK', 'GREEN', 'AEROPLANE']
cnt = 0
for word in word_list:
    print('Arrange the letters to form a valid word!')
    print(shuffle_word(word))
    if input().upper() == word:
        print('\nCorrect! (+1 point)\n')
        cnt+= 1
    else:
        print('\nWrong! (-1 point)\n')
        cnt-= 1
print('Your total score is: {}'.format(cnt))