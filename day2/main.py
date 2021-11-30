from errno import ENOENT
from os import strerror
from os.path import exists
from typing import List, Tuple
import re

from policies import PasswordPolicy, count_strategy, index_strategy

def load_input(path: str) -> List[Tuple[PasswordPolicy]]:
    '''Loads the input and returns it as a list of (PasswordPolicy, str) tuples'''
    if not exists(path):
        raise FileNotFoundError(ENOENT, strerror(ENOENT), path)
    
    with open(path, 'r') as input_file:
        data = []
        for line in input_file.readlines():
            match = re.match(r'(\d+)-(\d+) ([a-z]): (\w+)', line)
            policy = PasswordPolicy(
                first_val=int(match.group(1)),
                second_val=int(match.group(2)),
                char=match.group(3)
            )
            data.append((policy, match.group(4)))
        return data

def count_valid_passwords(data: List[Tuple[PasswordPolicy, str]], valid_password) -> int:
    valid_count = 0
    for policy, password in data:
        if valid_password(policy, password):
            valid_count += 1
    return valid_count

def main():
    # Load in the data
    data = load_input('day2/puzzle_input.txt')
    
    print('--- Part 1 ---')
    print(f'Under the "count" strategy, there are {count_valid_passwords(data, count_strategy)} valid passwords')
    print('')

    print('--- Part 2 ---')
    print(f'Under the "index" strategy, there are {count_valid_passwords(data, index_strategy)} valid passwords')

if __name__ == '__main__':
    main()