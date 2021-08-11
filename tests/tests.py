import unittest

from weight_converter.convert import MetricTonnes, Kilograms, Grams, Milligrams, Micrograms, ImperialTons, USTons, \
    Stones, Pounds, Ounces


class TestWeightCase(unittest.TestCase):

    def setUp(self):
        self.tonnes = MetricTonnes(1)
        self.kilograms = Kilograms(1)
        self.grams = Grams(1)
        self.milligrams = Milligrams(1)
        self.micrograms = Micrograms(1)
        self.imperial_tons = ImperialTons(1)
        self.us_tons = USTons(1)
        self.stones = Stones(1)
        self.pounds = Pounds(1)
        self.ounces = Ounces(1)

    def test_metric_tonnes(self):
        test = self.tonnes
        self.assertEqual(1.0, test.to_metric_tonnes(), msg="Expects a float or 1.0")
        self.assertEqual(1000.0, test.to_kilograms(), msg="Expects a float or 1000.0")
        self.assertEqual(1e6, test.to_grams(), msg="Expects a float or 1000000.0")
        self.assertEqual(1e9, test.to_milligrams(), msg="Expects a float or 1000000000.0")
        self.assertEqual(1e12, test.to_micrograms(), msg="Expects a float or 1000000000000.0")
        self.assertEqual(0.9842065276110608, test.to_imperial_tons(), msg="Expects a float or 0.9842065276110608")
        self.assertEqual(1.1023113109244, test.to_us_tons(), msg="Expects a float or 1.1023113109244")
        self.assertEqual(157.47304441777, test.to_stones(), msg="Expects a float or 157.47304441777")
        self.assertEqual(2204.6226218488, test.to_pounds(), msg="Expects a float or 2204.6226218488")
        self.assertEqual(35273.96194958, test.to_ounces(), msg="Expects a float or 35273.96194958")

    def test_kilograms(self):
        test = self.kilograms
        self.assertEqual(0.001, test.to_metric_tonnes(), msg="Expects a float or 0.001")
        self.assertEqual(1.0, test.to_kilograms(), msg="Expects a float or 1.0")
        self.assertEqual(1e3, test.to_grams(), msg="Expects a float or 1000.0")
        self.assertEqual(1e6, test.to_milligrams(), msg="Expects a float or 1000000.0")
        self.assertEqual(1e9, test.to_micrograms(), msg="Expects a float or 1000000000.0")
        self.assertEqual(0.0009842065276110606, test.to_imperial_tons(), msg="Expects a float or 0.0009842065276110606")
        self.assertEqual(0.001102311310924388, test.to_us_tons(), msg="Expects a float or 0.001102311310924388")
        self.assertEqual(0.1574730444177697, test.to_stones(), msg="Expects a float or 0.1574730444177697")
        self.assertEqual(2.2046226218488, test.to_pounds(), msg="Expects a float or 2.2046226218488")
        self.assertEqual(35.27396194958, test.to_ounces(), msg="Expects a float or 35.27396194958")

    def test_grams(self):
        test = self.grams
        self.assertEqual(1e-6, test.to_metric_tonnes(), msg="Expects a float or 0.000001")
        self.assertEqual(0.001, test.to_kilograms(), msg="Expects a float or 0.001")
        self.assertEqual(1.0, test.to_grams(), msg="Expects a float or 1.0")
        self.assertEqual(1e3, test.to_milligrams(), msg="Expects a float or 1000.0")
        self.assertEqual(1e6, test.to_micrograms(), msg="Expects a float or 1000000.0")
        self.assertEqual(9.842065276110607e-07, test.to_imperial_tons(), msg="Expects a float or 9.842065276110607e-07")
        self.assertEqual(1.102311310924388e-06, test.to_us_tons(), msg="Expects a float or 1.102311310924388e-06")
        self.assertEqual(0.00015747304441776972, test.to_stones(), msg="Expects a float or 0.00015747304441776972")
        self.assertEqual(0.002204622621848776, test.to_pounds(), msg="Expects a float or 0.002204622621848776")
        self.assertEqual(0.035273961949580414, test.to_ounces(), msg="Expects a float or 0.035273961949580414")

    def test_milligrams(self):
        test = self.milligrams
        self.assertEqual(1e-9, test.to_metric_tonnes(), msg="Expects a float or 1e-9")
        self.assertEqual(1e-6, test.to_kilograms(), msg="Expects a float or 1e-6")
        self.assertEqual(0.001, test.to_grams(), msg="Expects a float or 0.001")
        self.assertEqual(1.0, test.to_milligrams(), msg="Expects a float or 1.0")
        self.assertEqual(1e3, test.to_micrograms(), msg="Expects a float or 1000.0")
        self.assertEqual(9.842065276110607e-10, test.to_imperial_tons(), msg="Expects a float or 9.842065276110607e-10")
        self.assertEqual(1.102311310924388e-09, test.to_us_tons(), msg="Expects a float or 1.102311310924388e-09")
        self.assertEqual(1.574730444177697e-07, test.to_stones(), msg="Expects a float or 1.574730444177697e-07")
        self.assertEqual(2.204622621848776e-06, test.to_pounds(), msg="Expects a float or 2.204622621848776e-06")
        self.assertEqual(3.5273961949580415e-05, test.to_ounces(), msg="Expects a float or 3.5273961949580415e-05")

    def test_micrograms(self):
        test = self.micrograms
        self.assertEqual(1e-12, test.to_metric_tonnes(), msg="Expects a float or 1e-12")
        self.assertEqual(1e-9, test.to_kilograms(), msg="Expects a float or 1e-9")
        self.assertEqual(1e-6, test.to_grams(), msg="Expects a float or 1e-6")
        self.assertEqual(0.001, test.to_milligrams(), msg="Expects a float or 0.001")
        self.assertEqual(1.0, test.to_micrograms(), msg="Expects a float or 1.0")
        self.assertEqual(9.842065276110605e-13, test.to_imperial_tons(), msg="Expects a float or 9.842065276110605e-13")
        self.assertEqual(1.1023113109243879e-12, test.to_us_tons(), msg="Expects a float or 1.1023113109243879e-12")
        self.assertEqual(1.5747304441776971e-10, test.to_stones(), msg="Expects a float or 1.5747304441776971e-10")
        self.assertEqual(2.204622621848776e-09, test.to_pounds(), msg="Expects a float or 2.204622621848776e-09")
        self.assertEqual(3.5273961949580413e-08, test.to_ounces(), msg="Expects a float or 3.5273961949580413e-08")

    def test_imperial_tons(self):
        test = self.imperial_tons
        self.assertEqual(1.0160469088, test.to_metric_tonnes(), msg="Expects a float or 1.0160469088")
        self.assertEqual(1016.0469088, test.to_kilograms(), msg="Expects a float or 1016.0469088")
        self.assertEqual(1016046.9088, test.to_grams(), msg="Expects a float or 1016046.9088")
        self.assertEqual(1016046908.8, test.to_milligrams(), msg="Expects a float or 1016046908.8")
        self.assertEqual(1016046908800, test.to_micrograms(), msg="Expects a float or 1016046908800")
        self.assertEqual(1.0, test.to_imperial_tons(), msg="Expects a float or 1.0")
        self.assertEqual(1.12, test.to_us_tons(), msg="Expects a float or 1.12")
        self.assertEqual(160, test.to_stones(), msg="Expects a float or 160")
        self.assertEqual(2240, test.to_pounds(), msg="Expects a float or 2240")
        self.assertEqual(35840, test.to_ounces(), msg="Expects a float or 35840")

    def test_us_tons(self):
        test = self.us_tons
        self.assertEqual(0.90718473999999, test.to_metric_tonnes(), msg="Expects a float or 0.90718473999999")
        self.assertEqual(907.18474, test.to_kilograms(), msg="Expects a float or 907.18474")
        self.assertEqual(907184.74, test.to_grams(), msg="Expects a float or 907184.74")
        self.assertEqual(907184740, test.to_milligrams(), msg="Expects a float or 907184740")
        self.assertEqual(907184740000, test.to_micrograms(), msg="Expects a float or 907184740000")
        self.assertEqual(0.8928571428571428, test.to_imperial_tons(), msg="Expects a float or 0.8928571428571428")
        self.assertEqual(1.0, test.to_us_tons(), msg="Expects a float or 1.0")
        self.assertEqual(142.85714285714286, test.to_stones(), msg="Expects a float or 142.85714285714286")
        self.assertEqual(2000, test.to_pounds(), msg="Expects a float or 2000")
        self.assertEqual(32000, test.to_ounces(), msg="Expects a float or 32000")

    def test_stones(self):
        test = self.stones
        self.assertEqual(0.006350293179999987, test.to_metric_tonnes(), msg="Expects a float or 0.006350293179999987")
        self.assertEqual(6.35029318, test.to_kilograms(), msg="Expects a float or 6.35029318")
        self.assertEqual(6350.29318, test.to_grams(), msg="Expects a float or 6350.29318")
        self.assertEqual(6350293.18, test.to_milligrams(), msg="Expects a float or 6350293.18")
        self.assertEqual(6350293180, test.to_micrograms(), msg="Expects a float or 6350293180")
        self.assertEqual(0.00625, test.to_imperial_tons(), msg="Expects a float or 0.00625")
        self.assertEqual(0.007, test.to_us_tons(), msg="Expects a float or 0.007")
        self.assertEqual(1.0, test.to_stones(), msg="Expects a float or 1.0")
        self.assertEqual(14, test.to_pounds(), msg="Expects a float or 14")
        self.assertEqual(224, test.to_ounces(), msg="Expects a float or 224")

    def test_pounds(self):
        test = self.pounds
        self.assertEqual(0.000453592369999995, test.to_metric_tonnes(), msg="Expects a float or 0.000453592369999995")
        self.assertEqual(0.453592369999995, test.to_kilograms(), msg="Expects a float or 0.453592369999995")
        self.assertEqual(453.59237, test.to_grams(), msg="Expects a float or 453.59237")
        self.assertEqual(453592.37, test.to_milligrams(), msg="Expects a float or 453592.37")
        self.assertEqual(453592370, test.to_micrograms(), msg="Expects a float or 453592370")
        self.assertEqual(0.0004464285714285714, test.to_imperial_tons(), msg="Expects a float or 0.0004464285714285714")
        self.assertEqual(0.0005, test.to_us_tons(), msg="Expects a float or 0.0005")
        self.assertEqual(0.07142857142857142, test.to_stones(), msg="Expects a float or 0.07142857142857142")
        self.assertEqual(1.0, test.to_pounds(), msg="Expects a float or 1.0")
        self.assertEqual(16, test.to_ounces(), msg="Expects a float or 16")

    def test_ounces(self):
        test = self.ounces
        self.assertEqual(2.834952312500033e-05, test.to_metric_tonnes(), msg="Expects a float or 2.834952312500033e-05")
        self.assertEqual(0.028349523125000334, test.to_kilograms(), msg="Expects a float or 0.028349523125000334")
        self.assertEqual(28.349523125, test.to_grams(), msg="Expects a float or 28.349523125")
        self.assertEqual(28349.523125, test.to_milligrams(), msg="Expects a float or 28349.523125")
        self.assertEqual(28349523.125, test.to_micrograms(), msg="Expects a float or 28349523.125")
        self.assertEqual(2.7901785714285713e-05, test.to_imperial_tons(), msg="Expects a float or 2.7901785714285713e-05")
        self.assertEqual(3.125e-05, test.to_us_tons(), msg="Expects a float or 3.125e-05")
        self.assertEqual(0.004464285714285714, test.to_stones(), msg="Expects a float or 0.004464285714285714")
        self.assertEqual(0.0625, test.to_pounds(), msg="Expects a float or 0.0625")
        self.assertEqual(1.0, test.to_ounces(), msg="Expects a float or 1.0")








