import tkinter as tk
from tkinter import ttk
from data import InputData
from converter import Converter


class Ui:
    def __init__(self, converter: Converter):
        self.converter = converter
        self.root = tk.Tk()
        self.root.title("Summarizer")
        self.tabControl = ttk.Notebook(self.root)
        self.create_web_tab()
        self.create_text_tab()
        self.tabControl.pack(expand=1, fill="both")
        self.root.mainloop()

    def __submit(self, web: bool):
        if web:
            data = InputData(url=self.url_entry.get(), p=self.check1_var.get(), h=self.check2_var.get(),
                             length_min=self.web_spinbox_min_var.get(),
                             length_max=self.web_spinbox_max_var.get(),
                             browser=self.browser_combobox.get())
            try:
                self.converter.collect_elements(data)
            except:
                print("Browser has been closed!")
        else:
            data = InputData(file_path=self.file_path.get(), length_min=self.file_spinbox_min_var.get(),
                             length_max=self.file_spinbox_max_var.get(),
                             save_path=self.save_path.get())
            self.converter.save_to_file(data)

    def create_web_tab(self):
        web_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(web_tab, text='Site summarizer')

        tk.Label(web_tab, text="Enter url:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.url_entry = tk.Entry(web_tab)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(web_tab, text="Content:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.check1_var = tk.IntVar()
        self.check2_var = tk.IntVar()
        check1 = tk.Checkbutton(web_tab, text="paragraphs", variable=self.check1_var)
        check2 = tk.Checkbutton(web_tab, text="headers", variable=self.check2_var)
        check1.grid(row=1, column=1, padx=10, pady=10)
        check2.grid(row=2, column=1, padx=10, pady=10)

        self.web_spinbox_min_var = tk.IntVar()
        self.web_spinbox_min_var.set(10)
        tk.Label(web_tab, text="Minimal content length (words):").grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.web_spinbox_min = tk.Spinbox(web_tab, from_=0, to=1000, textvariable=self.web_spinbox_min_var)
        self.web_spinbox_min.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(web_tab, text="Maximal summarized content length (letters):").grid(row=4, column=0, sticky='w',
                                                                                    padx=10, pady=10)
        self.web_spinbox_max_var = tk.IntVar()
        self.web_spinbox_max_var.set(100)
        self.web_spinbox_max = tk.Spinbox(web_tab, from_=0, to=1000, textvariable=self.web_spinbox_max_var)
        self.web_spinbox_max.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(web_tab, text="Select browser:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
        self.browser_combobox = ttk.Combobox(web_tab, values=["Chrome", "Firefox", "Safari"])
        self.browser_combobox.current(0)
        self.browser_combobox.grid(row=5, column=1, padx=10, pady=10)

        submit_button = tk.Button(web_tab, text="Submit", command=lambda: self.__submit(True))
        submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def create_text_tab(self):
        text_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(text_tab, text='File summarizer')

        tk.Label(text_tab, text="File path:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.file_path = tk.Entry(text_tab)
        self.file_path.grid(row=0, column=1, padx=10, pady=10)

        self.file_spinbox_min_var = tk.IntVar()
        self.file_spinbox_min_var.set(10)
        tk.Label(text_tab, text="Minimal content length (words):").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.file_spinbox_min = tk.Spinbox(text_tab, from_=0, to=1000, textvariable=self.file_spinbox_min_var)
        self.file_spinbox_min.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(text_tab, text="Maximal summarized content length (letters):").grid(row=2, column=0, sticky='w',
                                                                                     padx=10, pady=10)
        self.file_spinbox_max_var = tk.IntVar()
        self.file_spinbox_max_var.set(100)
        self.file_spinbox_max = tk.Spinbox(text_tab, from_=0, to=1000, textvariable=self.file_spinbox_max_var)
        self.file_spinbox_max.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(text_tab, text="Save path (with file name):").grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.save_path = tk.Entry(text_tab)
        self.save_path.grid(row=3, column=1, padx=10, pady=10)

        submit_button = tk.Button(text_tab, text="Submit", command=lambda: self.__submit(False))
        submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
