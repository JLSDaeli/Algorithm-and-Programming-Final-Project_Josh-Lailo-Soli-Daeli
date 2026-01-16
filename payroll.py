# Wage rate of an hour is used to calculate salaries. 
HOURLY_RATE = 50000

class PayrollCalculator:
    @staticmethod 
    def calculate_daily_salary(hours):
        # Compute a salary of a single day according to data of working hours.
        return hours * HOURLY_RATE
    
    @staticmethod
    def calculate_total_pay(timecard):
        # Operate total salary.
        total_salary = 0

        # Loop is processed for each recorded day from the time card.
        for day in timecard.days:
            # Sum daily salary by the calculated job hours.
            total_salary += PayrollCalculator.calculate_daily_salary(
                day.calculate_total_hours()
            )
        # Return total salary of the whole period of time card.
        return total_salary 