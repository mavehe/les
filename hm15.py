# 1
class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date
    def show(self):
        print(self.get_info())
    def get_info(self):
        return f"{self.title} — {self.date}"
# 2
class Training(Event):
    def __init__(self, title, date, trainer):
        super().__init__(title, date)
        self.trainer = trainer
    def show(self):
        print(self.get_info())
    def get_info(self):
        return f"Training: {self.title} — {self.date}, Trainer: {self.trainer}"
class Birthday(Event):
    def __init__(self, title, date, person):
        super().__init__(title, date)
        self.person = person
    def show(self):
        print(self.get_info())
    def get_info(self):
        return f"Birthday: {self.title} — {self.date}, Person: {self.person}"
# 5
class OnlineEvent(Event):
    def __init__(self, title, date, link):
        super().__init__(title, date)
        self.link = link
    def show(self):
        print(self.get_info())
    def get_info(self):
        return f"Online: {self.title} — {self.date}, Link: {self.link}"
# 3
events = [
    Event("Meeting", "10.04.2026"),
    Training("Python lesson", "11.09.2026", "Teacher"),
    Birthday("Party", "12.04.2026", "Friend"),
    OnlineEvent("Online lesson", "13.06.2026", "Zoom")
]
# 4
for event in events:
    event.show()
