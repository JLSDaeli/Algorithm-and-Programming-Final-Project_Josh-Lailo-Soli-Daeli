class DayEntry:
    def __init__(self, day_name, sh, sm, sap, eh, em, eap, break_min):
        # Apply the day name.
        self.day_name = day_name
        # Adjust the start time in hour, minute, and AM/PM.
        self.sh = sh
        self.sm = sm
        self.sap = sap
        # Adjust the end time in hour, minute, and AM/PM.
        self.eh = eh
        self.em = em
        self.eap = eap
        # Set the break duration in minutes.
        self.break_min = break_min

    def _to_minutes(self, h, m, ap):
        # Convert the format of 12-hour into total minutes during midnight.
        if ap == "PM" and h != 12:
            h += 12
        # Settle a midnight case.
        if ap == "AM" and h == 12:
            h = 0
        # Return total minutes.
        return h * 60 + m

    def calculate_total_hours(self):
        # Set start time in minutes.
        start = self._to_minutes(self.sh, self.sm, self.sap)
        # Set end time in minutes.
        end = self._to_minutes(self.eh, self.em, self.eap)

        # Calculate the total work minutes subtracting the break time.
        total = end - start - self.break_min
        # Avoid the number of work time below or equal to zero.
        if total <= 0:
            return 0

        # Form minutes into hours and round into 2 decimals.
        return round(total / 60, 2)

class TimeCard:
    def __init__(self, employee_name, date):
        # Apply employee name.
        self.employee_name = employee_name
        # Apply time card date.
        self.date = date
        # List is used to keep entries of daily work.
        self.days = []

    def add_day(self, entry):
        # Settle a DayEntry object on the time card.
        self.days.append(entry)

    def total_work_hours(self):
        # Calculate the total working hours from every DayEntry object.
        return sum(day.calculate_total_hours() for day in self.days)