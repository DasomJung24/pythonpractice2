print ('I am thinking of a number from 10 to 50, guess it')
start = 10
end = 50
answer = 37
guess = input()
if guess < str(answer) :
    print ('Your guess ' + guess + ' is smaller than the answer.')
if guess > str(answer) :
    print ('Your guess ' + guess + ' is bigger than the answer.')
if guess == str(answer) :
    print ('Correct! The answer is ' + str(answer) + '.')
