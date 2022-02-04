from email.policy import default
from app import create_app, db
from flask_script import Manager,Server
from decouple import config

app = create_app(config('env', default="development"))

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db)

if __name__ == '__main__':
    manager.run()