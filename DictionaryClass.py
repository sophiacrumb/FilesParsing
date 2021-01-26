class NewDictionary(dict):
    def __init__(self):
        super().__init__()

    def add(self, key, value):
        self[key] = value
