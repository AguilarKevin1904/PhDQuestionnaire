from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

from models.entities.question import Question

# Models:
from models.ModelUser import ModelUser
from models.Modelquestion import ModelQuestion

#Entities
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form.get('fullname'), None, request.form.get('password'))
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('adminPanel'))
            else:
                flash("Invalid password...")
                return render_template('login.html')
        else:
            flash("User not found...")
            return render_template('login.html')
    else:   
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(0, request.form.get('fullname'), request.form.get('email'), request.form.get('password'))
        ModelUser.registerUser(db,user)
        return render_template('login.html')
    else:
        return render_template('register.html')
    
@app.route('/adminPanel', methods=['GET', 'POST'])
@login_required
def adminPanel():
    if request.method == 'POST':
        question = Question(0, request.form.get('newQuestion'))
        ModelQuestion.addQuestion(db, question)
        print('pregunta añadida exitosmente')
        return render_template('adminPanel.html')
    else:
        return render_template('adminPanel.html')
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/protected')
@login_required
def protected():
    return "<h1> Esta es una vista protegida, solo para usuarios autenticados.</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1> Pagina no encontrada </h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()