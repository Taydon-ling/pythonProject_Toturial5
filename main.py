from selectors import SelectSelector

print("# # # Term 1 # # #")

def result1(a1,m1,p1,cp1):
    if 0 <= a1 <= 100 and 0 <= m1 <= 100 and 0 <= p1 <= 100 and 0 <= cp1 <= 100: # check if every score is within the range of 0 to 100
        if a1 >= 40 and m1 >= 40 and p1 >= 40 and cp1 >= 40: # check if every score is 40 and above
            print("Thank you, Term 1 is inputted.")
        else:
            print("Sorry, you must at least get 40% in all subjects.")
            quit()
    else:
        print("This is not a valid input. Goodbye.")
        quit() # if they typed an invalid number, it will instantly end.

a1 = int(input("AES: "))
m1 = int(input("Maths 1: "))
p1 = int(input("Physics 1: "))
cp1 = int(input("Computer Programming 1: ")) # It will ask the student to type in their results.

print(result1(a1,m1,p1,cp1))

print("# # # Term 2 # # #")

def result2(a2,m2,p2,cp2):
    if 0 <= a2 <= 100 and 0 <= m2 <= 100 and 0 <= p2 <= 100 and 0 <= cp2 <= 100:
        if a2 >= 40 and m2 >= 40 and p2 >= 40 and cp2 >= 40:
            print("Thank you, Term 1 is inputted.")
        else:
            print("Sorry, you must at least get 40% in all subjects.")
            quit()
    else:
        print("This is not a valid input. Goodbye.")
        quit()

a2 = int(input("AES: "))
m2 = int(input("Maths 2: "))
p2 = int(input("Physics 2: "))
cp2 = int(input("Computer Programming 2: "))
print(result2(a2,m2,p2,cp2))

def result3(a3,m3,p3,cp3):
    if 0 <= a3 <= 100 and 0 <= m3 <= 100 and 0 <= p3 <= 100 and 0 <= cp3 <= 100:
        if a3 >= 40 and m3 >= 40 and p3 >= 40 and cp3 >= 40:
            print("Thank you, Term 1 is inputted.")
        else:
            print("Sorry, you must at least get 40% in all subjects.")
            quit()
    else:
        print("This is not a valid input. Goodbye.")
        quit()

print("# # # Term 3 # # #")
a3 = int(input("AES: "))
m3 = int(input("Maths 3: "))
p3 = int(input("Physics 3: "))
cp3 = int(input("Computer Programming 3: "))

print(result3(a3,m3,p3,cp3))

def overall(a1,a2,a3,m1,m2,m3,p1,p2,p3,cp1,cp2,cp3):
    if (a1+a2+a3+m1+m2+m3+p1+p2+p3+cp1+cp2+cp3)/12 >= 60: # It calculates the overall average and check if it is 60 and above.
        if (m2+m3)/2 > 65: # It only calculates the average of math 1 and 2, then check if is 65 and above.
            if a3 > 60: # it checks if the term 3's AES result is 60 and above.
                if (a1+a2+a3+m1+m2+m3+p1+p2+p3+cp1+cp2+cp3)/12 == 100: # it checks if the overall average is 100.
                    print("Amazing! You progress!!! WOW you cooked! 100 in everything!!!")
                else:
                    print("Well done! You progress!!!")
            else:
                print("Sorry, you do not progress. You must at least get 60% in AES term 3")
        else:
            print("Sorry, you do not progress. You must at least get 65% in Maths 2 and Maths 3.")
    else:
        print("Sorry, you do not progress. You must at least get 60% overall.")

print(overall(a1,a2,a3,m1,m2,m3,p1,p2,p3,cp1,cp2,cp3))

quit()