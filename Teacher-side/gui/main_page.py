# from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel
# from tkinter import ttk, CENTER, BOTH, RIGHT, Y, VERTICAL, messagebox


# class MainPage(CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Main Page")
#         self.geometry('700x500')
#         self.minsize(700, 500)
#         # main red frame
#         self.main_frame = CTkFrame(master=self, border_color='red', border_width=2)
#         self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
#         #elements frame for holdign eveything in center 
#         self.element_frame = CTkFrame(master=self.main_frame, fg_color='transparent')
#         self.element_frame.place(relx=0.5, rely=0.5, anchor='center')
        
#         ## code here ##


#         # elements 
#         self.main_label = CTkLabel(master=self.element_frame, text='Students Status', font=('montserrat', 30, 'bold'))
#         self.exit_button = CTkButton(master=self.element_frame, text='Exit', font=('montserrat', 20, 'bold'), height=30, width=250, fg_color='red', hover_color='#6B0011', border_color='white', border_width=2, command=lambda: self.destroy())

#         # placing elements in element_frame      
#         self.main_label.grid(row=0, column=0 ,sticky='n')
#         self.exit_button.grid(row=2, column=0, pady=(10,0))

#     def run(self):
#         self.mainloop()


# def main_page_func():
#     app = MainPage()
#     app.run()


# if __name__ == '__main__' : 
#     main_page_func()








from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel
from tkinter import ttk, CENTER, BOTH, RIGHT, Y, VERTICAL, messagebox


class MainPage(CTk):
    def __init__(self):
        super().__init__()

        self.title("Main Page")
        self.geometry('900x600')
        self.minsize(900, 600)
        # main red frame
        self.main_frame = CTkFrame(master=self, border_color='red', border_width=2)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        #elements frame for holding everything in center 
        self.element_frame = CTkFrame(master=self.main_frame, fg_color='transparent')
        self.element_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        ## Adding Table ##
        # Creating Treeview (Table)
        self.table = ttk.Treeview(
            master=self.element_frame,
            columns=("Name", "face1", "face2", "face3", "Accuracy rate", "Desktop"),
            show='headings',
            height=15
        )

        # Defining Columns
        for col in ("Name", "face1", "face2", "face3", "Accuracy rate", "Desktop"):
            self.table.heading(col, text=col, anchor=CENTER)
            if col == 'Name' or col == 'Accuracy rate' or col == 'Desktop' :
                self.table.column(col, anchor=CENTER, width=150)
            else:
                self.table.column(col, anchor=CENTER, width=50)


        # Adding Sample Data
        for i in range(1, 31):
            self.table.insert("", "end", values=(f"Row {i} Col 1", f"Row {i} Col 2", f"Row {i} Col 3", f"Row {i} Col 4", f"Row {i} Col 5", f"Row {i} Col 6", f"Row {i} Col 7"))

        # Adding Scrollbar
        self.scrollbar = ttk.Scrollbar(self.element_frame, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # Placing Table and Scrollbar
        self.table.grid(row=1, column=0, pady=20)
        self.scrollbar.grid(row=1, column=0, sticky='nes', pady=20)

        # elements 
        self.main_label = CTkLabel(master=self.element_frame, text='Students Status', font=('montserrat', 30, 'bold'))
        self.exit_button = CTkButton(master=self.element_frame, text='Exit', font=('montserrat', 20, 'bold'), height=30, width=250, fg_color='red', hover_color='#6B0011', border_color='white', border_width=2, command=lambda: self.destroy())

        # placing elements in element_frame      
        self.main_label.grid(row=0, column=0 ,sticky='n')
        self.exit_button.grid(row=2, column=0, pady=(10,0), sticky='we')

    def run(self):
        self.mainloop()


def main_page_func():
    app = MainPage()
    app.run()


if __name__ == '__main__' : 
    main_page_func()
