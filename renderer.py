class PageRenderer:

    @staticmethod
    def render_form():
        # List of weekly days for creating table rows.
        days = [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday"
        ]

        # Assisting function is used to creating time input fields including hour, minute, and AM/PM.
        def time_input(prefix):
            return f"""
            <input type="number" name="{prefix}_h" min="1" max="12"
                    style="width:45px" placeholder="--">
            :
            <input type="number" name="{prefix}_m" min="0" max="59"
                    style="width:45px" placeholder="--">
            <select name="{prefix}_ap">
                <option value="AM">AM</option>
                <option value="PM">PM</option>
            </select>
            """
        
        # Construct table rows of each weekly day.
        rows = ""
        for d in days:
            rows += f"""
            <tr>
                <td>{d}</td>
                <td>{time_input(d + "_s")}</td>
                <td>{time_input(d + "_e")}</td>
                <td>
                    <input type="number" name"{d}_break" min="0"
                            value="0" style="width:60px"> min
                </td>
            </td>
            """
        # Return the completed page in HTML structure for the input form.
        return f"""
        <html>
        <head>
            <title>Josh's Timesheet</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f4f7fb;
                }}
                .card {{
                    background: #fff;
                    width: 900px;
                    margin: 40px auto;
                    padding: 25px;
                    border-radius: 12px;
                    box-shadow: 0 10px 25px rgba(0,0,0,.1);
                }}
                h2 {{
                    text-align: center;
                    color: #0d6efd;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th {{
                    background: #0d6efd;
                    color: white;
                    padding: 10px;
                }}
                td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: center;
                }}
                .btn {{
                    background: #0d6efd;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    margin-top: 15px;
                }}
                .btn:hover {{
                    background: #084298;
                }}
                .header-input {{
                    margin-bottom: 10px;
                }}
            </style>
        </head>
        <body>

        <div class="card">
            <h2>Josh's Timesheet</h2>

            <form method="POST">

                <div class="header-input">
                    <label>Name:</label>
                    <input name="name">
                </div>

                <div class="header-input">
                    <label>Date:</label>
                    <select name="day">
                        {''.join(f"<option>{i}</option>" for i in range(1,32))}
                    </select>
                    <select name="month">
                        {''.join(f"<option>{m}</option>" for m in [
                            "January","February","March","April","May","June",
                            "July","August","September","October","November","December"
                        ])}
                    </select>
                    <select name="year">
                        {''.join(f"<option>{y}</option>" for y in range(2023,2031))}
                    </select>
                </div>

                <table>
                    <tr>
                        <th>Day</th>
                        <th>Start</th>
                        <th>End</th>
                        <th>Break</th>
                    </tr>
                    {rows}
                </table>

                <button class="btn" type="submit">Calculate Payroll</button>

            </form>
        </div>

        </body>
        </html>
        """
    
    @staticmethod
    def render_result(card, total_hours, total_salary):
        # Create table rows to enhance payroll results.
        rows = ""

        for day in card.days:
            # Compute work hours of each day
            hours = day.calculate_total_hours()

            # Jump over days without work hours.
            if hours <= 0:
                continue

            rows += f"""
            <tr>
                <td>{day.day_name}</td>
                <td>{hours:.2f}</td>
                <td>Rp {hours * 50000:,.0f}</td>
            </tr>
            """

        # Return the completed page in HTML structure for payroll summary.
        return f"""
        <html>
        <head>
            <title>Payroll Summary</title>
            <style>
                body {{
                    font-family: Arial;
                    background: #f4f7fb;
                }}
                .card {{
                    .background: white;
                    width: 700px;
                    margin: 40px auto;
                    padding: 25px;
                    border-radius: 12px;
                    box-shadow: 0 10px 25px rgba(0,0,0,.1);
                }}
                th {{
                    background: #198754;
                    color: white;
                    padding: 8px;
                }}
                td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: center;
                }}
                .btn {{
                    background: #198754;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 6px;
                }}
            </style>
        </head>
        <body>

        <div class="card">
            <h2>Payroll Summary</h2>

            <p><strong>Name:</strong> {card.employee_name}</p>
            <p><strong>Date:</strong> {card.date}</p>

            <table width="100%">
                <tr>
                    <th>Day</th>
                    <th>Hours</th>
                    <th>Salary (Rp)</th>
                </tr>
                {rows}
            </table>

            <h3>Total Hours: {total_hours:.2f}</h3>
            <h3>Total Salary: Rp {total_salary:,.0f}</h3>

            <button class="btn" onclick="window.print()">Print Payroll</button>
            <br><br>
            <a href="/">Back</a>
        </div>

        </body>
        </html>
        """
    