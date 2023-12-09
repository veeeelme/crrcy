from google_currency import convert
import json
from sys import argv


# function for convert from currency to currency without interactive mode
def convert_non_interactive_mode(from_crrcy, to_crrcy, amount):
    return convert(from_crrcy, to_crrcy, amount)


def convert_interactive_mode():  # function for convert from currency to currency in interactive mode
    while True:
        try:
            from_crrcy = input('From what currency you want to convert >> ')
            to_crrcy = input('To what currency you want to convert >> ')
            amount = int(
                input('What amount of currency you want to convert >> '))
        except ValueError as ve:
            print(ve)
            print('Responce cant be empty')
        convert_data = convert(from_crrcy, to_crrcy, amount)
        return convert_data


def convert_data_parser(data):  # function that parse json data from previous methods
    parsed_data = json.loads(data)
    return f'It is {parsed_data["amount"]} {parsed_data["to"]}'


try:
    if argv[1] == '-i':
        print(convert_data_parser(convert_interactive_mode()))
        print('See crrcy -h for help')

    if argv[1] == '-h':
        print('For use programm in one line: crrcy [currency you want to convert] [currency you want to convert to] [amount]\n'
              'For interactive mode: crrcy -in\n'
              'For help: crrcy -h or crrcy -help')

    if len(argv) >= 4:
        to_crrcy = argv[1]
        from_crrcy = argv[2]
        amount = int(argv[3])
        print(convert_data_parser(
            convert_non_interactive_mode(to_crrcy, from_crrcy, amount)))
        print('See crrcy -h for help')
except Exception as e:
    print(e)
    print('Some error has occured. See crrcy -h for')
