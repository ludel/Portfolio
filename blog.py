#!/usr/bin/python
# -*- coding: latin-1 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', titre="Ludovic DELSOL - Portfolio")

@app.route('/etude')
def etude():
    return render_template('etude.html', titre="Portfolio Ludovic DELSOL - Etude")

@app.route('/experience')
def experience():
    return render_template('experience.html', titre="Portfolio Ludovic DELSOL - Experiences Pros")

@app.route('/competence')
def compentence():
    return render_template('compentence.html', titre="Portfolio Ludovic DELSOL - Compétences")

@app.route('/projet')
def project():
    return render_template('projet.html', titre="Portfolio Ludovic DELSOL - Projets")


if __name__ == '__main__':
    app.run(debug=True)
