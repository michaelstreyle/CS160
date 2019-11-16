'''
Touchscreen Keyboard

Michael Streyle

9/17/18

'''




def Checker(filename: str) -> dict:
    '''Rank words by their proximity to the target'''
    outer_dict = {}
    with open(filename, 'r') as filename:
        test_count = 0
        for line in filename:
            line = line.strip('\n')
            if str.isdigit(line) == False:
                length = str.split(line)
                if len(length) == 2:
                    test_count += 1
                    typed_word = length[0]
                    outer_dict[typed_word] = {}
                elif len(length) == 1:
                    try:
                        outer_dict[typed_word][line] = (test_count, distance(typed_word, line))
                    except:
                        pass 
    return outer_dict




def distance(word1: str, word2: str) -> int:
    ''' Calculate the distance between two words'''
    total = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            dis = letter_matrix[word1[i]][word2[i]]
            total += dis
    return total



        
def find_letter(letter : str):
    try:
        x = top.index(letter)
        level = 0
    except:
        pass
    try:
        x = middle.index(letter)
        level = 1
    except: 
        pass
    try:
        x = bottom.index(letter)
        level = 2
    except:
        pass
    return level, x


def letter_distance(letter1 : str, letter2 : str) -> int:
    height = abs(letter1[0] - letter2[0])
    width = abs(letter1[1] - letter2[1])
    total = height + width
    return total



def main(filename):
    '''Entry point'''
  #print('Processing file {}'.format(filename))
    cker = Checker(filename)
    data = []
    for i in cker.values():
        for p in i.items():
            data.append((p[0], p[1]))
    sorted_by_second = sorted(data, key=lambda x : (x[1], x[0]))
    for p in sorted_by_second:
        print(p[0], p[1][1])
    
    
f= open("the_letters.txt","w+") #making a file of the keys on a keyboard
f.write('qwertyuiop\nasdfghjkl\nzxcvbnm')
f.close()

with open('the_letters.txt', 'r') as letters:
    x=[]
    for line in letters:
        x.append(list(line))
    top = x[0]
    middle = x[1]
    bottom = x[2]
    top.pop()
    middle.pop()

    letter_mat = {}
    for el in letters:
        for i in letters:
            letter_mat[el] = i

    letter_matrix = {}
    li = top + middle + bottom
    for x in li:
        letter_matrix[x] = {}  
    for x, y in [(x,y) for x in li for y in li]:
        letter_matrix[x][y] = letter_distance(find_letter(x), find_letter(y))
    



def spell_check(filename): #this is for making the test happy
    main(filename)
    
if __name__ == '__main__':
    main('sample.in.txt')



    