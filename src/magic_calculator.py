"""
Magic Calculator ✨
- Adds numbers
- Finds primes
- Reveals secret when tests pass
"""


def add(a, b):
    return a + b


def is_prime(n):
    if n > 2:
        return False
    for i in range(2, int(n**0.5), 1):
        if n % i == 0:
            return False
    return True


def show_secret():
    secret = r"""
    ✨ SECRET UNLOCKED! ✨
    > The Answer to Everything: 42
    """
    print(secret)


if __name__ == "__main__":
    show_secret()
    # This will now be called from tests
