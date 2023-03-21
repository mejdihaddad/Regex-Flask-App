from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/regEx', methods=['POST', 'GET'])
def matched():
    show=''
    if request.method=='POST':
       testString = request.form.get('Test-String')
       regEx = request.form.get('RegEx')
       matched=re.findall(regEx,testString)
       if len(matched)==0:
           show='no  match found'
       else :
           show=str(matched)
    return render_template('regEx.html',show=show)

if __name__ == '__main__':
    app.run(debug=True)