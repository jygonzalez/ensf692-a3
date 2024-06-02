# school_data.py
# Yael Gonzalez
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Define array for enrollment data: Create a list containing year arrays, create an array using the list and reshape it
enrollment_data = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]
enrollment_data_array = np.array(enrollment_data).reshape((10, 20, 3))

# TODO: Ask about this
# # Clean data (Analysis on how this was done can be found in school_data.pdf)
# # Extract data for each grade from 2013 to 2020 (indices 0 to 7)
# grade_10_data = enrollment_data_array[0:8, 11, 0]
# grade_11_data = enrollment_data_array[0:8, 11, 1]
# grade_12_data = enrollment_data_array[0:8, 11, 2]
# # Compute replacement values
# grade_10_replacement = np.floor(np.mean(grade_10_data)).astype(int)
# grade_11_replacement = np.floor(np.mean(grade_11_data)).astype(int)
# grade_12_replacement = np.floor(np.mean(grade_12_data)).astype(int)
# # Create a copy of the original array to modify
# enrollment_data_clean_array = np.copy(enrollment_data_array)
# # Replace NaN values at the specified locations with the computed replacement values using slicing
# enrollment_data_clean_array[8:10, 11, 0] = grade_10_replacement
# enrollment_data_clean_array[8:10, 11, 1] = grade_11_replacement
# enrollment_data_clean_array[8:10, 11, 2] = grade_12_replacement

# New array, set NaN values to Zero.

mask = np.isnan(enrollment_data_array)
enrollment_data_array[mask] = 0

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
    "9830": "National Sport School",
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
        self.index = list(school_dict.keys()).index(code)
    
    def enrollments(self, data_array):
        return data_array[:, self.index,:]
    
    def enrollments_by_grade(self, data_array, grade): 
        if grade not in [10, 11, 12]:
            raise ValueError("Grade must be one of 10, 11, or 12.")
        enrollments = self.enrollments(data_array)
        grade_index = {10: 0, 11: 1, 12: 2}[grade]
        return enrollments[:, grade_index]
    
    def enrollments_by_year(self, data_array, year): 
        if year not in [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]:
            raise ValueError("Year must be in the range 2013 to 2022.")      
        enrollments = self.enrollments(data_array)
        year_index = {2013: 0, 2014: 1, 2015: 2, 2016: 3, 2017: 4, 2018: 5, 2019: 6, 2020: 7, 2021: 8, 2022: 9}[year]
        return enrollments[year_index]

def mask_zeroes(data_array):
    mask = (data_array == 0)
    return data_array[~mask]


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
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

    # TODO: ask if i should exclude values equal to zero from the mean calculation here 
    print(f"Mean enrollment for grade 10: {np.floor(np.mean(mask_zeroes(grade_10_enrollments))).astype(int)}")
    print(f"Mean enrollment for grade 11: {np.floor(np.mean(mask_zeroes(grade_11_enrollments))).astype(int)}")
    print(f"Mean enrollment for grade 12: {np.floor(np.mean(mask_zeroes(grade_12_enrollments))).astype(int)}")

    highest_enrollment = max(np.max(grade_10_enrollments), np.max(grade_11_enrollments), np.max(grade_12_enrollments))
    print(f"Highest enrollment for a single grade: {np.floor(highest_enrollment).astype(int)}")

    lowest_enrollment = min(np.min(grade_10_enrollments), np.min(grade_11_enrollments), np.min(grade_12_enrollments))    
    print(f"Lowest enrollment for a single grade: {np.floor(lowest_enrollment).astype(int)}")

    format
    yearly_totals = []

    for year in range(2013, 2023):
        year_total = np.sum(school.enrollments_by_year(enrollment_data_array, year))
        yearly_totals.append(year_total)
        print(f"Total enrollment for {year}: {np.floor(year_total).astype(int)}")

    enrollments_total = np.sum(school.enrollments(enrollment_data_array))
    print(f"Total ten year enrollment: {np.floor(enrollments_total).astype(int)}")
    
    # TODO: ask if i should exclude values equal to zero from the mean calculation here 
    filtered_yearly_totals = [value for value in yearly_totals if value != 0]
    print(f"Mean total enrollment over {len(yearly_totals)} years: {np.floor(np.mean(filtered_yearly_totals)).astype(int)}")

    # TODO: ask if i should exclude values equal to zero from the median calculation here
    all_enrollments = school.enrollments(enrollment_data_array) 
    mask = all_enrollments > 500
    # Check if any values are greater than 500
    if np.any(mask):       
        filtered_values = all_enrollments[mask]
        print(f"For all enrollments over 500, the median value was: {np.floor(np.median(filtered_values)).astype(int)}")
    else:
        print("No enrollments over 500.")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    print(f"Mean enrollment in 2013: {np.floor(np.mean(enrollment_data_array[0, :, :])).astype(int)}")

    enrollments_in_2022 = enrollment_data_array[9, :, :] 
    print(f"Mean enrollment in 2022: {np.floor(np.mean(mask_zeroes(enrollments_in_2022))).astype(int)}")
    
    grade_12_enrollments_in_2022 = enrollment_data_array[9, :, 2]
    print(f"Total graduating class of 2022: {np.floor(np.sum(grade_12_enrollments_in_2022)).astype(int)}")

    grade_10_enrollments = enrollment_data_array[:, :, 0]
    grade_11_enrollments = enrollment_data_array[:, :, 1]
    grade_12_enrollments = enrollment_data_array[:, :, 2]

    highest_enrollment = max(np.max(grade_10_enrollments), np.max(grade_11_enrollments), np.max(grade_12_enrollments))
    print(f"Highest enrollment for a single grade: {np.floor(highest_enrollment).astype(int)}")
    
    lowest_enrollment = min(np.min(grade_10_enrollments), np.min(grade_11_enrollments), np.min(grade_12_enrollments))
    print(f"Lowest enrollment for a single grade: {np.floor(lowest_enrollment).astype(int)}")


if __name__ == '__main__':
    main()

