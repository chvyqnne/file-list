import os
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to browse source directory
def browse_source():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, folder_selected)

# Function to browse destination directory
def browse_dest():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        dest_entry.delete(0, tk.END)
        dest_entry.insert(0, folder_selected)

# Function to generate CSV
def generate_csv():
    source_path = source_entry.get()
    dest_path = dest_entry.get()

    if not source_path or not dest_path:
        messagebox.showerror("Error", "Please select both source and destination paths.")
        return

    csv_file = os.path.join(dest_path, "file_list.csv")
    
    try:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Full Path", "File Name", "Folder Name"])

            for foldername, subfolders, filenames in os.walk(source_path):
                for filename in filenames:
                    full_path = os.path.join(foldername, filename)
                    writer.writerow([full_path, filename, os.path.basename(foldername)])

        messagebox.showinfo("Success", f"CSV file created at {csv_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Setting up the GUI
root = tk.Tk()
root.title("File Lister")

# Source Path
tk.Label(root, text="Source Path:").grid(row=0, column=0, padx=10, pady=5)
source_entry = tk.Entry(root, width=40)
source_entry.grid(row=0, column=1, padx=10, pady=5)
browse_source_btn = tk.Button(root, text="Browse", command=browse_source)
browse_source_btn.grid(row=0, column=2, padx=10, pady=5)

# Destination Path
tk.Label(root, text="Destination Path:").grid(row=1, column=0, padx=10, pady=5)
dest_entry = tk.Entry(root, width=40)
dest_entry.grid(row=1, column=1, padx=10, pady=5)
browse_dest_btn = tk.Button(root, text="Browse", command=browse_dest)
browse_dest_btn.grid(row=1, column=2, padx=10, pady=5)

# Generate CSV button
generate_btn = tk.Button(root, text="Generate CSV", command=generate_csv)
generate_btn.grid(row=2, column=1, pady=20)

root.mainloop()
