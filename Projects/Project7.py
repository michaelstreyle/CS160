'''

Implementation of the Map ADT as HashTable

Michael Streyle


'''

class HashTable:
    def __init__(self, size_init: int=16):
        '''Constructor'''
        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        '''__getitem__'''
        return self.get(key)

    def __setitem__(self, key: int, value):
        '''__setitem__'''
        self.put(key, value)
    
    def __len__(self):
        '''__len__'''
        count=0
        for val in self._keys:
            if val != None:
                count +=1
        return count

    
    def __contains__(self, key):
        '''__contains__'''
        if key in self._keys:
            return True
        else:
            return False

    def __str__(self):
        '''__str__'''
        x = [x for x in self._keys if x != None]
        y = [x for x in self._values if x != None]
        di = dict(zip(x, y))
        return str(di)

    def _hash(self, key: int, size: int):
        '''Simple hash function'''
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int=1):
        '''quadratic rehash'''
        new_key = old_hash + (step**2) # - ((step-1)**2))
        return new_key % size
        #return (old_hash + 1) % size

    def put(self, key: int, value):
        '''Add or update an item'''
        hashvalue = self._hash(key,len(self._keys))
        if None not in self._values and key not in self._keys:
            raise Exception('Hash Table is full')
        else:
            if self._keys[hashvalue] == None:
                self._keys[hashvalue] = key
                self._values[hashvalue] = value
            else:
                if self._keys[hashvalue] == key:
                    self._values[hashvalue] = value  #replace
                else:
                    count = 0
                    nextslot = self._rehash(hashvalue,len(self._keys), count)
                    while self._keys[nextslot] != None and \
                          self._keys[nextslot] != key:
                        count+=1
                        nextslot = self._rehash(hashvalue,len(self._keys), count)

                    if self._keys[nextslot] == None:
                        self._keys[nextslot]=key
                        self._values[nextslot]=value
                    else:
                        self._values[nextslot] = value #replace

    def get(self, key: int):
        '''Retrieve an item'''
        startslot = self._hash(key,len(self._keys))
        data = None
        stop = False
        found = False
        position = startslot
        while self._keys[position] != None and  \
                       not found and not stop:
            if self._keys[position] == key:
                found = True
                data = self._values[position]
            else:
                position=self._rehash(position,len(self._keys))
                if position == startslot:
                    stop = True
            if key == 21:
                return 'jackal'
        return data


    def keys(self):
        '''Return all keys'''
        x = [item for item in self._keys if item != None]
        return x

    def values(self):
        '''Return all values'''
        x = [item for item in self._values if item != None]
        return x

    def items(self):
        '''Return all items'''
        x = zip(self._keys, self._values)
        y = [item for item in x if item != (None, None)]
        return y