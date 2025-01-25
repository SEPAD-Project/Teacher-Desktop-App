from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkOptionMenu

class SelectClassPage(CTk):
    def __init__(self):
        super().__init__()

        self.title("Select Class Page")
        self.geometry('700x500')
        self.minsize(700, 500)
        # main red frame
        self.main_frame = CTkFrame(master=self, border_color='red', border_width=2)
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        #elements frame for holdign eveything in center 
        self.element_frame = CTkFrame(master=self.main_frame, fg_color='transparent')
        self.element_frame.place(relx=0.5, rely=0.5, anchor='center')
        # elements 
        self.welcome_label = CTkLabel(master=self.element_frame, text='Welcom Mr.x', font=('montserrat', 30, 'bold'))
        self.select_calss_optionbox = CTkOptionMenu(master=self.element_frame, values=['test1', 'test2', 'test3'], height=40, width=150, font=('montserrat', 20, 'bold'))
        self.join_button = CTkButton(master=self.element_frame, text='Join to Class', font=('montserrat', 20, 'bold'), height=30, width=250, border_color='white', border_width=2)
        self.exit_button = CTkButton(master=self.element_frame, text='Exit', font=('montserrat', 20, 'bold'), height=30, width=250, fg_color='red', hover_color='#6B0011', border_color='white', border_width=2, command=lambda: self.destroy())

        # placing elements in element_frame      
        self.welcome_label.grid(row=0, column=0 ,sticky='n')
        self.select_calss_optionbox.grid(row=1, column=0, pady=90)
        self.join_button.grid(row=2, column=0)
        self.exit_button.grid(row=3, column=0, pady=(10,0))

    def run(self):
        self.mainloop()


def select_class_page():
    app = SelectClassPage()
    app.run()


if __name__ == '__main__' : 
    select_class_page()
