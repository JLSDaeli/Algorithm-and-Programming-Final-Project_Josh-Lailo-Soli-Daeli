# import request object from Flask to connect form data and HTTP functions
from flask import request
# import data models to be used on time card and daily work entries
from model import TimeCard, DayEntry
# import renderer to lead the presentation of HTML pages
from renderer import PageRenderer

#List of days is set to arrange and adjust form inputs.
DAYS = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

def index():
    # If the request method is GET, present the input form.
    if request.method == "GET":
        return PageRenderer.render_form()
    
    # collect an employee name from the form which is filled
    name = request.form.get("name", "")
    # construct date string from the inputs of day, month, and year
    date = f"{request.form.get('day')} {request.form.get('month')} {request.form.get('year')}"

    # Form a TimeCard object for an employee's name and a report date
    card = TimeCard(name, date)

    # The loop is formed, and it processes through each weekly day
    for d in DAYS:
        # Grab start hour and end hour inputs
        sh = request.form.get(f"{d}_s_h")
        eh = request.form.get(f"{d}_e_h")

        # If a start or end hour is unknown, skip the day.
        if not sh or not eh:
            continue

        # Form a DayEntry object with specific details about full time
        entry = DayEntry(
            d,                                          # Day name
            int(sh),                                    # Start hour
            int(request.form.get(f"{d}_s_m", 0)),       # Start minute
            request.form.get(f"{d}_s_ap", "AM"),        # Start AM/PM
            int(eh),                                    # End hour
            int(request.form.get(f"{d}_e_m", 0)),       # End minute
            request.form.get(f"{d}_e_ap", "PM"),        # End AM/PM
            int(request.form.get(f"{d}_break", 0))      # Break time in minutes
        )

        # add the day's entry with the time card
        card.add_day(entry)

    # calculate total work hours for the week
    total_hours = card.total_work_hours()
    # calculate total salary following the hourly rate
    total_salary = total_hours * 50000

    # Distribute the result page following the calculated data
    return PageRenderer.render_result(card, total_hours, total_salary)