# Builder: assemble a bulletin one part at a time.
from srp_signal_archive import SignalArchive, SignalParser


class Bulletin:
    def __init__(self, title, entries, footer):
        self.title = title
        self.entries = entries
        self.footer = footer

    def show(self):
        print(self.title)
        for entry in self.entries:
            print(entry)
        print(self.footer)


class BulletinBuilder:
    def __init__(self):
        self.title = "Untitled bulletin"
        self.entries = []
        self.footer = "End of bulletin"

    def set_title(self, title):
        self.title = title
        return self

    def add_signal(self, signal):
        moon, message = signal
        self.entries.append(f"{moon}: {message}")
        return self

    def set_footer(self, footer):
        self.footer = footer
        return self

    def build(self):
        return Bulletin(self.title, self.entries.copy(), self.footer)


def main():
    parser = SignalParser()
    archive = SignalArchive()
    archive.add(parser.parse("Io: volcano awakened"))
    archive.add(parser.parse("Europa: ocean discovered"))

    builder = BulletinBuilder().set_title("Moon Watch")
    for signal in archive.signals:
        builder.add_signal(signal)
    bulletin = builder.set_footer("Report complete").build()
    bulletin.show()


if __name__ == "__main__":
    main()
