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
    
    
    print(core.make_pretty(disk.open_log('inventory.txt')))


    first = slow_type('\n-What Audio File would you like to rent today? You can rent up to a week.\n\n')

    if first == '1':
        scarecrow = slow_type('\nYou have chosen Dr. Crane\'s "A Study In Fear".\nThe rental fee is 1.00, with a deposit of 4.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if scarecrow == 'Yes':
            print(core.receipt(5.00))
        elif scarecrow == 'No':
            print('Very well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '2':
        hatter = slow_type('\nYou have chosen Jervis Tetch\'s "Wonderful Wonderland Fairy Tales!".\nThe rental fee is 1.00, with a deposit of 2.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if hatter == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif hatter == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '3':
        riddler = slow_type('\nYou have chosen Edward Nygma\'s "Riddles To Blow The Mind...Literally!".\nThe rental fee is 1.00, with a deposit of 3.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if riddler == 'Yes':
            print('\nThank you for doing business with us!')
        elif riddler == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '4':
        joker = slow_type('\nYou have chosen The Joker\'s "Ultimate Guide To Annoying The Bat".\nThe rental fee is 1.00, with a down payment of 2.70. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if joker == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif joker == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '5':
        harley = slow_type('\nYou have chosen Harley Quinn\'s "How To Love A Psychopath".\nThe rental fee is 1.00, with a down payment of 2.30. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if harley == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif harley == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '6':
        twoface = slow_type('\nYou have chosen Two-Face\'s "A Sigh Of Duality: Coping With Your Scars".\nThe rental fee is 1.00, with a down payment of 2.60. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if twoface == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif twoface == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '7':
        fries = slow_type('\nYou have chosen Mr. Freeze\'s "Loving Unconditionally".\nThe rental fee is 1.00, with a down payment of 3.00. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if fries == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif fries == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '8':
        bane = slow_type('\nYou have chosen Bane\'s "Breaking The Bat: It\'s A Snap!".\nThe rental fee is 1.00, with a down payment of 3.60. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if bane == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif bane == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '9':
        strange = slow_type('\nYou have chosen Hugo Strange\'s "The Dark History Of The Medical Practice".\nThe rental fee is 1.00, with a down payment of 1.20. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if strange == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif strange == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '10':
        penguin = slow_type('\nYou have chosen Oswald Cobblepot\'s "Betrayal And Evil Laughter: Squawk!".\nThe rental fee is 1.00, with a down payment of 2.50. Your deposit will be refunded after you return the rented Audio File.\nWould you like to rent it? Please input yes or no.\n\n-').title()
        if penguin == 'Yes':
            print('\nThank you for your business! Please come again!')
        elif penguin == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    else:
        print('Invalid Input.')

    
    with open('inventory.txt') as file:
        lines = file.readlines()
    message = core.pretty_menu(lines)

    inventory = disk.open_inventory()

def main():
    begin()
if __name__ == '__main__':
    main()