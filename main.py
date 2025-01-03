import matplotlib.pyplot as plt
from Tools import Tools

if __name__ == "__main__":

    pointList = [
    [0, -1], [0.75, -0.75], [2, -2], [3.5, 0],[4, 2], [2, 2.75], [1, 5],[-0.5, 5], [-2, 4], [-3, 2.75], [-5, 2],
    [-5.5, 2.3], [-6.1, 1.5], [-6, 1], [-5.5, 0.75]
]
    tools_instance = Tools()
    tools_instance.trace(pointList)