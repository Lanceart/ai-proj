import heapq
import copy
import math
import sys
import threading
import time

n = 3
check_lists = []
play_misplaced = 0
play_Manhattan = 0
print_history = 0


class My_PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)

    def empty(self):
        return True if not self._queue else False


class maps:
    def __init__(self):
        self.costs = 0
        self.uniform = 0
        self.misplaced = 0
        self.manhattanD = 0
        self.number_map = [[0 for i in range(n)] for j in range(n)]
        self.x = 0
        self.y = 0

        self.maps_ancestor = []



def get_the_lists_map(temp,stage_map):
    if print_history == 1:
        temp.maps_ancestor.append(copy.deepcopy(stage_map))

def compare_state(map1, map2):
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[i][j]:
                return False

    return True


def swap(t1, t2):
    return t2, t1


def check_the_lists(map_for_check):
    for check in check_lists:
        if compare_state(check, map_for_check):
            return False
    return True


def check_displaced(map_for_check):
    misplaced = 0
    for i in range(n):
        for j in range(n):
            if map_for_check[i][j] == 0: continue
            if map_for_check[i][j] != map_goal.number_map[i][j]:
                misplaced += 1
    return misplaced

def check_the_manhattanD(map_for_check):
    manhattanD = 0
    for i in range(n):
        for j in range(n):
            manhattanD += abs(positions[map_for_check[i][j]][0] - i)
            manhattanD += abs(positions[map_for_check[i][j]][1] - j)
    return manhattanD

def count_the_cost(temp):
    temp.uniform += 1
    temp.misplaced = check_displaced(temp.number_map)
    temp.manhattanD = check_the_manhattanD(temp.number_map)
    return temp.uniform  + play_Manhattan * temp.manhattanD + play_misplaced * temp.misplaced

def my_printer(temp):
    print("#")
    print(temp.misplaced)
    print(temp.costs)
    print("#")

def cost_get_node(map_goal):
    # 探索下一个阶段
    total_pq = 0
    while not pq.empty():
        total_pq += 1
        map_begin = pq.pop()

        # my_printer(map_begin)

        # 判断是否结束
        if (compare_state(map_goal.number_map, map_begin.number_map) == True):
            print("The  expanded node total is :" + str(total_pq))
            print("The depth is :" + str(map_begin.uniform))
            print("==============")
            for i in range(n):
                for j in range(n):
                    print(str(map_puzzle.number_map[i][j]) + " ",end="")
                print(" ")
            print("==============")
            for i in map_begin.maps_ancestor:
                for p in range(n):
                    for q in range(n):
                        print(str(i[p][q])+" ",end="")
                    print(" ")
                print("==============")
            return 1

        # 生成与判断是否重复
        if map_begin.y - 1 >= 0:
            temp = copy.deepcopy(map_begin)
            temp.x = map_begin.x
            temp.y = map_begin.y - 1
            temp.costs = count_the_cost(temp)
            temp.number_map[temp.x][temp.y], temp.number_map[temp.x][temp.y + 1] = swap(temp.number_map[temp.x][temp.y],
                                                                                        temp.number_map[temp.x][
                                                                                            temp.y + 1])
            if check_the_lists(temp.number_map):
                get_the_lists_map(temp,temp.number_map)
                pq.push(temp, temp.costs)
                check_lists.append(temp.number_map)

        if map_begin.y + 1 < n:
            temp = copy.deepcopy(map_begin)
            temp.x = map_begin.x
            temp.y = map_begin.y + 1
            temp.costs = count_the_cost(temp)
            temp.number_map[temp.x][temp.y], temp.number_map[temp.x][temp.y - 1] = swap(temp.number_map[temp.x][temp.y],
                                                                                        temp.number_map[temp.x][
                                                                                            temp.y - 1])
            if check_the_lists(temp.number_map):
                get_the_lists_map(temp, temp.number_map)
                pq.push(temp, temp.costs)
                check_lists.append(temp.number_map)

        if map_begin.x - 1 >= 0:
            temp = copy.deepcopy(map_begin)
            temp.x = map_begin.x - 1
            temp.y = map_begin.y
            temp.costs = count_the_cost(temp)
            temp.number_map[temp.x][temp.y], temp.number_map[temp.x + 1][temp.y] = swap(temp.number_map[temp.x][temp.y],
                                                                                        temp.number_map[temp.x + 1][
                                                                                            temp.y])
            if check_the_lists(temp.number_map):
                get_the_lists_map(temp, temp.number_map)
                pq.push(temp, temp.costs)
                check_lists.append(temp.number_map)

        if map_begin.x + 1 < n:
            temp = copy.deepcopy(map_begin)
            temp.x = map_begin.x + 1
            temp.y = map_begin.y
            temp.costs = count_the_cost(temp)
            temp.number_map[temp.x][temp.y], temp.number_map[temp.x - 1][temp.y] = swap(temp.number_map[temp.x][temp.y],
                                                                                        temp.number_map[temp.x - 1][
                                                                                            temp.y])
            if check_the_lists(temp.number_map):
                get_the_lists_map(temp, temp.number_map)
                pq.push(temp, temp.costs)
                check_lists.append(temp.number_map)

    return 0


pq = My_PriorityQueue()
print("Please input the size of puzzle:")
n = int(input())

print("which method you want to use:\n input 0 is Uniform Search, 1 for Misplaced Based, and 2 for Manhattan Based")
choice = int(input())
if choice == 1:
    play_misplaced = 1
if choice == 2:
    play_Manhattan = 1

print("Do you want to print the traceback this time?\n Input 0 means no, and 1 means yes")
print_history = int(input())

map_puzzle = maps()
print("input the begin map")
for i in range(n):
    str_in = input()
    map_puzzle.number_map[i] = [int(n) for n in str_in.split()]
    for p in range(n):
        if map_puzzle.number_map[i][p] == 0:
            map_puzzle.x = i
            map_puzzle.y = p

map_goal = maps()
print("input the goal map")
for i in range(n):
    str_in = input()
    map_goal.number_map[i] = [int(n) for n in str_in.split()]
    for p in range(n):
        if map_goal.number_map[i][p] == 0:
            map_goal.x = i
            map_goal.y = p

positions = [[0 for i in range(2)] for j in range(n*n)]
for i in range(n):
    for j in range(n):
        positions[map_goal.number_map[i][j]][0] = i
        positions[map_goal.number_map[i][j]][1] = j

map_puzzle.manhattanD = check_the_manhattanD(map_puzzle.number_map)
map_puzzle.misplaced = check_displaced(map_puzzle.number_map)

pq.push(map_puzzle, map_puzzle.costs)

begin_time = time.time()
if cost_get_node(map_goal) == 1:
    print("Total spend "  +  str(format(time.time() - begin_time,'.2f')) + " seconds.")
    # print("The expanded node " + str(len(check_lists)))
else:
    print("the wrong puzzle!")
