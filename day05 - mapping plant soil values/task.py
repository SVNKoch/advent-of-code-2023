from __future__ import annotations
from typing import Callable


class DigitLookUp:
    def __init__(self) -> None:
        self.range_maps: dict[range, int] = {}

    def __getitem__(self, value: int) -> int:
        for this_range, this_map_value in self.range_maps.items():
            if value in this_range:
                return value + this_map_value
        return value

    def __setitem__(self, key: range, value: int) -> None:
        self.range_maps[key] = value


class GardeningMaps:
    def __init__(self) -> None:
        self.seeds: list[int] = []
        self.seed_to_soil_map = DigitLookUp()
        self.soil_to_fertilizer_map = DigitLookUp()
        self.fertilizer_to_water_map = DigitLookUp()
        self.water_to_light_map = DigitLookUp()
        self.light_to_temperature_map = DigitLookUp()
        self.temperature_to_humidity_map = DigitLookUp()
        self.humidity_to_location_map = DigitLookUp()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def add_seeds(self, seed_number: int):
        self.seeds.append(seed_number)

    def add_seed_to_soil_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.seed_to_soil_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def add_soil_to_fertilizer_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.soil_to_fertilizer_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def add_fertilizer_to_water_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.fertilizer_to_water_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def add_water_to_light_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.water_to_light_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def add_light_to_temperature_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.light_to_temperature_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def add_temperature_to_humidity_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.temperature_to_humidity_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def add_humidity_to_location_mapping(
        self,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        return self._add_mapping(
            lambda: self.humidity_to_location_map,
            destination_range_start,
            source_range_start,
            range_length,
        )

    def _add_mapping(
        self,
        lookup,
        destination_range_start: int,
        source_range_start: int,
        range_length: int,
    ) -> None:
        diff = destination_range_start - source_range_start
        lookup()[range(source_range_start, source_range_start + range_length)] = diff

    def get_corresponding_types(
        self, seed_number: int
    ) -> tuple[int, int, int, int, int, int, int]:
        soil_number = self.seed_to_soil_map[seed_number]
        fertilizer_number = self.soil_to_fertilizer_map[soil_number]
        water_number = self.fertilizer_to_water_map[fertilizer_number]
        light_number = self.water_to_light_map[water_number]
        temperature_number = self.light_to_temperature_map[light_number]
        humidity_number = self.temperature_to_humidity_map[temperature_number]
        location_number = self.humidity_to_location_map[humidity_number]

        return (
            soil_number,
            fertilizer_number,
            water_number,
            light_number,
            temperature_number,
            humidity_number,
            location_number,
        )


def read_line(line: str) -> tuple[int, int, int]:
    numbers_in_line = list(map(int, line.split(" ")))
    if len(numbers_in_line) != 3:
        raise ValueError(f'couldn\'t find 3 numbers in "{line}"')
    return tuple(numbers_in_line)  # type: ignore


def read_seeds(gm: GardeningMaps, string: str) -> GardeningMaps:
    gm.seeds = list(map(int, string.split("seeds: ")[1].split(" ")))
    return gm


def read_map_input(lines: list[str]) -> GardeningMaps:
    gm = GardeningMaps()

    function_list: dict[str, Callable[..., None]] = {
        "seed-to-soil map:": lambda tp: gm.add_seed_to_soil_mapping(*tp),
        "soil-to-fertilizer map:": lambda tp: gm.add_soil_to_fertilizer_mapping(*tp),
        "fertilizer-to-water map:": lambda tp: gm.add_fertilizer_to_water_mapping(*tp),
        "water-to-light map:": lambda tp: gm.add_water_to_light_mapping(*tp),
        "light-to-temperature map:": lambda tp: gm.add_light_to_temperature_mapping(
            *tp
        ),
        "temperature-to-humidity map:": lambda tp: gm.add_temperature_to_humidity_mapping(
            *tp
        ),
        "humidity-to-location map:": lambda tp: gm.add_humidity_to_location_mapping(
            *tp
        ),
    }

    # pylint: disable=unnecessary-lambda-assignment, unnecessary-lambda
    current_funcion = lambda tp: gm.add_seeds(tp)
    for line in lines:
        if line.strip() == "":
            continue
        if line in function_list:
            current_funcion = function_list[line]
        else:
            current_funcion(read_line(line))
    return gm


def part1(lines: list[str]) -> int:
    gm = read_map_input(lines[1:])
    read_seeds(gm, lines[0])

    return min(
        map(
            lambda seed_number: gm.get_corresponding_types(seed_number)[6],
            gm.seeds,
        )
    )


def part2():
    pass


def main() -> tuple[int, int]:
    with open("input.txt", "r", encoding="UTF8") as input_file:
        lines = input_file.read().split("\n")

    minimum_location = part1(lines)
    return minimum_location, -1


if __name__ == "__main__":
    print(main())
