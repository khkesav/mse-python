class Singleton:
    _instance = None  # Class attribute to hold the single instance

    def __new__(cls, *args):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        pass


s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

print(id(s1), id(s2), id(s3)) 
