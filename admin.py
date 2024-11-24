from tkinter import *
from tkinter import messagebox
import sqlite3

from Face_Recognition_System import Face_Recognition_System


class Admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("1290x768+0+0")

        # Admin login UI setup
        self.bg = Label(self.root, bg="white")
        self.bg.place(x=0, y=0, width=1290, height=768)

        title = Label(self.root, text="Admin Login", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title.place(x=0, y=20, width=1290, height=50)

        # Username Label and Entry
        lbl_user = Label(self.root, text="Username", font=("verdana", 20), bg="white")
        lbl_user.place(x=450, y=200)
        self.txt_user = Entry(self.root, font=("verdana", 15))
        self.txt_user.place(x=600, y=200, width=250)

        # Password Label and Entry
        lbl_pass = Label(self.root, text="Password", font=("verdana", 20), bg="white")
        lbl_pass.place(x=450, y=300)
        self.txt_pass = Entry(self.root, font=("verdana", 15), show="*")
        self.txt_pass.place(x=600, y=300, width=250)

        # Login Button
        btn_login = Button(self.root, text="Login", command=self.admin_login, font=("verdana", 15, "bold"), bg="navyblue", fg="white")
        btn_login.place(x=600, y=400, width=150, height=35)

    def admin_login(self):
        user = self.txt_user.get()
        password = self.txt_pass.get()

        # Connecting to SQLite database
        conn = sqlite3.connect("face_recognition.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (user, password))
        row = cursor.fetchone()
        conn.close()

        if row:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()  # Close the current window
            root = Tk()  # Create a new Tkinter window
            Face_Recognition_System(root)  # Launch the main Face Recognition UI
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

if __name__ == "__main__":
    root = Tk()
    app = Admin(root)  # Start with the AdminLogin UI
    root.mainloop()