print('*** Range ***')

for num in range(0,100, 13):
    print(num)

for num in range(0,1000,100):
    print(num)

nums = range(20)
list_of_nums = list(nums)
print(list_of_nums)

for _ in range(5):
    print('Hacer algo 5 veces')

def suma(a,b):
    """ Suma dos numero enteros """
    return a + b

print(suma(3,5))

