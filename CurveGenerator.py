import numpy as np
import matplotlib.pyplot as plt

class CurveGenerator:
    def __init__(self):
        pass

    def hermite_interpolation(self, x, x_points, y_points, dy_points):
        """
        Fonction pour calculer l'interpolation d'Hermite.
        """
        n = len(x_points)
        result = 0
        
        for i in range(n):
            h_i = 1  # Base polynomiale pour les points (valeurs)
            h_prime_i = 0  # Base polynomiale pour les dérivées
            
            for j in range(n):
                if j != i:
                    if x_points[i] != x_points[j]:  # Éviter division par zéro
                        h_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
                        h_prime_i += 1 / (x_points[i] - x_points[j])
                    else:
                        h_i = 0  # Si \( x_i = x_j \), cette base est nulle

            h_i_squared = h_i ** 2
            term1 = h_i_squared * (1 - 2 * (x - x_points[i]) * h_prime_i) * y_points[i]
            term2 = h_i_squared * (x - x_points[i]) * dy_points[i]
            
            result += term1 + term2
        
        return result

    def calculate_derivatives(self, x_points, y_points):
        """
        Calcule les dérivées approximatives en chaque point donné, avec gestion des x répétés.
        """
        n = len(x_points)
        derivatives = []

        for i in range(n):
            if i == 0:
                
                if x_points[i + 1] == x_points[i]:
                    slope = 0 
                else:
                    slope = (y_points[i + 1] - y_points[i]) / (x_points[i + 1] - x_points[i])
            elif i == n - 1:
                
                if x_points[i] == x_points[i - 1]:
                    slope = 0  
                else:
                    slope = (y_points[i] - y_points[i - 1]) / (x_points[i] - x_points[i - 1])
            else:
                
                if x_points[i + 1] == x_points[i - 1]:
                    slope = 0
                else:
                    slope = (y_points[i + 1] - y_points[i - 1]) / (x_points[i + 1] - x_points[i - 1])
            derivatives.append(slope)

        return derivatives

    def generate_segment(self, p1, p2, dy1, dy2, resolution=100):
        """
        Génère une courbe entre deux points p1 et p2.
        """
        x1, y1 = p1
        x2, y2 = p2
        
        x_range = np.linspace(x1, x2, resolution)
        y_range = [self.hermite_interpolation(x, [x1, x2], [y1, y2], [dy1, dy2]) for x in x_range]
        
        return x_range, y_range

    def trace_curve(self, pointList, resolution=100):
        """
        Trace la courbe segmentée point par point.
        """
        x_points = [point[0] for point in pointList]
        y_points = [point[1] for point in pointList]

        dy_points = self.calculate_derivatives(x_points, y_points)
        
        plt.figure(figsize=(12, 6))
        
        for i in range(len(pointList) - 1):
            p1, p2 = pointList[i], pointList[i + 1]
            dy1, dy2 = dy_points[i], dy_points[i + 1]
            seg_x, seg_y = self.generate_segment(p1, p2, dy1, dy2, resolution)
            plt.plot(seg_x, seg_y, color="blue")
        
        plt.scatter(*zip(*pointList), color="red", label="Points de contrôle", zorder=5)
        
        plt.title("Interpolation d'Hermite segmentée (2 points par 2 points)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.xlim(min(x_points)-1, max(x_points)+1)
        plt.ylim(min(y_points)-1, max(y_points)+1)
        plt.show()