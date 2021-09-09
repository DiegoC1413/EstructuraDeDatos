

def boom (r):
    r -= 1
    if r > 0:
       print(r)
       boom(r)
    else:
        print( "BOOOOMMM" )
boom(10)
