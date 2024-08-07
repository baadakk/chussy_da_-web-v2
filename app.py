 
from flask import Flask, jsonify, render_template
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()  # Load all jobs
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs(): 
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)  # Fetch the job based on the ID
    if job:
        return render_template('jobpage.html', job=job)
    else:
        return jsonify({'error': 'Job not found'}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
