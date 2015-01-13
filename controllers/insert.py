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
def user():
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
def loFinder(mob):
    return loc.index(mob)
def fBuyerId(ema,nam):
    Buyer(ema,nam)
    for row in db(db.Buyer.email==ema).select():
        return row.id 
def fSellerID(num):
    Seller(num)
    for row in db(db.Seller.phonenumber==num).select():
        return row.id
def fCropID(crName):
    for row in db(db.crop.cropName==crName).select():
        return row.id
@service.run
def Supply(n,p,cr):
    dt = datetime.date.today()
    num= n[len(n)-10:]
    loca=loFinder(num)
    sid=fSellerID(num)
    cid=fCropID(cr)
    db.SupplyList.insert(Price=p,tstamp=dt,loc=loca,seller_id=sid,crop_id=cid)
@service.run
def Demand(mp,ema,nam,cr):
    dt = datetime.date.today()
    bid=fBuyerId(ema,nam)
    cid=fCropID(cr)
    db.DemandList.insert(MaxPrice=mp,tstamp=dt,buyer_id=bid,crop_id=cid)
@service.run
def Crop(cropN):
    db.crop.insert(cropName=cropN)
@service.run    
def Buyer(e,n):
    db.Buyer.update_or_insert(db.Buyer.email==e,email=e,name=n)
@service.run
def Seller(phone):
    db.Seller.update_or_insert(phonenumber=phone)
