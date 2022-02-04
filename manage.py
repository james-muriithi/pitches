from email.policy import default
from app import create_app
from flask_script import Manager,Server
from decouple import config

app = create_app(config('env', default="development"))

manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()