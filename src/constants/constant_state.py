constant_state = list([
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
    {
        "name": "your field players",
        "row": 10,
        "cols": 12,
    },
    {
        "name": "your keeper",
        "rows": 1,
        "cols": 12
    }
])


class ConstantState:
    @staticmethod
    def row(index: int = 0):
        if index >= ConstantState.length():
            raise IndexError("Error")
        return constant_state[index]["row"]

    @staticmethod
    def length():
        return len(constant_state)

    @staticmethod
    def col(index: int = 0):
        if index >= ConstantState.length():
            raise IndexError("Error")
        return constant_state[index]["col"]

    @staticmethod
    def name(index: int = 0):
        if index >= ConstantState.length():
            raise IndexError("Error")
        return constant_state[index]["name"]
