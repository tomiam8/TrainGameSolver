def operation(num1, num2, operation):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1 / num2
    
def solve(a, b, c, d):
    symbols = ["+", "-", "*", "/"]
    for s1 in symbols:
        for s2 in symbols:
            for s3 in symbols:
                try:
                    num = operation(operation(operation(a, b, s1), c, s2), d, s3)
                    if num == 10:
                        print("((" + str(a) + s1 + str(b) + ")" + s2 + str(c) + ")" + s3 + str(d))
                except ZeroDivisionError:
                    pass
n1 = int(input("1 :"))
n2 = int(input("2 :"))
n3 = int(input("3 :"))
n4 = int(input("4 :"))

if True:#input("In order or out of order? (y/n)").lower() == "n": #originially you could choose if you wanted it go go in order or not. Now you can't, cause that was dumb. But I was lazy so this is horribly structured anyway.
    solutions  = [[n1, n2, n3, n4], [n1, n2, n4, n3], [n1, n3, n2, n4], [n1, n3, n4, n2], [n1, n4, n2, n3], [n1, n4, n3, n2], [n2, n1, n3, n4], [n2, n1, n4, n3], [n2, n3, n1, n4], [n2, n3, n4, n1], [n2, n4, n1, n3], [n2, n4, n3, n1], [n3, n1, n2, n4], [n3, n1, n4, n2], [n3, n2, n1, n4], [n3, n2, n4, n1], [n3, n4, n1, n2], [n3, n4, n2, n1], [n4, n1, n2, n3], [n4, n1, n3, n2], [n4, n2, n1, n3], [n4, n2, n3, n1], [n4, n3, n1, n2], [n4, n3, n2, n1]]
    for solution in solutions:
        solve(solution[0], solution[1], solution[2], solution[3])
#else:
#    solve(n1, n2, n3, n4)
