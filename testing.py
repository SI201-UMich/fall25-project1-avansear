import unittest
from main import get_median_yield, above_median, calc_avg_rain

class TestCalc(unittest.TestCase):
    
    #testing get_median_yield general case 1
    def test1(self):
        data = [
            {"Yield_tons_per_hectare": "5.0"},
            {"Yield_tons_per_hectare": "10.0"},
            {"Yield_tons_per_hectare": "7.0"}
        ]
        self.assertEqual(get_median_yield(data), 7.0)

    #testing get_median_yield general case 2
    def test2(self):
        

if __name__ == "__main__":
    unittest.main()