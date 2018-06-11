from flask import Blueprint
from flask import render_template
from flask import request
from .froms import PostForm
from models import Post, Tag
from app import db
from flask import redirect, url_for
from flask_security import login_required


posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            pass
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<url_for_pers>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(url_for_pers):
    post = Post.query.filter(Post.url_for_pers==url_for_pers).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', url_for_pers=post.url_for_pers))

    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post, form=form)


@posts.route('/')
def index():

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page=1


    posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=6)


    return render_template('posts/index.html', posts=posts, pages=pages)

@posts.route('/<url_for_pers>')
def post_detail(url_for_pers):
    post = Post.query.filter(Post.url_for_pers==url_for_pers).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)

@posts.route('/tag/<url_for_tag>')
def tag_detail(url_for_tag):
    tag = Tag.query.filter(Tag.url_for_tag==url_for_tag).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)