# -*- coding: utf-8 -*-
"""
Created on Mon May 18 03:38:00 2020

@author: madnoorkar shivam
"""

from flask import Flask,render_template,request
import pickle
model=pickle.load(open("bool_of_active.pkl","rb"))
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("fitness.html")
@app.route("/login",methods=["POST"])
def login():
    sc=request.form['sc']
    s=request.form['a']
    if(s=="sad"):
        s1=100
    if(s=="neutral"):
        s1=200
    if(s=="happy"):
        s1=300
    hs=request.form['hs']
    cb=request.form['cb']
    w=request.form['w']
    total=[[int(sc),s1,int(cb),int(hs),int(w)]]
    y_pred=model.predict(total)
    if y_pred == 0:
        y_pred= "in active"
    else:
        y_pred="active"
    print(y_pred)
    return render_template('fitness.html',showcase=y_pred)
if __name__=="__main__":
    app.run(debug=False)