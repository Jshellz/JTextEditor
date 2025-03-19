import tkinter as tk
from tkinter import filedialog


class TextEditor:
    def __init__(self, root, label="JTextEditor"):
        self.root = root
        self.root.label = label
        self.root.geometry("1000x800")

        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

        # self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        # self.menu_bar.add_cascade(label="About", menu=self.about_menu)

    def exit_app(self):
        self.root.destroy()

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text files", ".txt"), ("All files", "*.*")]
        )
        if file_path:
            self.text_area.delete(1.0, tk.END)
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.insert(1.0, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", ".txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
