from flask import Flask, render_template, request
from flask_cors import CORS 
from models import create_post, get_posts, clear_posts
from datetime import datetime

app = Flask(__name__, static_url_path='/static')
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        if request.form['submit']=='postit':
            name = request.form.get('name')
            post = request.form.get('post')
            time = datetime.now().strftime('%H:%M')
            create_post(name, post, time)

        elif request.form['submit']=='clear':
            clear_posts()
        
        else:
            pass

    posts = get_posts()
    
    return render_template('index.html', posts=posts)

@app.route('/delete', methods=['POST'])
def delete():
    clear_posts()


if __name__ == '__main__':
        app.run(debug=True)