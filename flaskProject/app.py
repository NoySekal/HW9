from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '123456789'


USERS_DB ={
              'adi1':{'fname':'Adi','Email':'adi1@gmail.com','Phone':'0544934111'},
              'noy2': {'fname': 'Noy', 'Email': 'noy2@gmail.com', 'Phone': '0544934222'},
              'noy3': {'fname': 'Noy', 'Email': 'noy3@gmail.com', 'Phone': '0544934333'},
              'noy4': {'fname': 'Noy', 'Email': 'noy4@gmail.com', 'Phone': '0544934444'},
              'noy5': {'fname': 'Noy', 'Email': 'noy5@gmail.com', 'Phone': '0544934555'}
          }

@app.route('/')
def home_func():  # put application's code here
    return render_template('homepage.html')

@app.route('/CV')
def CV_func():  # put application's code here
    return render_template('CV.html')

@app.route('/About')
def About_func():  # put application's code here
    return render_template('About.html',
                           profile={'name': 'Noy', 'second_name': 'Sekal'},
                           university='BGU',
                           degrees=['BA', 'Mc'],
                           hobbies=('art', 'dance', 'music', 'dogs', 'web'))

@app.route('/Catalog')
def Catalog_func():
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('Catalog.html', p_product = product, p_size = size)
    return render_template('Catalog.html')

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    if request.method == 'GET':
        username =''
        email =''
        fname =''
        if 'UserName' in request.args:
            username = request.args['UserName']
        if username in USERS_DB:
            fname = USERS_DB[username]['fname']
            email = USERS_DB[username]['Email']
        return render_template('assignment9.html', p_username=username, p_email=email, p_fname=fname, p_users_db=USERS_DB, p_submit=True)

    p_registration = True
    if p_registration:
        if request.method == 'POST':
            UserName = request.form['UserName']
            Email = request.form['Email']
            Phone = request.form['Phone']
            Password = request.form['Password']
            session['UserName'] = UserName
        return redirect(url_for('assignment9_func', p_registration= False))
    return redirect(url_for('assignment9_func'))
    #return request(url_for('Catalog_fחצצצunc'))
    #return render_template('assignment9.html')

    @app.route('/login', methods=['GET', 'POST'])
    def Login_func():  # put application's code here
        if request.method == 'GET':
            return render_template('login.html')

        if request.method == 'POST':
            # DB
            UserName = request.form['UserName']
            password = request.form['password']

            found = True
            if found:
                session ['UserName'] = UserName
                return redirect(url_for('home_func'))
            else:
                return render_template('Login_func')
           # return render_template('login.html', UserName=UserName)

        @app.route('/logout')
        def logout_func():  # put application's code here
            for k,v in session.items():
                if 'UserName' in k:
                    session[k]= ''
            session['UserName'] = ''
            return render_template('homepage.html')


if __name__ == "__main__":
    app.secret_key = '123'
    app.run(debug=True)
