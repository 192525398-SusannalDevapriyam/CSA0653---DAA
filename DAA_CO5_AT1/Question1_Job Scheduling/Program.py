# 192525398 -S.Susannal Devariyam

# JOB SCHEDULING USING BACKTRACKING

# Problem:

# A company must assign jobs to employees.

# Constraints:

# Every job must be assigned to exactly one employee.
# An employee can handle only one job at a time.
# A job can be assigned only if the employee is qualified.
# All jobs should be completed before their deadlines.

# Approach:

# - Use Backtracking (Constraint Satisfaction Technique).
# - Recursively assign jobs to employees.
# - If a constraint is violated, backtrack immediately.

    # This approach guarantees a feasible solution if one exists.

# List of employees
employees = ["E1", "E2", "E3"]

# List of jobs
jobs = ["J1", "J2", "J3"]

# Employee qualifications
# True means employee can perform the job

qualification = {
    "E1": ["J1", "J2"],
    "E2": ["J2", "J3"],
    "E3": ["J1", "J3"]
}

# Stores final assignments

assignment = {}

# Track employees already assigned

used_employees = set()


def assign_job(job_index):
    """
    Recursive function that assigns jobs one by one.
    Backtracks whenever a constraint is violated.
    """

    # Base Case:
    # All jobs assigned successfully

    if job_index == len(jobs):
        return True

    current_job = jobs[job_index]

    # Try assigning current job to each employee

    for employee in employees:

        # Constraint Check:
        # Employee must be qualified
        # Employee should not already have another job

        if (current_job in qualification[employee]
                and employee not in used_employees):

            # Assign job

            assignment[current_job] = employee
            used_employees.add(employee)

            # Recursive call

            if assign_job(job_index + 1):
                return True

            # Backtrack if assignment fails

            del assignment[current_job]
            used_employees.remove(employee)

    return False


# Start scheduling process

if assign_job(0):
    print("Job Assignment:")
    for job, employee in assignment.items():
        print(job, "->", employee)
else:
    print("No feasible assignment found.")

# -----------------------------------------------------------

# Time Complexity:
# O(n!)
# where n = number of jobs
#
# Space Complexity:
# O(n)

input("\n\n\npress enter to exit...")