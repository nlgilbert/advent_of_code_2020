from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class PasswordPolicy:
    '''A genereal password policy'''
    first_val: int
    second_val: int
    char: str

def count_strategy(policy: PasswordPolicy, password: str) -> bool:
    count = password.count(policy.char)
    if policy.first_val <= count <= policy.second_val:
        return True
    return False

def index_strategy(policy: PasswordPolicy, password: str) -> bool:
    char1 = password[policy.first_val - 1]
    char2 = password[policy.second_val - 1]
    return (char1 == policy.char) ^ (char2 == policy.char)
