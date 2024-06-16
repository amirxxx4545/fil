from flask import Flask


app=Flask(__name__)

@app.route('/')
def s_name():
    return "hi my name amir"




@app.route('/name<name>')
def say_name(name):
    return f"hi my name{name}"
    

@app.route("/amir")
def ori_name():
    return " <h1>say_ name _ali_mohammd</h1>"

if __name__=="__main__":
    app.run(debug=True)
    
    
