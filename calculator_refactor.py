def handle_addition(num1,num2):
    # Case 1: Both positive
    if num1 > 0 and num2 > 0:
        result = num1 + num2
        explanation = (
            f"Both numbers are positive. We add {num1} and {num2} to get {result}."
        )
        return result,explanation

    # Case 2: One positive, one negative
    elif (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0):
        result = num1 + num2
        if abs(num1) > abs(num2):
            dominant = num1
        else:
            dominant = num2
        explanation = f"""One number is negative, we subtract the absolute values.Answer takes the sign of the number farthest from zero."""
        return result,explanation
    # Case 3: Both negative
    elif num1 < 0 and num2 < 0:
        result = num1 + num2
        explanation = f"""Both numbers are negative. We add the absolute values of each.The result {result} takes a negative sign, since both values are negative."""

    else:
        explanation = "Invalid inputs."
        return result,explanation
    

def handle_subtraction(num1,num2):
