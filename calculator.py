# smart calculator
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = input ("Choose operator +,-,*,/:")

# placeholder for the results
result = None 
explanation = " "

# logic
# Addition Operator
# Case 1 :positive numbers
if operator == "+":
    # Case 1: Both positive
    if num1 > 0 and num2 > 0:
        result = num1 + num2
        explanation = (
            f"Both numbers are positive. We add {num1} and {num2} to get {result}."
        )

    # Case 2: One positive, one negative
    elif (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0):
        result = num1 + num2
        if abs(num1) > abs(num2):
            dominant = num1
        else:
            dominant = num2
        explanation = f"""One number is negative, we subtract the absolute values.
Answer takes the sign of the number farthest from zero."""

    # Case 3: Both negative
    elif num1 < 0 and num2 < 0:
        result = num1 + num2
        explanation = f"""Both numbers are negative. We add the absolute values of each.
The result {result} takes a negative sign, since both values are negative."""

    else:
        explanation = "Invalid inputs."


# Subtraction Operator
# Positive number & Negative numbers
elif operator == "-":
    if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0) :
        result = num1-num2
        if abs(num1) > abs(num2):
            dominant = num1
        else:
            dominant = num2
        explanation = f"""Add the opposite of  {num2} to {num1},subtract their absolute values, result takes sign
        of the lager number {dominant}."""
    else:
        explanation = f"invalid inputs"
# Multiplication Operator

elif operator == "*":
    # Same sign
    if (num1 < 0 and num2 < 0) or (num1 > 0 and num2 > 0) :
        result = num1*num2
        explanation =f"""Both numbers have same sign, we find the product of their absolute values.Result takes 
     a positive sign because both values have the same sign."""
        # Different signs
    elif (num1 > 0 and num2 < 0 ) or (num1 < 0 and num2 > 0 ):
        result = num1*num2
        explanation =f"""Both numbers have different signs, we find the product of their absolute values . The result takes 
     a negative sign."""
    else:
        explanation = f"invalid inputs"

# Division Operator
elif operator == "/":
    # Same sign
    if (num1 < 0 and num2 < 0) or (num1 > 0 and num2 > 0) :
        result = num1/num2
        explanation =f"""Both numbers have same sign, we divide the absolute values . The result{result}, takes 
     a positive sign , because both values have the same sign."""
        # Different signs
    elif (num1 > 0 and num2 < 0 ) or (num1 < 0 and num2 > 0 ):
        result = num1/num2
        explanation =f"""Both numbers have different signs, we divide the absolute values . The result{result}, takes 
     a negative sign."""
    else:
        explanation = f"invalid inputs"

print(f"\n Explanation :{explanation}")
print(f"Result :{result}")
