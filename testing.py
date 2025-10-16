import unittest
from main import get_median_yield, above_median, calc_avg_rain

class TestCalc(unittest.TestCase):
    
    #get_median_yield general case 1
    def test1(self):
        data = [
            {"Yield_tons_per_hectare": "5.0"},
            {"Yield_tons_per_hectare": "10.0"},
            {"Yield_tons_per_hectare": "7.0"}
        ]

        self.assertEqual(get_median_yield(data), 7.0)

    #get_median_yield general case 2
    def test2(self):
        data = [
            {"Yield_tons_per_hectare": "3.0"},
            {"Yield_tons_per_hectare": "6.0"},
            {"Yield_tons_per_hectare": "9.0"},
            {"Yield_tons_per_hectare": "12.0"}
        ]

        self.assertEqual(get_median_yield(data), 7.5)

    #get_median_yield edge case 1
    def test3(self):
        data = [
            {"Yield_tons_per_hectare": "4.0"},
            {"Yield_tons_per_hectare": "4.0"},
            {"Yield_tons_per_hectare": "4.0"}
        ]

        self.assertEqual(get_median_yield(data), 4)
    
    #get_median_yield edge case 2
    def test4(self):
        data = [
            {"Yield_tons_per_hectare": "15.0"}
        ]

        self.assertEqual(get_median_yield(data), 15)

    #above_median general case 1
    def test5(self):
        data = [
            {"Yield_tons_per_hectare": "5.0"},
            {"Yield_tons_per_hectare": "10.0"},
            {"Yield_tons_per_hectare": "7.0"}
        ]

        result = above_median(data, 6.0)
        self.assertEqual(len(result), 2)

    #above_median general case 2
    def test6(self):
        data = [
            {"Yield_tons_per_hectare": "5.0"},
            {"Yield_tons_per_hectare": "10.0"},
            {"Yield_tons_per_hectare": "7.0"}
        ]

        result = above_median(data, 7.0)
        self.assertEqual(len(result), 1)

    #above_median edge case 1
    def test7(self):
        data = [
            {"Yield_tons_per_hectare": "5.0"},
            {"Yield_tons_per_hectare": "5.0"}
        ]

        result = above_median(data, 5.0)
        self.assertEqual(len(result), 0)

    #above_median edge case 2
    def test8(self):
        data = [
            {"Yield_tons_per_hectare": "12.0"}
        ]

        result = above_median(data, 10.0)
        self.assertEqual(len(result), 1)

    #calc_avg_rain general case 1
    def test9(self):
        data = [
            {"Rainfall_mm": "100"},
            {"Rainfall_mm": "200"},
            {"Rainfall_mm": "150"}
        ]

        avg = (100 + 200 + 150) / 3
        self.assertAlmostEqual(calc_avg_rain(data), avg)

    #calc_avg_rain general case 2
    def test10(self):
        data = [
            {"Rainfall_mm": "50"},
            {"Rainfall_mm": "75"},
            {"Rainfall_mm": "125"},
            {"Rainfall_mm": "100"}
        ]

        avg = (50 + 75 + 125 + 100) / 4
        self.assertAlmostEqual(calc_avg_rain(data), avg)

    #calc_avg_rain edge case 1
    def test11(self):
        data = [
            {"Rainfall_mm": "300"}
        ]

        self.assertAlmostEqual(calc_avg_rain(data), 300.0)

    #calc_avg_rain edge case 2
    def test12(self):
        data = [
            {"Rainfall_mm": "0"},
            {"Rainfall_mm": "0.5"},
            {"Rainfall_mm": "0.2"}
        ]

        avg = (0 + 0.5 + 0.2) / 3
        self.assertAlmostEqual(calc_avg_rain(data), avg)

def main():
    pass

if __name__ == "__main__":
    unittest.main()