class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = password
        self.age = int(age)


class Video:
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration):
        self.title = str(title)
        self.duration = int(duration)


class UrTube:
    current_user = None
    def __init__(self, users, videos):
        self.users = {}
        self.videos = {}

        def add_user(self, nickname, password):
            self.users[nickname]: password

        def add_video(self, title, duration):
            self.videos[title]: duration

    def log_in (self, login, password):
        if login in UrTube.users:
            if password == UrTube.users[login]:




