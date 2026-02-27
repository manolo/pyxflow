"""Tests that set_value() fires change listeners (matching Java Flow behavior).

Java's AbstractFieldSupport.setValue() always fires ValueChangeEvent even for
server-side calls (fromClient=false). These tests verify our Python implementation
matches that behavior.
"""

import datetime


class TestTextFieldSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import TextField
        tf = TextField()
        events = []
        tf.add_value_change_listener(lambda e: events.append(e))
        tf.set_value("hello")
        assert len(events) == 1
        assert events[0]["value"] == "hello"
        assert events[0]["from_client"] is False

    def test_no_fire_same_value(self):
        from pyflow.components import TextField
        tf = TextField()
        tf.set_value("hello")
        events = []
        tf.add_value_change_listener(lambda e: events.append(e))
        tf.set_value("hello")
        assert len(events) == 0

    def test_fires_multiple_listeners(self):
        from pyflow.components import TextField
        tf = TextField()
        events1, events2 = [], []
        tf.add_value_change_listener(lambda e: events1.append(e))
        tf.add_value_change_listener(lambda e: events2.append(e))
        tf.set_value("world")
        assert len(events1) == 1
        assert len(events2) == 1


class TestTextAreaSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import TextArea
        ta = TextArea()
        events = []
        ta.add_value_change_listener(lambda e: events.append(e))
        ta.set_value("text")
        assert len(events) == 1
        assert events[0]["value"] == "text"

    def test_no_fire_same_value(self):
        from pyflow.components import TextArea
        ta = TextArea()
        ta.set_value("text")
        events = []
        ta.add_value_change_listener(lambda e: events.append(e))
        ta.set_value("text")
        assert len(events) == 0


class TestEmailFieldSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import EmailField
        ef = EmailField()
        events = []
        ef.add_value_change_listener(lambda e: events.append(e))
        ef.set_value("a@b.com")
        assert len(events) == 1
        assert events[0]["value"] == "a@b.com"


class TestPasswordFieldSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import PasswordField
        pf = PasswordField()
        events = []
        pf.add_value_change_listener(lambda e: events.append(e))
        pf.set_value("secret")
        assert len(events) == 1
        assert events[0]["value"] == "secret"


class TestNumberFieldSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import NumberField
        nf = NumberField()
        events = []
        nf.add_value_change_listener(lambda e: events.append(e))
        nf.set_value(42.0)
        assert len(events) == 1
        assert events[0]["value"] == 42.0

    def test_no_fire_same_value(self):
        from pyflow.components import NumberField
        nf = NumberField()
        nf.set_value(42.0)
        events = []
        nf.add_value_change_listener(lambda e: events.append(e))
        nf.set_value(42.0)
        assert len(events) == 0

    def test_fires_none_to_value(self):
        from pyflow.components import NumberField
        nf = NumberField()
        events = []
        nf.add_value_change_listener(lambda e: events.append(e))
        nf.set_value(3.14)
        assert len(events) == 1


class TestIntegerFieldSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import IntegerField
        f = IntegerField()
        events = []
        f.add_value_change_listener(lambda e: events.append(e))
        f.set_value(7)
        assert len(events) == 1
        assert events[0]["value"] == 7

    def test_no_fire_same_value(self):
        from pyflow.components import IntegerField
        f = IntegerField()
        f.set_value(7)
        events = []
        f.add_value_change_listener(lambda e: events.append(e))
        f.set_value(7)
        assert len(events) == 0


class TestDatePickerSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import DatePicker
        dp = DatePicker()
        events = []
        dp.add_value_change_listener(lambda e: events.append(e))
        d = datetime.date(2025, 6, 15)
        dp.set_value(d)
        assert len(events) == 1
        assert events[0]["value"] == d

    def test_no_fire_same_value(self):
        from pyflow.components import DatePicker
        dp = DatePicker()
        d = datetime.date(2025, 6, 15)
        dp.set_value(d)
        events = []
        dp.add_value_change_listener(lambda e: events.append(e))
        dp.set_value(d)
        assert len(events) == 0


class TestTimePickerSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import TimePicker
        tp = TimePicker()
        events = []
        tp.add_value_change_listener(lambda e: events.append(e))
        t = datetime.time(14, 30)
        tp.set_value(t)
        assert len(events) == 1
        assert events[0]["value"] == t


class TestDateTimePickerSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import DateTimePicker
        dtp = DateTimePicker()
        events = []
        dtp.add_value_change_listener(lambda e: events.append(e))
        dt = datetime.datetime(2025, 6, 15, 14, 30)
        dtp.set_value(dt)
        assert len(events) == 1
        assert events[0]["value"] == dt


class TestListBoxSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import ListBox
        lb = ListBox()
        lb.set_items("A", "B", "C")
        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        lb.set_value("B")
        assert len(events) == 1
        assert events[0]["value"] == "B"
        assert events[0]["from_client"] is False

    def test_no_fire_same_value(self):
        from pyflow.components import ListBox
        lb = ListBox()
        lb.set_items("A", "B")
        lb.set_value("A")
        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        lb.set_value("A")
        assert len(events) == 0

    def test_fires_on_clear(self):
        from pyflow.components import ListBox
        lb = ListBox()
        lb.set_items("A", "B")
        lb.set_value("A")
        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        lb.set_value(None)
        assert len(events) == 1
        assert events[0]["value"] is None


class TestMultiSelectListBoxSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components.list_box import MultiSelectListBox
        lb = MultiSelectListBox()
        lb.set_items("A", "B", "C")
        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        lb.set_value({"A", "C"})
        assert len(events) == 1
        assert events[0]["value"] == {"A", "C"}

    def test_no_fire_same_value(self):
        from pyflow.components.list_box import MultiSelectListBox
        lb = MultiSelectListBox()
        lb.set_items("A", "B")
        lb.set_value({"A"})
        events = []
        lb.add_value_change_listener(lambda e: events.append(e))
        lb.set_value({"A"})
        assert len(events) == 0


class TestSelectSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import Select
        s = Select()
        s.set_items("X", "Y", "Z")
        events = []
        s.add_value_change_listener(lambda e: events.append(e))
        s.set_value("Y")
        assert len(events) == 1
        assert events[0]["value"] == "Y"

    def test_no_fire_same_value(self):
        from pyflow.components import Select
        s = Select()
        s.set_items("X", "Y")
        s.set_value("X")
        events = []
        s.add_value_change_listener(lambda e: events.append(e))
        s.set_value("X")
        assert len(events) == 0


class TestComboBoxSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import ComboBox
        cb = ComboBox()
        cb.set_items("Java", "Python", "JS")
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value("Python")
        assert len(events) == 1
        assert events[0]["value"] == "Python"

    def test_no_fire_same_value(self):
        from pyflow.components import ComboBox
        cb = ComboBox()
        cb.set_items("Java", "Python")
        cb.set_value("Java")
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value("Java")
        assert len(events) == 0


class TestMultiSelectComboBoxSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import MultiSelectComboBox
        cb = MultiSelectComboBox()
        cb.set_items("A", "B", "C")
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value({"A", "C"})
        assert len(events) == 1
        assert events[0]["value"] == {"A", "C"}

    def test_no_fire_same_value(self):
        from pyflow.components import MultiSelectComboBox
        cb = MultiSelectComboBox()
        cb.set_items("A", "B")
        cb.set_value({"A"})
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value({"A"})
        assert len(events) == 0


class TestCheckboxSetValueFiresListeners:
    def test_set_checked_fires_listener(self):
        from pyflow.components import Checkbox
        cb = Checkbox("Accept")
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_checked(True)
        assert len(events) == 1
        assert events[0]["value"] is True
        assert events[0]["from_client"] is False

    def test_set_value_fires_listener(self):
        from pyflow.components import Checkbox
        cb = Checkbox()
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_value(True)
        assert len(events) == 1

    def test_no_fire_same_value(self):
        from pyflow.components import Checkbox
        cb = Checkbox()
        cb.set_checked(True)
        events = []
        cb.add_value_change_listener(lambda e: events.append(e))
        cb.set_checked(True)
        assert len(events) == 0


class TestCheckboxGroupSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import CheckboxGroup
        cg = CheckboxGroup()
        cg.set_items("A", "B", "C")
        events = []
        cg.add_value_change_listener(lambda e: events.append(e))
        cg.set_value({"A", "B"})
        assert len(events) == 1
        assert events[0]["value"] == {"A", "B"}

    def test_no_fire_same_value(self):
        from pyflow.components import CheckboxGroup
        cg = CheckboxGroup()
        cg.set_items("A", "B")
        cg.set_value({"A"})
        events = []
        cg.add_value_change_listener(lambda e: events.append(e))
        cg.set_value({"A"})
        assert len(events) == 0


class TestRadioButtonGroupSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import RadioButtonGroup
        rg = RadioButtonGroup()
        rg.set_items("X", "Y", "Z")
        events = []
        rg.add_value_change_listener(lambda e: events.append(e))
        rg.set_value("Y")
        assert len(events) == 1
        assert events[0]["value"] == "Y"

    def test_no_fire_same_value(self):
        from pyflow.components import RadioButtonGroup
        rg = RadioButtonGroup()
        rg.set_items("X", "Y")
        rg.set_value("X")
        events = []
        rg.add_value_change_listener(lambda e: events.append(e))
        rg.set_value("X")
        assert len(events) == 0


class TestCustomFieldSetValueFiresListeners:
    def test_fires_listener(self):
        from pyflow.components import CustomField
        cf = CustomField()
        events = []
        cf.add_value_change_listener(lambda e: events.append(e))
        cf.set_value("custom")
        assert len(events) == 1
        assert events[0]["value"] == "custom"

    def test_no_fire_same_value(self):
        from pyflow.components import CustomField
        cf = CustomField()
        events = []
        cf.add_value_change_listener(lambda e: events.append(e))
        cf.set_value("")  # default is already ""
        assert len(events) == 0
