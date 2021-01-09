from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    #return '<p>Hello Flask</p>'
    return render_template('index.html')    

@app.route('/mainPage')
def view_topics():
    topics = ['HTML Review','CSS Review','Javascipt Review','Intro to Python', 'First time PI','Intro to Bash', 'Intro to FLASK', 'Web Development']
    #return '<p> this is the main page </p>'
    return render_template('topics.html', topics=topics)


if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1' )

#comment