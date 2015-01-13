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
def Crop():
    clist=[]
    for row in db().select(db.crop.ALL):
        x = row.cropName + " "
        clist.append(x)
    return dict(message=clist)
def Buyer():
    for row in db().select(db.Buyer.ALL):
        return dict(message=db().select(db.Buyer.ALL))
def Supply():
    rows = db((db.SupplyList.crop_id==db.crop.id) & (db.SupplyList.seller_id==db.Seller.id)).select(db.crop.cropName, db.SupplyList.tstamp, db.SupplyList.loc, db.SupplyList.Price,db.Seller.phonenumber)
    return dict(message=rows)
def Demand():
    rows = db((db.DemandList.crop_id==db.crop.id) & (db.DemandList.buyer_id==db.Buyer.id)).select(db.crop.cropName,db.DemandList.tstamp,db.DemandList.MaxPrice,db.Buyer.name,db.Buyer.email)
    return dict(message=rows)
def Seller():
    return dict(message=db().select(db.Seller.ALL))
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




