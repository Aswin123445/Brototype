class error(Exception):
    def __init__(self,string):
        self.string=string
try:
    print("helo")
    raise error("error has occured")
except error as e:
    print(e.string)
