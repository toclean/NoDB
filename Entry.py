import uuid

class Entry:
    def __init__(self, fields):
        self.identifier = uuid.uuid1()
        self.fields = fields
    def addField(self, field):
        self.fields.append(field)

class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value