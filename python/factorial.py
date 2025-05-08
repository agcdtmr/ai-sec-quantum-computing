def do_something(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * do_something(n - 1)

result: int = do_something(5)

print(f"The factorial of 5 is: {result}")