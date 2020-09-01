from flask import Flask 
app = Flask(__name__) 
  
@app.route('/<name>') 
def rev(name):
     name = "".join(reversed(name))
     return 'Reversed string is %s' %name

 
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True) 
