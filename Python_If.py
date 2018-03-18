def leapyr(y):
    if y%4==0:
        print("year %d is divisible by 4 but not by 100" %y)
    elif y%100==0:
        print("year %d is divisible by 100 but not by 4" %y)
    elif y%400==0:
        print("year %d is divisible by 400 but not by 100 or a" %y)
    else:
        print("year %d is not a leap year" %y)

def score ():
    scr=int(input("Enter Score Grade:"))
    if scr <0 or scr > 100:
         print('Score is out of bound')
    elif scr >=70:
        print ('you have scored a 1st')
    elif scr >=60:
         print('you have scored a 2.1')
    elif scr >=50:
         print('you have scored a 2.2')
    elif scr >=40:
         print ('you have scored a 3rd')
    else:
         print('you have failed')
