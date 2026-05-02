# 📊 Quiz Performance Analyzer

A GUI-based Quiz Application built with Python that tracks student scores, calculates performance, and stores results in a database. Built as part of my Computer Engineering Diploma project.

---

## 👩‍💻 About the Project

The **Quiz Performance Analyzer** is a fully interactive desktop application where students can take a quiz and instantly see their performance results. All scores are saved in a local database so statistics can be viewed anytime.

---

## ✨ Features

- 🖥️ **Graphical User Interface (GUI)** built with Tkinter
- ❓ **10 Random Questions** selected from a question bank of 12
- 📊 **Score & Percentage Calculation** after quiz completion
- 🏅 **Performance Remarks** — Excellent 🌟 / Good 👍 / Needs Improvement 📘
- 🗄️ **SQLite Database** — stores every student's name and score
- 📈 **Statistics Panel** — view total students tested and average score
- ✅ Input validation — only alphabetic names accepted

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| Tkinter | GUI (Graphical User Interface) |
| SQLite3 | Local database to store scores |
| Random | Random question selection |

---

## ▶️ How to Run

**1. Make sure Python is installed:**
```bash
python --version
```

**2. Clone this repository:**
```bash
git clone https://github.com/Kavya1234-thaker/quiz-performance-analyzer.git
cd quiz-performance-analyzer
```

**3. Run the program:**
```bash
python "Quiz sore analyzer.py"
```

> ✅ No extra libraries needed — all modules (Tkinter, SQLite3) come built-in with Python!

---

## 📸 How it Works

**Step 1 — Enter your name and click Start Quiz**
```
┌─────────────────────────────┐
│   QUIZ PERFORMANCE ANALYZER │
│                             │
│   Enter Name: [Kavya      ] │
│   [ Start Quiz ]            │
│   [ View Statistics ]       │
└─────────────────────────────┘
```

**Step 2 — Answer 10 random questions**
```
Q1. Capital of India?
  ○ Mumbai
  ● Delhi
  ○ Kolkata
  ○ Chennai

[ Next ]
```

**Step 3 — See your result instantly**
```
Kavya
Score      : 8/10
Percentage : 80.0%
Excellent 🌟
```

**Step 4 — View Statistics of all students**
```
Total Students : 5
Average Score  : 7.40

--- Student Records ---
Kavya  - 8/10
Priya  - 6/10
...
```

---

## 📚 What I Learned

- Building GUI applications using Python Tkinter
- Connecting Python with SQLite database
- Storing and retrieving data across multiple sessions
- Input validation and error handling
- Calculating statistics (average, percentage) programmatically

---

## 👤 Author

**Kavya Sandeep Thaker**
- 🎓 Diploma in Computer Engineering — Shri Bhagubhai Mafatlal Polytechnic (SBMP), Mumbai
- 🔗 [LinkedIn](https://www.linkedin.com/in/kavya-thaker-6b9b31332/)
- 🐙 [GitHub](https://github.com/Kavya1234-thaker)

---

## 📄 License

This project is open source and free to use for learning purposes.
