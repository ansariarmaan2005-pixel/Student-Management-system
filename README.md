# Student-Management-system
A Student Management System developed using Python and MySQL to efficiently manage student records and information. This project allows users to add, update, delete, and view student details through a simple and user-friendly interface. It helps in organizing student data securely and backend development using Python with MySQL integration.
# 📚 Student Management System

A **command-line based Student Management System** built with **Python** and **MySQL**. Manage student records efficiently with features to add, view, search, update, delete, and generate reports.

---

## ✨ Features

- ✅ **Add Students** — Register new students with all details
- ✅ **View All Students** — Display all records in a formatted table with sorting options
- ✅ **Search Students** — Find students by name, roll number, course, or email
- ✅ **Update Student** — Edit any student information
- ✅ **Delete Student** — Remove student records (with confirmation)
- ✅ **Generate Reports** — View statistics, top performers, course-wise breakdown
- ✅ **Export to CSV** — Download all records as an Excel file

---

## 📋 What Information is Stored?

Each student record includes:
- **Roll Number** (unique ID)
- **Name** — Full name
- **Age** — Student's age
- **Gender** — Male / Female / Other
- **Email** — Email address (unique)
- **Phone** — Contact number
- **Course** — BCA, BBA, BSc, etc.
- **Semester** — Current semester (1-8)
- **Marks** — Total marks / CGPA
- **Address** — Residential address
- **Enrollment Date** — When student was added
- **Timestamps** — Auto-recorded

---

## 🛠️ Tech Stack

- **Language:** Python 3.7+
- **Database:** MySQL
- **Library:** mysql-connector-python

---

## 📦 Requirements

Before you start, you need:

1. **Python 3.7 or higher** — [Download Python](https://www.python.org/downloads/)
2. **MySQL Server** — [Download MySQL](https://dev.mysql.com/downloads/mysql/) or use [XAMPP](https://www.apachefriends.org/)
3. **mysql-connector-python** — Installed via pip (see installation steps)

---

## 🚀 Installation & Setup

### Step 1: Clone or Download

If on GitHub:
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

Or simply download the `student_management.py` file.

---

### Step 2: Install Python Package

Open Command Prompt / Terminal and run:

```bash
pip install mysql-connector-python
```

If that doesn't work, try:
```bash
pip3 install mysql-connector-python
```

---

### Step 3: Start MySQL Server

**If you have XAMPP (easiest):**
1. Open **XAMPP Control Panel**
2. Click **Start** next to **MySQL**

**If you have MySQL installed directly:**

**Windows:**
```bash
net start mysql
```

**Mac/Linux:**
```bash
brew services start mysql
```

Or use **Windows Services**:
- Press `Win + R` → type `services.msc` → find MySQL → right-click → **Start**

---

### Step 4: Update Database Credentials

Open `student_management.py` with a text editor (Notepad, VS Code, etc.)

Find this section (around line 20):

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",  # ← CHANGE THIS
    "database": "student_db"
}
```

**Replace `"your_password"` with:**

- **If using XAMPP:** Leave it as `""` (empty)
  ```python
  "password": "",
  ```

- **If using MySQL with password:** Use your MySQL root password
  ```python
  "password": "yourpassword123",
  ```

**Don't change anything else!** The database will be auto-created.

---

### Step 5: Run the Program

Open Command Prompt / Terminal in the same folder and run:

```bash
python student_management.py
```

Or:
```bash
python3 student_management.py
```

If successful, you'll see:
```
  Connecting to MySQL...
  ✔ Database connected & ready!

  ╔══════════════════════════════════════════════════════╗
  ║        STUDENT MANAGEMENT SYSTEM                     ║
  ╚══════════════════════════════════════════════════════╝
  
  📚  Main Menu
  
    1.  ➕  Add New Student
    2.  📋  View All Students
    3.  🔍  Search Student
    4.  ✏️   Update Student
    5.  🗑️   Delete Student
    6.  📊  Generate Report / Export CSV
    0.  🚪  Exit
```

**Great! You're ready to use it!** 🎉

---

## 📖 How to Use

### 1️⃣ Add New Student (Option 1)

```
Enter choice: 1

Roll Number (e.g. BCA2025001): BCA2025001
Full Name: Arman Ansari
Age: 21
Gender: 1) Male  2) Female  3) Other
Choice: 1
Email Address: arman@email.com
Phone Number: 9876543210
Course (e.g. BCA, BBA, BSc): BCA
Semester (1–8): 5
Total Marks / CGPA: 8.5
Address: Ballabgarh, Haryana

Save this student? (y/n): y
✔ Student 'Arman Ansari' added successfully!
```

---

### 2️⃣ View All Students (Option 2)

```
Enter choice: 2

Sort by: 1) Name  2) Roll No  3) Marks (High→Low)  4) Course
Choice (default=1): 1
```

Shows all students in a formatted table:
```
  ┌─────┬──────────┬──────────────────────┬─────┬────────┬──────────────────┬─────┬───────┐
  │ ID  │ Roll No  │ Name                 │ Age │ Gender │ Course           │ Sem │ Marks │
  ├─────┼──────────┼──────────────────────┼─────┼────────┼──────────────────┼─────┼───────┤
  │ 1   │ BCA2025  │ Arman Ansari         │ 21  │ Male   │ BCA              │ 5   │ 8.5   │
  └─────┴──────────┴──────────────────────┴─────┴────────┴──────────────────┴─────┴───────┘
  1 record(s) found.
```

---

### 3️⃣ Search Student (Option 3)

```
Enter choice: 3

Search by: 1) Name  2) Roll Number  3) Course  4) Email
Choice: 1
Enter name: Arman
```

Shows matching records.

---

### 4️⃣ Update Student (Option 4)

```
Enter choice: 4

Enter Roll Number to update: BCA2025001

What to update?
1) Name      2) Age       3) Email
4) Phone     5) Course    6) Semester
7) Marks     8) Address

Choice: 7
New Marks: 9.0
✔ Updated 'marks' for Arman Ansari.
```

---

### 5️⃣ Delete Student (Option 5)

```
Enter choice: 5

Enter Roll Number to delete: BCA2025001

⚠ You are about to DELETE: Arman Ansari (BCA2025001) — BCA Sem 5
Type 'DELETE' to confirm: DELETE
✔ Student 'Arman Ansari' deleted permanently.
```

---

### 6️⃣ Generate Report (Option 6)

```
Enter choice: 6

1) Summary Statistics
2) Top 10 Students (by Marks)
3) Students by Course
4) Export ALL to CSV

Choice: 1
```

**Summary Statistics:**
```
  ═══════════════════════════════════════════════════════
  SUMMARY STATISTICS
  ═══════════════════════════════════════════════════════
  Total Students   : 25
  Average Marks    : 7.85
  Highest Marks    : 9.5
  Lowest Marks     : 5.2
  Total Courses    : 3
  ═══════════════════════════════════════════════════════
```

**Export to CSV:**
```
✔ Exported 25 records to 'students_export_20250601_143022.csv'
```

Download the CSV file and open it in **Excel** or Google Sheets!

---

### 0️⃣ Exit (Option 0)

```
Enter choice: 0

Goodbye, Arman! 👋
```

---

## 🐛 Troubleshooting

### ❌ Error: "No module named 'mysql'"

**Fix:** Install the MySQL connector
```bash
pip install mysql-connector-python
```

---

### ❌ Error: "Cannot connect to MySQL localhost"

**Fix:** Make sure MySQL server is running

- **XAMPP:** Open XAMPP Control Panel → Click **Start** next to MySQL
- **Windows Services:** Press `Win + R` → `services.msc` → find MySQL → **Start**

---

### ❌ Error: "Access denied for user 'root'@'localhost'"

**Fix:** Update the password in `DB_CONFIG`

If using XAMPP:
```python
"password": "",  # Leave empty
```

If you set a password during MySQL setup:
```python
"password": "your_mysql_password",
```

---

### ❌ Error: "Duplicate entry for key 'roll_no'"

**Fix:** Each roll number must be unique. Use a different roll number when adding a student.

---

## 📁 Database Structure

The system automatically creates:

**Database:** `student_db`

**Table:** `students`

```
Column Name    | Type        | Description
───────────────┼─────────────┼──────────────────────────
id             | INT         | Primary key (auto-increment)
roll_no        | VARCHAR(20) | Unique roll number
name           | VARCHAR     | Student name
age            | INT         | Age
gender         | ENUM        | Male/Female/Other
email          | VARCHAR     | Email (unique)
phone          | VARCHAR     | Phone number
course         | VARCHAR     | Course name
semester       | INT         | Semester (1-8)
marks          | FLOAT       | Total marks / CGPA
address        | VARCHAR     | Address
enrolled_on    | DATE        | Enrollment date
created_at     | TIMESTAMP   | Record creation time
```

---

## 💡 Tips & Best Practices

1. **Use consistent roll number format:** e.g., `BCA2025001`, `BBA2024015`
2. **Backup your data:** Regularly export CSV files as backup
3. **Validate data:** Check marks are realistic (0-10 for CGPA or 0-100 for percentage)
4. **Use strong email addresses:** Helps with searching and communication
5. **Keep phone numbers consistent:** Use country codes if needed

---

## 📊 Example Data

To test the system, try adding these sample students:

| Roll No | Name | Age | Course | Sem | Marks |
|---------|------|-----|--------|-----|-------|
| BCA2025001 | Arman Ansari | 21 | BCA | 5 | 8.5 |
| BCA2025002 | Priya Singh | 20 | BCA | 5 | 9.2 |
| BBA2025001 | Rahul Kumar | 21 | BBA | 4 | 7.8 |
| BSC2025001 | Neha Patel | 19 | BSc | 3 | 8.9 |

---

## 🔒 Security Notes

This system is designed for **local/educational use**.

For production/online use:
- Use hashed passwords instead of plain text
- Implement user authentication
- Add input validation & SQL injection protection
- Use environment variables for DB credentials
- Consider encrypting sensitive data

---

## 📝 File Structure

```
student-management-system/
├── student_management.py   # Main application
├── README.md               # This file
└── students_export_*.csv   # Generated export files
```

---

## 🎓 Learning Concepts

This project demonstrates:
- ✅ Object-oriented programming concepts
- ✅ Database design & SQL queries
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ User input validation
- ✅ Error handling
- ✅ File I/O (CSV export)
- ✅ Terminal UI design

---

## 🚀 Future Enhancements

- [ ] Web interface with Flask/Django
- [ ] User authentication & login
- [ ] Grade system with automatic GPA calculation
- [ ] Attendance tracking
- [ ] Payment/fee management
- [ ] Email notifications
- [ ] Mobile app version
- [ ] Advanced analytics & charts

---

## 📄 License

This project is open source and free to use for educational purposes.

---

## 👨‍💻 Author

**Arman Ansari**
- 📧 Email: ansariarmaan2005@gmail.com
- 🔗 GitHub: https://github.com/ansariarmaan2005-pixel
- 💼 LinkedIn: https://www.linkedin.com/in/armanansari-tech
- 🎓 BCA Student | Aspiring Software & Web Developer

---

## 📞 Support

If you have issues:
1. Check the **Troubleshooting** section above
2. Make sure **MySQL is running**
3. Verify credentials in `DB_CONFIG`
4. Check that `mysql-connector-python` is installed

---

## ⭐ If you like this project, please give it a star on GitHub!

Happy learning! 🚀

---

**Last Updated:** June 2026  
**Version:** 1.0
