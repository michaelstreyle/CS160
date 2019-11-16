'''Build a ladder of words using stacks and queues'''
#!/usr/bin/env python3

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


def read_file(filename: str) -> dict:
    '''Read a file into 3 sets'''
    fo = open(filename, "r")
    x= fo.readlines()
    three = []
    four = []
    five = []
    dict_wl = {'three': [], 'four': [], 'five': []}
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
    dict_wl = {3: len(three), 4: len(four), 5: len(five)}
    return dict_wl

def diff_by_one(word1: str, word2: str) -> int:
    '''Differences between words'''
    error = 0
    for i in  range(len(word1)):
        if word1[i] != word2[i]:
            error +=1
        else:
            error +=0
    return error

def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    list_words = []
    for item in all_words:
        x = diff_by_one(word, item)
        if x == 1:
            if item not in used_words:
                list_words.append(item)
        else:
            pass
    return list_words

def repeat(queue, words_to_use, used_words):
    #pass word find possible words
    New_Queue = Queue()
    recently_added = []
    try:
        for item_stack in queue.look():
            possible_words = diff_by_one_all(item_stack.peek(), words_to_use, used_words)
            for item_update in possible_words:
                #print(item.peek(), item_update)
                if item_update not in used_words:
                    used_words.add(item_update)
                    copy = item_stack.clone()
                    copy.push(item_update)
                    recently_added.append(item_update)
                    New_Queue.enqueue(copy)
        return [New_Queue, used_words, recently_added]
    except:
        pass
    
def match_found(que, word_stop, recently_added):
    for stack in que.items:
        for item in stack.items:
            #print(item)
            if item == word_stop:
                return True
            else:
                pass
    return False
        
    
def recursive_function(queue, word_stop, words_to_use, used_words, found):
    if found is False:
        word_stop = word_stop
        new_queue = repeat(queue, words_to_use, used_words)
        match = match_found(new_queue[0], word_stop, new_queue[2])
        if match is True:
            found = True
            recursive_function(new_queue[0], word_stop, words_to_use, new_queue[1], found)
        else:
            recursive_function(new_queue[0], word_stop, words_to_use, new_queue[1], found)
    else:
        return [queue,found]

def main():
    '''Main function'''
    x=read_file('words.txt')
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
    # TODO: Implement the algorithm
    used_words = set()
    fix_method = []
    current_words = diff_by_one_all(word_start, words_to_use, used_words)
    que = Queue()
    fix_method.append(word_start)
    for item in current_words:
        fix_method.append(item)
        stack_ = Stack()
        stack_.push(word_start)
        stack_.push(item)
        que.enqueue(stack_)
    used_words.update(fix_method)

    result = recursive_function(que, word_stop, words_to_use, used_words, False)
    print(result)
    if result[1] == True:
        print(result)
        found = True
    if found:
        print('Ladder found!')
        # TODO: Print the ladder
    else:
        print('Ladder not found')
if __name__ == '__main__':
    main()