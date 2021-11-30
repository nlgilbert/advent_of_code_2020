from errno import ENOENT
from os import cpu_count, strerror
from os.path import exists
from typing import List, Tuple

def load_input(path: str) -> List[str]:
    '''Loads the input and returns it as a list of (PasswordPolicy, str) tuples'''
    if not exists(path):
        raise FileNotFoundError(ENOENT, strerror(ENOENT), path)
    
    with open(path, 'r') as input_file:
        raw_data = input_file.readlines()
        stripped_data = [line.strip() for line in raw_data]
        return stripped_data

def count_trees(map: List[str], right: int, down: int) -> int:
    tree_count = 0
    col = 0
    for row in range(0, len(map), down):
        if map[row][col] == '#':
            tree_count += 1
        col = (col + right) % len(map[row])
    return tree_count

def main():
    # Load in the data
    map = load_input('day3/puzzle_input.txt')
    
    print('--- Part 1 ---')
    print(f'At a slope of "right 3, down 1" you would encounter {count_trees(map, 3, 1)} trees.')
    print('')

    print('--- Part 2 ---')
    tree_counts = {
        '1,1': count_trees(map, 1, 1),
        '3,1': count_trees(map, 3, 1),
        '5,1': count_trees(map, 5, 1),
        '7,1': count_trees(map, 7, 1),
        '1,2': count_trees(map, 1, 2)
    }
    print(f'At a slope of "right 1, down 1" you would encounter {tree_counts["1,1"]} trees.')
    print(f'At a slope of "right 3, down 1" you would encounter {tree_counts["3,1"]} trees.')
    print(f'At a slope of "right 5, down 1" you would encounter {tree_counts["5,1"]} trees.')
    print(f'At a slope of "right 7, down 1" you would encounter {tree_counts["7,1"]} trees.')
    print(f'At a slope of "right 1, down 2" you would encounter {tree_counts["1,2"]} trees.')
    product = 1
    for tree_count in tree_counts.values():
        product *= tree_count
    print(f'The product of all trees encountered is {product}.')


if __name__ == '__main__':
    main()