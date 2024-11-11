from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import cv2
from attendance import AttendanceMarker



class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1290x768+0+0")
        self.root.title("Face Recognition Panel")

        # This part is image labels setting start
        # first header image
        img = Image.open(r"Images_GUI\banner.png")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"), bg="white",
                          fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)


    # ================face recognition==================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in featuers:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = sqlite3.connect('face_recognition.db')
                cursor = conn.cursor()

                # Execute the query to fetch the name
                cursor.execute("SELECT name FROM Attendee WHERE id=?", (id,))
                n = cursor.fetchone()

                # If there's a result, join the tuple into a string
                if n:
                    n = "+".join(n)
                else:
                    n = None

                # Execute the query to fetch the id
                cursor.execute("SELECT id FROM Attendee WHERE id=?", (id,))
                i = cursor.fetchone()
                i_str = [str(x) for x in i]

                # If there's a result, join the tuple into a string
                if i:
                    i = "+".join(i_str)
                else:
                    i = None

                # Close the database connection
                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"id:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    attendance = AttendanceMarker()
                    attendance.mark_attendance(i,n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.getWindowProperty("Face Detector", cv2.WND_PROP_VISIBLE) < 1 or cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()