# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################
import datetime
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def test():
    return "some stuff"
def displayCrop():
    clist=[]
    for row in db().select(db.crop.ALL):
        x = row.cropName + " "
        clist.append(x)
    return dict(message=clist)
   
def displayBuyer():
    Blist=[[],[]]
    count=0
    for row in db().select(db.Buyer.ALL):
        x = row.email + " "
        y = row.name + " " 
        Blist[len(Blist):].append(x)
        Blist[len(Blist):].append(y)
        count=count+1
    return dict(message=Blist)
@service.run
def fSellerID(num):
    insertSeller(num)
    for row in db(db.Seller.phonenumber==num).select():
        return row.id
@service.run
def fCropID(crName):
    for row in db(db.crop.cropName==crName).select():
        return row.id
@service.run
def insertSupply(num,p,cr):
    dt = datetime.date.today()
    loca="India"
    sid=fSellerID(num)
    cid=fCropID(cr)
    db.SupplyList.insert(Price=p,tstamp=dt,loc=loca,seller_id=sid,crop_id=cid)
    return "yay"
def displaySlist():
    return dict(message=db().select(db.SupplyList.ALL))

    




def insertCrop():
    db.crop.insert(cropName='Wheat')
    print "success"
@service.run    
def insertBuyer(e,n):
    db.Buyer.insert(email=e,name=n)
    return "inserted email "+e+" and name"
@service.run
def insertSeller(phone):
    db.Seller.update_or_insert(phonenumber=phone)

    
def tryone():
    return 'sample'






def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

# def concat(a,b):
#     db.crop.insert(cropName=a)
#     print "abra"
#     return a+b
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
@service.run
def concat(a,b):
    db.crop.insert(cropName=a)
    print "abra"
    return a+b

"""@auth.requires_login() """
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)







