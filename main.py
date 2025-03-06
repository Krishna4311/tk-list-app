import tkinter as tk
from tkinter import messagebox, filedialog
from tabulate import tabulate

# Function to process the input list
def process_list(input_data):
    try:
        if ',' in input_data:
            return [item.strip() for item in input_data.split(',')]
        else:
            return input_data.split()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        return []

# Function to read list from a file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                entry_list.delete(0, tk.END)
                entry_list.insert(0, content)
        except Exception as e:
            messagebox.showerror("File Error", f"Could not read file: {e}")

# Function to save table to a file
def download_table():
    content = output_text.get("1.0", tk.END).strip()
    if content:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Success", "Table downloaded successfully.")
    else:
        messagebox.showerror("Error", "No table content to save.")

# Function to display the list with indexing
def lst_index(lst):
    if len(lst) <= 10:
        a = [[i, lst[i]] for i in range(len(lst))]
    else:
        a = [[i, lst[i]] for i in range(10)]
        a.append(['...', '...'])
        a.append([len(lst) - 1, lst[-1]])
    
    return tabulate(a, headers=["Index", "List Elements"], tablefmt="grid")

# Function to search for an element and display duplicates
def search_index(lst, element):
    if element not in lst:
        return "Element doesn't exist"
    elif lst.count(element) == 1:
        return f"{element} is in position {lst.index(element)}"
    else:
        duplicate_elements = [[i, lst[i]] for i in range(len(lst)) if lst[i] == element]
        return tabulate(duplicate_elements, headers=["Index", "Repeated Elements"], tablefmt="grid")

# Function to delete an element from the list
def delete_element():
    lst = process_list(entry_list.get())
    element = entry_element.get().strip()
    if element in lst:
        lst.remove(element)
        entry_list.delete(0, tk.END)
        entry_list.insert(0, ", ".join(lst))
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "Updated List:\n" + lst_index(lst))
    else:
        messagebox.showerror("Error", "Element not found in list.")

# Function to update an element in the list
def update_element():
    lst = process_list(entry_list.get())
    old_element = entry_element.get().strip()
    new_element = entry_update.get().strip()
    if old_element in lst:
        index = lst.index(old_element)
        lst[index] = new_element
        entry_list.delete(0, tk.END)
        entry_list.insert(0, ", ".join(lst))
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "Updated List:\n" + lst_index(lst))
    else:
        messagebox.showerror("Error", "Element not found in list.")

# GUI Application
def show_list():
    lst = process_list(entry_list.get())
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, lst_index(lst))

def search_element():
    lst = process_list(entry_list.get())
    element = entry_element.get().strip()
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, search_index(lst, element))

# Tkinter Window Setup
root = tk.Tk()
root.title("LIST APP")
root.geometry("700x500")


tk.Label(root, text="Enter a list (comma-separated or space-separated):").pack()
entry_list = tk.Entry(root, width=60)
entry_list.pack()

tk.Button(root, text="Load from File", command=load_file).pack()

tk.Button(root, text="Show Indexed List", command=show_list).pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter element to search/delete/update:").grid(row=0, column=0, padx=20, pady=5)
tk.Label(frame, text="Enter new value for update:").grid(row=0, column=2, padx=20, pady=5)

entry_element = tk.Entry(frame, width=20)
entry_element.grid(row=1, column=0, padx=20, pady=5)
entry_update = tk.Entry(frame, width=20)
entry_update.grid(row=1, column=2, padx=20, pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Search Element", command=search_element).grid(row=0, column=0, padx=(40,50))
tk.Button(button_frame, text="Delete Element", command=delete_element).grid(row=1, column=0, padx=(40,50))
tk.Button(button_frame, text="Update Element", command=update_element).grid(row=0, column=2, padx=(80,10))

output_text = tk.Text(root, height=12, width=70)
output_text.pack()

tk.Button(root, text="Download Table", command=download_table).pack(pady=5)

root.mainloop()