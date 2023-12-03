import unittest
import textwrap

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (55607, 55291))


class TestGivenExamples(unittest.TestCase):
    def test_part1(self):
        actual_sum = 0

        # fmt: off
        example_input = textwrap.dedent("""\
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet"""
        )
        # fmt: on

        for line in example_input.split("\n"):
            actual_sum += task.part1(line)

        self.assertEqual(actual_sum, 142)

    def test_part2(self):
        actual_sum = 0

        # fmt: off
        example_input = textwrap.dedent("""\
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen"""
        )
        # fmt: on

        for line in example_input.split("\n"):
            actual_sum += task.part2(line)

        self.assertEqual(actual_sum, 281)


class TestParts(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(task.part1("1"), 11)
        self.assertEqual(task.part1("12"), 12)
        self.assertEqual(task.part1("123"), 13)
        self.assertEqual(task.part1("a1b2c3d"), 13)

    def test_part2(self):
        self.assertEqual(task.part2("1"), 11)
        self.assertEqual(task.part2("one"), 11)
        self.assertEqual(task.part2("1two"), 12)
        self.assertEqual(task.part2("1two3"), 13)
        self.assertEqual(task.part2("one2three"), 13)
        self.assertEqual(task.part2("aoneb2cthreed"), 13)
        self.assertEqual(task.part2("eighthree"), 83)
        self.assertEqual(task.part2("sevenine"), 79)


class TestNumberConversion(unittest.TestCase):
    def test_int(self):
        self.assertEqual(task.toNumbers("1"), "1")

    def test_word(self):
        self.assertEqual(task.toNumbers("one"), "1")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            task.toNumbers("x")


if __name__ == "__main__":
    unittest.main(verbosity=2)
