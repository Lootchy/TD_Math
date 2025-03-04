import matplotlib.pyplot as plt
from Tools import Tools
from CurveGenerator import CurveGenerator

if __name__ == "__main__":

    pointList = [
        [0, -1], [0.75, -0.75], [1.9, -2], [3.4, 0], [4, 2], [2, 2.75], [1, 5], [-0.5, 5], 
        [-2, 4], [-3, 2.75], [-5, 2], [-5.3, 2.3], [-6, 2], [-6.05, 1.8], [-6.1, 1.5], 
        [-6.05, 1.2], [-6, 1], [-5.5, 0.75], [-5, 1], [-3, 2.4], [-2, 3], [-1.5, 3.3], [-1, 3],
        [-1.1, 2.6], [-1.2, 2.3], [-1.5, 2.1], [-2, 2], [-3.3, 1], [-4, 0], [-4.3, -1], 
        [-4.4, -1.6], [-4.3, -2.2], [-4, -3], [-3, -1.7], [-2, -1], [-1, -0.6], [0, -1]
    ]
    
    pointListHermite = [
        [0, -1], [2, -2],  [4, 2],  [1, 5], [-1.5, 5], [-2, 4]
    ]
    tools_instance = Tools()
    tools_instance.trace(pointList)


    # Générateur de courbes
    # generator = CurveGenerator()
    # generator.trace_curve(pointListHermite, resolution=200)