#RENTAL AGENCY

#FUNCTIONS FOR DECORATION
typing_speed = 17 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


typing_speed = 17 #wpm
def slow_type_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)

def insert_line(string, index):
    return string[:index] + '|\n|' + string[index:]
def print_squiggles(string):

    if len(string) <= 167:
        print('\n|' + '~' * len(string) + '|\n|' + string + '|\n|' + '~' * len(string) + '|\n')
    elif len(string) > 167 and len(string) < 334:
        print('\n|' + '~' * 167 + '|\n|' + insert_line(string, 167) +  ''.ljust(165), '|\n|' + '~' * 167 + ('|\n'))
    elif len(string) >= 334:
        s = insert_line(string, 167)
        b = 166 - (len(string) - 334)
        print('\n|' + '~' * 167 + '|\n|' + insert_line(s, 337) +  ''.ljust(b), '|\n|' + '~' * 167 + ('|\n'))

#MAIN CODE BELOW

def begin():