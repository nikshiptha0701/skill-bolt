def details(name,age):
    print(f'Hello, {name}! You will be {age+5} years old in 5 years')
name = input('What is your name? ')
age = int(input('How old are you? '))
details(name,age)
l=[]
for i in range(5):
    num=int(input('Enter a number: '))
    l.append(num)
print(l[::-1])
print(sum(l))
print(sum(l)//len(l))
