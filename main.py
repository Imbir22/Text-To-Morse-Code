from morse_code import morse_dict

print('Text to Morse Code Conventer')

def morse_conventer():
    user_input = input('\nInput your text here: ')
    morse_message = ''
    program_run = True
    for sign in user_input:
        if sign == ' ':
            morse_message += 'space,'
        elif sign.lower() not in morse_dict:
            print('Dissalowed signs try again\n')
            program_run = False
        else:
            morse_message += morse_dict[sign.lower()]+','

    if program_run == True:
        print(f'Your message in morse code is: \n\n {morse_message}')
    else:
        morse_conventer()

morse_conventer()
program_run = True
while program_run:
    answer = input('\nDo you want to code another message? Y/N?:\n')
    if answer.lower() == 'y':
        morse_conventer()
    elif answer.lower() == 'n':
        program_run = False
    else:
        print('Invalid answer. Try again!')



input('\n\nPress Enter to close the program')


