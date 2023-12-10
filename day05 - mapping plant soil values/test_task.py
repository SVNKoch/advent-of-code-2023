import unittest
import textwrap

import task


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(task.main(), (177942185, -1))


class TestGivenExamples(unittest.TestCase):
    def test_part1(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            seeds: 79 14 55 13

            seed-to-soil map:
            50 98 2
            52 50 48

            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15

            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4

            water-to-light map:
            88 18 7
            18 25 70

            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13

            temperature-to-humidity map:
            0 69 1
            1 0 69

            humidity-to-location map:
            60 56 37
            56 93 4"""
        )
        # fmt: on

        minimum_location = task.part1(example_text_input.split("\n"))

        self.assertEqual(minimum_location, 35)

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


class Test(unittest.TestCase):
    def test_read_line(self):
        self.assertEqual(task.read_line("50 98 2"), (50, 98, 2))
        self.assertEqual(task.read_line("0 15 37"), (0, 15, 37))

    def test_read_seeds(self):
        example_text_input = "seeds: 79 14 55 13"
        gm = task.GardeningMaps()
        gm = task.read_seeds(gm, example_text_input)
        self.assertEqual(gm.seeds, [79, 14, 55, 13])

    def test_read_map_input(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            seed-to-soil map:
            50 98 2
            52 50 48

            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15

            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4

            water-to-light map:
            88 18 7
            18 25 70

            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13

            temperature-to-humidity map:
            0 69 1
            1 0 69

            humidity-to-location map:
            60 56 37
            56 93 4"""
        )
        # fmt: on
        gm = task.read_map_input(example_text_input.split("\n"))
        self.assertEqual(gm.get_corresponding_types(79), (81, 81, 81, 74, 78, 78, 82))
        self.assertEqual(gm.get_corresponding_types(14), (14, 53, 49, 42, 42, 43, 43))
        self.assertEqual(gm.get_corresponding_types(55), (57, 57, 53, 46, 82, 82, 86))
        self.assertEqual(gm.get_corresponding_types(13), (13, 52, 41, 34, 34, 35, 35))

    def test_complete_read(self):
        # fmt: off
        example_text_input = textwrap.dedent("""\
            seeds: 79 14 55 13

            seed-to-soil map:
            50 98 2
            52 50 48

            soil-to-fertilizer map:
            0 15 37
            37 52 2
            39 0 15

            fertilizer-to-water map:
            49 53 8
            0 11 42
            42 0 7
            57 7 4

            water-to-light map:
            88 18 7
            18 25 70

            light-to-temperature map:
            45 77 23
            81 45 19
            68 64 13

            temperature-to-humidity map:
            0 69 1
            1 0 69

            humidity-to-location map:
            60 56 37
            56 93 4"""
        )
        # fmt: on

        lines = example_text_input.split("\n")

        gm = task.read_map_input(lines[1:])
        task.read_seeds(gm, lines[0])

        self.assertEqual(gm.get_corresponding_types(79), (81, 81, 81, 74, 78, 78, 82))
        self.assertEqual(gm.get_corresponding_types(14), (14, 53, 49, 42, 42, 43, 43))
        self.assertEqual(gm.get_corresponding_types(55), (57, 57, 53, 46, 82, 82, 86))
        self.assertEqual(gm.get_corresponding_types(13), (13, 52, 41, 34, 34, 35, 35))


class TestGardeningMaps(unittest.TestCase):
    def test_maps(self):
        gm = task.GardeningMaps()
        gm.add_seed_to_soil_mapping(50, 98, 2)
        gm.add_seed_to_soil_mapping(52, 50, 48)

        self.assertEqual(gm.seed_to_soil_map[0], 0)
        self.assertEqual(gm.seed_to_soil_map[1], 1)
        self.assertEqual(gm.seed_to_soil_map[48], 48)
        self.assertEqual(gm.seed_to_soil_map[49], 49)
        self.assertEqual(gm.seed_to_soil_map[50], 52)
        self.assertEqual(gm.seed_to_soil_map[51], 53)
        self.assertEqual(gm.seed_to_soil_map[96], 98)
        self.assertEqual(gm.seed_to_soil_map[97], 99)
        self.assertEqual(gm.seed_to_soil_map[98], 50)
        self.assertEqual(gm.seed_to_soil_map[99], 51)
        self.assertEqual(gm.seed_to_soil_map[100], 100)

    def test_chain(self):
        gm = task.GardeningMaps()
        gm.add_seed_to_soil_mapping(2, 1, 1)
        gm.add_soil_to_fertilizer_mapping(4, 2, 1)
        gm.add_fertilizer_to_water_mapping(6, 4, 1)
        gm.add_water_to_light_mapping(7, 6, 1)
        gm.add_light_to_temperature_mapping(10, 7, 1)
        gm.add_temperature_to_humidity_mapping(14, 10, 1)
        gm.add_humidity_to_location_mapping(15, 14, 1)
        self.assertEqual(gm.get_corresponding_types(1), (2, 4, 6, 7, 10, 14, 15))


class TestDigitLookUp(unittest.TestCase):
    def test_DigitLookUp(self):
        lu = task.DigitLookUp()
        self.assertEqual(lu[1], 1)
        lu[range(1, 3)] = 5
        self.assertEqual(lu[2], 7)


if __name__ == "__main__":
    unittest.main(verbosity=2)
