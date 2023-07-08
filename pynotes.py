import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

def display_menu():
    print("PyNotes - Simple Note-Taking Application")
    print("1. View existing notes")
    print("2. Add a new note")
    print("3. Delete a note")
    print("4. View the total number of notes")
    print("5. Exit")

def view_notes():
    if not os.path.exists("notes.txt"):
        messagebox.showinfo("Existing Notes", "No notes found.")
    else:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if not notes:
            messagebox.showinfo("Existing Notes", "No notes found.")
        else:
            notes_list = "".join([f"{i+1}. {note}" for i, note in enumerate(notes)])
            messagebox.showinfo("Existing Notes", notes_list)

def add_note(note_entry):
    note = note_entry.get("1.0", tk.END).strip()
    if not note:
        messagebox.showerror("Error", "Please enter a note.")
        return
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    messagebox.showinfo("Note Added", "Note added successfully.")
    note_entry.delete("1.0", tk.END)

def delete_note(note_number_entry):
    note_number = int(note_number_entry.get())
    with open("notes.txt", "r") as file:
        notes = file.readlines()
    if note_number < 1 or note_number > len(notes):
        messagebox.showerror("Invalid Note Number", "Invalid note number.")
        return
    del notes[note_number - 1]
    with open("notes.txt", "w") as file:
        file.writelines(notes)
    messagebox.showinfo("Note Deleted", "Note deleted successfully.")

def view_total_notes():
    if not os.path.exists("notes.txt"):
        total_notes = 0
    else:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        total_notes = len(notes)
    messagebox.showinfo("Total Number of Notes", f"Total number of notes: {total_notes}")

def main():
    window = tk.Tk()
    window.title("PyNotes - Simple Note-Taking Application")

    def on_view_notes():
        view_notes()

    def on_add_note():
        add_note(note_entry)

    def on_delete_note():
        delete_note(note_number_entry)

    def on_view_total_notes():
        view_total_notes()

    def on_exit():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            window.destroy()

    view_notes_button = tk.Button(window, text="View existing notes", command=on_view_notes)
    view_notes_button.pack()

    note_label = tk.Label(window, text="Enter your note:")
    note_label.pack()

    note_entry = scrolledtext.ScrolledText(window, width=30, height=10)
    note_entry.pack()

    add_note_button = tk.Button(window, text="Add a new note", command=on_add_note)
    add_note_button.pack()

    note_number_label = tk.Label(window, text="Enter the note number to delete:")
    note_number_label.pack()

    note_number_entry = tk.Entry(window)
    note_number_entry.pack()

    delete_note_button = tk.Button(window, text="Delete a note", command=on_delete_note)
    delete_note_button.pack()

    view_total_notes_button = tk.Button(window, text="View total number of notes", command=on_view_total_notes)
    view_total_notes_button.pack()

    exit_button = tk.Button(window, text="Exit", command=on_exit)
    exit_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
