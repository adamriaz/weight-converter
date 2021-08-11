from weight_converter.interfaces import IUnit
from weight_converter.utils import divide_by_zero_check


class MetricTonnes(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    def to_metric_tonnes(self) -> float:
        return self.value.__float__()

    def to_kilograms(self) -> float:
        return self.value * 1e3

    def to_grams(self) -> float:
        return self.value * 1e6

    def to_milligrams(self) -> float:
        return self.value * 1e9

    def to_micrograms(self) -> float:
        return self.value * 1e12

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / 1.0160469088

    def to_us_tons(self) -> float:
        return self.value * 1.1023113109244

    def to_stones(self) -> float:
        return self.value * 157.47304441777

    def to_pounds(self) -> float:
        return self.value * 2204.6226218488

    def to_ounces(self) -> float:
        return self.value * 35273.96194958


class Kilograms(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / 1e3

    def to_grams(self) -> float:
        return self.value * 1e3

    def to_kilograms(self) -> float:
        return self.value.__float__()

    def to_milligrams(self) -> float:
        return self.value * 1e6

    def to_micrograms(self) -> float:
        return self.value * 1e9

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / 1016.0469088

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / 907.18474

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / 6.35029318

    def to_pounds(self) -> float:
        return self.value * 2.2046226218488

    def to_ounces(self) -> float:
        return self.value * 35.27396194958


class Grams(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / 1e6

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / 1e3

    def to_grams(self) -> float:
        return self.value.__float__()

    def to_milligrams(self) -> float:
        return self.value * 1e3

    def to_micrograms(self) -> float:
        return self.value * 1e6

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / 1016046.9088

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / 907184.74

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / 6350.29318

    @divide_by_zero_check
    def to_pounds(self) -> float:
        return self.value / 453.59237

    @divide_by_zero_check
    def to_ounces(self) -> float:
        return self.value / 28.349523125


class Milligrams(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / 1e9

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / 1e6

    @divide_by_zero_check
    def to_grams(self) -> float:
        return self.value / 1e3

    def to_milligrams(self) -> float:
        return self.value.__float__()

    def to_micrograms(self) -> float:
        return self.value * 1e3

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / 1016046908.8

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / 907184740

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / 6350293.1

    @divide_by_zero_check
    def to_pounds(self) -> float:
        return self.value / 453592.37

    @divide_by_zero_check
    def to_ounces(self) -> float:
        return self.value / 28349.523125


class Micrograms(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self) -> float:
        return self.value / 1e12

    @divide_by_zero_check
    def to_kilograms(self) -> float:
        return self.value / 1e9

    @divide_by_zero_check
    def to_grams(self) -> float:
        return self.value / 1e6

    @divide_by_zero_check
    def to_milligrams(self) -> float:
        return self.value / 1e3

    def to_micrograms(self) -> float:
        return self.value.__float__()

    @divide_by_zero_check
    def to_imperial_tons(self) -> float:
        return self.value / 1016046908800

    @divide_by_zero_check
    def to_us_tons(self) -> float:
        return self.value / 907184740000

    @divide_by_zero_check
    def to_stones(self) -> float:
        return self.value / 6350293180

    @divide_by_zero_check
    def to_pounds(self):
        return self.value / 453592370

    @divide_by_zero_check
    def to_ounces(self):
        return self.value / 28349523.125


class ImperialTons(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    def to_metric_tonnes(self):
        return self.value * 1.016

    def to_kilograms(self):
        return self.value * 1016

    def to_grams(self):
        return self.value * 1.016e6

    def to_milligrams(self):
        return self.value * 1.016e9

    def to_micrograms(self):
        return self.value * 1.016e12

    def to_us_tons(self):
        return self.value * 1.12

    def to_stones(self):
        return self.value * 160

    def to_pounds(self):
        return self.value * 2240

    def to_ounces(self):
        return self.value * 35840


class USTons(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self):
        return self.value / 1.102

    def to_kilograms(self):
        return self.value * 907

    def to_grams(self):
        return self.value * 907185

    def to_milligrams(self):
        return self.value * 9.072e+8

    def to_micrograms(self):
        return self.value * 9.072e+11

    @divide_by_zero_check
    def to_imperial_tons(self):
        return self.value / 1.12

    def to_stones(self):
        return self.value * 143

    def to_pounds(self):
        return self.value * 2000

    def to_ounces(self):
        return self.value * 32000


class Stones(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self):
        return self.value / 157

    def to_kilograms(self):
        return self.value * 6.35

    def to_grams(self):
        return self.value * 6350

    def to_milligrams(self):
        return self.value * 6.35e+6

    def to_micrograms(self):
        return self.value * 6.35e9

    @divide_by_zero_check
    def to_imperial_tons(self):
        return self.value / 160

    @divide_by_zero_check
    def to_us_tons(self):
        return self.value / 143

    def to_pounds(self):
        return self.value * 14

    def to_ounces(self):
        return self.value * 224


class Pounds(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self):
        return self.value / 2205

    @divide_by_zero_check
    def to_kilograms(self):
        return self.value / 2.205

    def to_grams(self):
        return self.value * 454

    def to_milligrams(self):
        return self.value * 453592

    def to_micrograms(self):
        return self.value * 4.536e+8

    @divide_by_zero_check
    def to_imperial_tons(self):
        return self.value / 2240

    @divide_by_zero_check
    def to_us_tons(self):
        return self.value / 2000

    @divide_by_zero_check
    def to_stones(self):
        return self.value / 14

    def to_ounces(self):
        return self.value * 16


class Ounces(IUnit):

    def __init__(self, value: float = 1.0):
        self.value = value

    @divide_by_zero_check
    def to_metric_tonnes(self):
        return self.value / 16

    @divide_by_zero_check
    def to_kilograms(self):
        return self.value / 35.274

    def to_grams(self):
        return self.value * 28.35

    def to_milligrams(self):
        return self.value * 28350

    def to_micrograms(self):
        return self.value * 2.835e7

    @divide_by_zero_check
    def to_imperial_tons(self):
        return self.value / 35840

    @divide_by_zero_check
    def to_us_tons(self):
        return self.value / 32000

    @divide_by_zero_check
    def to_stones(self):
        return self.value / 224

    @divide_by_zero_check
    def to_pounds(self):
        return self.value / 16
