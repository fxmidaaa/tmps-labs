from collections.abc import Callable, Iterable

from ..domain.bulletin import BulletinEntry
from .builder import BulletinBuilder


class BulletinPublisher:
    def __init__(self, output: Callable[[str], None] = print):
        self._output = output

    def publish(self, title: str, entries: Iterable[BulletinEntry], footer: str) -> None:
        builder = BulletinBuilder().set_title(title)
        for entry in entries:
            builder.add_entry(entry)
        bulletin = builder.set_footer(footer).build()
        self._output(bulletin.render())
