from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkEntry, NORMAL, DISABLED, END
from tkinter import ttk, CENTER, VERTICAL
from pathlib import Path
import sys
from threading import Thread
from ping3 import ping
from datetime import datetime
from tkinter import messagebox

sys.path.append(str(Path(__file__).resolve().parent))

from backend.get_students import get_students_by_class_code
from backend.get_message import fetch_messages
from backend.get_active_window import get_active_window_from_server
from window_receiver_gui import creator
from backend.searching import get_students_name_by_national_code


class MainPage(CTk):
    def __init__(self, school_code, school_name, class_name, unic_class_code):
        super().__init__()
        self.unic_class_code = unic_class_code
        self.school_code = school_code
        self.school_name = school_name
        self.class_name = class_name
        print(f'school_code : {school_code}')
        print(f'school_name : {school_name}')
        print(f'class_name : {class_name}')
        self.student_rows = {}
        self.students_list = [False, 'NotAssigned']

        self.title("Main Page")
        self.geometry('900x680')
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
            columns=("Name", "Last Check result & Time", "Accuracy", "Desktop"),
            show='headings',
            height=15
        )
        Thread(target=self.get_students_list_func).start()

        # Defining Columns
        for col in ("Name", "Last Check result & Time", "Accuracy", "Desktop"):
            self.table.heading(col, text=col, anchor=CENTER)
            if col == 'Name' :
                self.table.column(col, anchor=CENTER, width=160)
            elif col == 'Desktop' :
                self.table.column(col, anchor=CENTER, width=160)
            else:
                self.table.column(col, anchor=CENTER, width=80)
            self.table.column('Last Check result & Time', anchor=CENTER, width=200)

        # Adding Scrollbar
        self.scrollbar = ttk.Scrollbar(self.element_frame, orient=VERTICAL, command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)

        # Placing Table and Scrollbar
        self.table.grid(row=1, column=0, pady=20, columnspan=3, sticky='we')
        self.scrollbar.grid(row=1, column=2, sticky='nes', pady=20)

        # elements 
        self.main_label = CTkLabel(master=self.element_frame, text=f'Students Class {school_name}-{class_name} Status', font=('montserrat', 30, 'bold'))
        self.ping_lbl_and_check_status = CTkLabel(master=self.element_frame, text='STATUS / PING', font=('montserrat', 20, 'bold'))
        self.checking_entry = CTkEntry(master=self.element_frame, height=40, width=150, font=('montserrat', 17, 'bold'), border_color='#2B2B2B', justify='right', fg_color='#2B2B2B')
        self.ping_entry = CTkEntry(master=self.element_frame, height=40, width=100, font=('montserrat', 17, 'bold'), border_color='#2B2B2B', justify='right', fg_color='#2B2B2B')
        self.more_info_button = CTkButton(master=self.element_frame, text='More Info', font=('montserrat', 20, 'bold'), height=30, width=250, border_color='white', border_width=2, command=self.show_more_info)
        self.exit_button = CTkButton(master=self.element_frame, text='Exit', font=('montserrat', 20, 'bold'), height=30, width=250, fg_color='red', hover_color='#6B0011', border_color='white', border_width=2, command=lambda: self.destroy())

        # placing elements in element_frame      
        self.main_label.grid(row=0, column=0 ,sticky='n',columnspan=3)
        self.more_info_button.grid(row=3, column=0, pady=(10,0), sticky='we', columnspan=3)
        self.exit_button.grid(row=4, column=0, pady=(10,0), sticky='we', columnspan=3)
        self.ping_lbl_and_check_status.grid(row=2, column=0, sticky='w')
        self.checking_entry.grid(row=2, column=1, sticky='e')
        self.ping_entry.grid(row=2, column=2, sticky='e')

        self.checking_entry.configure(state=DISABLED)
        self.ping_entry.configure(state=DISABLED)
        Thread(target=self.pinging).start()

    def update_entry(self, txt):
        self.checking_entry.configure(state='normal')
        self.checking_entry.delete(0, END)
        self.checking_entry.insert(0, txt)
        self.checking_entry.configure(state='disabled')

    def show_more_info(self):
        def show_info_thread_handler():
            selected_item = self.table.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a student first!")
                return
            
            # Get student data
            item_data = self.table.item(selected_item)['values']
            national_code = None
            
            # Find national code by student name
            for code, name in self.translated_name.items():
                if name == item_data[0]:
                    national_code = code
                    break
            
            if national_code:
                creator(self.school_code,
                        self.class_name,
                        national_code,
                        item_data[0])
            else:
                messagebox.showerror("Error", "Student data not found!")
        Thread(target=show_info_thread_handler).start()

    def pinging(self):
        try:
            response_time = ping('google.com', unit='ms')
            if response_time is not None:
                response_time = f"{response_time:.2f} ms"
            else:
                response_time = f"Failed"

            if response_time:
                self.ping_entry.configure(state=NORMAL)
                self.ping_entry.delete(0, END)
                self.ping_entry.insert(END, response_time)
            else:
                response_time == 'Failed'
                self.ping_entry.configure(state=NORMAL)
                self.ping_entry.delete(0, END)
                self.ping_entry.insert(END, response_time)
            self.ping_entry.configure(state=DISABLED)
        except Exception:
            self.ping_entry.configure(state=NORMAL)
            self.ping_entry.delete(0, END)
            self.ping_entry.insert(END, 'ERROR')            
            self.ping_entry.configure(state=DISABLED)
        self.after(1000, self.pinging)

    def get_students_list_func(self):
        self.students_list = get_students_by_class_code(unic_class_code=self.unic_class_code)
        if self.students_list[0]:
            self.update_entry('GETTING')
                                  # name : sum, count, last time
            self.accuracy_dict = {national_code:[0, 0, ''] for national_code in self.students_list[1]}
            Thread(target=self.translate_natoinal_code_to_name, daemon=True).start()
        else:
            self.update_entry('ERROR')
            print(f'--------------------\nERROR IS : \n{self.students_list[1]}\n--------------------')
            self.after(30000, self.get_students_list_func)

    def translate_natoinal_code_to_name(self):
        # national_code : name
        print(self.students_list[1])
        self.translated_name = {i:get_students_name_by_national_code(i) for i in self.students_list[1]}
        Thread(target=self.set_students_int_table, daemon=True).start()

    def set_students_int_table(self):

        if self.students_list[0] :
            # self.students_list = self.students_list[1]
            for student in self.students_list[1]:
                item_id = self.table.insert("", "end", values=(self.translated_name[student], 'N/A', 'N/A', 'N/A'))
                self.student_rows[student] = item_id 
            Thread(target=self.update_data, daemon=True).start()
        else:
            print(f'ERROR : {self.students_list[1]}')
            self.after(30000, self.set_students_int_table)

    def calculate_time_difference(self, input_time_str):
        given_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M:%S")
        current_time = datetime.now()

        delta = current_time - given_time
        delta_hours = delta.total_seconds() / 3600 
        delta_min = delta.total_seconds() / 60

        
        print(f"delta  {delta_hours:.1f} hours")
        

        if delta_hours >= 7:
            return [False, "no record found"]
        elif delta_hours < 7:
            return [True, f'{delta_min:.2f}min ago']

    def update_data(self):
        def update_data_thread_handler():
            print('--new round started')
            self.update_entry('UPDATING')
            if self.students_list[0]:
                for student in self.students_list[1] :
                    print(f'im going to get message of {student}...')
                    respond = fetch_messages(national_code=student, 
                                             school_code=self.school_code, 
                                             class_code=self.class_name)
                    
                    print(f'this is respond : <{respond}>')
                    if respond[0] :
                        if respond[1] != 'No messages yet':
                            code, message_time = str(respond[1]).split('|=|')[0], str(respond[1]).split('|=|')[1] 
                            status, time = self.calculate_time_difference(message_time)

                            print(status)
                            print(time)
                            if status :
                                open_window = 'Not in Class'
                                if code == '0':
                                    final_message = f'Needs updated'
                                elif code == '1':
                                    final_message = f'Students goes-{time}'
                                elif code == '2' :
                                    final_message = f'Identity not confirmed-{time}'
                                elif code == '3' :
                                    final_message = f'Sleeping-{time}'
                                elif code == '4':
                                    final_message = f'Not looking-{time}'
                                    window_respond = get_active_window_from_server(school=self.school_code,
                                                                   class_name=self.class_name,
                                                                   student_id=student)
                                    for i in ['Skyroom', 'Adobe Connect', 'Shad']:
                                        if i in str(window_respond) :
                                            open_window = i
                                            break
                                elif code == '5' :
                                    final_message = f'Looking-{time}'
                                    window_respond = get_active_window_from_server(school=self.school_code,
                                                                   class_name=self.class_name,
                                                                   student_id=student)
                                    for i in ['Skyroom', 'Adobe Connect', 'Shad']:
                                        if i in str(window_respond) :
                                            open_window = i
                                            break

                                print(f'getting accuracy rate {student} ...')
                                self.accuracy_data = self.accuracy_dict[student] # list [sum, count, last time]
                                print(f'last time is {self.accuracy_data[2]}')
                                print(f'message time is {message_time}')
                                if self.accuracy_data[2] != message_time:
                                    self.accuracy_data[2] = message_time     # setting new time
                                    self.accuracy_data[1] = int(self.accuracy_data[1]) + 1   # + count
                                    if code == '5': # if looking
                                        self.accuracy_data[0] += 1   # adding to sum
                                    else: # if not looking
                                        pass
                                    self.accuracy_rate = float((self.accuracy_data[0] / self.accuracy_data[1]) * 100).__round__(1)
                                    print(self.accuracy_rate)



                                self.table.item(self.student_rows[student], values=(self.translated_name[student], final_message, str(self.accuracy_rate)+'%', open_window))
                        
                            else:
                                final_message = f'last seen long time ago'
                                self.table.item(self.student_rows[student], values=(self.translated_name[student], final_message, "N/A", "N/A"))


                        else:
                            self.table.item(self.student_rows[student], values=(self.translated_name[student], 'No messages yet', "N/A", "N/A"))

                    else:
                        print('Error while getting last message')
                        self.update_entry('ERROR')
            else:
                print('an Error occured while getting students list')
            self.update_entry('STOPPED')
        Thread(target=update_data_thread_handler).start()
        self.after(30000, self.update_data)

    def run(self):
        self.mainloop()


def main_page_func_teacher(school_code, school_name, class_name, unic_class_code):
    app = MainPage(school_code, school_name, class_name, unic_class_code)
    app.run()


if __name__ == '__main__' : 
    main_page_func_teacher('123','hn1','1052')
