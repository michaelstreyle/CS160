'''
Hashing exercise code template

Michael Streyle

'''


import random


def hash_remainder(key: int, size: int):
    '''Find hash using remainder'''
    rem = key % size
    return rem

def hash_mid_sqr(key, size):
    '''Find hash using mid-square method'''
    zer = '0'
    x = str(key**2)
    if len(x)%2 == 0:
        end = len(x)
        midd = end/2
        y= int(x[int(midd)-1:int(midd)+1])  
    else:
        x = zer + x
        end = len(x)
        midd = end/2
        y= int(x[int(midd)-1:int(midd)+1])
    return y % size


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def hash_folding(key: str, size: int):
    '''Find hash using folding method'''
    summ = 0
    st = ''
    for po in key:
        if is_number(po):
            st = st + po
    start = 0            
    for s in [1, 3, 5, 7, 9]:
        summ += int(st[start:s+1])
        start = s+1
    return summ % size

def hash_str(key: str, size: int):
    '''Find string hash using simple sum-of-values method'''
    summ = 0
    for pos in range(len(key)):
        summ = summ + ord(key[pos])
    return summ%size

def hash_str_weighted(key: str, size: int):
    '''Find string hash using character positions as weights'''
    summ = 0
    for pos in range(len(key)):
        summ = summ + (ord(key[pos]) * pos)
    return summ%size


def main():
    '''Main function'''
    keys_int = [113, 117, 95, 106, 114, 108, 116, 105, 99]
    keys_int_2 = [54, 26, 93, 17, 77, 31]
    keys_intstr = ['563-555-1234', '800-555-8080', '888-555-0000']
    keys_intstr_2 = ['436-555-4601']
    keys_str = ['pavel', 'bruce', 'talia', 'harvey', 'jim', 'alfred', 'lucius', 'jonathan', 'bane']
    keys_str_2 = ['algorithm', 'logarithm']

    print('Simple remainder')
    print([hash_remainder(x, 16) for x in keys_int])
    print([hash_remainder(x, 11) for x in keys_int_2])

    print('Mid-square')
    print([hash_mid_sqr(x, 16) for x in keys_int])
    print([hash_mid_sqr(x, 11) for x in keys_int_2])

    print('Folding')
    print([hash_folding(x, 16) for x in keys_intstr])
    print([hash_folding(x, 11) for x in keys_intstr_2])

    print('String hashing')
    print([hash_str(x, 16) for x in keys_str])
    print([hash_str(x, 11) for x in keys_str_2])

    print('Weighted string hashing')
    print([hash_str_weighted(x, 16) for x in keys_str])
    print([hash_str_weighted(x, 11) for x in keys_str_2])


if __name__ == '__main__':
    main()