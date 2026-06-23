import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


scores = [450, 620, 300, 800, 700, 500]

sorted_scores = quick_sort(scores)

print("Leaderboard Scores:")

for score in sorted_scores[::-1]:
    print(score)

input("\n\n\npress enter to exit...")