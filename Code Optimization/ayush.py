from sqlalchemy import false, true

def strength_reduction():
    user_input = input("Enter th expression: ")
    l1 = list(user_input.split(" "))
    c = 0
    l2 = []
    for i in range(len(l1)):
        if l1[i] == "=":
            l2.append(l1[i])
            for j in range(i+1, len(l1)):
                if l1[j] == "*":
                    for k in range(1,int(l1[j+1])):
                        l2.append("+")
                        l2.append(l1[j-1])
                    break
                elif l1[j] == "^":
                    for r in range(1,int(l1[j+1])):
                        l2.append("*")
                        l2.append(l1[j-1])
                    break
                else:
                    l2.append(l1[j])
            break
        else:
            l2.append(l1[i])
    print(" ".join(l2))

def compile_time_evaluation():
    print("Select one")
    print("1. Constant Folding")
    print("2. Constant Propagation")

    ch = int(input("Enter a choice: "))
    if ch == 1:
        user_input = input("Enter an Expression: ")
        l1 = list(user_input.split(" "))
        
        l2 = []
        i = 0
        while i<len(l1):
            if l1[i].isdigit():
                if l1[i+1] == "+":
                    ans = str(int(l1[i]) + int(l1[i+2]))
                elif l1[i+1] == "*":
                    ans = str(int(l1[i]) * int(l1[i+2]))
                elif l1[i+1] == "-":
                    ans = str(int(l1[i]) - int(l1[i+2]))
                elif l1[i+1] == "/":
                    ans = str(float(int(l1[i]) / int(l1[i+2])))
                l2.append(ans)
                i = i+3
            else:
                l2.append(l1[i])
                i = i+1
        print(" ".join(l2))
    else:
        no_con = int(input("Enter number of constants in expression: "))
        d = {}
        for i in range(0,no_con):
            user_const = input("Enter the constant value: ")
            l1 = list(user_const.split(" "))
            d[l1[0]] = l1[2]
        user_input = input("Enter the Expression: ")
        l = list(user_input.split(" "))
        l2 = []
        for k in range(len(l)):
            if l[k] in d:
                l2.append(d[l[k]])
            else:
                l2.append(l[k])
        print(" ".join(l2))

def common_sub_exp_elimination():
    l1 = []
    l2 = []
    t = int(input("Enter Number of expression:"))
    for i in range(t):
        exp = input("Enter Expression:")
        t1, t2 = exp.split("=")
        l1.append(t1)
        l2.append(t2)
    temp = []
    for i in range(len(l2)):
        if l2[i] not in temp:
            temp.append(l2[i])
        else:
            print("Expression {} = {} is redundant.".format(l1[i], l2[i]))
            l1.remove(l1[i])
    # print(l1, temp)
    print("Expression after optimization-")
    for i, j in zip(l1, temp):
        print("{} = {}".format(i, j))

def code_movement():
    inp = input("Write code: \n")
    inp = inp.split(" ")
    for i in range(len(inp)):
        if inp[i] == 'for':
            temp = inp[i + 2]
        if ('=' in inp[i]) and (temp not in inp[i]):
            print("Exp. {} is redundant.".format(inp[i][0:-1]))
        else:
            continue
#     print(""" Before Optimization
#         for ( int j = 0 ; j < n ; j ++)
#         {

#             x = y + z ;

#             a[j] = 6 x j;

#             }
#             """)

#     print("""After Optimization
#         x = y + z ;
#         for ( int j = 0 ; j < n ; j ++)
#         {
#             a[j] = 6 x j;
#         }
# """)

def dead_code_elimination():
    print(""" Before Optimization
        i = 0
        if (i == 1) :
            a = i + 5
            print(a)
        """)

    print("""After Optimization
        i = 0 """)

user = true
while user==true:
    print("select a method: ")
    print("1. Compile Time Evaluation")
    print("2. Common Sub-Expression Elimination")
    print("3. Code Movement")
    print("4. Dead Code Elimination")
    print("5. Strength Reduction")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        compile_time_evaluation()
    elif choice == 2:
        common_sub_exp_elimination()
    elif choice == 3:
        code_movement()
    elif choice == 4:
        dead_code_elimination()
    elif choice == 5:
        strength_reduction()
    else:
        print("Please select a valid choice.")
    
    con = input("Do you want to continue Y/N?: ")
    if con == ("Y" or "y"):
        user = true
    else:
        user = false

'''
Enter a choice: 1
Enter an Expression: a=( 22 / 7 ) + rem
a=( 3.142857142857143 ) + rem

Enter a choice: 2
Enter number of constants in expression: 2
Enter the constant value: pi = 3
Enter the constant value: v = 4
Enter the Expression: r = pi + v + v
r = 3 + 4 + 4

Enter your choice: 2
Enter Number of expression:3
Enter Expression:a = 21 + 20
Enter Expression:c = 21 + 22
Enter Expression:f = 21 + 22
Expression f  =  21 + 22 is redundant.
Expression after optimization-





Enter your choice: 5
Enter th expression:  a = a * 5
 a = a + a + a + a + a

'''