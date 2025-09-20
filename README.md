### **Procedure to Run the Application**

#### **Setup Instructions**
1. Clone the Repository (if applicable):
```
git clone <repository-url>
cd face-recognition-attendance-system
```

## Face Recognition Attendance System 

---
## 🎯 **Project Scope & Objectives**

### **Primary Goal**
Development of an automated attendance management system utilizing advanced computer vision and machine learning technologies to eliminate manual attendance tracking inefficiencies and provide accurate, real-time attendance monitoring.

### **Academic Significance**
This project demonstrates practical application of theoretical computer science concepts including:
- **Computer Vision Algorithms** (Haar Cascades, LBPH)
- **Machine Learning Implementation** (Supervised Learning, Pattern Recognition)
- **Software Engineering Principles** (Modular Design, Database Integration)
- **Human-Computer Interaction** (Professional GUI Development)

---
2. Create Virtual Environment (Recommended):

```
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate

```
3. Install Dependencies:

```pip install -r requirements.txt```
4.Start the Application:

```python admin.py```

Requirements.txt Contents
```
opencv-python==4.8.1.78
numpy==1.24.3
pillow==10.0.1
tkinter
sqlite3
openpyxl==3.1.2
scikit-learn==1.3.0
```

#### **Usage Flow**

Administrator Mode: Register new users and generate training datasets
Attendance Mode: Real-time face recognition and logging
Report Generation: Export attendance data to Excel format

#### **performance metric**
Confidence: 87% under stable lighting condition
