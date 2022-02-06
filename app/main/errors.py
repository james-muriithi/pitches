from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html', error=error),404

@main.app_errorhandler(403)
def four_Ow_three(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html', error=error),403