# OCP: walk through the rooms of an unusual museum
class Room:
    # Every new room implements this method.
    def enter(self, energy):
        raise NotImplementedError


class WhisperingRoom(Room):
    def enter(self, energy):
        print("Whispering Room: -2 energy")
        return energy - 2


class MagicSpring(Room):
    def enter(self, energy):
        print("Magic Spring: +3 energy")
        return energy + 3


class MuseumTour:
    # the tour works with any Room without checking its type.
    def run(self, rooms):
        energy = 5
        print(f"Starting energy: {energy}")
        for room in rooms:
            energy = room.enter(energy)
        print(f"Final energy: {energy}")


def main():
    rooms = [WhisperingRoom(), MagicSpring()]
    MuseumTour().run(rooms)


if __name__ == "__main__":
    main()
