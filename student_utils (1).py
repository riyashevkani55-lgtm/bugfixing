PASS_MARK = 40

def calculate_average(marks):
    total = 0
    for m in marks:
        total = total + m
    # Fix 1: Divide by actual count len(marks), not len(marks) - 1
    return total / len(marks)

def is_passing(mark):
    # Fix 2: Use >= so that 40 is treated as passing
    if mark >= PASS_MARK:
        return True
    return False

def get_grade(average):
    # Fix 3: Evaluate >= 90 first so Distinction is not eclipsed by >= 60
    if average >= 90:
        return "Distinction"
    elif average >= 60:
        return "First"
    elif average >= 45:
        return "Second"
    return "Fail"
