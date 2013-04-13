import json

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for line in data:
            mapper(self, line)

        for key in self.intermediate:
            reducer(self, key, self.intermediate[key])

        jenc = json.JSONEncoder(encoding='latin-1')
        for item in self.result:
            print jenc.encode(item)

def execute(data, mapper, reducer):
    mr = MapReduce()
    mr.execute(data, mapper, reducer)
