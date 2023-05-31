from app import app 
from flask import render_template

@app.route('/')
def index():
    first_name = 'Mason'
    last_name = 'Sinner'
    job_title = 'Full Stack Software Developer, Part Time Baller'
    return render_template('index.html', first_name=first_name, last_name=last_name, job_title=job_title)

@app.route('/favorite_list.html')
def test():
    favorite_teams = ['Dodgers', 'Angels', 'Rangers', 'Red Sox', 'Phillies', 'Astros']
    return render_template('favorite_list.html', favorite_teams=favorite_teams)