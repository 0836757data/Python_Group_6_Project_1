from flask import Flask, render_template
import sqlite3
import pathlib

main = Flask(__name__) # Flask is a class

base_path = pathlib.Path().cwd()
db_name = "Austin_bicycle.db"
file_path = base_path / db_name


@main.route("/")
def index():
    return render_template( "content.html")

@main.route("/about")
def about():
    return render_template( "about_APD.html")

@main.route("/data")
def data():
    con = sqlite3.connect(file_path)
    cursor = con.cursor()
    APD_data = cursor.execute("SELECT * FROM Austin_data").fetchall()
    con.close()
    return render_template( "APD_Crash_data.html", APD_data = APD_data)


if __name__=="__main__":
    main.run(debug=True)