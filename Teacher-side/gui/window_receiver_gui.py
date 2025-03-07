from customtkinter import CTk, CTkFrame, CTkLabel, CTkScrollableFrame
from threading import Thread
from datetime import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "backend"))
from window_receiver_backend import StudentMonitorBackend


class CheckStudentScreen(CTk):
    def __init__(self, school, class_name, student_id, student_name):
        super().__init__()
        self.student_name = student_name
        self.backend = StudentMonitorBackend(school, class_name, student_id)
        self.is_running = True  # Flag for managing running status
        self.init_ui()
        self.setup_window()
        self.start_monitoring()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def init_ui(self):
        """Initialize all UI components"""
        self.main_frame = CTkFrame(master=self, border_color='white', border_width=2, fg_color='transparent')
        self.main_frame.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Configure main frame grid
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        self.element_frame = CTkFrame(master=self.main_frame, fg_color='transparent')
        self.element_frame.grid(row=0, column=0, sticky='nsew')
        
        # Configure element frame grid
        self.element_frame.grid_columnconfigure(0, weight=1)
        self.element_frame.grid_rowconfigure(2, weight=1)  # For scrollable frame

        # Student Info Section
        self.student_name_lbl = CTkLabel(
            master=self.element_frame, 
            text=self.student_name,
            font=('Arial', 16, 'bold')
        )
        
        # Active Window Section
        self.active_window_lbl = CTkLabel(
            master=self.element_frame,
            text="ACTIVE WINDOW : Loading...",
            font=('Arial', 12)
        )
        
        # Windows List - Remove fixed width
        self.windows_list = CTkScrollableFrame(self.element_frame)
        
        # Time Stamp
        self.time_label = CTkLabel(
            master=self.element_frame,
            text="Last Update: -",
            font=('Arial', 10)
        )

        # Layout with sticky parameters
        self.student_name_lbl.grid(row=0, column=0, pady=5, sticky='ew')
        self.active_window_lbl.grid(row=1, column=0, pady=5, sticky='ew')
        self.windows_list.grid(row=2, column=0, pady=10, sticky='nsew')  # Changed here
        self.time_label.grid(row=3, column=0, pady=5, sticky='ew')

    def setup_window(self):
        """Configure main window settings"""
        self.geometry('800x600')  # Increased default size
        self.minsize(600, 450)
        self.title(f'Student Monitor - {self.student_name}')
        self.after(1000, self.update_ui)
        
        # Enable resizing configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def start_monitoring(self):
        """Start backend monitoring"""
        self.backend.start_monitoring()

    def update_ui(self):
        """Update UI with latest data"""
        if not self.is_running:  # do not run, if app was closed
            return
        data = self.backend.get_latest_data()
        if data:
            # Update active window
            self.active_window_lbl.configure(
                text=f"ACTIVE WINDOW: {data.get('active', 'N/A')}"
            )
            
            # Update timestamp
            timestamp = data.get('timestamp')
            if timestamp:
                dt = datetime.fromtimestamp(timestamp)
                self.time_label.configure(
                    text=f"Last Update: {dt.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            
            # Update windows list
            for widget in self.windows_list.winfo_children():
                widget.destroy()
                
            for window in data.get('open_windows', []):
                label = CTkLabel(self.windows_list, text=window)
                label.pack(anchor='w', padx=5, pady=2)
        
        if self.is_running:
            self.after(1000, self.update_ui)

    def on_close(self):
        """stop everythings"""
        self.is_running = False  # disabling updates
        self.backend.stop_monitoring() 
        self.destroy() 

    def run(self):
        self.mainloop()

def creator(school_code, class_code, national_code, std_name):
    print(school_code)
    print(class_code)
    print(national_code)
    print(std_name)
    app = CheckStudentScreen(
        school=school_code,
        class_name=class_code,
        student_id=national_code,
        student_name=std_name
    )
    app.run()   

if __name__ == '__main__':
    app = CheckStudentScreen(
        school='123',
        class_name='1052',
        student_id='09295',
        student_name="Abolfazl Rashidian"
    )
    app.run()