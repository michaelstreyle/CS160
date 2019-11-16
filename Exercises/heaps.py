"""

Limited size max Binary Heap implementation

Michael Streyle
11/15/18



"""


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self, limit: int = 0):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while (cur_idx - 1) // 2 >= 0:
            if self.heap[cur_idx] > self.heap[(cur_idx - 1) // 2]:
                tmp = self.heap[(cur_idx - 1) // 2]
                self.heap[(cur_idx - 1) // 2] = self.heap[cur_idx]
                self.heap[cur_idx] = tmp
            cur_idx = (cur_idx - 1) // 2

    def perc_down(self, cur_idx):
        """Moving a node down"""
        while (cur_idx * 2 + 1) < self.size:
            mc = self.get_max_child(cur_idx)
            if self.heap[cur_idx] < self.heap[mc]:
                tmp = self.heap[cur_idx]
                self.heap[cur_idx] = self.heap[mc]
                self.heap[mc] = tmp
            cur_idx = mc

    def insert(self, item):
        """Adding a new item"""
        if self.size < self.max_size or self.max_size == 0:
            self.heap.append(item)
            self.size = self.size + 1
            self.perc_up(self.size - 1)
        else:
            self.smallest = min(self.heap)
            self.heap.remove(self.smallest)
            self.heap.append(item)
            self.perc_up(self.size - 1)




    def heapify(self, not_a_heap):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_max_child(self, parent_idx):
        """Getting a larger child"""
        if 2 * parent_idx + 2 > self.size - 1:
            return 2 * parent_idx + 1
        else:
            if self.heap[2 * parent_idx + 1] > self.heap[2 * parent_idx + 2]:
                return 2 * parent_idx + 1
            else:
                return 2 * parent_idx + 2

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)


