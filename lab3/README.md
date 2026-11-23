# Lab 3 — Structural Design Patterns

Moon Watch is a console app that publishes a bulletin of signals from Jupiter's moons. A bulletin can contain individual signals, nested sections, and entries with urgency or source labels.

## Build and run

Use Python 3.9 or newer. The app uses the standard library and runs directly from source. Run these commands from the repository root.

```bash
python3 -m lab3.app
```

The demo prints this bulletin.

```text
Moon Watch
Jupiter system
  Alerts
    [URGENT] Io: Volcano awakened [source: Orbiter 7]
  Europa: Ocean discovered
Report complete
```

## Project structure

| Location | Contents |
| --- | --- |
| [domain/](domain/) | `BulletinEntry` interface, individual signals, and the finished bulletin. |
| [patterns/](patterns/) | Composite, Decorator, Facade, and the Builder adapted from [Lab 2](../lab2/builder_signal_bulletin.py). |
| [app/](app/) | A console demo that uses all three structural patterns together. |
| [tests/](tests/) | Unit tests for each pattern and a test for the complete demo. |

## How the patterns work together

| Pattern | Where it appears |
| --- | --- |
| Composite | [`SignalSection`](patterns/composite.py) holds objects that implement `BulletinEntry`. It renders a single signal and a nested section through the same `render()` method. |
| Decorator | [`UrgentEntry` and `SourceTaggedEntry`](patterns/decorator.py) wrap a `BulletinEntry` and add labels. They can wrap an individual signal, a section, or another decorator. |
| Facade | [`BulletinPublisher.publish()`](patterns/facade.py) calls the Builder, renders the finished bulletin, and sends it to the configured output in one call. |

The demo puts a signal wrapped by both decorators inside `Alerts`, then nests that section under `Jupiter system`. A call to `publish()` renders the section tree and prints the resulting bulletin. To add a label such as `[VERIFIED]`, define an `EntryDecorator` subclass with its own `_decorate_heading()` method and wrap an entry with it in the demo.

## Run tests

```bash
python3 -m unittest discover -s lab3/tests -v
```

The eight tests cover nested sections, stacking decorators in either order, the publication sequence, independence between bulletins, and the complete console output.
