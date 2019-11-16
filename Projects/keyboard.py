'''
Touchscreen Keyboard

Michael Streyle
'''
#!/usr/bin/env python3

class Keyboard:
    '''Class Keyboard'''
    def __init__(self, filename) -> None:
        '''QWERTY Keyboard Constructor'''
        with open(filename, 'r') as letters:
            x=[]
            for line in letters:
                x.append(list(line))
            self._top = x[0]
            self._middle = x[1]
            self._bottom = x[2]
            self._top.pop()
            self._middle.pop()

    def find_letter(self, letter):
        try:
            x = self._top.index(letter)
            level = 0
        except: ValueError('Not in top list')
        try:
            x = self._middle.index(letter)
            level = 1
        except: ValueError('Not in middle list')
        try:
            x = self._bottom.index(letter)
            level = 2
        except: ValueError('Not a valid Letter')
        return level, x
        
    def letter_distance(self, letter1, letter2):
        height = abs(letter1[0] - letter2[0])
        width = abs(letter1[1] - letter2[1])
        self._total = height + width
        return self._total    

    def spell_check(self, filename: str):
        '''Rank words by their proximity to the target'''
        with open(filename, 'r') as filename:
            self._outer_dict = {}
            for line in filename:
                line = line.strip('\n')
                if str.isdigit(line) == False:
                    length = str.split(line)
                    if len(length) == 2:
                        typed_word = length[0]
                        self._outer_dict[typed_word] = {}
                    if len(length) == 1:
                        try:
                            self._outer_dict[typed_word][line] = self.distance(typed_word, line)
                        except:
                            pass 
        return self._outer_dict



    def distance(self, word1: str, word2: str):
        ''' Calculate the distance between two words'''
        if len(word1) == len(word2):
            self._total = 0
            for i in range(0, len(word1)):
                l1 = self.find_letter(word1[i])
                l2 = self.find_letter(word2[i])
                dis = self.letter_distance(l1, l2)
                self._total += dis
            return self._total
        else:
            raise ValueError('Words must be the same length')
    



    # def __str__(self) -> str:
    #     '''Object as a string'''
    #     if self.numerator > self.denominator:
    #         return str(self.numerator // self.denominator) + ' ' + \
    #             str(self.numerator % self.denominator) + '/' + str(self.denominator)
    #     else:
    #         return str(self.numerator) + '/' + str(self.denominator)

    




def main(filename):
    '''Entry point'''
    print('Processing file {}'.format(filename))
    keyb = Keyboard(filename)
    keyb.spell_check(filename)
    data = []
    for i in keyb.spell_check(filename).values():
        for p in i.items():
            data.append((p[0], p[1]))
    sorted_by_second = sorted(data, key=lambda tup: tup[1])

    for p in sorted_by_second:
        print(p[0], p[1])


if __name__ == "__main__":
    main('sample.in.txt')

