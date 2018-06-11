from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    title = StringField('Post Title')
    body = TextAreaField('Text for post')
