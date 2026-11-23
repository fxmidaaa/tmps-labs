from abc import ABC, abstractmethod
from dataclasses import dataclass


class BulletinEntry(ABC):
    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError


@dataclass(frozen=True)
class SignalEntry(BulletinEntry):
    moon: str
    message: str

    def render(self) -> str:
        return f"{self.moon}: {self.message}"


@dataclass(frozen=True)
class Bulletin:
    title: str
    entries: tuple[BulletinEntry, ...]
    footer: str

    def render(self) -> str:
        lines = [self.title]
        for entry in self.entries:
            lines.append(entry.render())
        lines.append(self.footer)
        return "\n".join(lines)
