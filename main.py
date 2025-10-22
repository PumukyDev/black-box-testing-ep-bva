from decimal import Decimal

def isPassed(grade: Decimal) -> bool:
    if not isinstance(grade, (int, float, Decimal)):
        raise ValueError("The grade must be a number")

    grade = Decimal(grade)
    if grade < 0 or grade > 10:
        raise ValueError("The grade must be between 0 and 10")

    return grade >= 5
