import random
def hangstring(i):
    hangstr=['''
       +---+
       O   |
      /|\\  |
      / \\  |
          ===''','''
       +---+
       O   |
      /|\\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\\  |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''','''
       +---+
       O   |
           |
           |
          ===''','''
       +---+
           |
           |
           |
          ===''']
    print(hangstr[i])

game_word_list=["tomato","potato","apple","orange"]
game_word=random.choice(game_word_list)
display=[]
for i in range(len(game_word)):
    display +="_"
print(game_word)
print(display)
life=6
flag=False
while not flag:
    guess = input("guess a letter:: ").lower()
    for i in range(len(game_word)):
        if game_word[i]==guess:
            display[i]=guess
    print(display)
    if guess not in game_word:
        life -=1
        if life==0:
            print("You lose")
            flag=True
    if "_" not in display:
        print("You win")
        flag=True
    hangstring(life)
