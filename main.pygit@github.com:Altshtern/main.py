def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def extract_primes(numbers):
    return [n for n in numbers if is_prime(n)]

def main():
    sample_numbers = [10, 15, 23, 42, 57, 89, 97, 100]
    primes = extract_primes(sample_numbers)
    print("Prime numbers in the list:", primes)

if __name__ == "__main__":
    main()
