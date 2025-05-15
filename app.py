from flask import Flask , render_template , request
import pickle
with open('model.pkl','rb') as file:
    model=pickle.load(file)
app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/ans',methods=['GET',"POST"])
def predict():
        if request.method=='POST':
            print(request.form.get('1_par'))
            print(request.form.get('2_par'))
            print(request.form.get('3_par'))
            print(request.form.get('4_par'))
            p1,p2,p3,p4=request.form.get('1_par'),request.form.get('2_par'),request.form.get('3_par'),request.form.get('4_par')
            p_value=model.predict([[int(p1),int(p2),int(p3),int(p4)]])
        return render_template('ans.html',ans=p_value)
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
    
