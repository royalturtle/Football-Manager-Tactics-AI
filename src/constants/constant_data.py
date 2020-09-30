constant_data = list([
    {
        "name": "my field players",
        "row": 10,
        "cols": 12,
    },
    {
        "name": "my keeper",
        "rows": 1,
        "cols": 12
    },
])


class ConstantData:
    @staticmethod
    def row(index: int = 0):
        if index >= ConstantData.length():
            raise IndexError("Error")
        return constant_data[index]["row"]

    @staticmethod
    def length():
        return len(constant_data)

    @staticmethod
    def col(index: int = 0):
        if index >= ConstantData.length():
            raise IndexError("Error")
        return constant_data[index]["col"]

    @staticmethod
    def name(index: int = 0):
        if index >= ConstantData.length():
            raise IndexError("Error")
        return constant_data[index]["name"]
