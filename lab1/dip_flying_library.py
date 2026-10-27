# DIP: warn when a flying book gets too close to the ground

class Alarm:
    # all alarms provide the same action.
    def warn(self, book):
        raise NotImplementedError


class BellAlarm(Alarm):
    def warn(self, book):
        print(f"Alarm! Book {book} is flying too low")


class LogAlarm(Alarm):
    def __init__(self):
        self.messages = []

    def warn(self, book):
        self.messages.append(f"Rescue book {book}")


class BookGuard:
    # the guard knows the Alarm interface, not a specific alarm.
    def __init__(self, alarm: Alarm):
        self.alarm = alarm

    def check(self, book, height):
        if height < 5:
            self.alarm.warn(book)


def main():
    books = [
        ("Atlas of Winds", 2),
        ("Dragon Handbook", 8),
    ]

    guard = BookGuard(BellAlarm())

    for book, height in books:
        guard.check(book, height)

    log = LogAlarm()
    BookGuard(log).check("Atlas of Winds", 2)
    print(f"Log: {log.messages}")


if __name__ == "__main__":
    main()
