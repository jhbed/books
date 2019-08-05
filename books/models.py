from books import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20))
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    is_fiction = db.Column(db.Boolean, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    star_rating = db.Column(db.Integer, nullable=False)
    is_must_read = db.Column(db.Boolean, nullable=False)
    other_notes = db.Column(db.Text)

    def __repre__(self):
        return f'Title: {self.title}, By: {self.author}'