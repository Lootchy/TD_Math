import matplotlib.pyplot as plt

def ellipse(xC, yC, a, b, points=100):
    """
    Trace une ellipse de centre (xC, yC), demi-grand axe a et demi-petit axe b.
    Le paramètre `points` détermine la résolution de l'ellipse.
    """
    # Initialisation des listes pour stocker les points
    x_vals = []
    y_vals = []
    
    # Paramètre t varie de 0 à 2*pi
    t = 0
    delta_t = (2 * 3.141592653589793) / points  # Pas d'incrément pour t
    
    # Variables pour les approximations de cos(t) et sin(t)
    cos_t = 1  # cos(0)
    sin_t = 0  # sin(0)
    fact = 1   # Factorielle pour les termes du développement de Taylor
    t_power = 0  # Puissance de t
    
    # Calcul des points de l'ellipse
    for i in range(points + 1):  # Inclure le point final
        # Ajout des coordonnées calculées
        x_vals.append(xC + a * cos_t)
        y_vals.append(yC + b * sin_t)
        
        # Calcul approximé des nouvelles valeurs de cos(t + delta_t) et sin(t + delta_t)
        t += delta_t
        t_power = t  # Recalculer la puissance
        fact = 1  # Réinitialisation pour la factorielle
        cos_t = 1  # Réinitialisation de cos(t)
        sin_t = t  # Premier terme pour sin(t)
        sign = -1  # Alterne entre + et -
        
        # Approximations avec les 10 premiers termes du développement de Taylor
        for n in range(1, 10):
            fact *= (2 * n) * (2 * n - 1)  # Factorielle pour le terme actuel
            t_power *= t ** 2  # Mise à jour de la puissance de t
            cos_t += sign * t_power / fact  # Ajouter le terme de Taylor pour cos(t)
            sign *= -1  # Alterner les signes

        t_power = t  # Réinitialisation pour sin
        fact = 1
        sin_t = t
        sign = -1
        
        for n in range(1, 10):
            fact *= (2 * n + 1) * (2 * n)  # Factorielle pour sin(t)
            t_power *= t ** 2  # Mise à jour de la puissance de t
            sin_t += sign * t_power / fact
            sign *= -1
    
    # Tracé de l'ellipse
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, label=f"Ellipse: a={a}, b={b}")
    plt.scatter([xC], [yC], color="red", label="Centre (xC, yC)")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title("Tracé d'une ellipse")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

# Exemple d'utilisation
ellipse(0, 0, 50, 50)
