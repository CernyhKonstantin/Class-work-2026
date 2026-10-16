from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user = 'joe_due2025'
    return render_template('index.html', username=user)
    # return "Hello from Flask1"

class contact:
    name: str
    number: str

    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number
    
    def __str__(self) -> str:
        return f"{self.name}: {self.number}"

@app.route("/about")
def about():
    contacts = [
        contact("Joe CEO", "(206) 342-8631"),
        contact("Jack HR", "(717) 550-1675"),
        contact("Bob Manager", "(253) 644-2182"),
        contact("Mike", "(262) 162-15851"),
        contact("Steve", "(201) 874-8593"),
    ]
    return render_template("about.html", contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True, port=8000)