import tkinter as tk
from tkinter import messagebox
import random
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("quiz_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER
)
""")
conn.commit()

# ---------------- QUESTIONS ----------------
questions_data = [
    {"q": "Capital of India?", "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"], "answer": "Delhi"},
    {"q": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"q": "AI language?", "options": ["Python", "HTML", "CSS", "C"], "answer": "Python"},
    {"q": "Sun is a?", "options": ["Planet", "Star", "Galaxy", "Moon"], "answer": "Star"},
    {"q": "Inventor of computer?", "options": ["Newton", "Einstein", "Charles Babbage", "Tesla"], "answer": "Charles Babbage"},
    {"q": "Fastest?", "options": ["Car", "Bike", "Plane", "Train"], "answer": "Plane"},
    {"q": "Water formula?", "options": ["H2O", "CO2", "O2", "NaCl"], "answer": "H2O"},
    {"q": "Largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"q": "HTML stands for?", "options": ["Hyper Text Markup Language", "High Tech Machine Language", "None", "Home Tool"], "answer": "Hyper Text Markup Language"},
    {"q": "CPU stands for?", "options": ["Central Processing Unit", "Computer Unit", "Central Print Unit", "None"], "answer": "Central Processing Unit"},
    {"q": "Programming language?", "options": ["Python", "Google", "Windows", "CPU"], "answer": "Python"},
    {"q": "Earth is?", "options": ["Star", "Planet", "Galaxy", "Asteroid"], "answer": "Planet"}
]

questions = random.sample(questions_data, 10)

current_q = 0
score = 0
student_name = ""

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Quiz Performance Analyzer")
root.geometry("520x450")
root.configure(bg="#1e1e2f")

# ---------------- FUNCTIONS ----------------

def start_quiz():
    global student_name
    student_name = name_entry.get().strip()

    if not student_name.isalpha():
        messagebox.showerror("Error", "Name must contain only alphabets!")
        return

    start_frame.pack_forget()
    quiz_frame.pack()
    show_question()

def show_question():
    q = questions[current_q]
    question_label.config(text=f"Q{current_q+1}. {q['q']}")

    for i, option in enumerate(q["options"]):
        options[i].config(text=option, value=option)

    var.set("")

def next_question():
    global current_q, score

    selected = var.get()

    if selected == "":
        messagebox.showwarning("Warning", "Select an option!")
        return

    if selected == questions[current_q]["answer"]:
        score += 1

    current_q += 1

    if current_q < 10:
        show_question()
    else:
        save_result()
        show_result()

def save_result():
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (student_name, score))
    conn.commit()

def show_result():
    quiz_frame.pack_forget()
    result_frame.pack()

    percentage = (score / 10) * 100

    if percentage >= 80:
        remark = "Excellent 🌟"
    elif percentage >= 50:
        remark = "Good 👍"
    else:
        remark = "Needs Improvement 📘"

    result_label.config(
        text=f"{student_name}\nScore: {score}/10\nPercentage: {percentage:.1f}%\n{remark}"
    )

# ----------- SHOW STATS -----------

def show_stats():
    cursor.execute("SELECT COUNT(*), AVG(score) FROM students")
    total, avg = cursor.fetchone()

    cursor.execute("SELECT name, score FROM students")
    data = cursor.fetchall()

    stats_text = f"Total Students: {total}\nAverage Score: {avg:.2f}\n\n--- Student Records ---\n"

    for name, sc in data:
        stats_text += f"{name} - {sc}/10\n"

    messagebox.showinfo("Quiz Statistics", stats_text)

# ---------------- START FRAME ----------------
start_frame = tk.Frame(root, bg="#1e1e2f")
start_frame.pack(pady=80)

tk.Label(start_frame, text="QUIZ PERFORMANCE ANALYZER",
         fg="white", bg="#1e1e2f", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(start_frame, text="Enter Name",
         fg="white", bg="#1e1e2f").pack()

name_entry = tk.Entry(start_frame, font=("Arial", 14))
name_entry.pack(pady=10)

tk.Button(start_frame, text="Start Quiz", command=start_quiz,
          bg="#4CAF50", fg="white").pack(pady=10)

tk.Button(start_frame, text="View Statistics", command=show_stats,
          bg="#FF9800", fg="white").pack(pady=10)

# ---------------- QUIZ FRAME ----------------
quiz_frame = tk.Frame(root, bg="#1e1e2f")

question_label = tk.Label(quiz_frame, fg="white", bg="#1e1e2f",
                          wraplength=450, font=("Arial", 14))
question_label.pack(pady=20)

var = tk.StringVar()

options = []
for i in range(4):
    rb = tk.Radiobutton(quiz_frame, variable=var, fg="white",
                        bg="#1e1e2f", font=("Arial", 12),
                        selectcolor="#333")
    rb.pack(anchor="w", padx=60)
    options.append(rb)

tk.Button(quiz_frame, text="Next", command=next_question,
          bg="#2196F3", fg="white").pack(pady=20)

# ---------------- RESULT FRAME ----------------
result_frame = tk.Frame(root, bg="#1e1e2f")

result_label = tk.Label(result_frame, fg="white",
                        bg="#1e1e2f", font=("Arial", 16))
result_label.pack(pady=40)

tk.Button(result_frame, text="Exit", command=root.quit,
          bg="red", fg="white").pack()

# Run app
root.mainloop()