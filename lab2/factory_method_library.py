# Factory Method: each station decides which alarm to create.
from dip_flying_library import BellAlarm, BookGuard, LogAlarm


class LibraryStation:
    def create_alarm(self):
        raise NotImplementedError

    def check_books(self, books):
        alarm = self.create_alarm()
        guard = BookGuard(alarm)
        for book, height in books:
            guard.check(book, height)
        return alarm


class NoisyStation(LibraryStation):
    def create_alarm(self):
        return BellAlarm()


class QuietStation(LibraryStation):
    def create_alarm(self):
        return LogAlarm()


def main():
    books = [("Atlas of Winds", 2), ("Dragon Handbook", 8)]

    print("Noisy station:")
    NoisyStation().check_books(books)

    print("Quiet station:")
    alarm = QuietStation().check_books(books)
    print(f"Log: {alarm.messages}")


if __name__ == "__main__":
    main()
