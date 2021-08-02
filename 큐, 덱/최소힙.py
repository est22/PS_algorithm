class PriorityQueue_MinHeap:

    def __init__(self):
        self.data = [0]

    def push(self, value):
        self.data.append(value)

        index = len(self.data)-1

        while index != 1 :
            if self.data[index//2] > self.data[index]:
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp
                index = index//2
            else:
                break

    def pop(self):
        if len(self.data) == 1:
            return
        
        self.data[1] = self.data[-1]
        self.data.pop()

        index = 1

        while True:
            priority =  -1
            if len(self.data) - 1 < index * 2:
                break
            elif len(self.data)-1 < index * 2 + 1:
                priority = index *  2
            
            else:
                if self.data[index*2] < self.data[index*2 + 1]:
                    priority = index *  2
                else:
                    priority = index *  2 + 1
            
            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                index = priority

            else:
                break


    def top(self):
        if len(self.data) == 1:
            return -1
        else:
            return self.data[1]