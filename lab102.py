#The authors' names are Abby Newton and Elise Ward
class RightRect:
    def __init__(rectangle,height,length):
        rectangle.height=height
        rectangle.length=length

rr1 = RightRect(5,10)

print(rr1.height)
print(rr1.length)
