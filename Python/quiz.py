print('Welcome to the quiz!')

playing = input('Would you like to try?> ')   

if playing != 'yes':
    quit()

print('Okay! lets play!') 
score = 0

answer = input('Whats 2+1?> ')
if answer == '3':
    print('Well done!') 
    score += 1
else:
    print('Incorrect!') 

answer = input('Whats 3+4?> ')
if answer == '7':
    print('Well done!') 
    score += 1
else:
    print('Incorrect!') 

answer = input('Whats 12-2?> ')
if answer == '10':
    print('Well done!')
    score += 1  
else:
    print('Incorrect!') 

answer = input('Whats 15+3?> ')
if answer == '18':
    print('Well done!') 
    score += 1
else:
    print('Incorrect!') 

print('You got ' + str(score) + ' questions right!')   
print('You got ' + str((score/4) * 100)+ ' percent of questions right!')   
print('Thats all for now, good bye!')  