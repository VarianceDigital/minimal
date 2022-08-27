from flask import render_template

#ERROR HANDLERS
def error_404(e):
    #mc is for the menu highlighting, which in this case should not be set
    return render_template('errorpages/error404.html',mc=""),404

def error_500(e):
    #mc is for the menu highlighting, which in this case should not be set
    return render_template('errorpages/error500.html',mc=""),500
