from flask import render_template
from app import app

@app.route('/')

@app.route('/index')

def index():
    user = {'username': 'Garan'}
    posts = [
        {
            'author':{'username':'John'},
            'body': 'Beautiful day in Porland!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Averangers movie was so cool!'

        }
    ]
    
    
    
    
    return render_template('index.html',title='Home',user=user,posts=posts)



