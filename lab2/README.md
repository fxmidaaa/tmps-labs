# Lab 2: Creational Design Patterns

This document explains the three creational patterns added to Lab 1: Builder, Prototype, and Factory Method. Each example reuses classes from the SOLID programs in this folder.

Run the examples from this folder:

```bash
cd ~/Desktop/uni/TMPS/lab2
python3 builder_signal_bulletin.py
python3 prototype_museum_rooms.py
python3 factory_method_library.py
```

Builder fits a bulletin assembled from several parts. Prototype creates museum rooms from a configured template. Factory Method lets library stations choose which alarm to create.

## 1. Builder

**File:** [`builder_signal_bulletin.py`](builder_signal_bulletin.py)

### Introduction

Builder creates an object step by step. It is useful when some parts are optional or are added one at a time.

### Implementation

- `BulletinBuilder` sets a title, adds signals, and sets a footer.
- `build()` creates a `Bulletin` with its own copy of the entries.
- The program uses `SignalParser` and `SignalArchive` from the SRP example.

### Description

The program receives two moon signals. It then builds and displays a bulletin titled "Moon Watch". The builder keeps the construction steps in one place while `Bulletin` represents the finished result.

## 2. Prototype

**File:** [`prototype_museum_rooms.py`](prototype_museum_rooms.py)

### Introduction

Prototype creates a new object by copying an existing object. The existing object serves as a template.

### Implementation

- `EnergyRoom` implements the `Room` interface from the OCP example.
- `clone()` returns a copy of an existing room.
- The program clones `Quiet Cave` to create `Mirror Cave` and `Healing Cave`, then gives all three rooms to `MuseumTour`.

### Description

Each cloned room starts with the template's settings and can then be changed independently. The tour runs every room through the same `enter()` method.

## 3. Factory Method

**File:** [`factory_method_library.py`](factory_method_library.py)

### Introduction

Factory Method lets subclasses choose which concrete object to create. The main workflow calls a creation method without naming the concrete class.

### Implementation

- `LibraryStation` defines `create_alarm()` and the shared `check_books()` workflow.
- `NoisyStation` creates a `BellAlarm`.
- `QuietStation` creates a `LogAlarm`.
- Both alarms and `BookGuard` come from the DIP example.

### Description

Both stations check the same books. One prints an alarm, while the other stores it in a log. The checking workflow stays in `LibraryStation`; each subclass chooses its alarm by overriding `create_alarm()`.
