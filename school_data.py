# school_data.py
# Yael Gonzalez
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Clean data
school12_grade10_years_2013_to_2020 = [year_2013.reshape(20, 3)[11][0], year_2014.reshape(20, 3)[11][0], year_2015.reshape(20, 3)[11][0], year_2016.reshape(20, 3)[11][0], year_2017.reshape(20, 3)[11][0], year_2018.reshape(20, 3)[11][0], year_2019.reshape(20, 3)[11][0], year_2020.reshape(20, 3)[11][0]]
school12_grade11_years_2013_to_2020 = [year_2013.reshape(20, 3)[11][1], year_2014.reshape(20, 3)[11][1], year_2015.reshape(20, 3)[11][1], year_2016.reshape(20, 3)[11][1], year_2017.reshape(20, 3)[11][1], year_2018.reshape(20, 3)[11][1], year_2019.reshape(20, 3)[11][1], year_2020.reshape(20, 3)[11][1]]
school12_grade12_years_2013_to_2020 = [year_2013.reshape(20, 3)[11][2], year_2014.reshape(20, 3)[11][2], year_2015.reshape(20, 3)[11][2], year_2016.reshape(20, 3)[11][2], year_2017.reshape(20, 3)[11][2], year_2018.reshape(20, 3)[11][2], year_2019.reshape(20, 3)[11][2], year_2020.reshape(20, 3)[11][2]]

import math

school12_mean_grade10 = math.floor(np.mean(school12_grade10_years_2013_to_2020))
school12_mean_grade11 = math.floor(np.mean(school12_grade11_years_2013_to_2020))
school12_mean_grade12 = math.floor(np.mean(school12_grade12_years_2013_to_2020))

clean_2D_2021 = year_2021.reshape(20, 3)

clean_2D_2021[11][0] = school12_mean_grade10
clean_2D_2021[11][1] = school12_mean_grade11
clean_2D_2021[11][2] = school12_mean_grade12

year_2021_clean = clean_2D_2021.reshape(60)

clean_2D_2022 = year_2022.reshape(20, 3)

clean_2D_2022[11][0] = school12_mean_grade10
clean_2D_2022[11][1] = school12_mean_grade11
clean_2D_2022[11][2] = school12_mean_grade12

year_2022_clean = clean_2D_2022.reshape(60)

# Declare any global variables needed to store the data here
school_dict = {
    "1224": "Centennial High School",
    "1679": "Robert Thirsk School", 
    "9626": "Louise Dean School",
    "9806": "Queen Elizabeth High School",
    "9813": "Forest Lawn High School",
    "9815": "Crescent Heights High School",
    "9816": "Western Canada High School",
    "9823": "Central Memorial High School",
    "9825": "James Fowler High School",
    "9826": "Ernest Manning High School",
    "9829": "William Aberhart High School",
    "9836": "Henry Wise Wood High School",
    "9847": "Bowness High School",
    "9850": "Lord Beaverbrook High School",
    "9856": "Jack James High School",
    "9857": "Sir Winston Churchill High School",
    "9858": "Dr. E. P. Scarlett High School",
    "9860": "John G Diefenbaker High School",
    "9865": "Lester B. Pearson High School"
}


# You may add your own additional classes, functions, variables, etc.
class School:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.index = list(school_dict.keys()).index(code) + 1
    
    def enrollments(self, data_array):
        enrollments = []
        for i in range(data_array.shape[0]):
            enrollments.append(data_array[i][self.index])
        return enrollments
    
    def enrollments_by_grade(self, data_array, grade): 
        if grade not in [10, 11, 12]:
            raise ValueError("Grade must be one of 10, 11, or 12.")

        enrollments = self.enrollments(data_array)
        grade_index = {10: 0, 11: 1, 12: 2}[grade]
        grade_enrollments = [enrollment[grade_index] for enrollment in enrollments]
        return grade_enrollments
    
    def enrollments_by_year(self, data_array, year): 
        if year not in [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]:
            raise ValueError("Year must be in the range 2013 to 2022.")
        
        enrollments = self.enrollments(data_array)
        year_index = {2013: 0, 2014: 1, 2015: 2, 2016: 3, 2017: 4, 2018: 5, 2019: 6, 2020: 7, 2021: 8, 2022: 9}[year]

        year_enrollments = enrollments[year_index]
        return year_enrollments


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    enrollment_data = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]
    enrollment_data_array = np.array(enrollment_data).reshape((10, 20, 3))

    enrollment_clean_data = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021_clean, year_2022_clean]
    enrollment_clean_data_array = np.array(enrollment_clean_data).reshape((10, 20, 3))

    print("Shape of full data array: ", enrollment_data_array.shape)
    print("Dimensions of full data array: ", enrollment_data_array.ndim)    

    # Prompt for user input
    selection = input("Please enter the high school name or school code: ")

    # Print Stage 2 requirements here
    if (selection in school_dict):
        school_name = school_dict[selection]
        school_code = selection
    elif selection in school_dict.values():
        school_name = selection
        school_code = list(school_dict.keys())[list(school_dict.values()).index(school_name)]
    else:
        raise ValueError("You must enter a valid school name or code.")
    
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {school_name}, School Code: {school_code}")

    school = School(school_name, school_code)

    grade_10_enrollments = school.enrollments_by_grade(enrollment_data_array, 10)
    grade_11_enrollments = school.enrollments_by_grade(enrollment_data_array, 11)
    grade_12_enrollments = school.enrollments_by_grade(enrollment_data_array, 12)

    print(f"Mean enrollment for grade 10: {np.floor(np.mean(grade_10_enrollments)).astype(int)}")
    print(f"Mean enrollment for grade 11: {np.floor(np.mean(grade_11_enrollments)).astype(int)}")
    print(f"Mean enrollment for grade 12: {np.floor(np.mean(grade_12_enrollments)).astype(int)}")

    max_enrollments = [max(grade_10_enrollments), max(grade_11_enrollments), max(grade_12_enrollments)]
    
    print(f"Highest enrollment for a single grade: {np.floor(max(max_enrollments)).astype(int)}")

    min_enrollments = [min(grade_10_enrollments), min(grade_11_enrollments), min(grade_12_enrollments)]
    
    print(f"Lowest enrollment for a single grade: {np.floor(min(min_enrollments)).astype(int)}")

    yearly_totals = []
    grand_total = 0

    for year in range(2013, 2023):
        year_total = sum(school.enrollments_by_year(enrollment_data_array, year))
        grand_total = grand_total + year_total
        yearly_totals.append(year_total)
        print(f"Total enrollment for {year}: {np.floor(year_total).astype(int)}")

    print(f"Total ten year enrollment: {np.floor(grand_total).astype(int)}")

    print(f"Mean total enrollment over {len(yearly_totals)} years: {np.floor(np.mean(yearly_totals)).astype(int)}")

    all_enrollments = school.enrollments(enrollment_data_array) # list of 10 arrays each with 3 indexes
    all_enrollments = np.array(all_enrollments) # convert to array and flatten it to 1D
    # Check if any values are greater than 500
    if np.any(all_enrollments > 500):
        mask = all_enrollments > 500
        filtered_values = all_enrollments[mask]
        print(f"For all enrollments over 500, the median value was: {np.floor(np.median(filtered_values)).astype(int)}")
    else:
        print("No enrollments over 500.")

 
    # Mean enrollment for Grade 10 across all years
    # * Mean enrollment for Grade 11 across all years
    # * Mean enrollment for Grade 12 across all years
    # * Highest enrollment for a single grade within the entire time period
    # * Lowest enrollment for a single grade within the entire time period
    # * Total enrollment for each year from 2013 to 2022
	# * Total ten year enrollment
	# * Mean total yearly enrollment over 10 years
    # * Education planners want to better understand the impact of large-scale classes in high schools. Determine if any enrollment numbers were over 500. If not, print “No enrollments over 500.” If yes, print the median value of the >500 enrollments.

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

