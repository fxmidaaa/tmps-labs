# SRP: receive and display signals from distant moons
class SignalParser:
    # Parse one incoming line.
    def parse(self, line):
        moon, message = line.split(":", 1)
        return moon.strip(), message.strip()


class SignalArchive:
    # Store received signals.
    def __init__(self):
        self.signals = []

    def add(self, signal):
        self.signals.append(signal)


class SignalReport:
    # Display stored signals.
    def show(self, signals):
        print("Signals from space:")
        for moon, message in signals:
            print(f"{moon}: {message}")


def main():
    incoming = [
        "Io: volcano awakened",
        "Europa: ocean discovered",
    ]

    parser = SignalParser()
    archive = SignalArchive()
    for line in incoming:
        archive.add(parser.parse(line))

    SignalReport().show(archive.signals)


if __name__ == "__main__":
    main()
