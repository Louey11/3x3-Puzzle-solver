import tkinter as tk
import customtkinter as ctk
import main as solver
import pyth as large
import etoile as etoile

# Define the final state of the puzzle
FINAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def get_initial_state(entries):
    # Convert the input entries into a 3x3 matrix
    initial = []
    for i in range(3):
        row = []
        for j in range(3):
            entry_text = entries[i][j].get()
            if entry_text.isdigit():
                row.append(int(entry_text))
            else:
                # Handle invalid input
                row.append(0)
        initial.append(row)
    return initial


def update_info(visited_result, closed_nodes_result):
    # Update the labels with the current search status
    visited_label.configure(text=f"gen nodes: {visited_result}")
    closed_nodes_label.configure(text=f"Closed nodes: {closed_nodes_result}")


def solve_puzzle():
    # Get the initial state from the entries and solve the puzzle
    initial_state = get_initial_state(entry_list)
    solver.recherche(initial_state, FINAL_STATE, callback=update_info)


def solve_puzzle2():
    # Get the initial state from the entries and solve the puzzle
    initial_state = get_initial_state(entry_list)
    large.solve_taquin(initial_state, FINAL_STATE, callback=update_info)


def solve_puzzle3():
    # Get the initial state from the entries and solve the puzzle
    initial_state = get_initial_state(entry_list)
    etoile.solve_taquin(initial_state, FINAL_STATE, callback=update_info)


# Create the main window
window = ctk.CTk()
window.title('3x3 Puzzle Solver')
window.geometry('600x400')

# Create a frame to hold the entry widgets
frame = ctk.CTkFrame(master=window, width=150, height=150)
frame.grid(row=0, column=0)

# Set the column and row weights of the frame to 1 to make it expand
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Create the entry widgets for the initial state
entry_list = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = ctk.CTkEntry(master=frame,
                             width=25,
                             height=35,
                             border_width=2,
                             corner_radius=10)
        entry.grid(row=i, column=j, sticky='nswe')
        row_entries.append(entry)
    entry_list.append(row_entries)

frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create the Solve button
button = ctk.CTkButton(
    master=window, text="Solve", command=solve_puzzle)
button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

button = ctk.CTkButton(
    master=window, text="Solve Largeur", command=solve_puzzle2)
button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

button = ctk.CTkButton(
    master=window, text="Solve A*", command=solve_puzzle3)
button.place(relx=0.2, rely=0.9, anchor=tk.CENTER)


# Create the labels to display search status
visited_label = ctk.CTkLabel(window, text="gen nodes: 0")
visited_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
closed_nodes_label = ctk.CTkLabel(window, text="Closed nodes: 0")
closed_nodes_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Start the main event loop
window.mainloop()
