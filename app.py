from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def calculate_orbit_degree(birthdate):
    day_of_year = birthdate.timetuple().tm_yday
    degree = (day_of_year / 365.25) * 360
    return degree

def degree_to_date(degree, year):
    day_of_year = int((degree / 360) * 365.25)
    astro_date = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)
    return astro_date

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birth_str = request.form["birthdate"]
        birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
        degree = calculate_orbit_degree(birthdate)
        current_year = datetime.now().year
        astro_date = degree_to_date(degree, current_year)

        return render_template("result.html",
                               original=birthdate.strftime("%B %d, %Y"),
                               degree=round(degree, 2),
                               synced=astro_date.strftime("%B %d, %Y"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
