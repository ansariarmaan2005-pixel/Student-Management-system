"""
╔══════════════════════════════════════════════════════╗
║        STUDENT MANAGEMENT SYSTEM                     ║
║        Built with Python + MySQL                     ║
║        By: Arman Ansari                              ║
╚══════════════════════════════════════════════════════╝

Requirements:
    pip install mysql-connector-python

Setup:
    1. Make sure MySQL server is running
    2. Update DB_CONFIG below with your credentials
    3. Run: python student_management.py
"""

import mysql.connector
from mysql.connector import Error
import csv
import os
from datetime import datetime

# ─────────────────────────────────────────────
#  DATABASE CONFIGURATION  ← Update these!
# ─────────────────────────────────────────────
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # your MySQL username
    "password": "Arman_2005",  # your MySQL password
    "database": "student_db"
}

# ─────────────────────────────────────────────
#  COLORS FOR TERMINAL UI
# ─────────────────────────────────────────────
class Color:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"
    WHITE  = "\033[97m"
    DIM    = "\033[2m"

def success(msg): print(f"{Color.GREEN}  ✔  {msg}{Color.RESET}")
def error(msg):   print(f"{Color.RED}  ✘  {msg}{Color.RESET}")
def info(msg):    print(f"{Color.CYAN}  ℹ  {msg}{Color.RESET}")
def warn(msg):    print(f"{Color.YELLOW}  ⚠  {msg}{Color.RESET}")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(f"\n{Color.DIM}  Press Enter to continue...{Color.RESET}")

def divider(char="─", width=56):
    print(f"{Color.DIM}  {''.join([char]*width)}{Color.RESET}")

def header(title):
    clear()
    print()
    print(f"{Color.CYAN}{Color.BOLD}  ╔{'═'*54}╗")
    print(f"  ║{'STUDENT MANAGEMENT SYSTEM':^54}║")
    print(f"  ╚{'═'*54}╝{Color.RESET}")
    print(f"{Color.BOLD}  {title}{Color.RESET}")
    divider()
    print()

# ─────────────────────────────────────────────
#  DATABASE SETUP
# ─────────────────────────────────────────────
def get_connection(with_db=True):
    cfg = DB_CONFIG.copy()
    if not with_db:
        cfg.pop("database", None)
    return mysql.connector.connect(**cfg)

def setup_database():
    """Create database and tables if they don't exist."""
    try:
        conn = get_connection(with_db=False)
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        cur.execute(f"USE {DB_CONFIG['database']}")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                roll_no     VARCHAR(20)  UNIQUE NOT NULL,
                name        VARCHAR(100) NOT NULL,
                age         INT          NOT NULL,
                gender      ENUM('Male','Female','Other') NOT NULL,
                email       VARCHAR(100) UNIQUE NOT NULL,
                phone       VARCHAR(15),
                course      VARCHAR(100) NOT NULL,
                semester    INT          NOT NULL,
                marks       FLOAT        DEFAULT 0.0,
                address     VARCHAR(255),
                enrolled_on DATE         DEFAULT (CURDATE()),
                created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Error as e:
        error(f"Database setup failed: {e}")
        return False

# ─────────────────────────────────────────────
#  DISPLAY TABLE
# ─────────────────────────────────────────────
def print_table(rows):
    if not rows:
        warn("No records found.")
        return

    cols = ["ID", "Roll No", "Name", "Age", "Gender", "Course", "Sem", "Marks", "Email"]
    col_w = [4, 10, 22, 4, 8, 18, 4, 6, 28]

    def row_fmt(vals):
        parts = []
        for v, w in zip(vals, col_w):
            s = str(v)[:w]
            parts.append(s.ljust(w))
        return "  │ " + " │ ".join(parts) + " │"

    sep = "  ├" + "┼".join(["─"*(w+2) for w in col_w]) + "┤"
    top = "  ┌" + "┬".join(["─"*(w+2) for w in col_w]) + "┐"
    bot = "  └" + "┴".join(["─"*(w+2) for w in col_w]) + "┘"

    print(f"{Color.DIM}{top}{Color.RESET}")
    print(f"{Color.BOLD}{Color.CYAN}{row_fmt(cols)}{Color.RESET}")
    print(f"{Color.DIM}{sep}{Color.RESET}")
    for r in rows:
        vals = [r[0], r[1], r[2], r[3], r[4], r[6], r[7], f"{r[8]:.1f}", r[5]]
        print(row_fmt(vals))
    print(f"{Color.DIM}{bot}{Color.RESET}")
    print(f"{Color.DIM}  {len(rows)} record(s) found.{Color.RESET}")

# ─────────────────────────────────────────────
#  1. ADD STUDENT
# ─────────────────────────────────────────────
def add_student():
    header("➕  Add New Student")

    def inp(label, required=True):
        while True:
            val = input(f"  {Color.YELLOW}{label}{Color.RESET}: ").strip()
            if val or not required:
                return val
            warn("This field is required.")

    try:
        roll_no  = inp("Roll Number (e.g. BCA2025001)")
        name     = inp("Full Name")

        while True:
            try:
                age = int(inp("Age"))
                if 10 <= age <= 100: break
                warn("Enter a valid age (10–100).")
            except ValueError:
                warn("Age must be a number.")

        print(f"  {Color.YELLOW}Gender{Color.RESET}: 1) Male  2) Female  3) Other")
        gender_map = {"1": "Male", "2": "Female", "3": "Other"}
        while True:
            g = input("  Choice: ").strip()
            if g in gender_map: gender = gender_map[g]; break
            warn("Enter 1, 2, or 3.")

        email    = inp("Email Address")
        phone    = inp("Phone Number", required=False) or "N/A"
        course   = inp("Course (e.g. BCA, BBA, BSc)")

        while True:
            try:
                sem = int(inp("Semester (1–8)"))
                if 1 <= sem <= 8: break
                warn("Semester must be between 1 and 8.")
            except ValueError:
                warn("Enter a valid number.")

        while True:
            try:
                marks = float(inp("Total Marks / CGPA"))
                break
            except ValueError:
                warn("Enter a valid number.")

        address = inp("Address", required=False) or "N/A"

        print()
        info("Preview:")
        divider()
        print(f"  Name: {name} | Roll: {roll_no} | Course: {course} ({sem} sem)")
        print(f"  Email: {email} | Phone: {phone} | Marks: {marks}")
        divider()
        confirm = input(f"  {Color.YELLOW}Save this student? (y/n): {Color.RESET}").strip().lower()
        if confirm != "y":
            warn("Cancelled.")
            pause()
            return

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO students (roll_no, name, age, gender, email, phone, course, semester, marks, address)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (roll_no, name, age, gender, email, phone, course, sem, marks, address))
        conn.commit()
        cur.close(); conn.close()
        success(f"Student '{name}' added successfully!")

    except Error as e:
        if "Duplicate" in str(e):
            error("Roll number or email already exists!")
        else:
            error(f"Database error: {e}")

    pause()

# ─────────────────────────────────────────────
#  2. VIEW ALL STUDENTS
# ─────────────────────────────────────────────
def view_all_students():
    header("📋  All Students")

    print(f"  Sort by:  1) Name   2) Roll No   3) Marks (High→Low)   4) Course")
    choice = input("  Choice (default=1): ").strip()
    order_map = {"1": "name", "2": "roll_no", "3": "marks DESC", "4": "course"}
    order = order_map.get(choice, "name")

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT id,roll_no,name,age,gender,email,course,semester,marks,address FROM students ORDER BY {order}")
        rows = cur.fetchall()
        cur.close(); conn.close()
        print()
        print_table(rows)
    except Error as e:
        error(f"Error: {e}")

    pause()

# ─────────────────────────────────────────────
#  3. SEARCH STUDENT
# ─────────────────────────────────────────────
def search_student():
    header("🔍  Search Student")

    print("  Search by:  1) Name   2) Roll Number   3) Course   4) Email")
    choice = input("  Choice: ").strip()
    field_map = {"1": "name", "2": "roll_no", "3": "course", "4": "email"}

    if choice not in field_map:
        warn("Invalid choice."); pause(); return

    keyword = input(f"  Enter {field_map[choice]}: ").strip()
    if not keyword:
        warn("Search term cannot be empty."); pause(); return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT id,roll_no,name,age,gender,email,course,semester,marks,address
            FROM students WHERE {field_map[choice]} LIKE %s
        """, (f"%{keyword}%",))
        rows = cur.fetchall()
        cur.close(); conn.close()
        print()
        print_table(rows)
    except Error as e:
        error(f"Error: {e}")

    pause()

# ─────────────────────────────────────────────
#  4. UPDATE STUDENT
# ─────────────────────────────────────────────
def update_student():
    header("✏️   Update Student")

    roll = input("  Enter Roll Number to update: ").strip()
    if not roll:
        warn("Roll number required."); pause(); return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE roll_no = %s", (roll,))
        student = cur.fetchone()

        if not student:
            error(f"No student found with Roll No: {roll}")
            cur.close(); conn.close(); pause(); return

        print()
        info(f"Found: {student[2]} ({student[1]}) — {student[7]}, Sem {student[8]}")
        divider()
        print("  What to update?")
        print("  1) Name      2) Age       3) Email")
        print("  4) Phone     5) Course    6) Semester")
        print("  7) Marks     8) Address")
        print()

        field_map = {
            "1": ("name", "New Name"),
            "2": ("age", "New Age"),
            "3": ("email", "New Email"),
            "4": ("phone", "New Phone"),
            "5": ("course", "New Course"),
            "6": ("semester", "New Semester"),
            "7": ("marks", "New Marks"),
            "8": ("address", "New Address"),
        }

        choice = input("  Choice: ").strip()
        if choice not in field_map:
            warn("Invalid choice."); cur.close(); conn.close(); pause(); return

        col, label = field_map[choice]
        new_val = input(f"  {label}: ").strip()
        if not new_val:
            warn("Value cannot be empty."); cur.close(); conn.close(); pause(); return

        cur.execute(f"UPDATE students SET {col} = %s WHERE roll_no = %s", (new_val, roll))
        conn.commit()
        cur.close(); conn.close()
        success(f"Updated '{col}' for {student[2]}.")

    except Error as e:
        error(f"Error: {e}")

    pause()

# ─────────────────────────────────────────────
#  5. DELETE STUDENT
# ─────────────────────────────────────────────
def delete_student():
    header("🗑️   Delete Student")

    roll = input("  Enter Roll Number to delete: ").strip()
    if not roll:
        warn("Roll number required."); pause(); return

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, course, semester FROM students WHERE roll_no = %s", (roll,))
        student = cur.fetchone()

        if not student:
            error(f"No student found with Roll No: {roll}")
            cur.close(); conn.close(); pause(); return

        print()
        warn(f"You are about to DELETE: {student[1]} ({roll}) — {student[2]} Sem {student[3]}")
        confirm = input(f"  {Color.RED}Type 'DELETE' to confirm: {Color.RESET}").strip()

        if confirm == "DELETE":
            cur.execute("DELETE FROM students WHERE roll_no = %s", (roll,))
            conn.commit()
            success(f"Student '{student[1]}' deleted permanently.")
        else:
            info("Deletion cancelled.")

        cur.close(); conn.close()

    except Error as e:
        error(f"Error: {e}")

    pause()

# ─────────────────────────────────────────────
#  6. GENERATE REPORT / EXPORT
# ─────────────────────────────────────────────
def generate_report():
    header("📊  Generate Report / Export")

    print("  1) Summary Statistics")
    print("  2) Top 10 Students (by Marks)")
    print("  3) Students by Course")
    print("  4) Export ALL to CSV")
    print()
    choice = input("  Choice: ").strip()

    try:
        conn = get_connection()
        cur = conn.cursor()

        if choice == "1":
            cur.execute("""
                SELECT
                    COUNT(*)                          AS total,
                    AVG(marks)                        AS avg_marks,
                    MAX(marks)                        AS highest,
                    MIN(marks)                        AS lowest,
                    COUNT(DISTINCT course)            AS courses
                FROM students
            """)
            r = cur.fetchone()
            print()
            divider("═")
            print(f"  {Color.BOLD}SUMMARY STATISTICS{Color.RESET}")
            divider("═")
            print(f"  Total Students   : {Color.CYAN}{r[0]}{Color.RESET}")
            print(f"  Average Marks    : {Color.CYAN}{r[1]:.2f}{Color.RESET}" if r[1] else "  Average Marks    : N/A")
            print(f"  Highest Marks    : {Color.GREEN}{r[2]}{Color.RESET}")
            print(f"  Lowest Marks     : {Color.RED}{r[3]}{Color.RESET}")
            print(f"  Total Courses    : {Color.CYAN}{r[4]}{Color.RESET}")
            divider("═")

        elif choice == "2":
            cur.execute("""
                SELECT id,roll_no,name,age,gender,email,course,semester,marks,address
                FROM students ORDER BY marks DESC LIMIT 10
            """)
            rows = cur.fetchall()
            print()
            info("Top 10 Students by Marks:")
            print()
            print_table(rows)

        elif choice == "3":
            cur.execute("""
                SELECT course, COUNT(*) as total, AVG(marks) as avg_marks
                FROM students GROUP BY course ORDER BY total DESC
            """)
            rows = cur.fetchall()
            print()
            divider("═")
            print(f"  {Color.BOLD}{'Course':<30} {'Students':>10} {'Avg Marks':>12}{Color.RESET}")
            divider("─")
            for r in rows:
                print(f"  {r[0]:<30} {r[1]:>10} {r[2]:>12.1f}")
            divider("═")

        elif choice == "4":
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            if not rows:
                warn("No data to export.")
            else:
                filename = f"students_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                with open(filename, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["ID","Roll No","Name","Age","Gender","Email","Phone",
                                     "Course","Semester","Marks","Address","Enrolled On","Created At"])
                    writer.writerows(rows)
                success(f"Exported {len(rows)} records to '{filename}'")

        else:
            warn("Invalid choice.")

        cur.close(); conn.close()

    except Error as e:
        error(f"Error: {e}")

    pause()

# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────
def main_menu():
    while True:
        header("📚  Main Menu")
        print(f"  {Color.BOLD}1.{Color.RESET}  ➕  Add New Student")
        print(f"  {Color.BOLD}2.{Color.RESET}  📋  View All Students")
        print(f"  {Color.BOLD}3.{Color.RESET}  🔍  Search Student")
        print(f"  {Color.BOLD}4.{Color.RESET}  ✏️   Update Student")
        print(f"  {Color.BOLD}5.{Color.RESET}  🗑️   Delete Student")
        print(f"  {Color.BOLD}6.{Color.RESET}  📊  Generate Report / Export CSV")
        print(f"  {Color.BOLD}0.{Color.RESET}  🚪  Exit")
        print()

        choice = input(f"  {Color.YELLOW}Enter choice: {Color.RESET}").strip()

        if   choice == "1": add_student()
        elif choice == "2": view_all_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6": generate_report()
        elif choice == "0":
            clear()
            print(f"\n  {Color.GREEN}Goodbye, Arman! 👋{Color.RESET}\n")
            break
        else:
            warn("Invalid choice. Enter 0–6.")
            pause()

# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    clear()
    print(f"\n{Color.CYAN}{Color.BOLD}  Connecting to MySQL...{Color.RESET}")

    if setup_database():
        success("Database connected & ready!")
        import time; time.sleep(0.8)
        main_menu()
    else:
        print()
        error("Could not connect to MySQL. Please check:")
        print(f"  {Color.DIM}  1. MySQL server is running")
        print(f"       2. Credentials in DB_CONFIG are correct")
        print(f"       3. mysql-connector-python is installed:{Color.RESET}")
        print(f"  {Color.YELLOW}     pip install mysql-connector-python{Color.RESET}")
        print()
