from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded list of papers (title, author, year)
papers = [
    {"title": "Attention Is All You Need", "author": "Vaswani et al.", "year": 2017},
    {"title": "BERT: Pre-training of Deep Bidirectional Transformers", "author": "Devlin et al.", "year": 2018},
    {"title": "Generative Adversarial Nets", "author": "Goodfellow et al.", "year": 2014},
]

@app.route('/')
def index():
    query = request.args.get('q', '')
    sort_by = request.args.get('sort', '')

    filtered = [p for p in papers if query.lower() in p['title'].lower() or query.lower() in p['author'].lower()]

    if sort_by == 'year':
        filtered = sorted(filtered, key=lambda x: x['year'], reverse=True)

    return render_template('index.html', papers=filtered, query=query, sort_by=sort_by)

@app.route('/add', methods=['POST'])
def add_paper():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    papers.append({"title": title, "author": author, "year": int(year)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
