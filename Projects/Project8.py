'''

Build a ladder of words using stacks and queues

Michael Streyle

'''


WORDS_OF_3 = set()
WORDS_OF_4 = set()
WORDS_OF_5 = set()

class Stack:
    '''Implementing Stack ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''Is stack empty?'''
        return self.items == []
    def size(self):
        '''Return stack size'''
        return len(self.items)
    def push(self, item):
        '''Add new item to stack'''
        self.items.append(item)
    def pop(self):
        '''Remove an item from stack'''
        return self.items.pop()
    def peek(self):
        '''Look at the top item'''
        return self.items[-1]
    def clone(self):
        '''Cloning a stack'''
        new_stack = Stack()
        new_stack.items = self.items.copy()
        return new_stack
    def look(self):
        return self.items

def set_variable(list_, truth):
    global result_
    global found_
    result_ = list_
    found_ = truth
    return      
    
class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []
    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []
    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)
    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()
    def size(self):
        '''How big is it?'''
        return len(self.items)
    def look(self):
        return self.items

def match(que, word_stop, added):
    for s in que.items:
        for i in s.items:
            if i == word_stop:
                return True
            else:
                pass
    return False

def read_file(filename: str) -> dict:
    '''Read a file into 3 sets'''
    i = open(filename, "r")
    x = i.readlines()
    three = []
    four = []
    five = []
    word_dict = {'three': [], 'four': [], 'five': []}
    for item in x:
        if len(item) == 6:
            item = item.rstrip('\n')
            five.append(item)
        elif len(item) == 5:
            item = item.rstrip('\n')
            four.append(item)
        elif len(item) == 4:
            item = item.rstrip('\n')
            three.append(item)
    WORDS_OF_3.update(three)
    WORDS_OF_4.update(four)
    WORDS_OF_5.update(five)
    word_dict = {3: len(three), 4: len(four), 5: len(five)}
    return word_dict

def repeat(queue, words_to_use, used_words):
    q = Queue()
    added = []
    try:
        for s in queue.look():
            pwords = diff_by_one_all(s.peek(), words_to_use, used_words)
            for i in pwords:
                if i not in used_words:
                    used_words.add(i)
                    copy = s.clone()
                    copy.push(i)
                    added.append(i)
                    q.enqueue(copy)
        return [q, used_words, added]
    except:
        pass

        
def distance(word1: str, word2: str) -> int:
    '''Differences between words'''
    dist = 0
    for i in  range(len(word1)):
        if word1[i] != word2[i]:
            dist +=1
        else:
            dist +=0
    return dist

def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    word_li = []
    for item in all_words:
        x = distance(word, item)
        if x == 1:
            if item not in used_words:
                word_li.append(item)
        else:
            pass
    return word_li




def build_ladder(queue, word_stop, words_to_use, used_words, found):
    if found is False:
        word_stop = word_stop
        new_queue = repeat(queue, words_to_use, used_words)
        match1 = match(new_queue[0], word_stop, new_queue[2])
        if match1 is True:
            found = True
            build_ladder(new_queue[0], word_stop, words_to_use, new_queue[1], found)
        else:
            build_ladder(new_queue[0], word_stop, words_to_use, new_queue[1], found)
    else:
        for stack in queue.items:
            if stack.peek() == 'water':
                set_variable(stack.items, found)
                return


def main():
    '''Main function'''
    read_file('words.txt')
    word_start = 'stone'
    word_stop = 'water'
    found = False
    if len(word_start) != len(word_stop):
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    if (len(word_start)) == 3:
        words_to_use = WORDS_OF_3
    elif (len(word_start)) == 4:
        words_to_use = WORDS_OF_4
    elif (len(word_start)) == 5:
        words_to_use = WORDS_OF_5
    else:
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    
    print("Let's turn '%s' into '%s'" % (word_start, word_stop))
    used_words = set()
    list4 = []
    current_words = diff_by_one_all(word_start, words_to_use, used_words)
    que = Queue()
    list4.append(word_start)
    for item in current_words:
        list4.append(item)
        stack_ = Stack()
        stack_.push(word_start)
        stack_.push(item)
        que.enqueue(stack_)
    used_words.update(list4)
    build_ladder(que, word_stop, words_to_use, used_words, False)
    if found_:
        found = found_
    else:
        found = False
    if found:
        print('Ladder found!')
        result_.reverse()
        for item in result_:
            print(item)
    else:
        print('Ladder not found')



if __name__ == '__main__':
    main()