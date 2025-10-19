def my_steps(n):
    if n > 25:
        raise ValueError("Input exceeds 25")
    if n <= 0:
        raise ValueError("Inputis less than 1")
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return my_steps(n-1) + my_steps(n-2)
