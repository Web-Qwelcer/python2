import requests
from pprint import pprint
URL = 'https://api.covid19api.com/summary'
covid19 = requests.get(URL)
covid19_global = covid19.json()['Global']
covid19 = covid19.json()['Countries']
tytles = [item for item in list(covid19[0].keys()) if item not in [
    'ID', 'CountryCode', "Slug", "Date", "Premium"]]

def byNewConfirmed_key(covid19):
    return covid19['NewConfirmed']

try:
    exit = False
    while not exit:
        choise = int(input('Select an action -> \n 1. Show COVID information\n 2. Sort by new confirmed\n 3. Show detail Country \n 4. Show global information \n5. Exit \n--->>'))
        if choise == 1:
            for item in tytles:
                if item == 'Country':
                    print("{0:_^31s}".format(item), end=' ')
                else:
                    print("{0:_>20s}".format(item), end=' ')
            else:
                print(' ')

            for item in covid19:
                for key in item:
                    if key in tytles:
                        if key == 'Country':
                            print("{0:<31}".format(item[key]), end=' ')
                        else:
                            print("{0:>20}".format(item[key]), end=' ')
                    else:
                        print('')
        elif choise == 2:
            covid19 = sorted(covid19, key=byNewConfirmed_key, reverse=True)
            for item in tytles:
                if item == 'Country':
                    print("{0:_^31s}".format(item), end=' ')
                else:
                    print("{0:_>20s}".format(item), end=' ')
            else:
                print(' ')

            for item in covid19:
                for key in item:
                    if key in tytles:
                        if key == 'Country':
                            print("{0:<31}".format(item[key]), end=' ')
                        else:
                            print("{0:>20}".format(item[key]), end=' ')
                else:
                    print('')
        elif choise == 3:
            country = (input('Enter the desired country ->\n')).capitalize()
            for item in covid19:
                for key in item:
                    if key in tytles:
                        if item[key] == country:
                            pprint(item)
        elif choise == 4:
            pprint(covid19_global)
        elif choise == 5:
            exit = True
            print('Bye!')
        else:
            print('')
except Exception:
    print('Error!!!\n Enter correct number...')
