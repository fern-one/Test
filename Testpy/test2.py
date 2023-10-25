n = int (input ("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i

fac_re = factorial
reversed_num = 0

while fac_re != 0:
    digit = fac_re % 10
    reversed_num = reversed_num * 10 + digit
    fac_re //= 10

re_vers = len(str(reversed_num))
fac = len(str(factorial))
count = fac - re_vers


print("Factorial is: ", factorial)
print(" 0 in fac is: ", count)

