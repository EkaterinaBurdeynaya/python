class Road:

    _length = None
    _width = None


    def __init__(self):
        self.length = int(input('please input the length of the road - '))
        self.width = int(input('please input the width of the road - '))
        print(f'Road is created')

    def mass(self):
        self.weight = 25
        self.thickness = 0.05
        print(f'Mass of asphalt is {self.length* self.width * self.weight * self.thickness}')

lenina = Road()
lenina.mass()
