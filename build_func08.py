x=int(input("x sonni kiriting: "))
y=int(input("y sonni kiriting: "))

def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func08

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    a = 5*pow(x,2)*pow(y,3)+x*pow(y,2)
    return a
print(main(x,y))