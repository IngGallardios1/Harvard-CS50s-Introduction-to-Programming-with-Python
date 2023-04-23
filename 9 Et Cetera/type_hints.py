# Run using mypy type_hints.py

def meow(n: int) -> str:
    """Meow n times."""
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")