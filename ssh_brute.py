from scripts import brute, scan
from scripts.helpers import get_parser
from configs.exceptions import ArgumentBadValueError, NoKeyError
from dotenv import dotenv_values
import os

def phase_1(env, arguments):
    os.system('clear')
    
    print('[SCAN] START SCANNING...\n')
    
    scan.start(env, arguments)
    
    if dotenv_values()['ENTER_TO_CONTINUE'] == 'true':
        input('PRESS ENTER TO CONTINUE...')

def phase_2(env, arguments):
    os.system('clear')
    
    print('[BRUTE] START BRUTEFORCING...')
    
    brute.start(env, arguments)

def main():
    ENV: dict = dotenv_values()
    ENV['THREADS'] = int(ENV['THREADS'])
    
    parser = get_parser(ENV)
    arguments = parser.parse_args()
    
    if arguments.mode == 'scan':
        phase_1(ENV, arguments)
    elif arguments.mode == 'brute':
        if arguments.logins_file and arguments.passwords_file:
            phase_2(ENV, arguments)
        else:
            raise NoKeyError()
    if arguments.mode == 'all':
        if arguments.logins_file and arguments.passwords_file:
            phase_1(ENV, arguments)
            phase_2(ENV, arguments)
        else:
            raise NoKeyError()
    else:
        raise ArgumentBadValueError('-m (--mode)')

if __name__ == '__main__':
    main()
