import unittest
import textwrap

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (16043, 0))


class TestGivenExamples(unittest.TestCase):
    def test_part1_example1(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            RL

            AAA = (BBB, CCC)
            BBB = (DDD, EEE)
            CCC = (ZZZ, GGG)
            DDD = (DDD, DDD)
            EEE = (EEE, EEE)
            GGG = (GGG, GGG)
            ZZZ = (ZZZ, ZZZ)"""
        )
        # fmt: on

        lines = example_text_input.split("\n")

        self.assertEqual(task.part1(lines), 2)

    def test_part1_example2(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            LLR

            AAA = (BBB, BBB)
            BBB = (AAA, ZZZ)
            ZZZ = (ZZZ, ZZZ)"""
        )
        # fmt: on

        lines = example_text_input.split("\n")

        self.assertEqual(task.part1(lines), 6)

    def test_part1_example3(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            R

            AAA = (BBB, BBB)
            BBB = (CCC, CCC)
            CCC = (DDD, DDD)
            DDD = (EEE, EEE)
            EEE = (FFF, FFF)
            FFF = (GGG, GGG)
            GGG = (ZZZ, ZZZ)
            ZZZ = (ZZZ, ZZZ)"""
        )
        # fmt: on

        lines = example_text_input.split("\n")

        self.assertEqual(task.part1(lines), 7)

    @unittest.skip("")
    def test_part2(self):
        actual_sum = 0

        # fmt: off
        example_text_input = textwrap.dedent("""\
            """
        )
        # fmt: on

        for line in example_text_input.split("\n"):
            actual_sum += task.part2(line)

        self.assertEqual(actual_sum, 9999999)


class TestPath(unittest.TestCase):
    def test_follow_path_to_zzz(self):
        # fmt: off
        text_input = textwrap.dedent("""\
            AAA = (BBB, CCC)
            BBB = (DDD, EEE)
            CCC = (ZZZ, GGG)
            DDD = (DDD, DDD)
            EEE = (EEE, EEE)
            GGG = (GGG, GGG)
            ZZZ = (ZZZ, ZZZ)"""
        )
        # fmt: on
        lines = text_input.split("\n")
        network = task.read_map(lines)

        self.assertEqual(task.follow_path_to_zzz("RL", network, "AAA"), (2, "ZZZ"))
        self.assertEqual(task.follow_path_to_zzz("RLRRR", network, "AAA"), (2, "ZZZ"))
        self.assertEqual(task.follow_path_to_zzz("RR", network, "AAA"), (2, "GGG"))
        self.assertEqual(task.follow_path_to_zzz("RR", network, "ZZZ"), (0, "ZZZ"))

    def test_step_count_till_zzz(self):
        # fmt: off
        text_input = textwrap.dedent("""\
            AAA = (BBB, BBB)
            BBB = (AAA, ZZZ)
            ZZZ = (ZZZ, ZZZ)"""
        )
        # fmt: on
        lines = text_input.split("\n")
        network = task.read_map(lines)

        self.assertEqual(task.step_count_till_zzz("LLR", network, "AAA"), 6)
        self.assertEqual(task.step_count_till_zzz("LLR", network, "ZZZ"), 0)
        self.assertEqual(task.step_count_till_zzz("RLL", network, "AAA"), 4)
        self.assertEqual(task.step_count_till_zzz("R", network, "BBB"), 1)


class TestReading(unittest.TestCase):
    def test_read_map(self):
        # fmt: off
        text_input = textwrap.dedent("""\
            AAA = (BBB, CCC)
            BBB = (DDD, EEE)"""
        )
        # fmt: on
        lines = text_input.split("\n")

        self.assertEqual(
            task.read_map(lines), {"AAA": ("BBB", "CCC"), "BBB": ("DDD", "EEE")}
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
