import core, disk, time, sys

#ARKHAM ASYLUM AUDIO FILE RENTAL AGENCY
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
    return stringy + '\n'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FUNCTIONS FOR DECORATION END
#MAIN CODE BELOW

def receipt(price, due_date):
    """(float) -> float

    prints all information to user in the form of a receipt.

    >>> receipt(2.00, 5)
    <BLANKLINE>
    ___________________________________
    |
    |Original Price: 2.0
    |+ State Tax: 0.14
    |+ County Tax: 0.12
    |Due In: 5 days.
    |Total: 7.26
    |__________________________________
    <BLANKLINE>
    Here's your receipt! Thank you for shopping with us!
    ''
    """
    revenue = 0
    inventory = 0
    print('\n___________________________________\n|\n|Original Price: {}'.format(price))
    state_taxes = core.StateSalesTax(price)
    print('|+ State Tax: {}'.format(state_taxes))
    county_taxes = core.CountySalesTax(price)
    print('|+ County Tax: {}'.format(county_taxes))
    rental_price = 1.0
    total = float(price) + state_taxes + county_taxes
    print('|Due In: {} days.'.format(due_date))
    due_date = float(due_date)
    totally = float(rental_price * due_date)
    totally1 = totally + total
    print('|Total: {}'.format(totally1))
    print('|__________________________________\n\nHere\'s your receipt! Thank you for shopping with us!')
    return ''

def opening_message():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    listey = disk.open_inventory()
    listey1 = make_pretty(listey)
    print(listey1)

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def choose_the_audio_file():
    while True:
        print('To exit this application, click "q". Type Below, Please:\n')
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
        due_date = slow_type('\nHow many days would you like to rent?\n\n-').title()
        if due_date == 'Q':
            quit()
        elif due_date not in valid_number_list:
            print('\nInvalid Input. Please input a number that is 1-7. Try again.')
        else:
            return due_date
            break
    return str(due_date)
def how_many_tapes():
    while True:
        how_many1 = slow_type('\nHow many would you like to rent?\n\n-').title()
        how_many2 = int(how_many1)
        if how_many2 == 'Q':
            exit()
        elif how_many2 > 100:
            print('\nSorry, we have a limit of 100 audio tape copies. Please input a lower number.\n\n-')
        elif how_many2 <= 100:
            return how_many2
            break
        else:
            print('\nInvalid input. Try again.\n\n-')            

def pay_deposit_and_rent(s, a, x):
    while True:
        listey = disk.open_inventory()
        if s == 'Q':
            quit()
        elif s == '1':
            item = str(listey[0][0]).strip('1. ')
            deposit = core.deposit(40.00)
            price = core.rent_price(40.00, deposit)
            print('\nYou must pay a ' + deposit + ' deposit. It will be refunded after you return the Audio Tape.')
            print(receipt(price, a))
            disk.append_history(item, price, x)
            disk.update_inventory(item, x, listey)
            disk.resupply(listey)
            break
        elif s == '2':
            item = str(listey[1][0].strip('2. '))
            deposit = core.deposit(20.00)
            price = core.rent_price(20.00, deposit)
            print('\nYou must pay a ' + deposit + ' deposit. It will be refunded after you return the Audio Tape.')
            print(receipt(price, a))
            disk.append_history(item, y, how_many1)
            disk.update_inventory(item, how_many1, listey)
            disk.resupply(listey)
            break
        elif s == '3':
            item = str(listey[2][0]).strip('3. ')
            deposit = core.deposit(30.50)
            price = core.rent_price(30.50, deposit)
            print('\nYou must pay a ' + deposit + ' deposit. It will be refunded after you return the Audio Tape.')
            print(receipt(price, a))
            disk.append_history(item, price, how_many1)
            disk.update_inventory(item, how_many1, listey)
            disk.resupply(listey)
            break
        elif s == '4':
            item = str(listey[3][0]).strip('4. ')
            deposit = core.deposit(36.00)
            price = core.rent_price(36.00, deposit)
            print('\nYou must pay a ' + deposit + ' deposit. It will be refunded after you return the Audio Tape.')
            print(receipt(price, a))
            disk.append_history(item, price, how_many1)
            disk.update_inventory(item, how_many1, listey)
            disk.resupply(listey)
            break
        elif s == '5':
            item = (str(listey[4][0]).strip('5. '))
            deposit = core.deposit(12.00)
            price = core.rent_price(12.00, deposit)
            rental = 1.0
            print('\nYou must pay a ' + deposit + ' deposit. It will be refunded after you return the Audio Tape.')
            print(receipt(price, a))
            disk.append_history(item, price, how_many1)
            disk.update_inventory(item, how_many1, listey)
            disk.resupply(listey)
            break
        else:
            input('got: {}'.format(s))
    return price

# def returning_audio_file():
#     while True:
#         listey = disk.open_inventory()
#         listey1 = make_pretty(listey)
#         print(listey1)

#         returning = slow_type('\nWhich audio file do you need to return?\n\n-')
#         if returning == '1':

def employee_or_customer_choice():
    log = disk.open_log('history.txt')
    print((pretty_border('Welcome to Arkham Asylum Library Files! Where the villains of Gotham record '
                        'Audio Files, Available to rent to the public!')))
    while True:
        employee_or_customer = slow_type('\nAre you:\n\n1.An Employee\n2.A Customer.\n\n-').title()
        if employee_or_customer == 'Q':
            exit()
        elif employee_or_customer == '1':
            continuing_employee()
        elif employee_or_customer == '2':
            continuing_customer()
        else:
            print('\n\nInvalid. Try again\n')

def continuing_employee():
    while True:
        log = disk.open_log('history.txt')
        print('\nWhat would you like to do?\n\n')
        choosey = slow_type('1. See inventory.\n2. See revenue.\n3. See past transactions.\n\n-').title()

        if choosey == 'Q':
            exit()
        elif choosey == '1':
            opening_message()
        elif choosey == '2':
            rev = str(core.revenue1(log))
            print('\n')
            print(pretty_border(rev))
        elif choosey == '3':
            print(disk.open_log('history.txt'))
        else:
            print('\nInvalid input. Try again.\n\n')

def continuing_customer():
    while True:
        log = disk.open_log('history.txt')
        print('\n\nWhat would you like to do?\n\n')
        choose = slow_type('1. Return an Audio File.\n2. Rent an Audio File.\n3. Exit.\n\n-').title()
        if choose == 'Q':
            quit()
        # elif choose == '1':
        #   returning_audio_file()

        elif choose == '2':
            opening_message()
            s = choose_the_audio_file()
            a = due()
            x = how_many_tapes()
            w = pay_deposit_and_rent(s, a, x)
        elif choose == '3':
            exit()
        else:
            print('Invalid input. Try again.')
def main():
    employee_or_customer_choice()
if __name__ == '__main__':
    main()