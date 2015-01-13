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
import loc
import mailz
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))

def prepareMail():
    rows = db((db.SupplyList.crop_id==db.DemandList.crop_id) & (db.SupplyList.seller_id==db.Seller.id) & (db.DemandList.buyer_id==db.Buyer.id) &(db.SupplyList.crop_id==db.crop.id) & (db.SupplyList.Price<=db.DemandList.MaxPrice)).select(orderby=db.Buyer.id)
    first=rows[0].Buyer.email
    blist=[]
    info=[]
    flist=[[],[]]
    listing=""
    blist.append(first)
    for row in rows:
        if row.Buyer.email!=first:
            first=row.Buyer.email
            blist.append(row.Buyer.email)
    for x1 in blist:
        x2 = db((db.SupplyList.crop_id==db.DemandList.crop_id) & (db.SupplyList.seller_id==db.Seller.id) & (db.DemandList.buyer_id==db.Buyer.id) &(db.SupplyList.crop_id==db.crop.id) & (db.SupplyList.Price<=db.DemandList.MaxPrice) &(db.Buyer.email==x1)).select(orderby=db.Buyer.id)    
        for x3 in x2:
            tlist=("Crop:"+x3.crop.cropName+"\n"+"Seller Quoted Price:"+str(x3.SupplyList.Price)+"\n"+"Seller Phone:"+str(x3.Seller.phonenumber)+"\n"+"Seller Location:"+x3.SupplyList.loc+"\n"+"Date Posted:"+str(x3.SupplyList.tstamp)+"\n")
            listing=listing+"\n\n\n"+tlist
        info.append(listing)
        listing=""    
    for x in xrange(0,(len(blist))):
        flist[0].append(blist[x])
        flist[1].append(info[x])
    return flist

def sendMail():
    content=prepareMail()
    for x in xrange(0,(len(content))):
        mailz.index(content[0][x],"Farket Report for "+str(datetime.date.today()),content[1][x])    
def tryone():
    return "Great success!"






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







