import unittest
from contextlib import redirect_stdout
from io import StringIO

from lab3.app.__main__ import main
from lab3.domain.bulletin import SignalEntry
from lab3.patterns.builder import BulletinBuilder
from lab3.patterns.composite import SignalSection
from lab3.patterns.decorator import SourceTaggedEntry, UrgentEntry
from lab3.patterns.facade import BulletinPublisher


class CompositeTests(unittest.TestCase):
    def test_signal_and_section_use_the_same_interface(self):
        signal = SignalEntry("Io", "Volcano awakened")
        section = SignalSection("Alerts", [signal])
        bulletin = BulletinBuilder().add_entry(signal).add_entry(section).build()

        self.assertEqual(
            bulletin.render(),
            "Untitled bulletin\nIo: Volcano awakened\nAlerts\n  Io: Volcano awakened\nEnd of bulletin",
        )

    def test_nested_sections_render_in_order(self):
        alerts = SignalSection("Alerts", [SignalEntry("Io", "Volcano awakened")])
        jupiter = SignalSection("Jupiter system", [alerts, SignalEntry("Europa", "Ocean discovered")])

        self.assertEqual(
            jupiter.render(),
            "Jupiter system\n  Alerts\n    Io: Volcano awakened\n  Europa: Ocean discovered",
        )


class DecoratorTests(unittest.TestCase):
    def test_decorators_stack_in_either_order(self):
        signal = SignalEntry("Io", "Volcano awakened")
        expected = "[URGENT] Io: Volcano awakened [source: Orbiter 7]"

        self.assertEqual(UrgentEntry(SourceTaggedEntry(signal, "Orbiter 7")).render(), expected)
        self.assertEqual(SourceTaggedEntry(UrgentEntry(signal), "Orbiter 7").render(), expected)
        self.assertEqual(signal.render(), "Io: Volcano awakened")

    def test_decorated_section_keeps_its_children(self):
        section = SignalSection("Alerts", [SignalEntry("Io", "Volcano awakened")])
        tagged = SourceTaggedEntry(section, "Orbiter 7")

        self.assertEqual(tagged.render(), "Alerts [source: Orbiter 7]\n  Io: Volcano awakened")


class FacadeTests(unittest.TestCase):
    def test_publisher_renders_entries_before_sending_one_bulletin(self):
        events = []

        class RecordingEntry(SignalEntry):
            def render(self):
                events.append(self.moon)
                return super().render()

        publisher = BulletinPublisher(events.append)
        publisher.publish(
            "Moon Watch",
            [RecordingEntry("Io", "Alert"), RecordingEntry("Europa", "Update")],
            "Done",
        )

        self.assertEqual(events, ["Io", "Europa", "Moon Watch\nIo: Alert\nEuropa: Update\nDone"])

    def test_each_publication_has_its_own_entries(self):
        output = []
        publisher = BulletinPublisher(output.append)
        publisher.publish("First", [SignalEntry("Io", "Alert")], "Done")
        publisher.publish("Second", [SignalEntry("Europa", "Update")], "Done")

        self.assertEqual(output, ["First\nIo: Alert\nDone", "Second\nEuropa: Update\nDone"])


class BuilderTests(unittest.TestCase):
    def test_built_bulletin_is_independent_of_later_builder_changes(self):
        builder = BulletinBuilder().add_entry(SignalEntry("Io", "Alert"))
        bulletin = builder.build()
        builder.add_entry(SignalEntry("Europa", "Update"))

        self.assertEqual(bulletin.render(), "Untitled bulletin\nIo: Alert\nEnd of bulletin")


class DemoTests(unittest.TestCase):
    def test_demo_uses_all_three_structural_patterns_together(self):
        output = StringIO()
        with redirect_stdout(output):
            main()

        self.assertEqual(
            output.getvalue(),
            "Moon Watch\n"
            "Jupiter system\n"
            "  Alerts\n"
            "    [URGENT] Io: Volcano awakened [source: Orbiter 7]\n"
            "  Europa: Ocean discovered\n"
            "Report complete\n",
        )
