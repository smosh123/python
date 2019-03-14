import random
import time
from collections import Counter 
  
woorden = 'coderclass tape telefoon computer schrift muis papier oordoppen appel stoel toetsenbord ninja sticker bord eten'
  
woorden = woorden.split(' ') 
word = random.choice(woorden)

def tekengalg():
    if wrong == 1:
        print("_________")
    elif wrong == 2:
        print("_________")
        print("|/      |")
    elif wrong == 3:
        print("_________")
        print("|/      |")
        print("|      ( )")
                
    elif wrong == 4:
        print("_________")
        print("|/      |")
        print("|      ( )")           
        print("|      /|\ ")
                
    elif wrong == 5:
        print("_________")
        print("|/      |")
        print("|      ( )")           
        print("|      /|\ ")

    elif wrong == 6:
        print("_________")
        print("|/      |")
        print("|      ( )")           
        print("|      /|\ ")
        print("|      / \ ")
                
    elif wrong == 7:
        print("_________")
        print("|/      |")
        print("|      ( )")           
        print("|      /|\ ")
        print("|      / \ ")
        print("|")

    elif wrong == 8:
        print("_________")
        print("|/      |")
        print("|      ( )")           
        print("|      /|\ ")
        print("|      / \ ")
        print("|")
        print("|")
        print("|")

    elif wrong == 9:
        print("_________")
        print("|/      |")
        print("|      ( )")           
        print("|      /|\ ")
        print("|      / \ ")
        print("|")
        print("|")
        print("|")
        print("|__________")

if __name__ == '__main__': 
    print(' ') 
      
    for i in word: 
        print('_', end = ' ')         
    print() 
  
    playing = True
    letterGuessed = ''                 
    chances = 10
    correct = 0
    wrong = 0
    
  
    try: 
        while (chances != 0): 
            print() 
            chances -= 1
            try: 
                guess = str(input('Typ een letter in: ')) 
            except: 
                print('Alleen een letter!') 
                continue
            if not guess.isalpha(): 
                print('Alleen een letter typen!') 
                continue
            elif len(guess) > 1: 
                print('Alleen 1 letter') 
                continue
            elif guess in letterGuessed: 
                print('Je hebt die letter al geraden') 
                continue
            if not guess in word:
                time.sleep(0.02)
                wrong += 1
                tekengalg()
                

            
                
  
            if guess in word: 
                letterGuessed += guess 
  
            for char in word: 
                if char in letterGuessed: 
                    print(char, end = ' ') 
                    correct += 1
                else: 
                    print('_', end = ' ')


        if (Counter(letterGuessed) == Counter(word)): 
            print() 
            print('Gefeliciteerd, You won!')
            
        if wrong == 9: 
            print() 
            print('Game Over..') 
            print('het woord was {}'.format(word))

        if chances == 0: 
            print() 
            print('Game Over..') 
            print('het woord was {}'.format(word))
                    
                    


  

            
         

            
            
            
            
  
    except KeyboardInterrupt: 
        print() 
        print('doei! Probeer nog een keer.') 
        exit() 
