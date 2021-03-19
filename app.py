#!/usr/bin/python3
from habit_maker import Habit
from flask import Flask, render_template, redirect, jsonify
from flask import request


app = Flask(__name__)

habitList = []


@app.route("/update_decimal", methods=["POST"])
def updatedecimal():
    id = int(request.form.get("id"))
    for i in range(1, len(habitList)+1):
        try:
            if i == id:
                print("chosen id: ", id)
                obj = habitList[id-1]
                obj.addCount()
                count = obj.count
                name = obj.name
                location = obj.location
                time = obj.time
                print(count)
                return jsonify('', render_template("count.html",
                                                   count=count,
                                                   id=id,
                                                   name=name,
                                                   time=time,
                                                   location=location,
                                                   newclass="newclass"))
        except Exception:
            raise


@app.route('/', methods=["GET", "POST"])
def home_page():
    classlist = []
    if len(habitList) > 0:
        for obj in habitList:
            obj.press()
            if obj.count == 0:
                newclass = "learn-more"
                classlist.append(newclass)
            else:
                newclass = "newclass"
                classlist.append(newclass)
        return render_template(
            "home.html", objList=habitList, classlist=classlist)
    else:
        return render_template(
            "home.html", objList=habitList, count=0, newclass="learn-more")


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        habitName = request.form.get("habitName")
        location = request.form.get("location")
        time = request.form.get("time")
        print("time is: ", time)
        hour, minu = time.split(":")
        if int(hour) < 12:
            # if int(hour) < 10:
                # time = hour[1] + ":" + minu + "am"
            # else:
            time = hour + ":" + minu + "am"
        elif int(hour) == 12:
            time = hour + ":" + minu + "m"
        else:
            time = str(int(hour)-12) + ":" + minu + "pm"
        # obj is a new insatnce of the class Habit
        obj = Habit(habitName, location, time)
        habitList.append(obj)
        return redirect("/")
    return render_template("new.html")


if __name__ == "__main__":
    app.run(debug=True)
