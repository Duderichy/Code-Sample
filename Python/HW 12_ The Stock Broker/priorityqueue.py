
class PriorityQueue:
    def __init__(self, entries=None, key=lambda x: x):
        self._entries = list(entries or [])
        self.key = key
        self._heapify()

    def insert(self, item):
        self._entries.append(item)
        self._upheap(len(self) - 1)

    def _parent(self, i):
        return (i - 1) // 2

    def _children(self, i):
        left, right = 2 * i + 1, 2 * i + 2
        return range(left, min(len(self), right + 1))
    
    def findtop(self):
        try:
            return self._entries[0]
        except:
            return None

    def removetop(self):
        L = self._entries
        if len(L) == 0:
            return None
        self._swap(0, len(L) - 1)
        item = L.pop()
        self._downheap(0)
        return item

    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    # implement this method 
    def _upheap(self, i):
        # check to see if everything above it has higher priority
        # time complexity?
        # O(log n)
        print(i, len(self._entries))
        parent = self._parent(i)
        if parent >= 0 and parent < len(self) and i >= 0 and i < len(self):
            if self.priority(i) < self.priority(parent):
                self._swap(i, self._parent(i))
                self._upheap(self._parent(i))
    
    # implement this method
    def _downheap(self, i):
        # O(log n)
        # smallest child gets promoted
        # print(self._entries)
        # print("i", i)
        children = self._children(i)
        usethis = None
        for child in children:
            if child >= 0 and child < len(self) and i >=0 and i < len(self):
                if self.priority(i) > self.priority(child):
                    # self._swap(i, child)
                    # self._downheap(child)
                    # break
                    if usethis != None:
                        if self.priority(child) < self.priority(usethis):
                            usethis = child
                    else:
                        usethis = child
                    # print("current i", i, "usethis", usethis)
        if usethis != None:
            self._swap(i, usethis)
            self._downheap(usethis)
        # else:
            # print("done")
            # print(self._entries)

    def __len__(self):
        return len(self._entries)

    def _heapify(self):
        for i in range(len(self)):
            self._downheap(len(self) - i - 1)
    
    # implement this method
    def update(self, other):
        # O(n) time complexity
        for item in other._entries:
            self.insert(item)
    
    # implement this method
    def _isheap(self):
        # everything must be in right place
        # that is everything must be larger
        # runs in O(n)
        # must check parents are smaller, children are larger
        # can't impliment this until downheap is implimented
        entries = self._entries 
        key = self.key
        for i, item in enumerate(self._entries):
            parent = self._parent(i)
            children = self._children(i)
            if self.inrange(i) and self.inrange(parent):
                if key(entries[parent]) > key(entries[i]):
                    # print(entries[parent], entries[item])
                    return False
            for child in children:
                if self.inrange(i) and self.inrange(child):
                    # print(entries[child], entries[item])
                    if key(entries[child]) < key(entries[i]):
                        return False
        return True

    def priority(self, i):
        return self.key(self._entries[i])

    def inrange(self, i):
        if i >= 0 and i < len(self):
            return True
        else:
            return False

if __name__=="__main__":
    p = PriorityQueue([i for i in range(20)])
    for i in range(10):
        for child in p._children(i):
            print("i", i, "children", child)
        # else:
        #     print("no more", i)
        #     print(p._children(i))
        print("i", i, "parent", p._parent(i))
        print(p._isheap())
