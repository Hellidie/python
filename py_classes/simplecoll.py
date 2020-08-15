from collections import namedtuple


Car = namedtuple('Car', ['color','brand'])


class Garage:
    def __init__(self):
        self._cars = [
                Car(color='brown', brand='Porsche'),
                Car(color='black', brand='BMW'),
                Car(color='silver', brand='Mercedes')
        ]

    def __len__(self):
        return len(self._cars)

    def __getitem__(self, position):
        return self._cars[position]
