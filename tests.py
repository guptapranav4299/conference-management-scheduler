import unittest
import conference_scheduler

class ConferenceTest(unittest.TestCase):
    def test_parse_input_file(self):
        status = conference_scheduler.Conference(name="My Times", file="input.txt", starts_at="09:00", ends_at="17:00", lunch_at="12:00",
                      networking_at="17:00").parse_input_file("input.txt")
        self.assertEqual(status,True)

if __name__ == '__main__':
    ConferenceTest().test_parse_input_file()