from abc import abstractmethod

from ..domain.bulletin import BulletinEntry


class EntryDecorator(BulletinEntry):
    def __init__(self, entry: BulletinEntry):
        self._entry = entry

    def render(self) -> str:
        heading, newline, body = self._entry.render().partition("\n")
        return f"{self._decorate_heading(heading)}{newline}{body}"

    @abstractmethod
    def _decorate_heading(self, heading: str) -> str:
        raise NotImplementedError


class UrgentEntry(EntryDecorator):
    def _decorate_heading(self, heading: str) -> str:
        return f"[URGENT] {heading}"


class SourceTaggedEntry(EntryDecorator):
    def __init__(self, entry: BulletinEntry, source: str):
        super().__init__(entry)
        self._source = source

    def _decorate_heading(self, heading: str) -> str:
        return f"{heading} [source: {self._source}]"
