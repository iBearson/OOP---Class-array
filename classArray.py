from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Initializes attributes name and age 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Objects of people class
people = [
    Person("Jason", 23),
    Person("Frank", 31),
    Person("Kendrick", 34),
    Person("Lamelo", 21),
    Person("Al Pacino", 53)
]

def get_people_data():
    data = [{"ID": i+1, "Name": person.name, "Age": person.age} for i, person in enumerate(people)]
    return pd.DataFrame(data).to_dict(orient="records")

# Home route to display table
@app.route('/')
def index():
    people_data = get_people_data()
    return render_template("index.html", people=people_data)

# Function to add a person to the list
@app.route('/add', methods=['POST'])
def add_person():
    name = request.form['name']
    age = int(request.form['age'])
    people.append(Person(name, age))
    return redirect(url_for('index'))

# Function to remove a person from the list
@app.route('/remove/<int:id>')
def remove_person(id):
    if 1 <= id <= len(people):
        del people[id - 1]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
