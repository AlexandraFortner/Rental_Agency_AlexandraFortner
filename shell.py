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


    first = slow_type('\n-What Audio File would you like to rent today?\n\n')
    

    if first == '1':
        scarecrow = slow_type('\nYou have chosen Dr. Crane\'s "A Study In Fear". The rental fee is 2.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if scarecrow == 'Yes':
            print('\nYou have paid a down of ')
        elif scarecrow == 'No':
            print('Very well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '2':
        hatter = slow_type('\nYou have chosen Jervis Tetch\'s "Wonderful Wonderland Fairy Tales!". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if hatter == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif hatter == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '3':
        riddler = slow_type('\nYou have chosen Edward Nygma\'s "Riddles To Blow The Mind...Literally! The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if riddler == 'Yes':
            print('\nThank you for doing business with us!')
        elif riddler == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '4':
        joker = slow_type('\nYou have chosen The Joker\'s "Ultimate Guide To Annoying The Bat". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if joker == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif joker == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '5':
        harley = slow_type('\nYou have chosen Harley Quinn\'s "How To Love A Psychopath". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if harley == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif harley == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '6':
        twoface = slow_type('\nYou have chosen Two-Face\'s "A Sigh Of Duality: Coping With Your Scars". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if twoface == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif twoface == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '7':
        fries = slow_type('\nYou have chosen Mr. Freeze\'s "Loving Unconditionally". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if fries == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif fries == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '8':
        bane = slow_type('\nYou have chosen Bane\'s "Breaking The Bat: It\'s A Snap!". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if bane == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif bane == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '9':
        strange = slow_type('\nYou have chosen Hugo Strange\'s "The Dark History Of The Medical Practice". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if strange == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif strange == 'No':
            print('\nVery well! Have a nice day!')
        else:
            print('Invalid Input.')
    elif first == '10':
        penguin = slow_type('\nYou have chosen Oswald Cobblepot\'s "Betrayal And Evil Laughter: Squawk!". The rental fee is 4.00. Would you like to rent it? Please input yes or no.\n\n-').title()
        if penguin == 'Yes':
            print('\nOh! Calloo, Callay!')
        elif penguin == 'No':
            print('\nVery well! Have a nice day!')
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