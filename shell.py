import core, disk, time, sys

#RENTAL AGENCY

#MY INNER NERD HAS ACTIVATED

#FUNCTIONS FOR DECORATION BEGIN
#BELOW
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

def pretty_choice(choice):
    string = ''
    for item in choice:
        string == string.strip('\'')
    return string

def make_pretty(inventory):

    stringy = ''
    for item in inventory:
       stringy += "\n {:<60}{:>40}".format(item[0], "Stocked Inventory: " + str(item[1]))
    return stringy + '\n\n'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FUNCTIONS FOR DECORATION END
#MAIN CODE BELOW

def receipt(price, due):
    """(float) -> float

    prints all information to user in the form of a receipt.

    >>> receipt(2.00)
    <BLANKLINE>
    ___________________________________
    |
    |Original Price:2.0
    |+ State Tax:0.16
    |+ County Tax:0.14
    |Due In:  days.
    |Total:2.3000000000000003
    |__________________________________
    <BLANKLINE>
    Here's your receipt! Thank you for shopping with us!
    """
    revenue = 0
    inventory = 0
    print('\n___________________________________\n|\n|Original Price:' + str(price))
    state_taxes = core.StateSalesTax(price)
    print('|+ State Tax:' + str(state_taxes))
    county_taxes = core.CountySalesTax(price)
    print('|+ County Tax:' + str(county_taxes))
    total = price + state_taxes + county_taxes
    print('|Due In: ' + str(due) + ' days.')
    print('|Total:' + str(total))
    print('|__________________________________\n\nHere\'s your receipt! Thank you for shopping with us!')

def begin():
    print((pretty_border('Welcome to Arkham Asylum Library Files! Where the villains of Gotham record '
                        'Audio Files, Available to rent to the public!')))
    
    
    listey = disk.open_inventory()
    listey1 = make_pretty(listey)
    print(listey1)

    print('To exit this application, click "q". Type Below, Please:\n')

def choose_the_audio_file():
    while True:
        listey = disk.open_log('inventory.txt')
        
        first = slow_type('\n-What Audio File would you like to rent today?\n\n-').title()
        
        if first == '1':
            print('\n•You\'ve chosen ' + str(listey[0][0]).strip('1. ') + '•')
            break
        elif first == '2':
            print('\n•You have chosen ' + str(listey[1][0]).strip('2. ') + '•')
            break
        elif first == '3':
            print('\n•You have chosen ' + str(listey[2][0]).strip('3. ') + '•')
            break
        elif first == '4':
            print('\n•You have chosen ' + str(listey[3][0]).strip('4. ') + '•')
            break
        elif first == '5':
            print('\n•You have chosen ' + str(listey[4][0]).strip('5. ') + '•')
            break
        elif first == 'Q':
            quit()
        else:
            print('\nInvalid Audio Tape number. Please try again.')
        
    return first #now s = first(the choice of Audio Tape from user's input)
        
def due():
    while True:
        valid_number_list = ['1', '2', '3', '4', '5', '6', '7']

        due_date = slow_type('\nHow many days would you like to rent it?\n\n-').title()
        
        if due_date == 'Q':
            quit()
        elif due_date not in valid_number_list:
            print('\nInvalid Input. Please input a number that is 1-7. Try again.')
        else:
            return due_date

def pay_deposit(s):
    while True:
        if s == 'Q':
            quit()
        elif s == '1':
            print('\nYou must pay a ' + core.deposit(40.00) + ' deposit. It will be refunded after you return the Audio Tape.')
            break
        elif s == '2':
            print('\nYou must pay a ' + core.deposit(20.00) + ' deposit. It will be refunded after you return the Audio Tape.')
            break
        elif s == '3':
            print('\nYou must pay a ' + core.deposit(30.50) + ' deposit. It will be refunded after you return the Audio Tape.')
            break
        elif s == '4':
            print('\nYou must pay a ' + core.deposit(36.00) + ' deposit. It will be refunded after you return the Audio Tape.')
            break
        elif s == '5':
            print('\nYou must pay a ' + core.deposit(12.00) + ' deposit. It will be refunded after you return the Audio Tape.')
            break
        else:
            input('got: {}'.format(s))

            #ME TO ME: RENTAL FEE NEXT SHOULD BE EASY TRY TO ADD IT TO THE FUNCTION ABOVE, MY DUDE

#     if first == '1':
#         scarecrow = slow_type('\nYou have chosen Dr. Crane\'s "A Study In Fear".\nThe rental fee is 1.00, with a deposit of 4.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
#         if scarecrow == 'Yes':
#             due = int(slow_type('\nHow many days will you be renting?\n\n-'))
#             if due <= 7:
#                 return core.receipt(5.00, due)
#            

        
def main():
    begin()
    s = choose_the_audio_file()
    due()
    pay_deposit(s)
if __name__ == '__main__':
    main()