import unittest

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (23441, 5923918))


class TestGivenExamples(unittest.TestCase):
    def test_part1(self):
        # fmt: off
        self.assertEqual(task.part1("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"), 8)
        self.assertEqual(task.part1("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"), 2)
        self.assertEqual(task.part1("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"), 2)
        self.assertEqual(task.part1("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"), 1)
        self.assertEqual(task.part1("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"), 0)
        self.assertEqual(task.part1("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"), 0)
        # fmt: on

    def test_part2(self):
        tl = task.TicketList(6)
        # fmt: off
        self.assertEqual(tl.tickets, [1]*6)
        self.assertEqual(task.part2(tl, "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53").tickets, [1, 1+1, 1+1,   1+1,     1+1,     1])
        self.assertEqual(task.part2(tl, "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19").tickets, [1, 1+1, 1+1+2, 1+1+2,   1+1,     1])
        self.assertEqual(task.part2(tl, "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1").tickets, [1, 1+1, 1+1+2, 1+1+2+4, 1+1+4,   1])
        self.assertEqual(task.part2(tl, "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83").tickets, [1, 1+1, 1+1+2, 1+1+2+4, 1+1+4+8, 1])
        self.assertEqual(task.part2(tl, "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36").tickets, [1, 1+1, 1+1+2, 1+1+2+4, 1+1+4+8, 1])
        self.assertEqual(task.part2(tl, "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11").tickets, [1, 1+1, 1+1+2, 1+1+2+4, 1+1+4+8, 1])
        self.assertEqual(                                                       [1, 2, 4, 8, 14, 1], [1, 1+1, 1+1+2, 1+1+2+4, 1+1+4+8, 1])
        # fmt: on
        self.assertEqual(sum(tl.tickets), 30)


class Test(unittest.TestCase):
    def test_reading_card(self):
        # fmt: off
        self.assertEqual(task.read_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"), 
                                        (1, [41, 48, 83, 86, 17], [83, 86,  6, 31, 17,  9, 48, 53]))
        self.assertEqual(task.read_card("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"), 
                                        (2, [13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]))
        self.assertEqual(task.read_card("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"), 
                                        (3, [ 1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14,  1]))
        self.assertEqual(task.read_card("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"), 
                                        (4, [41, 92, 73, 84, 69], [59, 84, 76, 51, 58,  5, 54, 83]))
        self.assertEqual(task.read_card("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"), 
                                        (5, [87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]))
        self.assertEqual(task.read_card("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"), 
                                        (6, [31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]))
        # fmt: on

    def test_get_winning_subset(self):
        self.assertEqual(
            sorted(
                task.get_winning_subset(
                    [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]
                )
            ),
            sorted([48, 83, 17, 86]),
        )

    def test_increase(self):
        tl = task.TicketList(5)

        tl.tickets = [1] * 5
        self.assertEqual(tl.increase(1, 2).tickets, [1, 2, 2, 1, 1])

        tl.tickets = [2, 2, 1, 2, 2]
        self.assertEqual(tl.increase(1, 3).tickets, [2, 2 + 2, 1 + 2, 2 + 2, 2])

        tl.tickets = [2, 2, 1, 2, 2]
        self.assertEqual(tl.increase(1, 0).tickets, [2, 2, 1, 2, 2])

        tl.tickets = [6, 5, 4, 3, 2]
        self.assertEqual(tl.increase(2, 3).tickets, [6, 5, 4 + 5, 3 + 5, 2 + 5])

        tl.tickets = [6, 5, 4, 3, 2]
        self.assertEqual(tl.increase(2, 99).tickets, [6, 5, 4 + 5, 3 + 5, 2 + 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
