import core, disk, time, sys

#RENTAL AGENCY

#MY INNER NERD HAS ACTIVATED

#FUNCTIONS FOR DECORATION BELOW

typing_speed = 17 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


def insert_line(string, index):
    return string[:index] + '|\n|' + string[index:]
def pretty_border(string):

    if len(string) <= 167:
        return '\n|' + '~' * len(string) + '|\n|' + string + '|\n|' + '~' * len(string) + '|\n'
    elif len(string) > 167 and len(string) < 334:
        return '\n|' + '~' * 167 + '|\n|' + insert_line(string, 167) +  ''.ljust(165), '|\n|' + '~' * 167 + ('|\n')
    elif len(string) >= 334:
        s = insert_line(string, 167)
        b = 166 - (len(string) - 334)
        return '\n|' + '~' * 167 + '|\n|' + insert_line(s, 337) +  ''.ljust(b), '|\n|' + '~' * 167 + ('|\n')
    
#MAIN CODE BELOW

def begin():
    print((pretty_border('Welcome to Arkham Asylum Library Files! Where the villains of Gotham record '
                        'Audio Files, Available to rent to the public!')))
    
    
    listey = disk.open_inventory()
    listey1 = core.make_pretty(listey)
    print(listey1)

    print('To exit this application, click "q". Type Below, Please:\n')

def begin2():
    while True:
        listey = disk.open_log('inventory.txt')
        
        first = slow_type('\n-What Audio File would you like to rent today? You can rent up to a week.\n\n-').title()
        
        if first == '1':
            print('\nYou\'ve chosen ' + str(listey[0][0]).strip('1. ') + '.')
            break
        elif first == '2':
            print('\nYou have chosen ' + str(listey[1][0]).strip('2. ') + '.')
            break
        elif first == '3':
            print('\nYou have chosen ' + str(listey[2][0]).strip('3. ') + '.')
            break
        elif first == '4':
            print('\n\nYou have chosen ' + str(listey[3][0]).strip('4. ') + '.')
            break
        elif first == '5':
            print('\nYou have chosen ' + str(listey[4][0]).strip('5. ') + '.')
            break
        elif first == 'Q':
            quit()
        else:
            print('\nInvalid. Please try again.')
        return first #now s = first(the choice of Audio Tape from user's input)
        
def due(s):
    valid_number_list = ['1', '2', '3', '4', '5', '6', '7']
    due_date = slow_type('\nHow many days would you like to rent it?\n\n-')
    if due_date not in valid_number_list:
        print('Invalid Input. Try again.')
    else:
        return due_date


        
# def pick_choice():

#     if first == '1':
#         scarecrow = slow_type('\nYou have chosen Dr. Crane\'s "A Study In Fear".\nThe rental fee is 1.00, with a deposit of 4.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
#         if scarecrow == 'Yes':
#             due = int(slow_type('\nHow many days will you be renting?\n\n-'))
#             if due <= 7:
#                 return core.receipt(5.00, due)
#             else:
#                 print('\nInvalid. Please input a number betweeen 1-7.')
#         elif scarecrow == 'No':
#             print('Very well! Have a nice day!')
#         else:
#             print('Invalid Input.')

#     elif first == '2':
#         hatter = slow_type('\nYou have chosen Jervis Tetch\'s "Wonderful Wonderland Fairy Tales!".\nThe rental fee is 1.00, with a deposit of 2.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
#         if hatter == 'Yes':
#             print('\nThank you for your business! Please come again!')
#         elif hatter == 'No':
#             print('\nVery well! Have a nice day!')
#         else:
#             print('Invalid Input.')

#     elif first == '3':
#         riddler = slow_type('\nYou have chosen Edward Nygma\'s "Riddles To Blow The Mind...Literally!".\nThe rental fee is 1.00, with a deposit of 3.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
#         if riddler == 'Yes':
#             print('\nThank you for doing business with us!')
#         elif riddler == 'No':
#             print('\nVery well! Have a nice day!')
#         else:
#             print('Invalid Input.')

#     elif first == '4':
#         bane = slow_type('\nYou have chosen Bane\'s "Breaking The Bat: It\'s A Snap!".\nThe rental fee is 1.00, with a down payment of 3.60. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
#         if bane == 'Yes':
#             print('\nThank you for your business! Please come again!')
#         elif bane == 'No':
#             print('\nVery well! Have a nice day!')
#         else:
#             print('Invalid Input.')

#     elif first == '5':
#         strange = slow_type('\nYou have chosen Hugo Strange\'s "The Dark History Of The Medical Practice".\nThe rental fee is 1.00, with a down payment of 1.20. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
#         if strange == 'Yes':
#             print('\nThank you for your business! Please come again!')
#         elif strange == 'No':
#             print('\nVery well! Have a nice day!')
#         else:
#             print('Invalid Input.')

        
    with open('inventory.txt') as file:
        lines = file.readlines()
    message = lines

    inventory = disk.open_inventory()
    



def main():
    begin()
    s = begin2()
    due(s)
    # pick_choice()
if __name__ == '__main__':
    main()