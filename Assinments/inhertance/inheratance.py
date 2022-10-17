class man:
    def __init__(self) :
        print("in part of man")
    def work(self):
        print("work outside from home")
    def ficnic(self):
        print("with yaraan in Arghandab")

class woman(man):
    def __init__(self):
        super().__init__()
        print("in part of woman")
    def work(self):
        print("work inside from home")
    def ficnic(self):
        print("go to onther house")

defer=woman()
defer.work()
defer.ficnic()
    