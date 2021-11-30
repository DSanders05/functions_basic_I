#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#prints the number 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#returns an error for the first function not being defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#returns the number 5 and ignores the second return statement because the first return ends the function


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#prints the number 5 and ignores the next print 10 statement because the return ends the function

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#prints the number 5 listed in the function instructions and prints a none for x because x doesn't have a return from the function to store a value into it.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#prints values 3 and 5 separately

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#prints the string value 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#prints 100, then returns 10 and ignores the second return statement. then prints 10 from the statement on line 57

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prints 7 from line 67, prints 14 from line 68, prints 21 from line 69. ignores return on line 66


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#prints the number 8. ignores return on line 76.

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#prints 500, then prints 500, then prints 300, then prints 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#prints 500, then 500, then 300, then 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#prints 500, then 500, then 300,then 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#prints 1, then 3, then 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#prints 1, then 3, then 5, then 10.