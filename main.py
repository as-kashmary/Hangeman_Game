import random

word_list=["kash","mary","cash","ask"];

chosen_word=random.choice(word_list);
out_list=["_"];
for i in range(1,len(chosen_word)):
    out_list.append("_")

f=True;
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=len(stages)-1;
k=False;
while f:
    guess=input("enter a letter: ").lower();
    for i in range(0,len(chosen_word)):
        if chosen_word[i]==guess:
            out_list[i]=guess;
            k=True;
    
    print(out_list)
    if not k:
      print(stages[lives]);
      lives-=1;
    if "_" not in out_list:
        f=False;
        print("YOU WIN");
        break;
    k=False;
    if lives==0:
      print("GAME OVER");
      break;
    
    
            
    
