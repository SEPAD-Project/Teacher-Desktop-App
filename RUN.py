import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent)+"\\source\\backend")
sys.path.append(str(Path(__file__).resolve().parent)+"\\source\\gui")
print(str(Path(__file__).resolve())+"\\source\\gui")
# class ignore:
#     def write(self, *a):
#         pass
#     def flush(self):
#         pass

# stdout = sys.stdout
# sys.stdout = ignore() # blocking output
# sys.stdout = stdout

if __name__ == "__main__":
    try:
        from source.gui import authentication_page
        app = authentication_page.TeacherSideAppLoginPage()
        app.run()
    except Exception as e:
        print("Critical error occured")
        print(str(e))