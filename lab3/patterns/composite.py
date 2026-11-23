from collections.abc import Iterable
from textwrap import indent

from ..domain.bulletin import BulletinEntry


class SignalSection(BulletinEntry):
    def __init__(self, title: str, entries: Iterable[BulletinEntry]):
        self._title = title
        self._entries = tuple(entries)

    def render(self) -> str:
        lines = [self._title]
        for entry in self._entries:
            lines.append(indent(entry.render(), "  "))
        return "\n".join(lines)
