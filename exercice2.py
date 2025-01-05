import matplotlib.pyplot as plt
import math


#  1   :  5      ->
#  4   :  2      <-
#  2   : -2      <-
#  0   : -1      <-
# -4   : -3      <-
# -4.5 : -1.6    ->
# -2   :  2      ->
# -1   :  3.3    <-
# -5   :  1      <-
# -6.2 :  1.5    ->
# -5.5 :  2.4    ->
# -5   :  2      ->
# -2   :  4      ->



def Hermite( X: list[ float], FX: list[ float ], FPX: list[ float ], t: float ) -> float:
    result: float = 0

    H: list = [
        lambda x:  2*x**3 - 3*x**2     + 1,
        lambda x: -2*x**3 + 3*x**2        ,
        lambda x:    x**3 - 2*x**2 + x    ,
        lambda x:    x**3 -   x**2
    ]

    F: list = [ FX[0], FX[1], FPX[0], FPX[1] ]
    for i in range( 4 ):
        result += H[i]( ( t - X[0] ) / ( X[1] - X[0] ) ) * F[i]
    return result



# LIST: list[ list[ float ] ] = [
#     [  1  ,  5  , -8   ],
#     [  4  ,  2  , -1/6 ],
    
#     [  2  , -2  , 1/11 ], #
#     [  4  ,  2  ,  3   ], #
    
#     [  0  , -1  ,  4/5 ], #
#     [  2  , -2  , -5   ], #
    
#     [ -4  , -3  ,  2   ], #
#     [  0  , -1  , -2/3 ], #

#     [ -3  , -4  , -1   ],
#     [  2  , -2  ,  3   ],
    
#     [  2  ,  -2 ,  5   ],
#     [  3.3,  -1 , -1/3 ],
    
#     [ -6  ,  1  , -1   ], #
#     [ -1  ,  3.3, -1   ], #

#     [  1  , -6  , -1   ],
#     [  2  , -6  ,  1   ],
    
#     [ -6  ,  2  ,  1   ],
#     [ -5  ,  2  , -3/2 ],
    
#     [ -5  ,  2  ,  0   ],
#     [ -2  ,  4  ,  5   ],
    
#     [ -2  ,  4  ,  3   ],
#     [  1  ,  5  , -1/3 ]
# ] 

LIST: list[ list[ float ] ] = [
    [  1  ,  5  , -8   ],
    [  4  ,  2  , -1/6 ],

    [ -1  ,  3  ,  6/5 ], ###
    [  2  ,  4  ,  1/3 ], ###

    [  2  , -2  ,  1/11], #
    [  3  , -1  ,  2   ], #
    
    [  0  , -1  ,  4/5 ], #
    [  2  , -2  , -5   ], #
    
    [ -4  , -3  ,  6   ], #
    [  0  , -1  , -5/2 ], #

    [ -3  , -4  , -2   ], ## 
    [  2  , -2  ,  7   ], ##
    
    [  2  ,  -2 ,  3.5 ], ##
    [  3.3,  -1 , -0.1   ], ##
    
    [ -2  ,  3  ,  2/3 ], #
    [ -1  ,  3.3, -1/3 ], #

    [ -5  ,  1  ,  2   ], #
    [ -2  ,  3  ,  2   ], #

    [ -6  ,  1  , -1   ], #
    [ -5  ,  1  ,  1   ], #

    [  1  , -6  , -1/2 ], ##
    [  2  , -6  ,  1/2 ], ##
    
    [ -6  ,  2  ,  1/2 ],
    [ -5  ,  2  , -5/2 ],
    
    [ -5  ,  2  ,  0   ],
    [ -2  ,  4  ,  6   ],
    
    [ -2  ,  4  ,  6   ],
    [  1  ,  5  , -1   ]
]

inverseX: list[ bool ] = [
    False,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
    True,
    True,
    False,
    False,
    False,
    False
]

inverseY: list[ bool ] = [
    False,
    True,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    True,
    False,
    False,
    False
]

resultX: list[ float ] = []
resultY: list[ float ] = []

X: list[ float ] = [ values[0] for values in LIST ]
FX: list[ float ] = [ values[1] for values in LIST ]
FPX: list[ float ] = [ values[2] for values in LIST ]

for i in range( 0, len( LIST ), 2 ):
    subX: list[ float ] = [ X[i], X[i+1] ]
    subFX: list[ float ] = [ FX[i], FX[i+1] ]
    subFPX: list[ float ] = [ FPX[i], FPX[i+1] ]
    x: float = subX[0]

    tempResultX: list[ float ] = []
    tempResultY: list[ float ] = []
    while ( x < subX[1] ):
        tempResultX.append( x )
        tempResultY.append( Hermite( subX, subFX, subFPX, x ) )
        x += 0.1
    
    varRange: list[ int ] = range( len( tempResultX ) )

    if ( inverseX[ i//2 ] ):
        varRange = range( len( tempResultX )-1, -1, -1 )
    
    if ( inverseY[ i//2 ] ):
        tempResultX, tempResultY = tempResultY, tempResultX
    
    for j in varRange:
        resultX.append( tempResultX[j] )
        resultY.append( tempResultY[j] )

resultX.append( resultX[0] )
resultY.append( resultY[0] )



for i in range( len( resultX ) ):
    print( "[", end="" )
    print( round( resultX[i], 1 ), end=", " )
    print( round( resultY[i], 1 ), end="]\n" )



plt.rc( "grid", linestyle=(0, (3, 3)), color="grey" )
plt.plot( [ -7, 5 ], [ 0, 0 ], color="black" )
plt.plot( [ 0, 0 ], [ -4, 6 ], color="black" )
plt.plot( resultX, resultY, color="#00a2e8" )

plt.title("Exercice 2")
plt.xlabel("x")
plt.ylabel("y")

plt.xlim( -6.5, 4.5 )
plt.ylim( -3.5, 6   )
plt.xticks( range( -7, 5, 1 ) )
plt.yticks( range( -4, 6, 1 ) )

plt.grid( True )
plt.show()