import math

def f ( r ) :

    return 4 * math.log( 2 * math.e * r * math.log( r ) ) / math.log( r )

for r in range( 2 , 30 ) :

    for C in range( 1 , 1000 ) :

        if C - 4 * math.log( C ) > f( r ) :

            print( r , C )

            break
