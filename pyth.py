import numpy as np
from collections import deque


class TaquinState:
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def get_neighbors(self):
        # Renvoie les états voisins valides en effectuant les mouvements possibles
        neighbors = []
        zero_pos = np.argwhere(self.state == 0)[0]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Droite, Gauche, Bas, Haut

        for move in moves:
            new_pos = zero_pos + move
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_state = np.copy(self.state)
                new_state[zero_pos[0], zero_pos[1]
                          ] = self.state[new_pos[0], new_pos[1]]
                new_state[new_pos[0], new_pos[1]] = 0
                neighbors.append(TaquinState(new_state, parent=self))
        return neighbors

    def get_path(self):
        # Renvoie le chemin complet depuis l'état initial jusqu'à cet état
        path = []
        current_state = self
        while current_state:
            path.append(current_state)
            current_state = current_state.parent
        return list(reversed(path))


def solve_taquin(initial_state, final_state, callback=None):
    open_list = deque()
    closed_list = set()

    initial_state = TaquinState(np.array(initial_state))
    open_list.append(initial_state)

    while open_list:
        current_state = open_list.popleft()
        if np.array_equal(current_state.state, final_state):
            return current_state.get_path()

        closed_list.add(tuple(current_state.state.flatten()))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.state.flatten()) not in closed_list:
                if callback:
                    callback(len(closed_list), len(open_list))
                open_list.append(neighbor)
                closed_list.add(tuple(neighbor.state.flatten()))

    # Si aucune solution n'est trouvée
    return None
