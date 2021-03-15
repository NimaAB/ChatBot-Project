class Person:
    def __init__(self, name=None, address=None, connection=None):
        self.name = name
        self.address = address
        self.connection = connection

    def __str__(self):
        return f"{{\n " \
               f"\t\"sender\" : \"{self.name}\",\n" \
               f"\t\"address\" : \"{self.address}\",\n" \
               f"\t\"connection\" : \"{self.connection}\"\n" \
               f"}}"
