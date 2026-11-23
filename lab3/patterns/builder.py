from ..domain.bulletin import Bulletin, BulletinEntry


class BulletinBuilder:
    """Adapt the Lab 2 Builder to store objects that can render themselves."""

    def __init__(self):
        self._title = "Untitled bulletin"
        self._entries: list[BulletinEntry] = []
        self._footer = "End of bulletin"

    def set_title(self, title: str):
        self._title = title
        return self

    def add_entry(self, entry: BulletinEntry):
        self._entries.append(entry)
        return self

    def set_footer(self, footer: str):
        self._footer = footer
        return self

    def build(self) -> Bulletin:
        return Bulletin(self._title, tuple(self._entries), self._footer)
