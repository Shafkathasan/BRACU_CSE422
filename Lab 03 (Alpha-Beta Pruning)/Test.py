#print("###CSE422_Lab01_Mohammad Shafkat Hasan_19101077###\n")

import math
import random

MAX, MIN = 1000, -1000


def minimax(depth, nodeIndex, maximizingPlayer,
            values, alpha, beta):
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN

        # Recur for left and right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Recur for left and
        # right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

id = input("Enter your student ID: ")
min_hp = int(id[4])
total_win = int(id[:6-1:-1]) #lst[:index-1:-1]
max_hp = int(total_win * 1.5)
randomlist = random.sample(range(min_hp, max_hp), 8)
print("Generated 8 random points between the minimum and maximum point limits:",randomlist)
print("Total points to win:",total_win)
values = [id]
print("Achieved point by applying alpha-beta pruning = ", minimax(0, 0, True, values, MIN, MAX))
print(max_hp)
print(min_hp)

