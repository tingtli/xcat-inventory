#!/usr/bin/python
from dbsession import *
from copy import *
from sqlalchemy import inspect
import pdb

class mixin(object):
    def getdict(self):
        mydict={}
        for mykey in self.__dict__.keys():
           if mykey in self.__table__.columns:
              mydict[self.__tablename__+'.'+mykey.encode()]= self.__dict__[mykey] if self.__dict__[mykey] is None else self.__dict__[mykey].encode()
        try:
            self.__class__.outprocess(mydict)
        except:
            pass 
        return mydict

    @classmethod
    def getkey(cls):
        ins = inspect(cls)
        return ins.primary_key[0].key

########################################################################
class passwd(Base,mixin):
    """"""
    __tablename__ = 'passwd'
    __table_args__ = {'autoload':True}

########################################################################
'''
class networks(Base,mixin):
    """"""
    __tablename__ = 'networks'
    __table_args__ = {'autoload':True}
'''
########################################################################
class networks(Base,mixin):
    """"""
    __tablename__ = 'networks'
    __table_args__ = {'autoload':True}

########################################################################
class nodetype(Base,mixin):
    """"""
    __tablename__ = 'nodetype'
    __table_args__ = {'autoload':True} 

########################################################################
'''
class hosts(Base,mixin):
    """"""
    __tablename__ = 'hosts'
    __table_args__ = {'autoload':True}
'''
########################################################################
class noderes(Base,mixin):
    """"""
    __tablename__ = 'noderes'
    __table_args__ = {'autoload':True}

########################################################################
class switch(Base,mixin):
    """"""
    __tablename__ = 'switch'
    __table_args__ = {'autoload':True}
########################################################################
class switches(Base,mixin):
    """"""
    __tablename__ = 'switches'
    __table_args__ = {'autoload':True}
########################################################################
class mac(Base,mixin):
    """"""
    __tablename__ = 'mac'
    __table_args__ = {'autoload':True}
########################################################################
class postscripts(Base,mixin):
    """"""
    __tablename__ = 'postscripts'
    __table_args__ = {'autoload':True}
    
########################################################################
class bootparams(Base,mixin):
    """"""
    __tablename__ = 'bootparams'
    __table_args__ = {'autoload':True}

########################################################################
class nodelist(Base,mixin):
    """"""
    __tablename__ = 'nodelist'
    __table_args__ = {'autoload':True}

########################################################################
class vm(Base,mixin):
    """"""
    __tablename__ = 'vm'
    __table_args__ = {'autoload':True}
########################################################################
class nodehm(Base,mixin):
    """"""
    __tablename__ = 'nodehm'
    __table_args__ = {'autoload':True}
########################################################################
class nodegroup(Base,mixin):
    """"""
    __tablename__ = 'nodegroup'
    __table_args__ = {'autoload':True}
########################################################################
class vpd(Base,mixin):
    """"""
    __tablename__ = 'vpd'
    __table_args__ = {'autoload':True}
########################################################################
class servicenode(Base,mixin):
    """"""
    __tablename__ = 'servicenode'
    __table_args__ = {'autoload':True}
########################################################################
class hosts(Base,mixin):
    """"""
    __tablename__ = 'hosts'
    __table_args__ = {'autoload':True}
########################################################################
class nics(Base,mixin):
    """"""
    __tablename__ = 'nics'
    __table_args__ = {'autoload':True}
#----------------------------------------------------------------------

def query_table_by_node(session, tclass, tkey):
    """"""
    result=session.query(tclass).filter(tclass.node == tkey).all()
    if not result:
       return None 
    return result[0].getdict()


def query_nodelist_by_key(session, nodelist):
    """"""
    nodelist_value = {}
    for node in nodelist:
        nodelist_value[node]={}
        classlist = [Bootparams,Nodetype,Hosts,Switch,Mac,Noderes]
        for eachclass in classlist:
            clsdict = query_table_by_node(session,eachclass,node)
            nodelist_value[node].update(clsdict)
    return nodelist_value

if __name__ == "__main__":

    session = loadSession()
    nodelist_value = {}
    nodelist = ['node0001','node0002']
    mymac={}
    mymac['node0001']={}
    mymac['node0001']['node']="node0001"
    mymac['node0001']['mac']="11:22:33:44"
    #pdb.set_trace()
    print networks.getkey()
    exit()

    print dir(mac.getkey())
    print mac.getkey().asc
    mynode=mac(mymac['node0001'])
    print mynode.getdict()
    #mymac=mac()
    #session.add(mymac)
    #session.commit()
    print dir(mac)
    session.close()
