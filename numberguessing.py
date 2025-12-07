
import random
import math
range = 100
x = random.randint(1,range) #this is my random number
changing_x1 = random.randint(0,22)
if x > 20 and x < 80:   #this is to prevent negative valuse being created in hint2 and hint3
    changing_x2 = random.randint(0,22)
else:
    changing_x2 = random.randint(0,5)
print('Welcome to random number guesser!')
guess1= int(input(f'The guessometer is thinking of a number between 1 and {range} can you guess what it is? ')) #the first prompt every one after this is made in the loop
attempt = 1 #the starting number
emotes = ['Oops', 'Yikes', 'Oh no!'] #just some fun additions
def guesses():
    global guess1, attempt, emotes
    left = 4 - attempt
    print(f'{emotes[attempt - 1]} you have {left} attempts left') #checks users status
    guess1 = int(input('The guessometer is still thinking of a number can you guess what it is? '))
while attempt < 4:
    if attempt == 1: #the first clue is quite vague telling the user if the number is even or odd as well as if it is smaller or bigger than the unknown
        hint1 = x % 2
        if x  > guess1:
            print('Your guess is close but too small!')
        else:
            print('Your guess is close but too big!')
        if hint1 == 1:
            print('The number is odd')
        else:
            print('The number is even')
    if attempt == 3: #give the closes square root to the guess
        square = math.sqrt(x)
        hint4 = round(square,1)
        print('This is your last hint: ') 
        print(f'The number has a square root of approx {hint4}')
    if attempt == 2: #gives a range of values near the guess while still remaining quite random!
        hint2 , hint3= (x + changing_x1), (x - changing_x2)
        print(f'The number is in the range {hint3} - {hint2}')
    if guess1 == x and attempt == 1: #some closing statements varying based of of attempt status
        print('Wow you won on your first try!')
        break
    else:
        guesses() #runs the prompt again if guess has not been found and attempts have not run out
        attempt += 1
    if x == guess1 and attempt == 4:
        print('Hurray you won just in time!')
        break
    if x == guess1:
        print('Yay you guessed the number!')
        break
else:
    print(f'Sorry you ran out of attempts :( The number is {x}' )
