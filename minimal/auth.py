import functools
from flask import current_app
from flask import (
    Blueprint, g, redirect, request, session, Response
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
            
    g.policyCode = -1 #SET DEFAULT INDEPENDENTLY TO WRAPPER
    policyCode = session.get("cookie-policy")
    #possible values Null -> no info, 0 -> Strict, 1 -> Minimal, 
    #                                 2 -> Analisys, 3 -> All
    if policyCode !=None:
        g.policyCode = policyCode


#WRAPPER FOR COOKIE SETTINGS 
def manage_cookie_policy(view):

    @functools.wraps(view)
    def wrapped_view(**kwargs):

        g.showCookieAlert = False #DEFAULT
        if g.policyCode == -1:
            g.showCookieAlert = True

        return view(**kwargs)

    return wrapped_view


@bp.route('/ajcookiepolicy/',methods=('GET', 'POST'))
def ajcookiepolicy():
    #DECIDE COOKIE PREFERENCE STRATEGY
    if request.method == 'POST':
        data = request.json
        btn_name = data['btnselected']
        checkbox_analysis = data['checkboxAnalysis']
        checkbox_necessary = data['checkboxNecessary']
        if btn_name == 'btnAgreeAll':
            session['cookie-policy'] = 3
        elif btn_name == 'btnAgreeEssential':
            session['cookie-policy'] = 1
        elif btn_name == 'btnSaveCookieSettings':
            session['cookie-policy'] = 0 #default
            if checkbox_necessary and not checkbox_analysis:
                session['cookie-policy'] = 1
            elif checkbox_analysis and not checkbox_necessary:
                #never happends if main checkbox disabled!
                session['cookie-policy'] = 2
            elif checkbox_necessary and checkbox_analysis:
                session['cookie-policy'] = 3

    return Response(status=204)