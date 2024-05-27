print(" do ta adad benevis to barat taghsim konam")
while True :
    
        aval=input("adade aval ro benevis :")
        if aval == 'tamam' :
          break
        dovom =input("adade dovom ro benevis :")
        if dovom == 'tamam' :
         break
        try :
            javab = int(aval) / int(dovom)
        except ZeroDivisionError :
            print(f" you cant divide{aval} by {dovom}")
        else :
            print(javab)