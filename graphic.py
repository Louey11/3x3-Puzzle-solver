import main as test
import tkinter as tk
import customtkinter as ctk

initial = [[1, 2, 3],
           [8, 0, 6],
           [7, 5, 4]
           ]

final = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]


def update_info(visitedResult, closedNodesResult):
    visited_label.configure(text=f"Visited nodes: {visitedResult}")
    closed_nodes_label.configure(text=f"Closed nodes: {closedNodesResult}")


def Solve():
    global initial, final
    test.recherche(initial, final, callback=update_info)


window = ctk.CTk()
window.title('3x3 Puzzle Solver')
window.geometry('600x400')


button = ctk.CTkButton(
    master=window, text="Recherche", command=Solve)
button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


visited_label = ctk.CTkLabel(window, text="Visited nodes: 0")
visited_label.grid(row=0, column=0)
visited_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
closed_nodes_label = ctk.CTkLabel(window, text="Closed nodes: 0")
closed_nodes_label.grid(row=1, column=0)
closed_nodes_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

window.mainloop()
