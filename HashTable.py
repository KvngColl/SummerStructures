import random
import time
import matplotlib.pyplot as plots


class HashTable:
    def _init_(self):
        self.MAX = 509
        self.array = [[] for _ in range(self.MAX)]
        self.Tree_Array = [None] * 509

    def H_ash(self, key):
        hash = key
        return hash % self.MAX

    def Insert_Chain(self, key, val):
        h = self.H_ash(key)
        if not (self.array[h] == "[]"):
            self.array[h].append(val)
        else:
            self.array[h] = val

    def Insert_Tree(self, key, val):
        h = self.H_ash(key)
        # print(self.Tree_Array[h])
        if (self.Tree_Array[h] == None):
            self.Tree_Array[h] = Tree()
            self.Tree_Array[h].insertT(val)
        else:
            self.Tree_Array[h].insertT(val)

    def display_hash(self):
        size = self.MAX
        for i in range(size):
            print("[", i, "]", end=" ")
            print(self.array[i])

    def Display_Tree(self):
        size = self.MAX
        for i in range(size):
            print("[", i, "]", end=" ")
            if self.Tree_Array[i] != None:
                print("[ ", end="")
                self.Tree_Array[i].In_order()
            else:
                print("[]")


class Node:
    def _init_(self, val):
        self.value = val
        self.Left_Child = None
        self.Right_Child = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.Left_Child:
                return self.Left_Child.insert(data)
            else:
                self.Left_Child = Node(data)
                return True

        else:
            if self.Right_Child:
                return self.Right_Child.insert(data)
            else:
                self.Right_Child = Node(data)
                return True

    def In_order(self):
        if self:
            if self.Left_Child:
                self.Left_Child.In_order()
            print(str(self.value), end=" ")
            if self.Right_Child:
                self.Right_Child.In_order()


class Tree:
    def _init_(self):
        self.root = None

    def insertT(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def In_order(self):
        if self.root is not None:
            self.root.In_order()
            print(']\n', end="")


Table_A = HashTable()
Table_B = HashTable()
T_y1, T_y2, T_y3, T_y4, T_y5, T_y6, T_y7, T_y8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
C_y1, C_y2, C_y3, C_y4, C_y5, C_y6, C_y7, C_y8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

# hash with chain
print("Hash with chain")
count = 0
sum_time = 0
for current in range(8192):
    count = count + 1
    start_time = time.time()
    rand = int(random.uniform(16384, 65535))
    CSeed= rand
    CSeed= CSeed* CSeed
    CSeed= CSeed/ 100
    Mid_Square = int(CSeed% 10000)
    Table_B.Insert_Chain(Mid_Square, rand)

    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_milliSeconds = elapsed_time * 1000
    sum_time = sum_time + elapsed_time_milliSeconds

    if (current == 1023):
        C_y1 = round(sum_time / count, 6)
        print(C_y1)
        sum_time = 0
    if (current == 2047):
        C_y2 = round(sum_time / count, 6)
        print(C_y2)
        sum_time = 0
    if (current == 3071):
        C_y3 = round(sum_time / count, 6)
        print(C_y3)
        sum_time = 0
    if (current == 4095):
        C_y4 = round(sum_time / count, 6)
        print(C_y4)
        sum_time = 0
    if (current == 5119):
        C_y5 = round(sum_time / count, 6)
        print(C_y5)
        sum_time = 0
    if (current == 6143):
        C_y6 = round(sum_time / count, 6)
        print(C_y6)
        sum_time = 0
    if (current == 7167):
        C_y7 = round(sum_time / count, 6)
        print(C_y7)
        sum_time = 0
    if (current == 8191):
        C_y8 = round(sum_time / count, 6)
        print(C_y8)
        sum_time = 0

# Table_B.display_hash()


print("\n")
print(
    "<------------------------------------------------>")
print("\n")
print("Hash with Binary Tree")
count = 0
sum_time = 0
for current in range(8192):
    count = count + 1
    start_time = time.time()
    rand = int(random.uniform(16385, 65335))
    CSeed= rand
    CSeed= CSeed* midSqSeed
    CSeed= CSeed/ 100
    Mid_Square = int(CSeed% 10000)
    Table_A.Insert_Tree(Mid_Square, rand)
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_milliSeconds = elapsed_time * 1000
    sum_time = sum_time + elapsed_time_milliSeconds

    if (current == 1023):
        T_y1 = round(sum_time / count, 6)
        print(T_y1)
        sum_time = 0
    if (current == 2047):
        T_y2 = round(sum_time / count, 6)
        print(T_y2)
        sum_time = 0
    if (current == 3071):
        T_y3 = round(sum_time / count, 6)
        print(T_y3)
        sum_time = 0
    if (current == 4095):
        T_y4 = round(sum_time / count, 6)
        print(T_y4)
        sum_time = 0
    if (current == 5119):
        T_y5 = round(sum_time / count, 6)
        print(T_y5)
        sum_time = 0
    if (current == 6143):
        T_y6 = round(sum_time / count, 6)
        print(T_y6)
        sum_time = 0
    if (current == 7167):
        T_y7 = round(sum_time / count, 6)
        print(T_y7)
        sum_time = 0
    if (current == 8191):
        T_y8 = round(sum_time / count, 6)
        print(T_y8)
        sum_time = 0

# Table_A.Display_Tree()

x = ["1024", "2048", "3072", "4096", "5120", "6144", "7168", "8192"]
chain = [C_y1, C_y2, C_y3, C_y4, C_y5, C_y6, C_y7, C_y8]
print(chain)
tree = [T_y1, T_y2, T_y3, T_y4, T_y5, T_y6, T_y7, T_y8]
print(tree)
plots.plot(x, tree)
plots.plot(x, chain)
plots.xlabels("Intervals")
plots.title("Runtime Comparison:")
plots.show()
