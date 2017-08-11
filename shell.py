import core, disk, time, sys, random
#ARKHAM ASYLUM AUDIO FILE RENTAL AGENCY
#FUNCTIONS FOR DECORATION BEGIN
#BELOW
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
typing_speed = 17  #wpm


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
        return '\n|' + '~' * len(
            string) + '|\n|' + string + '|\n|' + '~' * len(string) + '|\n'
    elif len(string) > 167 and len(string) < 334:
        return '\n|' + '~' * 167 + '|\n|' + insert_line(
            string, 167) + ''.ljust(165), '|\n|' + '~' * 167 + ('|\n')
    elif len(string) >= 334:
        s = insert_line(string, 167)
        b = 166 - (len(string) - 334)
        return '\n|' + '~' * 167 + '|\n|' + insert_line(
            s, 337) + ''.ljust(b), '|\n|' + '~' * 167 + ('|\n')


def pretty_choice(choice):
    string = ''
    for item in choice:
        string == string.strip('\'')
    return string


def make_pretty(inventory):
    stringy = ''
    for i in range(1, len(inventory) + 1):
        stringy += "\n {}. {:<60}{:>30}".format(
            inventory[i]['Number'], inventory[i]['Name'],
            "Stocked Inventory: " + inventory[i]['How Many'])
    return stringy + '\n'


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#FUNCTIONS FOR DECORATION END
#MAIN CODE BELOW
def id_letters_random(log):
    """
    Generates a random string of certain specified letters. For Id purposes.
    """
    id1 = ''
    choicey1 = 'F', 'u', 'A', 'Y', 'E', 'd', 'k', 'a', 'i', 'm', 'e', 'o', 'w', 'x', 'X', 'b', 'L', 'T', 'G', 'h'
    for i in range(5):
        id1 += random.choice(choicey1)
    return id1


def receipt(price, due_date, id2):
    """(float) -> float
    prints all information to user in the form of a receipt.
    """
    totally1 = core.math_for_receipt(price, due_date)
    print('\n___________________________________\n|\n|Original Price: {}'.
          format(price))
    print('|+ State Tax: {:.2f}'.format(core.StateSalesTax(price)))
    print('|+ County Tax: {:.2f}'.format(core.CountySalesTax(price)))
    print('|Due In: {} days.'.format(due_date))
    print('|Total: {:.2f}'.format(totally1))
    print('|Id: {} <-REMEMBER THIS ID.'.format(id2))
    print(
        '|____________________________________\n\nHere\'s your receipt! Thank you for shopping with us!'
    )
    return ''


def opening_message():
    print(
        '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    )

    listey = disk.open_inventory()
    listey1 = make_pretty(listey)
    print(listey1)

    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
    )


def choose_the_comic_book():
    while True:
        print('To exit this application, click "q". Type Below, Please:\n')
        listey = disk.open_inventory()
        first = slow_type(
            '\n-What comic book would you like to rent today?\n\n-').title()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if first == 'Q':
            quit()
        elif first not in numbers:
            print('\n\nInvalid choice. Try again.\n-')
        elif first in numbers:
            item = str(listey[int(first)]['Name'])
            print('\n•You\'ve chosen ' + item + '•')
            break
        else:
            print('\nInvalid Input. Try again.\n\n-')

    return first


def choose_the_comic_book_return():
    while True:
        print('To exit this application, click "q". Type Below, Please:\n')
        listey = disk.open_inventory()
        first = slow_type(
            '\n-What comic book would you like to return today?\n\n-').title()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if first == 'Q':
            quit()
        elif first not in numbers:
            print('\n\nInvalid choice. Try again.\n-')
        elif first in numbers:
            item = str(listey[int(first)]['Name'])
            print('\n•You\'ve chosen ' + item + '•')
            break

    return first


def due():
    while True:
        valid_number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        due_date = slow_type(
            '\nHow many days would you like to rent?\n\n-').title()
        if due_date == 'Q':
            quit()
        elif due_date not in valid_number_list:
            print(
                '\nInvalid Input. Please input a number that is 1-7. Try again.'
            )
        else:
            return due_date
            break
    return str(due_date)


def how_many_comics():
    while True:
        how_many1 = int(
            slow_type('\nHow many would you like to rent?\n\n-').title())
        if how_many1 == 'Q':
            exit()
        elif how_many1 > 100:
            print(
                '\nSorry, we have a limit of 100 comic book copies. Please input a lower number.\n\n-'
            )
        elif how_many1 <= 100:
            return how_many1
            break
        else:
            print('\nInvalid input. Try again.\n\n-')


def how_many_comics_returning():
    while True:
        how_many1 = slow_type(
            '\nHow many would you like to return?\n\n-').title()
        if how_many1 == 'Q':
            exit()
        elif how_many1 > 100:
            print(
                '\nSorry, we have a limit of 100 comic book copies. Please input a lower number.\n\n-'
            )
        elif how_many1 <= 100:
            return int(how_many1)
            break
        else:
            print('\nInvalid input. Try again.\n\n-')


def pay_deposit_and_rent(choose_a_comic_book1, due_in, how_many_comics1):
    while True:
        valid_number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        if choose_a_comic_book1 == 'Q':
            quit()
        elif choose_a_comic_book1 not in valid_number_list:
            print('\nTry again.\n\n-')
        else:
            log = disk.open_log('history.txt')
            listey = disk.open_inventory()
            item = str(listey[int(choose_a_comic_book1)]['Name'])
            current_state = 'rented'
            id2 = id_letters_random(log)
            x = float(listey[int(choose_a_comic_book1)]['Price'])
            deposit = core.deposit(x)
            price = core.rent_price(x, deposit)
            log[id2] = {
                'Name': item.strip(),
                'Price': price,
                'How Many': how_many_comics1,
                'Id Letters': id2.strip(),
                'Current State': current_state
            }
            print(
                '\nYou must pay a ' + deposit +
                ' deposit. It will be refunded after you return the Audio Tape.'
            )
            print(receipt(price, due_in, id2))
            disk.append_history(item, price, how_many_comics1, id2,
                                current_state)
            disk.update_inventory(item, how_many_comics1, listey,
                                  choose_a_comic_book1)
            disk.resupply(listey)
            break
    return price


def returning_comics(choose_comic_to_return, choose_a_comic_book):
    while True:
        log = disk.open_log('history.txt')
        inventory = disk.open_inventory()
        current_state = 'returned'
        returning = slow_type(
            '\nPlease input your Id on your previous receipt.\n\n-')
        if returning == 'q':
            quit()
        if returning in log.keys():
            log[returning]['Current State'] = 'returned'
            print('\nAmount of Deposit Returned: {}'.format(
                log[returning]['Price']))
            disk.update_inventory_returning(returning, choose_a_comic_book,
                                            inventory, choose_comic_to_return)
            str_log = core.convert_into_string(log)
            disk.append_history_returning(
                log[returning]['Name'], log[returning]['Price'],
                choose_a_comic_book, log[returning]['Id Letters'],
                current_state)
        return None
        print(
            '\nSorry! That is not a valid code for our past transactions! Try again!\n'
        )


def employee_or_customer_choice():
    print((pretty_border('Welcome to The Arkham Asylum!')))
    while True:
        employee_or_customer = slow_type(
            '\nAre you:\n\n1.An Employee\n2.A Customer.\n\n-').title()
        if employee_or_customer == 'Q':
            exit()
        elif employee_or_customer == '1':
            continuing_employee()
        elif employee_or_customer == '2':
            continuing_customer()
        else:
            print('\n\nInvalid. Try again.\n')


def continuing_employee():
    while True:
        log = disk.open_log('history.txt')
        print('\nWhat would you like to do?\n\n')
        choosey = slow_type(
            '1. See inventory.\n2. See revenue.\n3. Exit to beginning.\n4. Exit the program.\n\n-'
        ).title()

        if choosey == 'Q':
            exit()
        elif choosey == '1':
            opening_message()
        elif choosey == '2':
            revenue2 = disk.open_log('history.txt')
            rev = core.revenue1(revenue2)
            print('\n')
            print(rev)
        elif choosey == '3':
            print(employee_or_customer_choice())
        elif choosey == '4':
            exit()
        else:
            print('\nInvalid input. Try again.\n\n')


def continuing_customer():
    while True:
        print('\nWhat would you like to do?\n\n')
        choose = slow_type(
            '1. Return an comic book.\n2. Rent an comic book.\n3. Exit to beginning.\n4. Exit the program.\n\n-'
        ).title()
        if choose == 'Q':
            quit()
        elif choose == '1':
            opening_message()
            choose_comic_to_return = choose_the_comic_book_return()
            choose_a_comic_book = how_many_comics_returning()
            returning_comics(choose_comic_to_return, choose_a_comic_book)
        elif choose == '2':
            opening_message()
            choose_a_comic_book1 = choose_the_comic_book()
            due_in = due()
            how_many_comics1 = how_many_comics()
            pay_deposit_and_rent(choose_a_comic_book1, due_in,
                                 how_many_comics1)
        elif choose == '3':
            print(employee_or_customer_choice())
        elif choose == '4':
            exit()
        else:
            print('Invalid input. Try again.')


def main():
    employee_or_customer_choice()


if __name__ == '__main__':
    main()