from flask import Flask, render_template
app = Flask(__name__)

@app.route('/lists')
def render_lists():

    person_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Susupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", person = person_info)


if __name__=="__main__":
    app.run(debug=True, port=5001)

