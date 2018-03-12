from app import app

class library:
    def __init__(self):
        self.words = ["hello", "word"]

    def put(self, word):
        if type(word) is str:
            self.words.append(word)
        else:
            return

    def get(self):
        return str(self.words)
