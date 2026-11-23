from ..domain.bulletin import SignalEntry
from ..patterns.composite import SignalSection
from ..patterns.decorator import SourceTaggedEntry, UrgentEntry
from ..patterns.facade import BulletinPublisher


def main():
    io = UrgentEntry(SourceTaggedEntry(SignalEntry("Io", "Volcano awakened"), "Orbiter 7"))
    europa = SignalEntry("Europa", "Ocean discovered")
    alerts = SignalSection("Alerts", [io])
    jupiter = SignalSection("Jupiter system", [alerts, europa])

    BulletinPublisher().publish("Moon Watch", [jupiter], "Report complete")


if __name__ == "__main__":
    main()
