# EXAM TIMETABLING USING GRAPH COLORING

# Problem:

# A university must schedule exams so that:

# Constraints:

#  No student should have overlapping exams.
#  Conflicting exams must be placed in different slots.
#  Available time slots are limited.
#  Rooms must be utilized efficiently.

# Graph Coloring Concept:

#   Each exam is represented as a vertex.
#   An edge between two exams means
#   some students are enrolled in both exams.
#   Adjacent vertices cannot have the same color.
#   Colors represent exam time slots.


# Number of exams

num_exams = 4

# Conflict Graph

# 1 indicates conflict between exams

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# Number of available time slots

slots = 3

# Store assigned slot for each exam

colors = [0] * num_exams


def is_safe(exam, slot):
    """
    Check whether assigning a slot
    creates a conflict with adjacent exams.
    """

    for neighbor in range(num_exams):
        if graph[exam][neighbor] == 1 and colors[neighbor] == slot:
            return False

    return True


def solve(exam):

    """
    Assign slots recursively using Backtracking.
    """

    # Base Case:
    # All exams scheduled

    if exam == num_exams:
        return True

    # Try all possible slots

    for slot in range(1, slots + 1):

        if is_safe(exam, slot):

            # Assign slot
            colors[exam] = slot

            # Recursive call

            if solve(exam + 1):
                return True

            # Backtrack

            colors[exam] = 0

    return False


# Generate timetable

if solve(0):
    print("Exam Timetable:")
    for i in range(num_exams):
        print("\nExam", i + 1, "-> Time Slot", colors[i])
else:
    print("No feasible timetable found.")

# Time Complexity:
# O(m^n)

# where:
# n = number of exams
# m = number of available slots

# Space Complexity:
# O(n)

input("\n\n\npress enter to exit...")