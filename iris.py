class Iris:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    flower_type: str

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, flower_type):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.flower_type = flower_type
