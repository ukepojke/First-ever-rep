class Lenovo:
    def __init__(self, processor, ram, gpu, hdd, motherboard, display):
        self.processor = processor
        self.ram = ram
        self.gpu = gpu
        self.hdd = hdd
        self.motherboard = motherboard
        self.display = display

    def settings(self):
        return {"lenovo":{"processor": self.processor,"ram": self.ram,"gpu": self.gpu,"hdd": self.hdd,"motherboad": self.motherboard,"display": self.display}}

lap = Lenovo(processor="intel",ram=8,gpu="amd",hdd=500,motherboard="hyperx",display="720p")
Data1 = lap.settings()

class dict_lol:
    def __init__(self,dict):
        self.dict = dict

    def tup(self):
        return tuple(dict)

a = dict_lol(Data1)
b = a.dict

print(b)