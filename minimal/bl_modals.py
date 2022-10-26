from flask import (
    Blueprint, render_template, url_for, flash
)
from .layoutUtils import *
from .auth import *

bp = Blueprint('bl_modals', __name__, url_prefix='/modals')

@bp.route('/',methods=('GET', 'POST'))
@manage_cookie_policy
def testmodals():
    mc = set_menu("test")

    error=0
    
    if request.method == 'POST':
        if 'btn_error' in request.form:
            error=9 #SHOW ERROR n. 9
        elif 'btn_alert' in request.form:
            flash("Msg1") #SEE incl_modal.py -> shows first message in popup
        elif 'btn_msg' in request.form:
            flash('Msg2')
            return redirect(url_for('bl_home.index')) 

    return render_template('modals/testmodals.html', mc=mc, error=error)


