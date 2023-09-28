import joblib
import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def validate_url():
    if request.method=="POST":
        Url=request.form.get('url')

        # processing the url (..pending..)


        result=[1,-1,-1,1,-1,1,-1,1,-1,1,1,1,1,1,0,-1,1,1,1,1,1,1,1,-1,-1,1,-1,1,-1,1]   # expected 1 30Data
        res=[1,1,1,1,1,-1,0,1,1,1,1,1,-1,0,0,-1,-1,-1,0,1,1,1,1,-1,1,1,1,1,-1,-1]  # expected -1

        # arr=np.array(result).reshape(1,31)

        
        loaded_model = joblib.load('rf_model.pkl')
        val=loaded_model.predict([result])[0]



        return f'<h1>{val} is Validated! SAFE to Use</h1>'
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)

