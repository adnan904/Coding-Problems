# A program to check if t
def check_balanced(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)

        elif char.isalnum() or char in ["+", "-", "*", "/"] or char.isspace():
            continue

        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    expr = "{(123 + 34)/ 100} * [400])"

    # Function call
    if check_balanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")