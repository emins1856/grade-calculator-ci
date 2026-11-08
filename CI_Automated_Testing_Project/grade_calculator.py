"""Simple student grade calculator for a CI testing demonstration."""


def calculate_average(grades):
    """Return the mean of scores between 0 and 100."""
    if not grades:
        raise ValueError("At least one grade is required")
    if any(not isinstance(grade, (int, float)) or isinstance(grade, bool)
           or not 0 <= grade <= 100 for grade in grades):
        raise ValueError("Grades must be numbers between 0 and 100")
    return sum(grades) / len(grades)


def has_passed(average):
    """A result of at least 50 is passing."""
    return average >= 50


def letter_grade(average):
    """Convert a 0-100 numeric grade into a letter grade."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    if average >= 50:
        return "E"
    return "F"


if __name__ == "__main__":
    scores = [85, 70, 95]
    average = calculate_average(scores)
    print(f"Grades: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {has_passed(average)}")
    print(f"Letter grade: {letter_grade(average)}")
