import time

class TrafficLight:

    _color = None
    _colors = {'Red': 7, 'Yellow': 2, 'Green': 5}

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        while True:
            for key, value in TrafficLight._colors.items():
                print(key)
                time.sleep(value)

lenina = TrafficLight()
lenina.running()

