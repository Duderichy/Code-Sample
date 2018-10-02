class LastK:
    def __init__(self, k):
        self._L = []
        self.k = k
        self.current = 0
        self._length = 0

    def __len__(self):
        return self._length

    def add(self, item):
        if len(self) == self.k:
            self._L[self.current] = item
            self.current = (self.current + 1) % self.k 
            # print(self.current)
            # print(self.k)
        if len(self) < self.k:
            self._length += 1
            self._L.append(item)


    def first(self):
        if len(self) == 0:
            raise IndexError
        else:
            return self._L[self.current % self._length]


    def last(self):
        if len(self) == 0:
            raise IndexError
        else:
            if self.current - 1 < 0:
                return self._L[self._length - 1]
            else:
                return self._L[self.current - 1 % self._length]

    def clear(self):
        self._L = []
        self.current = 0
        self._length = 0

    def getitem(self, i):
        # print("__getitem__")
        # print(self.current, "current")
        # print(self.k)
        # print(i)
        # print(self._L)
        if i >= self._length:
            raise IndexError
        else:
            newlist = self._L[:]
            newlist.sort()
            i = i % self.k
            # print(self._L[i])
            return self._L[i]

    def __getitem__(self, i):
        if i >= self._length:
            raise IndexError
        else:
            newlist = self._L[:]
            newlist.sort()
            i = i % self.k
            return newlist[i]



