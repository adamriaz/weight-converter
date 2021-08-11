import unittest

from weight_converter.convert import MetricTonnes, Kilograms, Grams, Milligrams, Micrograms


class TestWeightCase(unittest.TestCase):

    def setUp(self):
        self.tonnes = MetricTonnes(1)
        self.kilograms = Kilograms(1)
        self.grams = Grams(1)
        self.milligrams = Milligrams(1)
        self.micrograms = Micrograms(1)

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
        self.assertEqual(1.574730464015905e-07, test.to_stones(), msg="Expects a float or 1.574730464015905e-07")
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

