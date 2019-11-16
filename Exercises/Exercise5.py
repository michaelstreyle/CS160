'''

Recursion exercise code template

Michael Streyle
10/11/18

I added a line at the bottom of my output to check that the gcd function works. 

'''


def gcd(a: int, b: int) -> int:
    if not b:
        return a
    return gcd(b, a % b)

def iterative_hg(levels: int) -> None:
    for i in range(levels -1, -1, -1):
        print('{:^{}}'.format('*' * (2 * i + 1), 2 * (levels -1) + 1))
    for i in range (1, levels):
        print('{:^{}}'.format('*' * (2 * i + 1), 2 * (levels - 1) + 1))

    

def iterative_diamond(levels: int) -> None:
    for i in range(levels - 1):
        print('{:^{}}'.format('*' * (2 * i + 1), 2 * (levels -1) + 1))
    for i in range (levels -1, -1, -1):
        print('{:^{}}'.format('*' * (2 * i + 1), 2 * (levels - 1) + 1))



def recursive_hg(levels: int) -> None:
    third_tree(levels-1, levels)
    print('{:^{}}'.format('*', 2 * (levels -1) + 1))
    first_tree(1, levels)

def third_tree(level, levels):
    if level < 1:
        return
    print('{:^{}}'.format('*' * (2 * level + 1), 2 * (levels -1) + 1))
    third_tree(level - 1, levels)  

def first_tree(level, levels):
    if level == levels:
        return
    print('{:^{}}'.format('*' * (2 * level + 1), 2 * (levels -1) + 1))
    first_tree(level +1, levels)


def recursive_diamond(levels: int) -> None:
    second_tree(0, levels)
    print('{:^{}}'.format('*' * (2 * (levels - 1) + 1), 2 * (levels - 1) + 1))
    fourth_tree(levels - 1, levels)

def second_tree(level, levels):
    if level == levels -1:
        return
    print('{:^{}}'.format('*' * (2 * level + 1), 2 * (levels - 1) + 1))
    second_tree(level + 1, levels)

def fourth_tree(level, levels):
    if level < 1:
        return
    print('{:^{}}'.format('*' * (2 * (level - 1) + 1), 2 * (levels - 1) + 1))
    fourth_tree(level - 1, levels)




def main():
    '''Main function'''

    print('Hourglass (iterative)')
    iterative_hg(5)
    print('Hourglass (recursive)')
    recursive_hg(5)
    print('Diamond (iterative)')
    iterative_diamond(5)
    print('Diamond (recursive)')
    recursive_diamond(5)
    print()
    print('Check Recursive GCD Function with gcd(1860,2020):' , gcd(1860, 2020))
    


if __name__ == '__main__':
    main()