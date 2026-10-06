# Lab 1: Three SOLID Principles

This folder contains three small Python programs. Run each file separately:

```bash
cd ~/Desktop/TMPS/lab1
python3 srp_signal_archive.py
python3 ocp_strange_expedition.py
python3 dip_flying_library.py
```

## 1. Single Responsibility Principle

**File:** [`srp_signal_archive.py`](srp_signal_archive.py)

### Introduction

Each class should have one clear job. A change to one job should not require changes to unrelated parts of the program.

### Implementation

- `SignalParser` splits an incoming line into a moon and a message.
- `SignalArchive` stores the signals.
- `SignalReport` displays the signals.

### Description

The program receives two messages from distant moons, stores them, and prints them. If the input format changes, update `SignalParser`. If the display format changes, update `SignalReport`.

## 2. Open/Closed Principle

**File:** [`ocp_strange_expedition.py`](ocp_strange_expedition.py)

### Introduction

You should be able to add new behavior without rewriting the main part of the program.

### Implementation

- `Room` defines the shared `enter()` action.
- `WhisperingRoom` and `MagicSpring` change a visitor's energy in different ways.
- `MuseumTour` calls `enter()` on each room without checking its type.

### Description

A visitor walks through the museum and sees their energy change. To add another room, create a new `Room` class with an `enter()` method and put it in the list. `MuseumTour` does not need to change.

## 3. Dependency Inversion Principle

**File:** [`dip_flying_library.py`](dip_flying_library.py)

### Introduction

An important rule should rely on a shared interface instead of one specific device.

### Implementation

- `Alarm` defines the shared `warn()` action.
- `BellAlarm` prints a warning.
- `LogAlarm` records a warning.
- `BookGuard` checks a book's height and uses the alarm it was given.

### Description

When a book flies below 5 meters, `BookGuard` calls `warn()`. One alarm prints a message; another saves it in a log. You can swap alarms without changing the height check.
