#! /mnt/c/Users/josep/AppData/Local/Continuum/anaconda3/python.exe

def first(rise, fall):
    def second(data):
        print(rise + ':' + data + ":" + fall)
    return second

third = first("water", "stone")
the = third("grinds")
print(the)
print(third("grinds"))
