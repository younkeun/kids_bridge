import os
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
        post_id = len(posts) + 1  # 글 ID 생성 (고유값)
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        posts.append({'id': post_id, 'title': title, 'author': author, 'content': content, 'date': date, 'views': 0})
        return redirect(url_for('board'))  # 작성 후 글 목록 페이지로 리다이렉트
    return render_template('new_post.html')

# 글 상세보기 페이지
@app.route('/board/<int:post_id>')
def view_post(post_id):
    # ID에 해당하는 글 찾기
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        post['views'] += 1  # 조회수 증가
        return render_template('view_post.html', post=post)
    else:
        return "글을 찾을 수 없습니다.", 404
    
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


# 이미지 폴더 경로 설정
GALLERY_FOLDER = os.path.join(app.static_folder, 'images', 'gallery')

@app.route('/gallery')
def gallery():
    # gallery 폴더 내 이미지 파일만 필터링
    images = [f for f in os.listdir(GALLERY_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
