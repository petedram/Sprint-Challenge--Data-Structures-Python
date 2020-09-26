# FIFO will ensure oldest item is dequeued?
# enqueued items are at the back of the queue


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def __len__(self):
        return len(self.storage)

    def append(self, item):
        if len(self.storage) == self.capacity:
            del self.storage[self.count]
            self.storage.insert(self.count, item)
            if self.count == self.capacity -1:
                self.count = 0
            else:
                self.count +=1
        else:
            self.storage.append(item)

    def get(self):
        # need to check for None values
        get_list = [i for i in self.storage if i is not None]
        return get_list




buffer = RingBuffer(3)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']
