from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


posts = []
post_count = 1



@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/create', methods=['GET','POST'])
def create_post():
    global post_count
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'id':post_count, 'title': title, 'content': content})
        post_count += 1
        return redirect(url_for('home'))
    return render_template('create_post.html')


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
