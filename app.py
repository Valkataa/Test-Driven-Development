class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class App:
    def __init__(self):
        self.users = {}
        self.tasks = {}

    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists")
        user = User(username, password)
        self.users[username] = user

    def login(self, username, password):
        if username not in self.users:
            raise ValueError("User does not exist")
        user = self.users[username]
        if user.password != password:
            raise ValueError("Incorrect password")
        return user

    def create_task(self, user, title, description):
        task = Task(title, description)
        if user.username not in self.tasks:
            self.tasks[user.username] = []
        self.tasks[user.username].append(task)

    def get_user_tasks(self, user):
        if user.username not in self.tasks:
            return []
        return self.tasks[user.username]
