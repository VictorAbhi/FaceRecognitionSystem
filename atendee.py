import os
import re
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry

import sqlite3
import cv2

class Atendee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x768+0+0")
        self.root.title("Atendee Panel")

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mob = StringVar()
        self.var_address = StringVar()

        # This part is image labels setting start
        # first header image
        img = Image.open(r"Images_GUI\banner.png")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open(r"Images_GUI/bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Attendee Panel", font=("verdana", 30, "bold"), bg="white",
                          fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Creating Frame
        main_frame = Frame(bg_img, bd=2, bg="white")  # bd mean border
        main_frame.place(x=5, y=55, width=1355, height=510)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendee Details",
                                font=("verdana", 12, "bold"), fg="navyblue")
        left_frame.place(x=10, y=10, width=660, height=480)
        # -----------------------------------------------------

        # Class Attendee Information
        class_attendee_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Attendee Information",
                                          font=("verdana", 12, "bold"), fg="navyblue")
        class_attendee_frame.place(x=10, y=10, width=635, height=480)

        # id
        id_label = Label(class_attendee_frame, text="ID:", font=("verdana", 12, "bold"), fg="navyblue",
                         bg="white")
        id_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        id_entry = ttk.Entry(class_attendee_frame, textvariable=self.var_id, width=15,
                             font=("verdana", 12, "bold"))
        id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Attendee name
        attendee_name_label = Label(class_attendee_frame, text="Attendee-Name:", font=("verdana", 12, "bold"), fg="navyblue",
                                    bg="white")
        attendee_name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        attendee_name_entry = ttk.Entry(class_attendee_frame, textvariable=self.var_name, width=15,
                                        font=("verdana", 12, "bold"))
        attendee_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Gender
        attendee_gender_label = Label(class_attendee_frame, text="Gender:", font=("verdana", 12, "bold"), fg="navyblue",
                                      bg="white")
        attendee_gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        # combo box
        gender_combo = ttk.Combobox(class_attendee_frame, textvariable=self.var_gender, width=13,
                                    font=("verdana", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Date of Birth
        # Label for DOB
        attendee_dob_label = Label(class_attendee_frame, text="DOB:", font=("verdana", 12, "bold"), fg="navyblue",
                                   bg="white")
        attendee_dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        # DateEntry for selecting DOB
        attendee_dob_entry = DateEntry(class_attendee_frame, textvariable=self.var_dob, width=15,
                                       font=("verdana", 12, "bold"), date_pattern='yyyy-mm-dd')

        attendee_dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # Email
        attendee_email_label = Label(class_attendee_frame, text="Email:", font=("verdana", 12, "bold"), fg="navyblue",
                                     bg="white")
        attendee_email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        attendee_email_entry = ttk.Entry(class_attendee_frame, textvariable=self.var_email, width=15,
                                         font=("verdana", 12, "bold"))
        attendee_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone Number
        attendee_mob_label = Label(class_attendee_frame, text="Mob-No:", font=("verdana", 12, "bold"), fg="navyblue",
                                   bg="white")
        attendee_mob_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        attendee_mob_entry = ttk.Entry(class_attendee_frame, textvariable=self.var_mob, width=15,
                                       font=("verdana", 12, "bold"))
        attendee_mob_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        attendee_address_label = Label(class_attendee_frame, text="Address:", font=("verdana", 12, "bold"),
                                       fg="navyblue",
                                       bg="white")
        attendee_address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        attendee_address_entry = ttk.Entry(class_attendee_frame, textvariable=self.var_address, width=15,
                                           font=("verdana", 12, "bold"))
        attendee_address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)

        # save button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=7, font=("verdana", 12, "bold"),
                          fg="white", bg="navyblue")
        save_btn.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        # update button
        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=7, font=("verdana", 12, "bold"),
                            fg="white", bg="navyblue")
        update_btn.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        # delete button
        del_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=7, font=("verdana", 12, "bold"),
                         fg="white", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # reset button
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=7, font=("verdana", 12, "bold"),
                           fg="white", bg="navyblue")
        reset_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        # take photo button
        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take Pic", width=9,
                                font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        take_photo_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # update photo button
        update_photo_btn = Button(btn_frame, text="Update Pic", width=9, font=("verdana", 12, "bold"), fg="white",
                                  bg="navyblue")
        update_photo_btn.grid(row=0, column=5, padx=5, pady=10, sticky=W)

        # ----------------------------------------------------------------------
        # Right Label Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("verdana", 12, "bold"), fg="navyblue")
        right_frame.place(x=680, y=10, width=660, height=480)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame
        # Searching System in Right Label Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=90, width=635, height=360)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # create table
        self.attendee_table = ttk.Treeview(table_frame, column=(
            "ID", "Name", "Gender", "DOB", "Mob-No", "Address", "Email",
            "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendee_table.xview)
        scroll_y.config(command=self.attendee_table.yview)

        self.attendee_table.heading("ID", text="ID")
        self.attendee_table.heading("Name", text="Name")
        self.attendee_table.heading("Gender", text="Gender")
        self.attendee_table.heading("DOB", text="DOB")
        self.attendee_table.heading("Mob-No", text="Mob-No")
        self.attendee_table.heading("Address", text="Address")
        self.attendee_table.heading("Email", text="Email")
        self.attendee_table["show"] = "headings"

        # Set Width of Columns
        self.attendee_table.column("ID", width=100)
        self.attendee_table.column("Name", width=100)
        self.attendee_table.column("Gender", width=100)
        self.attendee_table.column("DOB", width=100)
        self.attendee_table.column("Mob-No", width=100)
        self.attendee_table.column("Address", width=100)
        self.attendee_table.column("Email", width=100)

        self.attendee_table.pack(fill=BOTH, expand=1)
        self.attendee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ==================Function Declaration==============================
    def add_data(self):
        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                # Validate that the DOB is not greater than the current date
                dob_str = self.var_dob.get()
                dob_datetime = datetime.strptime(dob_str, '%Y-%m-%d')
                if dob_datetime > datetime.now():
                    messagebox.showerror("Error", "Date of Birth cannot be in the future!", parent=self.root)
                    return

                # Validate email format using a regular expression
                email_str = self.var_email.get()
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, email_str):
                    messagebox.showerror("Error", "Invalid Email Format!", parent=self.root)
                    return

                # Validate mobile number using a regular expression (assuming 10-digit number)
                mob_str = self.var_mob.get()
                number_regex = r'^\d{10}$'
                if not re.match(number_regex, mob_str):
                    messagebox.showerror("Error", "Invalid Mobile Number! It must contain exactly 10 digits.",
                                         parent=self.root)
                    return

                conn = sqlite3.connect('face_recognition.db')
                cursor = conn.cursor()
                dob_str = self.var_dob.get()
                dob_datetime = datetime.strptime(dob_str, '%Y-%m-%d')
                cursor.execute("""INSERT INTO attendee VALUES (?, ?, ?, ?, ?, ?, ?)""", (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    dob_datetime,
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "All Records are Saved!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect('face_recognition.db')
            cursor = conn.cursor()

            # Execute the SQL query to fetch all records from the Attendee table
            cursor.execute("SELECT * FROM Attendee")
            data = cursor.fetchall()

            # Check if data was fetched
            if data:
                # Clear existing data in the Treeview widget
                self.attendee_table.delete(*self.attendee_table.get_children())
                # Insert each record into the Treeview widget
                for record in data:
                    self.attendee_table.insert("", "end", values=record)
            else:
                print("No data found in the database.")

            # Close the database connection
            conn.close()

        except sqlite3.Error as e:
            # Show an error message if something goes wrong
            messagebox.showerror("Database Error", f"An error occurred while fetching data: {e}", parent=self.root)

    # ================================get cursor function=======================

    def get_cursor(self, event=""):
        cursor_focus = self.attendee_table.focus()
        content = self.attendee_table.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_dob.set(data[3]),
        self.var_mob.set(data[4]),
        self.var_address.set(data[5]),
        self.var_email.set(data[6]),

    # ========================================Update Function==========================
    def update_data(self):
        pass

        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                # Validate that the DOB is not greater than the current date
                dob_str = self.var_dob.get()
                dob_datetime = datetime.strptime(dob_str, '%Y-%m-%d')
                if dob_datetime > datetime.now():
                    messagebox.showerror("Error", "Date of Birth cannot be in the future!", parent=self.root)
                    return

                # Validate email format using a regular expression
                email_str = self.var_email.get()
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if not re.match(email_regex, email_str):
                    messagebox.showerror("Error", "Invalid Email Format!", parent=self.root)
                    return

                # Validate mobile number using a regular expression (assuming 10-digit number)
                mob_str = self.var_mob.get()
                number_regex = r'^\d{10}$'
                if not re.match(number_regex, mob_str):
                    messagebox.showerror("Error", "Invalid Mobile Number! It must contain exactly 10 digits.",
                                         parent=self.root)
                    return
                Update = messagebox.askyesno("Update", "Do you want to Update this Atendee Details!", parent=self.root)
                if Update > 0:
                    conn = sqlite3.connect('face_recognition.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE attendee SET name = ?, gender = ?, dob = ?, mobile = ?, address = ?, email = ? WHERE id = ?",
                        (
                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_mob.get(),
                            self.var_address.get(),
                            self.var_email.get(),
                            self.var_id.get()
                        )
                    )

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ==============================Delete Function=========================================
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Id Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if delete:
                    conn = sqlite3.connect('face_recognition.db')
                    cursor = conn.cursor()
                    sql = "DELETE FROM attendee WHERE id = ?"
                    val = (self.var_id.get(),)
                    cursor.execute(sql, val)
                    conn.commit()
                    conn.close()

                    # Refresh the table to reflect changes
                    self.fetch_data()
                    image_deleted = False
                    for i in range(1, 101):  # Assuming there are 100 samples (1 to 100)
                        image_path = f"data_img/atendee.{self.var_id.get()}.{i}.jpg"
                        if os.path.exists(image_path):
                            os.remove(image_path)  # Delete the image file
                            print(f"Deleted image: {image_path}")
                            image_deleted = True

                    # Show info about images deleted
                    if image_deleted:
                        messagebox.showinfo("Images Deleted", "All associated images have been deleted.",
                                            parent=self.root)
                    else:
                        messagebox.showinfo("No Images Found", "No images were found to delete.", parent=self.root)

                    messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # Reset Function

    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_email.set(""),


    # =====================This part is related to Opencv Camera part=======================
    # ==================================Generate Data set take image=========================
    def generate_dataset(self):
        pass
        if self.var_id.get() == "" or self.var_name.get() == ""  or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" :
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:

                conn = sqlite3.connect('face_recognition.db')
                cursor = conn.cursor()
                cursor.execute("select * from attendee")
                result = cursor.fetchall()
                id = 0
                for x in result:
                    id += 1

                cursor.execute(
                    "UPDATE attendee SET name = ?, gender = ?, dob = ?, mobile = ?, address = ?, email = ? WHERE id = ?",
                    (
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_mob.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_id.get() == id+1
                    )
                )

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum naber 5
                    for (x, y, w, h) in faces:
                        face_croped = img[y:y + h, x:x + w]
                        return face_croped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data_img/atendee." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # main class object


if __name__ == "__main__":
    root = Tk()
    obj = Atendee(root)
    root.mainloop()
