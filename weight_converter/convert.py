from weight_converter.interfaces import IUnit
from weight_converter.utils import divide_by_zero_check

THOUSAND = 1e3
MILLION = 1e6
BILLION = 1e9
TRILLION = 1e12

METRIC_TONNES_TO_IMPERIAL_TONS = 1.0160469088
METRIC_TONNES_TO_US_TONS = 1.1023113109244
METRIC_TONNES_TO_STONES = 157.47304441777
METRIC_TONNES_TO_POUNDS = 2204.6226218488
METRIC_TONNES_TO_OUNCES = 35273.96194958

KILOS_TO_IMPERIAL_TONS = 1016.0469088
KILOS_TO_US_TONS = 907.18474
KILOS_TO_STONES = 6.35029318
KILOS_TO_POUNDS = 2.2046226218488
KILOS_TO_OUNCES = 35.27396194958

GRAMS_TO_IMPERIAL_TONS = 1016046.9088
GRAMS_TO_US_TONS = 907184.74
GRAMS_TO_STONES = 6350.29318
GRAMS_TO_POUNDS = 453.59237
GRAMS_TO_OUNCES = 28.349523125

MILLIGRAMS_TO_IMPERIAL_TONS = 1016046908.8
MILLIGRAMS_TO_US_TONS = 907184740
MILLIGRAMS_TO_STONES = 6350293.18
MILLIGRAMS_TO_POUNDS = 453592.37
MILLIGRAMS_TO_OUNCES = 28349.523125

MICROGRAMS_TO_IMPERIAL_TONS = 1016046908800
MICROGRAMS_TO_US_TONS = 907184740000
MICROGRAMS_TO_STONES = 6350293180
MICROGRAMS_TO_POUNDS = 453592370
MICROGRAMS_TO_OUNCES = 28349523.125

IMPERIAL_TONS_TO_US_TONS = 1.12
IMPERIAL_TONS_TO_STONES = 160
IMPERIAL_TONS_TO_POUNDS = 2240
IMPERIAL_TONS_TO_OUNCES = 35840

US_TONS_TO_STONES = 142.85714285714286
US_TONS_TO_POUNDS = 2000
US_TONS_TO_OUNCES = 32000

STONES_TO_POUNDS = 14
STONES_TO_OUNCES = 224

POUNDS_TO_OUNCES = 16


class MetricTonnes(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    def to_metric_tonnes(self) -> float:
        return self.value.__float__()

    def to_kilograms(self) -> float:
        return self.value * THOUSAND

    def to_grams(self) -> float:
        return self.value * MILLION

    def to_milligrams(self) -> float:
        return self.value * BILLION

    def to_micrograms(self) -> float:
        return self.value * TRILLION

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / METRIC_TONNES_TO_IMPERIAL_TONS

    def to_us_tons(self) -> float:
        return self.value * METRIC_TONNES_TO_US_TONS

    def to_stones(self) -> float:
        return self.value * METRIC_TONNES_TO_STONES

    def to_pounds(self) -> float:
        return self.value * METRIC_TONNES_TO_POUNDS

    def to_ounces(self) -> float:
        return self.value * METRIC_TONNES_TO_OUNCES


class Kilograms(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / THOUSAND

    def to_grams(self) -> float:
        return self.value * THOUSAND

    def to_kilograms(self) -> float:
        return self.value.__float__()

    def to_milligrams(self) -> float:
        return self.value * MILLION

    def to_micrograms(self) -> float:
        return self.value * BILLION

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / KILOS_TO_IMPERIAL_TONS

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / KILOS_TO_US_TONS

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / KILOS_TO_STONES

    def to_pounds(self) -> float:
        return self.value * KILOS_TO_POUNDS

    def to_ounces(self) -> float:
        return self.value * KILOS_TO_OUNCES


class Grams(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / MILLION

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / THOUSAND

    def to_grams(self) -> float:
        return self.value.__float__()

    def to_milligrams(self) -> float:
        return self.value * THOUSAND

    def to_micrograms(self) -> float:
        return self.value * MILLION

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / GRAMS_TO_IMPERIAL_TONS

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / GRAMS_TO_US_TONS

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / GRAMS_TO_STONES

    @divide_by_zero_check
    def to_pounds(self) -> float:
        return self.value / GRAMS_TO_POUNDS

    @divide_by_zero_check
    def to_ounces(self) -> float:
        return self.value / GRAMS_TO_OUNCES


class Milligrams(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / BILLION

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / MILLION

    @divide_by_zero_check
    def to_grams(self) -> float:
        return self.value / THOUSAND

    def to_milligrams(self) -> float:
        return self.value.__float__()

    def to_micrograms(self) -> float:
        return self.value * THOUSAND

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / MILLIGRAMS_TO_IMPERIAL_TONS

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / MILLIGRAMS_TO_US_TONS

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / MILLIGRAMS_TO_STONES

    @divide_by_zero_check
    def to_pounds(self) -> float:
        return self.value / MILLIGRAMS_TO_POUNDS

    @divide_by_zero_check
    def to_ounces(self) -> float:
        return self.value / MILLIGRAMS_TO_OUNCES


class Micrograms(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / TRILLION

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / BILLION

    @divide_by_zero_check
    def to_grams(self) -> float:
        return self.value / MILLION

    @divide_by_zero_check
    def to_milligrams(self) -> float:
        return self.value / THOUSAND

    def to_micrograms(self) -> float:
        return self.value.__float__()

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / MICROGRAMS_TO_IMPERIAL_TONS

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / MICROGRAMS_TO_US_TONS

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / MICROGRAMS_TO_STONES

    @divide_by_zero_check
    def to_pounds(self):
        return self.value / MICROGRAMS_TO_POUNDS

    @divide_by_zero_check
    def to_ounces(self):
        return self.value / MICROGRAMS_TO_OUNCES


class ImperialTons(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    def to_metric_tonnes(self) -> float:
        return self.value * METRIC_TONNES_TO_IMPERIAL_TONS

    def to_kilograms(self) -> float:
        return self.value * KILOS_TO_IMPERIAL_TONS

    def to_grams(self) -> float:
        return self.value * GRAMS_TO_IMPERIAL_TONS

    def to_milligrams(self) -> float:
        return self.value * MILLIGRAMS_TO_IMPERIAL_TONS

    def to_micrograms(self) -> float:
        return self.value * MICROGRAMS_TO_IMPERIAL_TONS

    def to_imperial_tons(self) -> float:
        return self.value.__float__()

    def to_us_tons(self) -> float:
        return self.value * IMPERIAL_TONS_TO_US_TONS

    def to_stones(self) -> float:
        return self.value * IMPERIAL_TONS_TO_STONES

    def to_pounds(self) -> float:
        return self.value * IMPERIAL_TONS_TO_POUNDS

    def to_ounces(self) -> float:
        return self.value * IMPERIAL_TONS_TO_OUNCES


class USTons(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / METRIC_TONNES_TO_US_TONS

    def to_kilograms(self) -> float:
        return self.value * KILOS_TO_US_TONS

    def to_grams(self) -> float:
        return self.value * GRAMS_TO_US_TONS

    def to_milligrams(self) -> float:
        return self.value * MILLIGRAMS_TO_US_TONS

    def to_micrograms(self) -> float:
        return self.value * MICROGRAMS_TO_US_TONS

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / IMPERIAL_TONS_TO_US_TONS

    def to_us_tons(self) -> float:
        return self.value.__float__()

    def to_stones(self) -> float:
        return self.value * US_TONS_TO_STONES

    def to_pounds(self) -> float:
        return self.value * US_TONS_TO_POUNDS

    def to_ounces(self) -> float:
        return self.value * US_TONS_TO_OUNCES


class Stones(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / METRIC_TONNES_TO_STONES

    def to_kilograms(self) -> float:
        return self.value * KILOS_TO_STONES

    def to_grams(self) -> float:
        return self.value * GRAMS_TO_STONES

    def to_milligrams(self) -> float:
        return self.value * MILLIGRAMS_TO_STONES

    def to_micrograms(self) -> float:
        return self.value * MICROGRAMS_TO_STONES

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / IMPERIAL_TONS_TO_STONES

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / US_TONS_TO_STONES

    def to_stones(self) -> float:
        return self.value.__float__()

    def to_pounds(self) -> float:
        return self.value * STONES_TO_POUNDS

    def to_ounces(self) -> float:
        return self.value * STONES_TO_OUNCES


class Pounds(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / METRIC_TONNES_TO_POUNDS

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / KILOS_TO_POUNDS

    def to_grams(self) -> float:
        return self.value * GRAMS_TO_POUNDS

    def to_milligrams(self) -> float:
        return self.value * MILLIGRAMS_TO_POUNDS

    def to_micrograms(self) -> float:
        return self.value * MICROGRAMS_TO_POUNDS

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / IMPERIAL_TONS_TO_POUNDS

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / US_TONS_TO_POUNDS

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / STONES_TO_POUNDS

    def to_pounds(self) -> float:
        return self.value.__float__()

    def to_ounces(self) -> float:
        return self.value * POUNDS_TO_OUNCES


class Ounces(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self):
        return self.value / METRIC_TONNES_TO_OUNCES

    @divide_by_zero_check
    def to_kilograms(self):
        return self.value / KILOS_TO_OUNCES

    def to_grams(self):
        return self.value * GRAMS_TO_OUNCES

    def to_milligrams(self):
        return self.value * MILLIGRAMS_TO_OUNCES

    def to_micrograms(self):
        return self.value * MICROGRAMS_TO_OUNCES

    @divide_by_zero_check
    def to_imperial_tons(self):
        return self.value / IMPERIAL_TONS_TO_OUNCES

    @divide_by_zero_check
    def to_us_tons(self):
        return self.value / US_TONS_TO_OUNCES

    @divide_by_zero_check
    def to_stones(self):
        return self.value / STONES_TO_OUNCES

    @divide_by_zero_check
    def to_pounds(self):
        return self.value / POUNDS_TO_OUNCES

    def to_ounces(self) -> float:
        return self.value.__float__()
