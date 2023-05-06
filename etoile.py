import heapq
import numpy as np


class TaquinState:
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def __init__(self, state, parent=None, g=0):
        # Initialisation d'un état avec une configuration de jetons donnée
        self.state = state
        # Le parent de l'état (état précédent dans le chemin)
        self.parent = parent
        # Le coût pour atteindre cet état
        self.g = g
        # L'heuristique pour atteindre l'état final depuis cet état
        self.h = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Calcul de l'heuristique : nombre de jetons mal placés
        return np.sum(self.state != self.goal_state)

    def get_neighbors(self):
        # Renvoie les états voisins valides en effectuant les mouvements possibles
        neighbors = []
        zero_pos = np.argwhere(self.state == 0)[0]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Droite, Gauche, Bas, Haut

        for move in moves:
            new_pos = zero_pos + move
            # Vérification que la nouvelle position est valide (pas en dehors du plateau de jeu)
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                # Création d'un nouvel état en échangeant les positions du zéro et d'un jeton adjacent
                new_state = np.copy(self.state)
                new_state[zero_pos[0], zero_pos[1]
                          ] = self.state[new_pos[0], new_pos[1]]
                new_state[new_pos[0], new_pos[1]] = 0
                neighbors.append(TaquinState(
                    new_state, parent=self, g=self.g + 1)) # zid el cout 1 kol mara 
        return neighbors

    def get_path(self):
        # Renvoie le chemin complet depuis l'état initial jusqu'à cet état
        path = []
        current_state = self
        while current_state:
            path.append(current_state)
            current_state = current_state.parent
        return list(reversed(path))

    def __lt__(self, other):
        # Surcharge de l'opérateur < pour permettre l'utilisation de heapq
        return (self.g + self.h) < (other.g + other.h)


def solve_taquin(initial_state, final, callback=None):
    # cree 2 liste
    open_list = []
    closed_list = []

    # ajout de taquin initial au open list
    initial_state = TaquinState(np.array(initial_state))
    heapq.heappush(open_list, initial_state)

    while open_list:
        #   yekhou  state baqal heurestique
        current_state = heapq.heappop(open_list)

        # kenou equal yokhrej
        if np.array_equal(current_state.state, final):
            return current_state.get_path()

        # izidha lil current state
        closed_list.append(tuple(current_state.state.flatten()))

        # yekhou neighbors mteaa state ou izidhom lil openlist ken msh visité
        for neighbor in current_state.get_neighbors():
            # flatten bsh najem ncompari state est ce que fil closed wela le
            if tuple(neighbor.state.flatten()) not in closed_list:
                if callback:
                    callback(len(closed_list), len(open_list))
                heapq.heappush(open_list, neighbor)

    return None
