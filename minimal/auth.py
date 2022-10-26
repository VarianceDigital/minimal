import functools
from flask import current_app
from flask import (
    Blueprint, g, redirect, request, session
)

import os

bp = Blueprint('auth', __name__, url_prefix='/auth')


#IMPORTANT! Called for every request
@bp.before_app_request
def pre_operations(): 

    #ALL STATIC REQUESTS BYPASS!!!
    if request.endpoint == 'static':
        return

    #REDIRECT http -> https
    if 'DYNO' in os.environ:
        current_app.logger.critical("DYNO ENV !!!!")
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)
            
    g.policyCode = 0 #SET DEFAULT INDEPENDENTLY TO WRAPPER

#WRAPPER FOR COOKIE SETTINGS 
def manage_cookie_policy(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):

        if request.method == 'POST':
            if 'btnAgreeAll' in request.form:
                session['cookie-policy'] = 3
            elif 'btnAgreeEssential' in request.form:
                session['cookie-policy'] = 0
            elif 'btnSaveCookieSettings' in request.form:
                session['cookie-policy'] = 0 #default
                if 'checkboxAnalysis' in request.form:
                    session['cookie-policy'] = 1
                if 'checkboxPersonalization' in request.form:
                    session['cookie-policy'] = 2
                if 'checkboxPersonalization' in request.form and 'checkboxAnalysis' in request.form:
                    session['cookie-policy'] = 3

        policyCode = session.get("cookie-policy")
        #possible values Null -> no info, 0 -> minimal, 1 -> Analysis, 
        #                                 2 -> Personalization, 3 -> All
        g.policyCode = 0
        if policyCode !=None:
            g.policyCode = policyCode

        g.showCookieAlert = False #DEFAULT
        if policyCode == None:
            g.showCookieAlert = True


        return view(**kwargs)

    return wrapped_view
