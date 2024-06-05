"""
    school_data.py
    Author: Yael Gonzalez
    A terminal-based application for computing and printing statistics based on 
    given input.
"""

# Add packages
import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Combine enrollment data for all years into a single array
# First, make a list containing each array 1D array
enrollment_data = [year_2013, year_2014, year_2015, year_2016,
                   year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]
# Then, create a single array with the list (2D, 10x60) and reshape it to a 3D array 10x20x3
# Where 10 = Years, 20 = Schools, 3 = Grades
enrollment_data_array = np.array(enrollment_data).reshape((10, 20, 3))

# Global Variables
# Mapping of year to index for data array
year_to_index = {
    2013: 0,
    2014: 1,
    2015: 2,
    2016: 3,
    2017: 4,
    2018: 5,
    2019: 6,
    2020: 7,
    2021: 8,
    2022: 9
}

# Mapping of school code to school name (used for program logic and as index for data array)
code_to_school = {
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

# Mapping of grade to index for data array
grade_to_index = {
    10: 0,
    11: 1,
    12: 2
}


# Additional classes, functions, variables, etc.
class School:
    """
    A class representing a school with methods to retrieve enrollment statistics.

    This class provides methods to retrieve enrollment data for a specific school,
    as well as for specific grades and years.

    Attributes
    ----------
     name : str
        School name.
    code : str
        School code.
    index : int
        Index used for accessing the data array representing the school.


    Methods
    -------
    enrollments(data_array):
        Retrieves all enrollment data for the school.
    enrollments_by_grade(data_array, grade):
        Retrieves enrollment data for a specific grade in the school.
    enrollments_by_year(data_array, year):
        Retrieves enrollment data for a specific year in the school.
    """

    def __init__(self, name, code):
        self.name = name
        self.code = code
        # Assign index for accessing the data array representing the school
        self.index = list(code_to_school).index(code)

    def enrollments(self, data_array):
        """
        Retrieves all enrollment data for the school.

        Parameters
        ----------
        data_array : ndarray
            The full data array containing enrollment data.

        Returns
        -------
        ndarray
            Array of enrollments for the school.
        """
        return data_array[:, self.index, :]

    def enrollments_by_grade(self, data_array, grade):
        """
        Retrieves enrollment data for a specific grade in the school.

        Parameters
        ----------
        data_array : ndarray
            The full data array containing enrollment data.
        grade : int
            Grade level (10, 11, or 12).

        Returns
        -------
        ndarray
            Array of enrollments for the specified grade.

        Raises
        ------
        ValueError
            If the specified grade is not valid.
        """
        if grade not in grade_to_index:
            raise ValueError(f"Grade must be one of {list(grade_to_index)}.")
        enrollments = self.enrollments(data_array)
        return enrollments[:, grade_to_index[grade]]

    def enrollments_by_year(self, data_array, year):
        """
        Retrieves enrollment data for a specific year in the school.

        Parameters
        ----------
        data_array : ndarray
            The full data array containing enrollment data.
        year : int
            Year for which data is to be retrieved.

        Returns
        -------
        ndarray
            Array of enrollments for the specified year.

        Raises
        ------
        ValueError
            If the year specified is not valid.
        """
        if year not in year_to_index:
            raise ValueError(f"Year must be one of {list(year_to_index)}.")
        enrollments = self.enrollments(data_array)
        return enrollments[year_to_index[year]]


def main():
    """
    Main function to execute the program and print enrollment statistics.
    """
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    # Print the shape and dimensions of the full data array
    print(f"Shape of full data array: {enrollment_data_array.shape}")
    print(f"Dimensions of full data array: {enrollment_data_array.ndim}")

    # Prompt for user input
    selection = input("Please enter the high school name or school code: ")

    # Print Stage 2 requirements here
    # Determine the school name and code based on the user input
    if selection in code_to_school:
        # If the user selected a code, then it should exist as a key in code_to_school dict
        school_name = code_to_school[selection]
        school_code = selection
    elif selection in code_to_school.values():
        # If the user selected a code, then it should exist as a value in code_to_school dict
        school_name = selection
        # 1. Create a list of values in code_to_school and get index of item with school name
        # 2. Create a list of the school codes and use the index found to get the school code
        school_code = list(code_to_school)[list(
            code_to_school.values()).index(school_name)]
    else:
        # If school code or name doesn't exist in code_to_school, raise an exception
        raise ValueError("You must enter a valid school name or code.")

    print("\n***Requested School Statistics***\n")
    # Print school name and code
    print(f"School Name: {school_name}, School Code: {school_code}")

    # Create a School object for the selected school
    school = School(school_name, school_code)

    # Retrieve enrollment statistics for each grade
    grade_10_enrollments = school.enrollments_by_grade(
        enrollment_data_array, 10)
    grade_11_enrollments = school.enrollments_by_grade(
        enrollment_data_array, 11)
    grade_12_enrollments = school.enrollments_by_grade(
        enrollment_data_array, 12)

    # Calculate and print the mean enrollment for each grade using numpy nanmean()
    # Then, explicitly cast it to an integer. Value is already floored after casting
    print(f"Mean enrollment for grade 10: {
          int(np.nanmean(grade_10_enrollments))}")
    print(f"Mean enrollment for grade 11: {
          int(np.nanmean(grade_11_enrollments))}")
    print(f"Mean enrollment for grade 12: {
          int(np.nanmean(grade_12_enrollments))}")

    # 1. Determine the highest enrollment per grade using numpy nanmax for each grade data array
    # 2. Determine the highest value out of all grades and print
    highest_enrollment = max(np.nanmax(grade_10_enrollments), np.nanmax(
        grade_11_enrollments), np.nanmax(grade_12_enrollments))
    print(f"Highest enrollment for a single grade: {
          int(highest_enrollment)}")

    # 1. Determine the lowest enrollment per grade using numpy nanmin for each grade data array
    # 2. Determine the lowest value out of all grades and print
    lowest_enrollment = min(np.nanmin(grade_10_enrollments), np.nanmin(
        grade_11_enrollments), np.nanmin(grade_12_enrollments))
    print(f"Lowest enrollment for a single grade: {
          int(lowest_enrollment)}")

    # Compute and print total enrollments for each year
    yearly_totals = []

    for year in range(2013, 2023):
        # Get all enrollments per year, then calculate the total using nansum
        year_total = np.nansum(school.enrollments_by_year(
            enrollment_data_array, year))
        print(f"Total enrollment for {year}: {
              int(year_total)}")
        # Collect each year total in a list for a next step
        yearly_totals.append(year_total)

    # Use nansum to calculate the total enrollments across all ten years and print
    enrollments_total = np.nansum(school.enrollments(enrollment_data_array))
    print(f"Total ten year enrollment: {
          int(enrollments_total)}")

    # Calculate the mean value over the across all collected years and print
    print(f"Mean total enrollment over {len(yearly_totals)} years: {
          int(np.mean(yearly_totals))}")

    # Check if any enrollments exceed 500 and print the median value if so
    # 1. Obtain all enrollments
    all_enrollments = school.enrollments(enrollment_data_array)
    # 2. Use numpy any() to check if any element in the 2D array is greater than 500
    if np.any(all_enrollments > 500):
        # If at least one element of the 2D array is greater than 500:
        # 1. Filter values greater than 500 using a mask
        # 2. Calculate the median with numpy median() of the filtered values
        filtered_values = all_enrollments[all_enrollments > 500]
        print(f"For all enrollments over 500, the median value was: {
              int(np.median(filtered_values))}")
    else:
        # If no element of the 2D array is greater than 500 print a message
        print("No enrollments over 500.")

    # Print Stage 3 requirements here, i.e., print general statistics for all schools
    print("\n***General Statistics for All Schools***\n")

    # Get enrollments in year 2013 using year_to_index dict and calculate the mean using nanmean()
    enrollments_in_2013 = enrollment_data_array[year_to_index[2013], :, :]
    print(f"Mean enrollment in 2013: {
          int(np.nanmean(enrollments_in_2013))}")

    # Get enrollments in year 2022 using year_to_index. Then calculate & print the mean
    enrollments_in_2022 = enrollment_data_array[year_to_index[2022], :, :]
    print(f"Mean enrollment in 2022: {
          int(np.nanmean(enrollments_in_2022))}")

   # Get graduating class in year 2022, i.e., grade 12. Then calculate & print the total
    grade_12_enrollments_in_2022 = enrollment_data_array[year_to_index[2022],
                                                         :, grade_to_index[12]]
    print(f"Total graduating class of 2022: {
          int(np.nansum(grade_12_enrollments_in_2022))}")

    # Get all enrollments for each grade
    grade_10_enrollments = enrollment_data_array[:, :, grade_to_index[10]]
    grade_11_enrollments = enrollment_data_array[:, :, grade_to_index[11]]
    grade_12_enrollments = enrollment_data_array[:, :, grade_to_index[12]]

    # 1. Determine the highest enrollment per grade using numpy nanmax for each grade data array
    # 2. Determine the highest value out of all grades and print
    highest_enrollment = max(np.nanmax(grade_10_enrollments), np.nanmax(
        grade_11_enrollments), np.nanmax(grade_12_enrollments))
    print(f"Highest enrollment for a single grade: {
          int(highest_enrollment)}")

    # 1. Determine the lowest enrollment per grade using numpy nanmin for each grade data array
    # 2. Determine the lowest value out of all grades and print
    lowest_enrollment = min(np.nanmin(grade_10_enrollments), np.nanmin(
        grade_11_enrollments), np.nanmin(grade_12_enrollments))
    print(f"Lowest enrollment for a single grade: {
          int(lowest_enrollment)}")


if __name__ == '__main__':
    main()
