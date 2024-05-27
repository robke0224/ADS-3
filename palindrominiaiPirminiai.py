def arPirminis(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def arPalindromas(n):
    return str(n) == str(n)[::-1]

def palindromaiPirminiai(a, b):
    for num in range(a, b + 1):
        if arPirminis(num) and arPalindromas(num):
            print(num)

a = int(input("Įveskite pradžios intervalo ribą a: "))
b = int(input("Įveskite pabaigos intervalo ribą b: "))

print(f"Palindrominiai pirminiai skaičiai intervale nuo {a} iki {b}:")
palindromaiPirminiai(a, b)
