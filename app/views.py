from flask import render_template, redirect, url_for, session
from app.forms import StoryForm
from app.story import Event, Story
from app import app

@app.before_request
def set_up_story():
    if 'story' not in session.keys():
        session['story'] = Story()

@app.route('/', methods=['GET', 'POST'])
def index():
    storyform = StoryForm()

    if storyform.validate_on_submit():
        session['story'].start_location = storyform.location.data
        return redirect(url_for("timing"))

    return render_template("index.html", storyform=storyform)

@app.route('/timing', methods=['GET', 'POST'])
def timing():
    storyform = StoryForm()

    if storyform.validate_on_submit():
        session['story'].start_time = storyform.time.data
        return redirect(url_for('events'))

    return render_template("timing.html", storyform=storyform)

@app.route('/events', methods=['GET', 'POST'])
def events():
    storyform = StoryForm()

    if storyform.validate_on_submit():
        if storyform.event_name.data not in ['Stop', 'stop', 'STOP']:
            session['story'].events.append(storyform.event_name.data)
            return render_template("events.html", storyform=storyform)
        else:
            return redirect(url_for("finale"))

@app.route("/finale")
def finale():
    return "Hello, world!"