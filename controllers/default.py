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


def loFinder(mob):
    return loc.index(mob)
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
        return dict(message=db().select(db.Buyer.ALL))
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
def insertSupply(n,p,cr):
    dt = datetime.date.today()
    num= n[len(n)-10:]
    loca=loFinder(num)
    sid=fSellerID(num)
    cid=fCropID(cr)
    db.SupplyList.insert(Price=p,tstamp=dt,loc=loca,seller_id=sid,crop_id=cid)
def fBuyerId(ema,nam):
    insertBuyer(ema,nam)
    for row in db(db.Buyer.email==ema).select():
        return row.id 
@service.run
def insertDemand(mp,ema,nam,cr):
    dt = datetime.date.today()
    bid=fBuyerId(ema,nam)
    cid=fCropID(cr)
    db.DemandList.insert(MaxPrice=mp,tstamp=dt,buyer_id=bid,crop_id=cid)

def displaySlist():
    rows = db((db.SupplyList.crop_id==db.crop.id) & (db.SupplyList.seller_id==db.Seller.id)).select(db.crop.cropName, db.SupplyList.tstamp, db.SupplyList.loc, db.SupplyList.Price,db.Seller.phonenumber)
    return dict(message=rows)
def insertCrop():
    db.crop.insert(cropName='Wheat')
    print "success"
@service.run    
def insertBuyer(e,n):
    db.Buyer.update_or_insert(db.Buyer.email==e,email=e,name=n)
@service.run
def insertSeller(phone):
    db.Seller.update_or_insert(phonenumber=phone)
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
    for x in xrange(0,(len(content)):
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







