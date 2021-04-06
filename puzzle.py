import random

print("Welcome to Yirong’s puzzle game, ......")

def print_list(dimension):                                  #Print the list in a dimension*dimension format
    for i in range(dimension):
        print('+-------', end='')
    print('+')
    for i in range(dimension**2):
        if i%dimension != (dimension-1):
            print('|', puzzle_list[i], end='\t')    
        else:
            print('|', puzzle_list[i], end='\t|\n')
            for i in range(dimension):
                print('+-------', end='')
            print('+')

def get_inverse_ordinal_num():                              #Count the inverse ordinal number of the form, in order to get a sovlable game
    counter = 0
    for i in range(dimension**2-1):
        for index in range(i+1, dimension**2):
            if puzzle_list[i] == ' ' or puzzle_list[index] == ' ':
                continue
            if puzzle_list[i] > puzzle_list[index]:
                counter += 1
    return counter

def get_hint(position):                                     #Find the proper direction input for each position of the space
    column = position % dimension
    line = position // dimension
    if column == 0:
        a = 0
    elif column == dimension - 1:
        a = 2
    else:
        a = 1
    if line == 0:
        b = 0
    elif line == dimension - 1:
        b = 2
    else:
        b = 1
    return a + b*3

def test_puzzle():                                          #Test whether the game is finished or not
    for i in range(dimension**2-1):
        if puzzle_list[i] != str(i+1):
            return False    
    return True

while True:                                                 #The loop is to let the user play again and again
    while True:                                             #The loop is to make the input 'dimension' valid
        try:
            dimension = int(input('Enter the desired dimension of the puzzle(dimension is form 3 to 10): '))
            if dimension >= 3 and dimension <= 10:
                puzzle_list = []
                for i in range(1, dimension**2):
                    i = str(i)
                    puzzle_list.append(i)
                puzzle_list.append(' ')
                break
            else:
                print('Please enter a valid input. Dimension is from 3 to 10.')
        except: 
            print('Please enter a valid input. Dimension is from 3 to 10.')
            
    while True:                                             #The loop is to make the input 'four_letter' valid
        four_letter = input('Enter four letters used for left, right, up and down directions(no white spaces between each character): ')
        if len(four_letter) != 4:
            print('Please enter a valid input.')
        else:
            break

    left = four_letter[0]
    right = four_letter[1]
    up = four_letter[2]
    down = four_letter[3]
    hint_total = [
        {'up':up, 'left':left}, 
        {'up':up, 'left':left, 'right':right}, 
        {'up':up, 'right':right}, 
        {'up':up, 'left':left, 'down':down}, 
        {'up':up, 'down':down, 'left':left, 'right':right}, 
        {'up':up, 'down':down, 'right':right}, 
        {'down':down, 'left':left}, 
        {'down':down, 'left':left, 'right':right}, 
        {'down':down, 'right':right}
        ]
    print('This is the target form')
    print_list(dimension)
    begin = input('Please press ENTER to begin>')

    while True:                                     #The loop is to get a accessible game and then print it
        random.shuffle(puzzle_list)
        counter = get_inverse_ordinal_num()
        if counter % 2 == 0:
            print_list(dimension)
            space = puzzle_list.index(' ')          #Get the position of the space
            break
    print('Please input your moves by entering a letter stands for the direction.\n' 
        + 'For example, right=>', right, ',left=>', left, ',up=>', up, ',down=>',  down)
    count = 0                                       #Step number
            
    while True:                                     #The loop is to let the user solve the game step by step
        hint = hint_total[get_hint(space)]
        hint_string = '(Step number:' \
            + str(count) \
            + ')Please enter your operation and press ENTER. Hint: Enter(' \
            + str(hint)[1:-1] + '):'
        step = input(hint_string)
        print()
        if step in hint.values():
            count += 1
            if step == up:
                puzzle_list[space], puzzle_list[space+dimension] = puzzle_list[space+dimension], puzzle_list[space]
                space += dimension
            elif step == down:
                puzzle_list[space], puzzle_list[space-dimension]= puzzle_list[space-dimension], puzzle_list[space]
                space -= dimension
            elif step == left:
                puzzle_list[space], puzzle_list[space+1] = puzzle_list[space+1], puzzle_list[space]
                space += 1
            elif step == right:
                puzzle_list[space], puzzle_list[space-1]= puzzle_list[space-1], puzzle_list[space]
                space -= 1
        else:
            print('Wrong input! Please type a valid step.')
        print_list(dimension)

        if test_puzzle() == True:
            print('WELL DONE! You finished the game in', count, 'steps.')
            break
            
    again = input('Begin a new game? (y for Yes/n for No): ')
    if again == 'y':
        continue
    elif again == 'n':
        break
    else:
        print('Wrong input.')

print('Thank you for playing, see you next time!')