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
