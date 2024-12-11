from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# 게시판 데이터 저장
posts = []

# 게시판 글 목록 페이지
@app.route('/board')
def board():
    return render_template('board.html', posts=posts)

# 게시판 글 작성 페이지
@app.route('/board/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # 작성된 글 데이터를 저장
        author = request.form['author']
        content = request.form['content']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        posts.append({'author': author, 'content': content, 'date': date})
        return redirect(url_for('board'))  # 작성 후 글 목록 페이지로 리다이렉트
    return render_template('new_post.html')  # GET 요청 시 글 작성 페이지 렌더링

# 홈 페이지
@app.route('/')
def home():
    return render_template('index.html')

# 회사 소개 페이지
@app.route('/about')
def about():
    return render_template('about.html')

# 서비스 소개 페이지
@app.route('/services')
def services():
    return render_template('services.html')

# 연락처 페이지
@app.route('/contact')
def contact():
    return render_template('contact.html')

# 갤러리 페이지
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
