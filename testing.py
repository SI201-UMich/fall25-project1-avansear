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

if __name__ == "__main__":
    unittest.main()