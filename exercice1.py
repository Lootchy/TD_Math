import matplotlib.pyplot as plt
import math



def factorial( x: float ) -> float:
    result: float = 1
    for i in range( 1, x+1 ):
        result *= i
    return result



def cos( x: float, precision: float = 10 ) -> float:
    result: float = 0
    negative: int = 1
    for i in range( 0, 2*precision+1, 2 ):
        result += x**i * negative / factorial(i)
        negative *= -1
    return result



def sin( x: float, precision: float = 10 ) -> float:
    result: float = 0
    negative: int = 1
    for i in range( 1, 2*precision+1, 2 ):
        result += x**i * negative / factorial(i)
        negative *= -1
    return result



def ellipse( xC: float, yC: float, a: float, b: float ) -> None:
    X: list[ float ] = []
    Y: list[ float ] = []
    h: float = 0.1
    t: float = 0
    
    while ( t < 2 * math.pi ):
        x = xC + a * cos(t)
        y = yC + b * sin(t)

        X.append(x)
        Y.append(y)
        t += h

    X.append( X[0] )
    Y.append( Y[0] )
    
    plt.figure( figsize=( 6, 6 ) )
    plt.axis( "equal" )
    
    plt.plot( X, Y, label=f"Ellipse (centre=({xC}, {yC}), a={a}, b={b})" )
    
    plt.title( "Tracé d'une ellipse" )
    plt.xlabel( "x" )
    plt.ylabel( "y" )
    plt.legend()
    
    plt.grid()
    plt.show()



ellipse( 0, 0, 5, 3 )