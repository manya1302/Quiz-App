# models.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.scores = {}

    def add_score(self, quiz_topic, score):
        self.scores[quiz_topic] = score

class Quiz:
    def __init__(self):
        self.questions = {
            "DBMS": [
                {"question": "What does DBMS stand for?", "options": ["Database Management System", "Data Mining System", "Database Maintenance System", "Data Management Software"], "answer": "Database Management System"},
                {"question": "Which of these is a database management system?", "options": ["Oracle", "Linux", "Python", "HTML"], "answer": "Oracle"},
                {"question": "SQL stands for?", "options": ["Structured Query Language", "Stylish Question Language", "Statement Query Language", "Standard Query Language"], "answer": "Structured Query Language"},
                {"question": "Which SQL command is used to remove a table?", "options": ["DELETE", "DROP", "REMOVE", "ERASE"], "answer": "DROP"},
                {"question": "A primary key can contain null values.", "options": ["True", "False"], "answer": "False"}
            ],
            "DSA": [
                {"question": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "LinkedList", "Array"], "answer": "Stack"},
                {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "answer": "O(log n)"},
                {"question": "In which data structure, elements are added and removed from only one end?", "options": ["Stack", "Queue", "Deque", "Array"], "answer": "Stack"},
                {"question": "Which of the following is a non-linear data structure?", "options": ["Array", "LinkedList", "Queue", "Tree"], "answer": "Tree"},
                {"question": "DFS stands for?", "options": ["Depth First Search", "Depth First Sort", "Data First Search", "Data First Sort"], "answer": "Depth First Search"}
            ],
            "Python": [
                {"question": "Who developed Python programming language?", "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"], "answer": "Guido van Rossum"},
                {"question": "Which keyword is used to define a function in Python?", "options": ["def", "function", "func", "define"], "answer": "def"},
                {"question": "What is the output of 3**2 in Python?", "options": ["6", "9", "3", "12"], "answer": "9"},
                {"question": "Which of the following is not a keyword in Python?", "options": ["pass", "eval", "assert", "nonlocal"], "answer": "eval"},
                {"question": "Python is a ____.", "options": ["Compiled language", "Interpreted language", "Both compiled and interpreted", "None of the above"], "answer": "Interpreted language"}
            ]
        }

    def get_questions(self, topic):
        return self.questions.get(topic, [])
