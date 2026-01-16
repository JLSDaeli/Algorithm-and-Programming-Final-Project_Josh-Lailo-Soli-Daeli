DAELI'S TIMESHEET (TIME CARD CALCULATOR)

The time card calculator is a function payroll computational system created with Python and Flask. 
Its application leads the inputting of employees' working shifts in weekly and calculates total hours and salary
with controlling a consistent record of every entry.

Solution Design:
The project is shaped with the pattern of Model-View-Controller (MVC). The edit maintains a proper separation
of concerns holding the system sustainable and scalable.
  a. The model including model.py and payroll.py works as the actual source. It clarifies the data systems for 
    shifts and has the financial equations to compute wages.
  b. The view including renderer.py handles the presentation layer. It applies HTML and CSS functionalities
    to shape the user-facing forms and the advanced payroll results with its details.
  c. The controller including controller.py works as the orchestrator. It grabs user input via Flask controlling
    with the Model for computations, and delivers data to the view for display.

Core Algorithms and Logic:
The systematic core of the project is the control of non-decimal time data by Normalization.

1. Time Normalization
The project system sets every time input in a linear integer format (Total Minutes since Midnight) to prevent
issues of mathematical functions in AM/PM.
  a. Equation: (Hours x 60) + Minutes
  b. If PM is picked to the clock management, 12 hours are collected to sum the total.

3. Duration and Overnight Shifts
  a. Developed Calculation: (End Minutes - Start Minutes) - Break Minutes
  b. In controller.py, the system uses 24 hours for the end time to confirm proper positive duration
    if the end time is less than the start time.

5. Data Structures Used
  a. DayEntry shapes the concept of individual shift data, and TimeCard works as an aggregate container for the week.
  b. TimeCard applies a list to keep the DayEntry objects in set that leading the system to operate through workdays
   for summation.
  c. Data is arranged into dictionaries for storage from history.json leading for consistent, human-readable information.

Implementation Details: 
a. Entry Point (main.py) operates the Flask server and routing.
b. Persistence (storage.py) settle every calculation on history.json for long-term tracking.
c. Validation (validator.py) repairs user inputs to avoid math errors or function damages.
d. Observability (logger.py) collects information of system events and mistakes for troubleshooting.
e. Configuration (config.py) maximizes global settings, such as DEBUG mode and HOURLY_RATE.

Procedure:
1. Install Flask (pip install flask)
2. Initialize the application (python main.py)
3. Open a browser with http://127.0.0.1:5000

  
