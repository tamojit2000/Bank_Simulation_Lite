from flask import Flask,render_template,request,redirect
from function import *







app=Flask(__name__)

@app.route('/')
def login():
    C_F,B_F,B_P,L_F=run()
    #display()
    if B_P<0:
        color='red'
    else:
        color='green'
    return render_template('login.html',c_f=formalize(C_F),b_f=formalize(B_F),b_p=formalize(B_P),l_f=formalize(L_F),col=color)



if __name__=='__main__':

    app.run(debug=True)
