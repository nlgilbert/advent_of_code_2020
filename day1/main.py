from errno import ENOENT
from os import strerror
from os.path import exists
from typing import List, Tuple

def load_input(path: str) -> List[int]:
    '''Loads the input numbers and returns them as a list.'''
    if not exists(path):
        raise FileNotFoundError(ENOENT, strerror(ENOENT), path)
    
    with open(path, 'r') as input_file:
        str_data = input_file.readlines()
        int_data = [int(x) for x in str_data]
        return int_data

def find_pair_with_sum(data: List[int], desired_sum: int) -> Tuple[int, int]:
    '''Finds the pair of numbers in the given list that add to the desired sum.'''
    sorted_data = sorted(data)
    
    low_idx = 0
    high_idx = len(sorted_data) - 1
    while low_idx < high_idx:
        low = sorted_data[low_idx]
        high = sorted_data[high_idx]
        sum = low + high
        if (sum < desired_sum):
            low_idx += 1
        elif(sum > desired_sum):
            high_idx -= 1
        else:
            # low + high = deisred_sum
            return (low, high)

    raise RuntimeError(f'No pair of numbers adds to {desired_sum}')

def find_triple_with_sum(data: List[int], desired_sum: int) -> Tuple[int, int, int]:
    '''Finds the triple of numbers in the given list that add to the desired sum.'''
    sorted_data = sorted(data)

    for low in sorted_data:
        try:
            sorted_data.remove(low)
            mid, high = find_pair_with_sum(sorted_data, desired_sum - low)
        except RuntimeError:
            # low was not a correct value. Move on
            continue

        return (low, mid, high)

    raise RuntimeError(f'No triple of numbers adds to {desired_sum}')


def main():
    # Load in the data
    data = load_input('day1/puzzle_input.txt')
    
    print('--- Part 1 ---')
    low, high = find_pair_with_sum(data, 2020)
    print(f'{low} + {high} = {low + high}')
    print(f'{low} * {high} = {low * high}')
    print('')

    print('--- Part 2 ---')
    low, mid, high = find_triple_with_sum(data, 2020)
    print(f'{low} + {mid} + {high} = {low + mid + high}')
    print(f'{low} * {mid} * {high} = {low * mid * high}')

if __name__ == '__main__':
    main()