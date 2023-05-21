def palindrome(a):
    for i in a:
        temp = i
        rev = 0
        while i > 0:
            dig = i % 10
            rev = rev * 10 + dig
            i = i // 10
        if temp == rev:
            print("True")
        else:
            print("False")


num = [round(float(x)) for x in input().split(", ")]

palindrome(num)
