from flask import Flask, render_template
from .models import DB, User, Tweet

# Create a "factory" for serving up the app when it is launched 
def create_app():

    #initializes our Flask app
    app = Flask(__name__)

    # configuration stuff
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Connect our database to our app object
    DB.init_app(app)

    # Make our "Home" or "root" route
    @app.route('/')
    def root():
        users = User.query.all()
        # Do this when somebody hits the home page
        return render_template('base.html', users=users)

    # Test another route
    @app.route('/test')
    def test():
        # removes everything from the DB
        DB.drop_all()
        # creates a new DB with indicated tables
        DB.create_all()
        # Make some Users
        # create a user object from our .models class
        papa = User(id=1, username='BigPapa3k')
        buby = User(id=2, username='Buby')
        # add the user to the database
        DB.session.add(papa)
        DB.session.add(buby)
        
        # Make some tweets
        # display our new user on the page
        # Make some tweets
        tweet1 = Tweet(id=1, text='I am the goat', user=papa)
        tweet2 = Tweet(id=2, text='Tenz get better', user=buby)
        tweet3 = Tweet(id=3, text='Valorant is the best game', user=papa)
        tweet4 = Tweet(id=4, text='Riot needs to close Valorant', user=buby)
        tweet5 = Tweet(id=5, text='I am ranked #1 world wide', user=papa)
        tweet6 = Tweet(id=6, text='I am ranked last', user=buby)

        # add the tweets to the DB Session
        DB.session.add(tweet1)
        DB.session.add(tweet2)
        DB.session.add(tweet3)
        DB.session.add(tweet4)
        DB.session.add(tweet5)
        DB.session.add(tweet6)
        
        # save the database
        DB.session.commit()

        # query to get all users
        users = User.query.all()
        return render_template('base.html', users=users, title='test')




    return app