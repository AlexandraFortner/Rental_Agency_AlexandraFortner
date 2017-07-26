import core, disk, time, sys
#RENTAL AGENCY

#FUNCTIONS FOR DECORATION

typing_speed = 17 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()

#PRETTY BORDER BELOW

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
                        'Audio Files, Available for rental to the public!')))
    print('\n-What book would you like to rent today?\n\n')
    first = input(core.make_pretty(disk.open_log('inventory.txt')))

    with open('inventory.txt') as file:
        lines = file.readlines()
    message = core.pretty_menu(lines)

    inventory = disk.open_inventory()

def main():
    begin()
    

if __name__ == '__main__':
    main()