from tkinter import Tk, messagebox

import openpyxl
from openpyxl import Workbook
from datetime import datetime
import os


class AttendanceMarker:
    def __init__(self, excel_file="attendance.xlsx"):
        # Initialize the excel file path
        self.excel_file = excel_file
        # Check if the excel file exists, create it if not
        if not os.path.exists(self.excel_file):
            self.create_excel_file()

    def create_excel_file(self):
        # Create a new Excel workbook and worksheet with headers
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Attendance"
        sheet.append(["ID", "Name", "Date", "Time"])
        workbook.save(self.excel_file)

    def mark_attendance(self, i, n):
        workbook = openpyxl.load_workbook(self.excel_file)
        sheet = workbook.active
        current_date = datetime.now().strftime("%d/%m/%Y")

        for row in sheet.iter_rows(values_only=True):
            if row[0] == i and row[2] == current_date:
                # Attendance is already marked for this ID today
                messagebox.showerror(f"Attendance already marked for {n} (ID: {i})")
                return

        current_time = datetime.now().strftime("%H:%M:%S")
        sheet.append([i, n, current_date, current_time])
        workbook.save(self.excel_file)
        messagebox.showerror(f"Attendance marked for {n} (ID: {i}) on {current_date} at {current_time}")

if __name__ == "__main__":
    root=Tk()
    obj=AttendanceMarker(root)
    root.mainloop()