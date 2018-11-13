#Write a function called digit_sum that takes a positive integer n as input
#  and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
#  (Assume that the number you are given will always be positive.)

try:
    #import re
    ###def digit_sum(x):
    ##  s=str(x)
    ##  #y=re.findall("\d",s)
    ##  j=0
    ##  for i in s:
    ##      j+=int(i)
    ##  return j
    ##print("sum of 21345 = ",digit_sum(21345))
 #Method-2
        sum=0
        def dig_sum(d):
            global sum
            if d//10 != 0:
                print("Sum for ",d,": ",sum)
                sum=sum + d%10
                dig_sum(d//10)               
            else:
                print("Sum for ",d,": ",sum)
                sum+=d%10     
        dig_sum(int(input("Enter number :")))
        print("sum : ",sum)
except Exception as e:
            print("Error:",e,"\n Please Enter proper int value")
