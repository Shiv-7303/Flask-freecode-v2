from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analysts',
        'location': 'Mumbai, India',
        'salary':'Rs. 15,00,0000'
    },
    {
        'id':2,
        'title':'Python Engineer',
        'location': 'Delhi, India',
        'salary':'Rs. 25,00,0000'
    },
    {
        'id':3,
        'title':'Web Developer',
        'location': 'Remote',
    },
    {
        'id':4,
        'title':'Backend Developer',
        'location': 'Remote',
        'salary':'Rs. 51,00,0000'
    },
]


@app.route("/")
def hello_world():
    return render_template("index.html", jobs = JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
    
    
    
if __name__ == "__main__":
    app.run(debug=True)