from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_uploads import configure_uploads, IMAGES, UploadSet
from flask_security import Security

from manager.database import db,migrate,user_datastore

from manager.book.views import mod as book,covers
from manager.student.views import mod as student,dps

def create_app():
    app=Flask(__name__)
    app.register_blueprint(book,url_prefix='/books')
    app.register_blueprint(student,url_prefix='/student')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/manager'
    app.config['UPLOADED_COVERS_DEST']='manager/book/static/uploads/covers'
    app.config['UPLOADED_DPS_DEST']='manager/student/static/uploads/dps'
    app.config['USER_ENABLED_EMAIL']=False
    app.config['SECURITY_PASSWORD_SALT']='ROHIT'
    app.config['SECRET_KEY']='ROHIT'
    app.config['SECURITY_LOGIN_USER_TEMPLATE']='login.html'
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
    
app=create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

configure_uploads(app,covers)
configure_uploads(app,dps)

security = Security(app, user_datastore)