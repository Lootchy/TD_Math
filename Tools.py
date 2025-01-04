import numpy as np
import matplotlib.pyplot as plt

class Tools:
    def __init__(self):
        pass
    
    def lagrange_interpolation(self, x, x_points, y_points):
        """Fonction pour calculer l'interpolation de Lagrange à un point donné x."""
        result = 0
        n = len(x_points)
        
        for i in range(n):
            term = y_points[i]
            for j in range(n):
                if j != i:
                    term *= (x - x_points[j]) / (x_points[i] - x_points[j])
            result += term
        return result
    
    def trace(self, pointList):
        # Séparer les coordonnées x et y
        x_points = np.array([point[0] for point in pointList])
        y_points = np.array([point[1] for point in pointList])

        plt.figure(figsize=(12, 10))
        
        # Tracer l'interpolation pour chaque groupe successif de 3 points
        for i in range(0, len(x_points) - 2, 2): 
            x_subset = x_points[i:i+3]
            y_subset = y_points[i:i+3]
            
            # Restreindre les valeurs de x à l'intervalle du 1er au dernier point
            x_vals = np.linspace(min(x_subset), max(x_subset), 100)
            
            # Calculer les valeurs y pour les valeurs de x dans x_vals
            y_vals_subset = [self.lagrange_interpolation(x, x_subset, y_subset) for x in x_vals]
            
            # Tracer chaque courbe pour le groupe de 3 points
            plt.plot(x_vals, y_vals_subset, label=f'Interpolation {i//2 + 1}', color='blue')
            
            # Marquer les points d'origine en rouge
            plt.scatter(x_subset, y_subset, color='red', zorder=5)

        # Ajouter les titres et labels
        plt.title("Interpolation de Lagrange pour les points donnés")
        plt.xlabel("x")
        plt.ylabel("y")
        
        # Ajouter une légende
        plt.legend()
        plt.grid(True)
        
        # Définir les limites des axes
        plt.xlim(min(x_points)-1, max(x_points)+1)
        plt.ylim(min(y_points)-1, max(y_points)+1)

        # Afficher le graphique
        plt.show()
