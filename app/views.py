from app import app
from flask import render_template

algorithms = [
            {
                'title': 'Beam Search',
                'url': 'https://embed-ssl.wistia.com/deliveries/70d6f4e10e2badb5ef394f00c17ad2bc1c14f6e7.jpg'
            },
            {
                'title': 'Binary search',
                'url': 'https://media.geeksforgeeks.org/wp-content/cdn-uploads/20191213191344/Why-Data-Structures-and-Algorithms-Are-Important-to-Learn.png'
            },
            {
                'title': 'Data compression',
                'url': 'https://i.pinimg.com/originals/d5/d0/ec/d5d0ec9a1e4808aff255152ed6cee04e.png'
            },
            {
                'title': 'Dijkstra\'s algorithm',
                'url': 'https://www.simplilearn.com/ice9/free_resources_article_thumb/10-algorithms-machine-learning-engineers-need-to-know-article.jpg'
            },
            {
                'title': 'fibonacci sequence algorithm',
                'url': 'https://holycoders.com/content/images/wordpress/2020/04/fibonacci-sequence-algorithm.png'
            },
            {
                'title': 'Buble Sort Algorithm',
                'url': 'https://www.codedrome.com/wp-content/uploads/2019/06/bubble_sort_python_banner.png'
            },
            {
                'title': 'Merge Sort Algorithm',
                'url': 'https://www.w3schools.in/wp-content/uploads/2016/09/Merge-Sort-Technique-1.png'
            },
            {
                'title': 'Insertion Sort Algorithm',
                'url': 'https://cdn.programiz.com/sites/tutorial2program/files/Insertion-sort-0_1.png'
            },
        ]


@app.route('/')
def home():
    context = {
        'algorithms': algorithms
    }

    return render_template('home.html', context=context)


@app.route('/algorithms')
def view_all_algorithms():
    context = {
        'algorithms': algorithms
    }
    return render_template('algorithms.html', context=context)


@app.route('/algorithms/<string:name>')
def view_algorithm(name):
    context = {
        'name': name
    }
    return render_template('view_algorithm.html', context=context)
