import unittest
import textwrap

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (533775, 78236071))


class TestGivenExamples(unittest.TestCase):
    def test_part1(self):
        actual_sum = 0

        # fmt: off
        example_line_input = textwrap.dedent("""\
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598.."""
        ).split("\n")
        # fmt: on

        actual_sum += task.part1(example_line_input)

        self.assertEqual(actual_sum, 4361)

    def test_part2(self):
        actual_sum = 0

        # fmt: off
        example_line_input = textwrap.dedent("""\
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598.."""
        ).split("\n")
        # fmt: on

        actual_sum += task.part2(example_line_input)

        self.assertEqual(actual_sum, 467835)


class TestPartNumberReading(unittest.TestCase):
    def test_find_part_numbers_all_singles(self):
        line_input = textwrap.dedent(
            """\
            .....
            .2.3.
            .4#5.
            .6.7.
            ....."""
        ).split("\n")
        expect = [2, 3, 4, 5, 6, 7]
        self.assertListEqual(sorted(task.find_part_numbers(line_input)), sorted(expect))
        self.assertListEqual(sorted(task.find_part_numbers(line_input, True)), [])

    def test_find_part_numbers_all_doubles(self):
        line_input = textwrap.dedent(
            """\
            .....
            12.34
            56#78
            90.23
            ....."""
        ).split("\n")
        expect = [12, 34, 56, 78, 90, 23]
        self.assertListEqual(sorted(task.find_part_numbers(line_input)), sorted(expect))
        self.assertListEqual(sorted(task.find_part_numbers(line_input, True)), [])

    def test_find_part_numbers_same_doubles(self):
        line_input = textwrap.dedent(
            """\
            .....
            10.10
            10#10
            10.10
            ....."""
        ).split("\n")
        expect = [10] * 6
        self.assertListEqual(sorted(task.find_part_numbers(line_input)), sorted(expect))
        self.assertListEqual(sorted(task.find_part_numbers(line_input, True)), [])

    def test_find_part_numbers_wide(self):
        line_input = textwrap.dedent(
            """\
            .....
            12345
            ..*..
            67890
            ....."""
        ).split("\n")
        expect = [12345, 67890]
        self.assertListEqual(sorted(task.find_part_numbers(line_input)), sorted(expect))
        self.assertListEqual(
            sorted(task.find_part_numbers(line_input, True)), [12345 * 67890]
        )


class TestDivers(unittest.TestCase):
    def test_find_symboles(self):
        line_input = textwrap.dedent(
            """\
            *.&.$.-.+.%./.#.=.@.
            ....................
            .*.&.$.-.+.%./.#.=.@"""
        ).split("\n")
        expect = list(map(lambda a: (0, a), range(0, 20, 2))) + list(
            map(lambda a: (2, a), range(1, 20, 2))
        )
        self.assertEqual(task.find_symbols(line_input), expect)
        self.assertEqual(task.find_symbols(line_input, r"\*"), [(0, 0), (2, 1)])

    def test_find_sourrounding_locations(self):
        dimension = (3, 4)
        self.assertEqual(task.sourrounding((0, 0), dimension), [(0, 1), (1, 0), (1, 1)])
        self.assertEqual(task.sourrounding((0, 3), dimension), [(0, 2), (1, 2), (1, 3)])
        self.assertEqual(task.sourrounding((2, 0), dimension), [(1, 0), (1, 1), (2, 1)])
        self.assertEqual(task.sourrounding((2, 3), dimension), [(1, 2), (1, 3), (2, 2)])
        self.assertEqual(
            task.sourrounding((1, 1), dimension),
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
        )

    def test_dimensions(self):
        line_input = textwrap.dedent(
            """\
            ....
            ....
            ...."""
        ).split("\n")
        expect = (3, 4)
        self.assertEqual(task.calculate_dimensions(line_input), expect)


if __name__ == "__main__":
    unittest.main(verbosity=2)
