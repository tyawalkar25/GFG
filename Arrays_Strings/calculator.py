from loguru import logger

operand_1 = int(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, =): ")

result = operand_1

while operator != "=":
    operand_2 = int(input("Enter the next number: "))
    
    if operator == "+":
        result += operand_2
    elif operator == "-":
        result -= operand_2
    elif operator == "*":
        result *= operand_2
    elif operator == "/":
        if operand_2 != 0:
            result /= operand_2
        else:
            logger.error("Cannot divide by zero.")
            break
    else:
        logger.error("Invalid operator. Please enter one of +, -, *, /, =.")
        break
    
    operator = input("Enter the next operator (+, -, *, /, =): ")

if operator == "=":
    logger.info(f"The result is: {result}")