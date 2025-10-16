# Your name: Vishruth Siddi
# Your student id: 33658544
# Your email: vsiddi@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Myself

import csv
import os

#reading csv into list of dicts
def reading(file):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, file)

    f = open(full_path)
    csv_f = csv.reader(f)

    headers = next(csv_f)
    d_list = []

    for row in csv_f:
        d = {}
        for i in range(len(headers)):
            d[headers[i]] = row[i]
        d_list.append(d)
    
    file.close()
    return d_list

def get_median_yield(d_list):
    yields = []
    string = "Yield_tons_per_hectare"

    for row in d_list:
        if string in row:
            val = float(row[string])
            yields.append(val)

    yields.sort()
    n = len(yields)

    if n % 2 == 1:
        mid = int(n / 2)
        median = yields[mid]
    else:
        mid1 = yields[int(n / 2)]
        mid2 = yields[int((n - 1) / 2)]
        median = (mid1 + mid2) / 2

    return median
    pass

def above_median(d_list, median):
    newd_list = []

    for row in d_list:
        val = float(row["Yields_tons_per_hectare"])
        if val > median:
            newd_list.append(row)
    
    return newd_list
    pass

def calc_avg_rain(newd_list):
    pass

def write_to_txt(median, crop_count, avg_rain):
    pass

def main():
    file = "crop_yield.csv"
    d_list = reading(file)

    median_yield = get_median_yield(d_list)
    newd_list = above_median(d_list, median_yield)
    avg_rain = calc_avg_rain(newd_list)
    crop_count = len(newd_list)

    write_to_txt(median_yield, crop_count, avg_rain)