import unittest
import textwrap

import task_part_2 as task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), 254837398)


class TestGivenExamples(unittest.TestCase):
    def test_part2(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            32T3K 765
            T55J5 684
            KK677 28
            KTJJT 220
            QQQJA 483"""
        )
        # fmt: on

        self.assertEqual(task.part2(example_text_input), 5905)


class TestHand(unittest.TestCase):
    def test_hand_type_classification(self):
        self.assertEqual(task.classify_hand_type("KTJJT"), task.Type.FOUR_OF_A_KIND)
        self.assertEqual(task.classify_hand_type("QQQJA"), task.Type.FOUR_OF_A_KIND)
        self.assertEqual(task.classify_hand_type("T55J5"), task.Type.FOUR_OF_A_KIND)
        self.assertEqual(task.classify_hand_type("KK677"), task.Type.TWO_PAIR)
        self.assertEqual(task.classify_hand_type("32T3K"), task.Type.ONE_PAIR)
        self.assertEqual(task.classify_hand_type("23456"), task.Type.HIGH_CARD)

    def test_comparison(self):
        self.assertTrue(
            task.Hand("32T3K")
            < task.Hand("KK677")
            < task.Hand("T55J5")
            < task.Hand("QQQJA")
            < task.Hand("KTJJT")
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
