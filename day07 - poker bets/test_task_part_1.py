import unittest
import textwrap

import task_part_1 as task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), 253954294)


class TestGivenExamples(unittest.TestCase):
    def test_part1(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            32T3K 765
            T55J5 684
            KK677 28
            KTJJT 220
            QQQJA 483"""
        )
        # fmt: on

        self.assertEqual(task.part1(example_text_input), 6440)


class TestHand(unittest.TestCase):
    def test_hand_type_classification(self):
        self.assertEqual(task.classify_hand_type("AAAAA"), task.Type.FIVE_OF_A_KIND)
        self.assertEqual(task.classify_hand_type("AA8AA"), task.Type.FOUR_OF_A_KIND)
        self.assertEqual(task.classify_hand_type("23332"), task.Type.FULL_HOUSE)
        self.assertEqual(task.classify_hand_type("TTT98"), task.Type.THREE_OF_A_KIND)
        self.assertEqual(task.classify_hand_type("23432"), task.Type.TWO_PAIR)
        self.assertEqual(task.classify_hand_type("A23A4"), task.Type.ONE_PAIR)
        self.assertEqual(task.classify_hand_type("23456"), task.Type.HIGH_CARD)

    def test_comparison(self):
        self.assertTrue(
            task.Hand("23456")
            < task.Hand("A23A4")
            < task.Hand("23432")
            < task.Hand("TTT98")
            < task.Hand("23332")
            < task.Hand("AA8AA")
            < task.Hand("AAAAA")
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
