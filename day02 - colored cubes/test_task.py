import unittest
import textwrap

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (2685, 83707))


class TestGivenExamples(unittest.TestCase):
    def test_part1(self):
        actual_sum = 0

        # fmt: off
        example_text_input = textwrap.dedent("""\
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        )
        # fmt: on

        for line in example_text_input.split("\n"):
            actual_sum += task.part1(task.toDraws(line), task.get_game_number(line))

        self.assertEqual(actual_sum, 8)

    def test_part2(self):
        actual_sum = 0

        # fmt: off
        example_text_input = textwrap.dedent("""\
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        )
        # fmt: on

        for line in example_text_input.split("\n"):
            actual_sum += task.part2(task.toDraws(line))

        self.assertEqual(actual_sum, 2286)


class TestNumberConversion(unittest.TestCase):
    def test_cube_drawing_single_complete(self):
        text_input = "Game 1: 1 red, 2 green, 3 blue"
        expect = [task.Draw(1, 2, 3)]
        self.assertEqual(task.toDraws(text_input), expect)

    def test_cube_drawing_single_incomplete(self):
        text_input = "Game 2: 1 red"
        expect = [task.Draw(1, 0, 0)]
        self.assertEqual(task.toDraws(text_input), expect)

    def test_cube_drawing_multiple_singles(self):
        text_input = "Game 3: 1 red; 2 green; 3 blue"
        expect = [task.Draw(1, 0, 0), task.Draw(0, 2, 0), task.Draw(0, 0, 3)]
        self.assertEqual(task.toDraws(text_input), expect)

    def test_cube_drawing_multiple(self):
        text_input = "Game 3: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expect = [task.Draw(4, 0, 3), task.Draw(1, 2, 6), task.Draw(0, 2, 0)]
        self.assertEqual(task.toDraws(text_input), expect)

    def test_cube_drawing_all_rgb_orderings(self):
        text_input = "Game 3: 1 red, 2 green, 3 blue; 4 red, 6 blue, 5 green; 8 green, 7 red, 9 blue; 11 green, 12 blue, 10 red; 15 blue, 13 red, 14 green; 18 blue, 17 green, 16 red"
        expect = [
            task.Draw(1, 2, 3),
            task.Draw(4, 5, 6),
            task.Draw(7, 8, 9),
            task.Draw(10, 11, 12),
            task.Draw(13, 14, 15),
            task.Draw(16, 17, 18),
        ]
        self.assertEqual(task.toDraws(text_input), expect)


class TestGameNumber(unittest.TestCase):
    def test_game(self):
        text_input = "Game 3: 1 red, 2 green, 3 blue; 4 red, 6 blue, 5 green; 8 green, 7 red, 9 blue; 11 green, 12 blue, 10 red; 15 blue, 13 red, 14 green; 18 blue, 17 green, 16 red"
        self.assertEqual(task.get_game_number(text_input), 3)
        text_input = "Game 123: 1 red, 2 green, 3 blue; 4 red, 6 blue, 5 green; 8 green, 7 red, 9 blue; 11 green, 12 blue, 10 red; 15 blue, 13 red, 14 green; 18 blue, 17 green, 16 red"
        self.assertEqual(task.get_game_number(text_input), 123)


class TestDraws(unittest.TestCase):
    def test_cube_summing(self):
        actual = task.Draw(1, 0, 0) + task.Draw(0, 2, 0) + task.Draw(0, 0, 3)
        expect = task.Draw(1, 2, 3)

        self.assertEqual(actual, expect)

    def test_cube_comparing(self):
        self.assertTrue(task.Draw(1, 0, 0) < task.Draw(10, 0, 0))
        self.assertTrue(task.Draw(0, 1, 0) < task.Draw(0, 10, 0))
        self.assertTrue(task.Draw(0, 0, 1) < task.Draw(0, 0, 10))
        self.assertTrue(task.Draw(1, 2, 3) < task.Draw(4, 5, 6))

        self.assertFalse(task.Draw(1, 0, 0) > task.Draw(10, 0, 0))
        self.assertFalse(task.Draw(0, 1, 0) > task.Draw(0, 10, 0))
        self.assertFalse(task.Draw(0, 0, 1) > task.Draw(0, 0, 10))
        self.assertFalse(task.Draw(1, 2, 3) > task.Draw(4, 5, 6))

        self.assertTrue(task.Draw(1, 2, 3) < task.Draw(1, 1, 4))
        self.assertTrue(task.Draw(1, 2, 3) > task.Draw(1, 1, 4))

        self.assertTrue(task.Draw(1, 0, 0) == task.Draw(1, 0, 0))
        self.assertTrue(task.Draw(0, 1, 0) == task.Draw(0, 1, 0))
        self.assertTrue(task.Draw(0, 0, 1) == task.Draw(0, 0, 1))
        self.assertTrue(task.Draw(1, 2, 3) == task.Draw(1, 2, 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
