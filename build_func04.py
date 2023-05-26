n = int(input())
def main(n):
    """A integer type variable 'n' is given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func04 

    Args:
        n (int): integer
        
    Returns:
        float: the value of the expression
    """
    a = pow((2+n)/3,2)

    return a
print(main(n))