from Point import getMax
from Point import getMin
from Point import boy
def test(a,b):
    print(getMin.min(a,b))
    print(getMax.max(a,b))
    name=['sam','jimmy']
    print(len(name))
    list=[x for x in range(10)]
    print("len:")
    print(len(list))
    num=[x for x in range(2,30)]
    print(num)
    num.pop()
    print(num)
    num.sort()
    print(num)
    d={7:'seven',8:'eight',9:'nine'}
    print(d[8])
    tub=(1,2,3)
    print(type(tub))
    perer = boy.boy()
    print(perer.gender)
    print(perer.say())
    print(perer.age())


#def main():
#    b=test(3,9)
#    print(b)
#   test(4,7)


print('hello!')
print(getMax.max(3,5))


if __name__ == '__main__':
 test(2,7)