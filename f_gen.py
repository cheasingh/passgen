from random import choice, shuffle
from math import ceil

# character to include
SPECIAL_CHAR = ['!', '@', '#', '$', '%', '^', '&', '*', '=']
ALPHA_CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CAP_ALPHA_CHAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUM_CHAR = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# add password to password pool
char_pool = [SPECIAL_CHAR, ALPHA_CHAR, NUM_CHAR, CAP_ALPHA_CHAR]


def gen_pass(password_char):
    # password need to be larger than 3
    if password_char <= len(char_pool):
        raise ValueError(
            f"Password length need to be larger than {len(char_pool)}")

    password = []

    run_round = ceil(password_char/len(char_pool))
    minus_res = password_char - len(char_pool)

    for i in range(run_round):

        if minus_res > 0:
            for p in char_pool:
                password += choice(p)

        if len(char_pool) >= minus_res:
            for x in range(minus_res):
                password += choice(char_pool[x])

        if minus_res <= password_char:
            minus_res -= len(char_pool)

    shuffle(password)

    usable_password = ''.join(password)
    return usable_password
