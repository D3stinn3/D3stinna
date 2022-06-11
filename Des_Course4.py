import random
import time


def mult():
    print('this is the multiplication game!')
    time.sleep(3)
    print('wacha tuanze...')
    time.sleep(3)
    num_1 = input('please input the first number: ')
    num_2 = input('please input the second number!')
    ns = int(num_1)
    nt = int(num_2)
    the_multiplication = ns * nt
    print(f'nambari ya kwanza: {ns}')
    print(f'nambari ya pili: {nt}')
    if num_1 == num_2:
        print(the_multiplication)
        print('this is the real multiplication')
    else:
        print('this is multiplication between numbers that are not the same!, the fake multiplication')
    if the_multiplication / nt == ns:
        print('this is the reverse percentage calculation')
    else:
        print('abomination in mathematics!')
    the_dict = dict.fromkeys('anna', 'naan')
    the_dict1 = {x: x.uppeer() for x in the_dict}
    if 'a' in the_dict1.keys():
        print('the gap is still there')
    elif 'n' in the_dict1.keys():
        print('the gap is between')
    else:
        print('where is the gap')
    return the_multiplication


def birthday_updated():
    birthday_dict = {'destinne': 'Apr 21', 'mary': 'Aug 10', 'trig': 'Jul 14'}

    while True:
        print('please input birthday to search in database\n')
        name = input()
        if name == '':
            break
        if name in birthday_dict:
            print('this name is existent in the database!')
            print('please wait, searching through...')
            time.sleep(3)
            print('request found!')
            time.sleep(3)
            print(birthday_dict[name] + ' is the birthdate for ' + name)
        else:
            print('please wait when searching through...')
            time.sleep(3)
            print('this name is non existent in the database!')
            time.sleep(3)
            birthday = input('please input birthdate for found applicant!\n')
            birthday_dict[name] = birthday
            time.sleep(2)
            print('Birthday database has been updated...')
            if (birthday == 'Jul 14' and name == 'trig') and (birthday == 'Apr 21' and name == 'destinne') and (
                    birthday == 'Aug 10' and name == 'mary'):
                time.sleep(3)
                print('this is the actual birthday nice choice')
                time.sleep(2)
                if birthday == name:
                    time.sleep(2)
                    print(f'{birthday} and {name} identical!')
                    break
                else:
                    time.sleep(2)
                    print('%s and %s not identical!' % (birthday, name))
        lis_by_key = birthday_dict.get('sam', 0)
        time.sleep(2)
        print(birthday_dict, lis_by_key)
        break


birthday_updated()
