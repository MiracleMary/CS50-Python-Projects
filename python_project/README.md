# PROJECT TITLE: CGPA_Calculator

#### Video Demo: <https://youtu.be/NQNUt4Dkxbk>

#### Description:
    The CGPA_Calculator program is designed to calculate a student's CGPA for a semester using the grading system of the University of Ilorin, Kwara State, Nigeria. The program allows users to input either their scores or grades, calculates the CGPA, and provides feedback based on the calculated grade point.

    #Features
        Input options for both scores and grades.
        Conversion of scores to grades based on the specified grading system.
        Calculation of grade points and CGPA.
        Output of grade class with encouraging words based on the CGPA

    #How It Works
        Initial Prompt:
            This is the first step in setting up the necessary information to perform the CGPA calculation.
            The program prompts the user to enter the total number of courses registered and the total units of the courses for the semester.
        Input Preference:
            The user is asked whether they would like to input their scores or grades.
            This flexibility allows the user to choose the method that is most convenient for them. Scores are numerical values typically ranging from 0 to 100, while grades are letter representations of performance.
        Course Details:
            Scores Input: If the user chooses to input scores, they enter each course score along with the respective course unit. The program will then convert these scores into grades based on the predefined grading system.
            Grades Input: If the user chooses to input grades, they enter each course grade along with the respective course unit. This method bypasses the need for score-to-grade conversion and directly uses the provided grades for CGPA calculation.
        Calculation and Display:
           Once the user has entered the required details for all courses, the program calculates the CGPA for the semester. It then displays the grade point and the respective grade class. The program also provides words of advice to encourage the user based on their performance, offering motivation and constructive feedback.
    #project.py
        The project.py file contains the main logic for the CGPA_Calculator program. Here are the key components:
        #Functions
            main()
                Prompts the user for the number of courses, total units, and input preference (scores or grades).
                Calls the compute() function to perform the CGPA calculation.
            convert_scores_to_grades(score)
                This function ensures that scores are translated into the appropriate grades.
                Converts numerical scores to letter grades based on the specified grading system.
            grade_weight(grade, units)
                This function multiplies the grade points by the course units to determine the contribution of each course to the overall CGPA.
                Calculates the weighted grade points for a given grade and course units.
            grade_class(gp)
                It categorizes the CGPA into different classes and offers encouraging words based on the class.
                Provides feedback based on the calculated grade point (gp).
            compute(no_of_courses, total_units, preference)
                Manages the input of course details and performs the CGPA calculation.
                Ensures the total units match the inputted values and handles exceptions, ensuring the integrity of the calculation process.
        #Running the Program
            Execute the program using the following command:
            python project.py
            This command will start the program and prompt the user to input the necessary information to calculate their CGPA.


    #test_project.py
        The test_project.py file contains tests for the main functions in the project.py file. Here are the key components:

        #Tests
            test_convert_scores_to_grades()
                Tests the convert_scores_to_grades function with different score inputs.
                Ensures that the function correctly converts scores to the appropriate grades.
            test_grade_weight()
                Tests the grade_weight function with different grade and unit inputs.
                Verifies that the function accurately calculates the weighted grade points.
            test_grade_class()
                Tests the grade_class function with different grade point inputs.
                Confirms that the function provides the correct feedback based on the CGPA.

        #Running Tests
            To run the tests, use the following command:
            pytest test_project.py

