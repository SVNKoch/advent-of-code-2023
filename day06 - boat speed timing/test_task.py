import unittest
import textwrap

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (170000, 20537782))


class TestGivenExamples(unittest.TestCase):
    def test_winning_option_amount(self):
        self.assertEqual(task.calculate_number_of_wining_press_options(7, 9), 4)
        self.assertEqual(task.calculate_number_of_wining_press_options(15, 40), 8)
        self.assertEqual(task.calculate_number_of_wining_press_options(30, 200), 9)


class Test(unittest.TestCase):
    def test_find_possible_press_range(self):
        self.assertEqual(task.find_possible_press_range(7, 9), range(2, 6))

    def test_read_input(self):
        # fmt: off
        text_input = textwrap.dedent("""\
            Time:      7  15   30
            Distance:  9  40  200
            """
        )
        # fmt: on
        self.assertEqual(
            task.read_input_part_1(text_input), [(7, 9), (15, 40), (30, 200)]
        )
        self.assertEqual(task.read_input_part_2(text_input), (71530, 940200))


if __name__ == "__main__":
    unittest.main(verbosity=2)
