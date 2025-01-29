from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel
from tkinter import ttk, CENTER, BOTH, RIGHT, Y, VERTICAL
from pathlib import Path
import sys
from threading import Thread

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir / "backend"))

from get_students import get_students_list, fetch_messages

class MainPage(CTk):
    def __init__(self, class_id):
        super().__init__()

        self.class_id = class_id
        self.student_rows = {}

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
            columns=("Name", "Last Check & Time", "Accuracy rate", "Desktop"),
            show='headings',
            height=15
        )
        self.students_list = get_students_list(school_name=str(self.class_id).split('-')[0], class_code=str(self.class_id).split('-')[1])
        if self.students_list[0] :
            self.students_list = self.students_list[1]
            for student in self.students_list:
                item_id = self.table.insert("", "end", values=(student, 'N/A', 'N/A', 'N/A'))
                self.student_rows[student] = item_id 
        # Defining Columns
        for col in ("Name", "Last Check & Time", "Accuracy rate", "Desktop"):
            self.table.heading(col, text=col, anchor=CENTER)
            if col == 'Name' or col == 'Last Check & Time' :
                self.table.column(col, anchor=CENTER, width=180)
            else:
                self.table.column(col, anchor=CENTER, width=100)


        # Adding Scrollbar
        self.scrollbar = ttk.Scrollbar(self.element_frame, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # Placing Table and Scrollbar
        self.table.grid(row=1, column=0, pady=20)
        self.scrollbar.grid(row=1, column=0, sticky='nes', pady=20)

        # elements 
        self.main_label = CTkLabel(master=self.element_frame, text=f'Students Class {self.class_id} Status', font=('montserrat', 30, 'bold'))
        self.exit_button = CTkButton(master=self.element_frame, text='Exit', font=('montserrat', 20, 'bold'), height=30, width=250, fg_color='red', hover_color='#6B0011', border_color='white', border_width=2, command=lambda: self.destroy())

        # placing elements in element_frame      
        self.main_label.grid(row=0, column=0 ,sticky='n')
        self.exit_button.grid(row=2, column=0, pady=(10,0), sticky='we')

        Thread(target=self.update_data, daemon=True).start()


    def update_data(self):
        for student in self.students_list :
            respond = fetch_messages(student=student, school_name=str(self.class_id).split('-')[0], class_code=str(self.class_id).split('-')[1])
            if respond[0] :
                self.table.item(self.student_rows[student], values=(student, respond[1], "N/A", "N/A"))
        self.after(30000, self.update_data)

    def get_last_status(self):
        self.students_list

    def run(self):
        self.mainloop()


def main_page_func(classid):
    app = MainPage(classid)
    app.run()


if __name__ == '__main__' : 
    main_page_func('hn1-1052')
