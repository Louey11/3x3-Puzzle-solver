import time
initial = [
    [5, 4, 2],
    [8, 1, 3],
    [0, 6, 7]
]

final = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]





def show_taquin(taquin):
    for row in taquin:
        print(" --   --   --")
        for col in row:
            print(" ", col, "|", end='')
        print('\n')


def get_empty_position(initial):
    for row in initial:
        for col, value in enumerate(row):
            if value == 0:
                return (initial.index(row), col)


def get_number_at_position(taquin, pos):
    return taquin[pos[0]][pos[1]]



def swap_positions(taquin, pos1, pos2):
    taquin[pos1[0]][pos1[1]], taquin[pos2[0]][pos2[1]] = taquin[pos2[0]][pos2[1]], taquin[pos1[0]][pos1[1]]


def transition(taquin):
    empty_pos = get_empty_position(taquin)
    possible_moves = {
        (1, 1): [(0, 1), (1, 2), (2, 1), (1, 0)],
        (0, 1): [(1, 1), (0, 0), (0, 2)],
        (1, 0): [(1, 1), (0, 0), (2, 0)],
        (1, 2): [(1, 1), (2, 2), (0, 2)],
        (2, 1): [(1, 1), (2, 2), (2, 0)],
        (0, 0): [(1, 0), (0, 1)],
        (0, 2): [(1, 2), (0, 1)],
        (2, 2): [(1, 2), (2, 1)],
        (2, 0): [(2, 1), (1, 0)]
    }
    # return empty list if empty_pos not found
    return possible_moves.get(empty_pos, [])

def successors_of(first_node):
    possible=transition(first_node)
    successors=[]
    for possible_transition in possible:
        T = [ele[:] for ele in first_node]
        swap_positions(T,get_empty_position(first_node),possible_transition)
        successors.append(T)
    return successors


def recherche(initial,final):
    if initial == final:
        success = True
        return [initial]
    free_nodes=[initial]
    closed_nodes=[]
    goalNode=[]
    success=False
    visited = 0
    while (free_nodes != [] and not(success)):
        first_node=free_nodes.pop()
        closed_nodes.append(first_node)
        generated_states=[]
        generated_states=successors_of(first_node)
        generated_states = [
            s for s in generated_states if 
            (
                s not in free_nodes and
                s not in closed_nodes
              )
        ]
        free_nodes += generated_states
        for s in generated_states:
            visited+=1
            with open("output.txt", "w") as f:
                f.write(str(visited))
            if s==final :
                success=True
                goalNode.append(s)
                with open("output.txt", "a") as f:
                    f.write("\n"+str(len(closed_nodes)))
                break

    return closed_nodes
        


result=recherche(initial,final)

for i in result:
    show_taquin(i)
    print("***************")

show_taquin(final)

# def dfs(graph, node):
#     visited = []
#     stack = deque()

#     visited.append(node)
#     stack.append(node)

#     while stack:
#         s = stack.pop()
#         print(s, end=" ")

#     for n in reversed(graph[s]):
#         if n not in visited:
#             visited.append(n)
#             stack.append(n)

