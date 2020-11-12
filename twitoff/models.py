"""SQLAlchemy models and utility functions for Twitoff Application"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

#User table
class User(DB.Model):
    """Twitter User Table that will correspond to tweets - SQLAlchemy syntax"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    name = DB.Column(DB.String, nullable=False) # name column
    newest_tweet_id = DB.Column(DB.BigInteger) #keeps track of user tweet

    def __repr__(self):
        return "<User: {}>".format(self.name)

# Tweet table
class Tweet(DB.Model):
    """Tweet text data - associated with Users table"""
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False) #
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey("user.id"), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)


def insert_example_users():
    """We will get an error if we run this twice without dropping and creating"""
    user1 = add_or_update_user()
    DB.session.add(nick)
    DB.session.add(elon)
    DB.session.commit()

def insert_example_tweets():
    tweet1 = Tweet(id=1, text="Writing fake tweets is annoying", user_id=1)
    tweet2 = Tweet(id=2, text="I love how Lambda School teaches me to be better",
                   user_id=1)
    tweet3 = Tweet(id=3, text="Mars is up for grabs!", user_id=2)
    tweet4 = Tweet(id=4, text="I'm a big fan of rockets", user_id=2)
    tweet5 = Tweet(id=5, text="One day I will be a teacher and I will wear Harry Potter glasses",
                   user_id=1)
    tweet6 = Tweet(id=6, text="Are you really even famous if you can pronounce your kid's name",
                   user_id=2)
    DB.session.add(tweet1)
    DB.session.add(tweet2)
    DB.session.add(tweet3)
    DB.session.add(tweet4)
    DB.session.add(tweet5)
    DB.session.add(tweet6)
    DB.session.commit()

