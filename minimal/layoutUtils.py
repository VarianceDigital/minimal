from flask import request

def read_data_from_form():
    record = {}
    for key in request.form:
        record[key] = request.form[key]
        if len(record[key]) == 0:
            record[key]=None
        elif record[key]=='on':
            #checkbox selected!!!
            record[key]=True
    #NOTE: if a checkbox is not selected,
    #      it will NOT be part of the record dict!
    return record


def set_menu(section):
    
    menuconfig = {}
    
    if len(section)>0:
        menuconfig[section]="active"

    return menuconfig
