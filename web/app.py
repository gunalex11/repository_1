#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from primarity import is_prime, euler_func
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/prim', methods = ['GET', 'POST'])
def primary():
    name_param=request.form.get('name')

    if name_param==None:
        name_param=""

    return flask.render_template(
        'prim.html',
        name=name_param,
        ans=is_prime(name_param),
        method=request.method
    )

@app.route('/eul', methods = ['GET', 'POST'])
def euler():
    name_param=request.form.get('name')

    if name_param==None:
        name_param=""

    return flask.render_template(
        'eul.html',
        name=name_param,
        ans=euler_func(name_param),
        method=request.method
    )


if __name__ == '__main__':
   app.run(debug = True)
