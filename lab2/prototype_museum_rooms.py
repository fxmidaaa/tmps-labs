# Prototype: copy a room template to create a similar room.
from copy import copy

from ocp_strange_expedition import MuseumTour, Room


class EnergyRoom(Room):
    def __init__(self, name, energy_change):
        self.name = name
        self.energy_change = energy_change

    def clone(self):
        # A shallow copy is enough because both fields are simple values.
        return copy(self)

    def enter(self, energy):
        print(f"{self.name}: {self.energy_change:+} energy")
        return energy + self.energy_change


def main():
    template = EnergyRoom("Quiet Cave", -1)

    mirror_cave = template.clone()
    mirror_cave.name = "Mirror Cave"
    mirror_cave.energy_change = -2

    healing_cave = template.clone()
    healing_cave.name = "Healing Cave"
    healing_cave.energy_change = 3

    MuseumTour().run([template, mirror_cave, healing_cave])


if __name__ == "__main__":
    main()
