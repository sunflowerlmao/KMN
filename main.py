import random, time, sys

print('''ПРАВИЛА:
- Камень побеждает ножницы.
- Бумага побеждает камень.
- Ножницы побеждают бумагу.
''')

# Переменные для отслеживания количества выигрышей, проигрышей и ничьих.
wins = 0
losses = 0
ties = 0

while True:  # Основной цикл игры.
    while True:  # Запрашиваем, пока игрок не введет R, P, S или Q.
        print('{} Побед, {} Поражений, {} Ничьи'.format(wins, losses, ties))
        print('Введите свой ход: (К)амень (Б)умага (Н)ожницы or (В)ыход')
        playerMove = input('> ').upper()
        if playerMove == 'В':
            qwe = "                     \n"
            print(qwe * 100)
            print('Досвидания!')
            time.sleep(1)
            sys.exit()

        if playerMove in ['К', 'Б', 'Н']:
            break
        else:
            print('Неверный ввод!')

    # Отображаем на экране выбранный игроком ход:
    if playerMove == 'К' or playerMove == 'к':
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

𝗩𝗦
''')

        playerMove = 'Камень'
    elif playerMove == 'Б' or playerMove == 'б':
        print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

𝗩𝗦
''')

        playerMove = 'Бумага'
    elif playerMove == 'Н' or playerMove == 'н':
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

𝗩𝗦
''')

        playerMove = 'Ножницы'

    # Считаем до трех с драматическими паузами:
    otchet = []
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)

    # Отображаем на экране выбранный компьютером ход:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'Камень'
        computerMove1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    elif randomNumber == 2:
        computerMove = 'Ножницы'
        computerMove1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    elif randomNumber == 3:
        computerMove = 'Бумага'
        computerMove1 = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

    print(computerMove1)
    time.sleep(0.5)

    # Отображаем и фиксируем победу/поражение/ничью:
    if playerMove == computerMove:
        print('НИЧЬЯ!')
        ties += 1
    elif (playerMove == 'Камень' and computerMove == 'Ножницы') or \
         (playerMove == 'Бумага' and computerMove == 'Камень') or \
         (playerMove == 'Ножницы' and computerMove == 'Бумага'):
        print('Ты победил!')
        wins += 1
    else:
        print('Ты проиграл!')
        losses += 1
