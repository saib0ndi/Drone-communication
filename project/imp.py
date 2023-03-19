from project.secp256k1 import curve,scalar_mult
from datetime import datetime
from project.Drone import drone
from project.acdg import *
from project.aes import * 
from project.ts import *
from project.acdd import * 
import random
import hashlib
#import base64
id_cr = "cr"
#print("Basepoint:\t", curve.g)
mk_cr= random.randrange(1,curve.n)
r_cr= random.randrange(1,curve.n)
pk_crt  = scalar_mult(mk_cr, curve.g)
pk_cr = str(pk_crt[0])
pub_crt = scalar_mult(r_cr, curve.g)
pub_cr = str(pub_crt[0])
#print("the public parameters are",curve.name,curve.g,pk_cr,pub_cr)
#id_dr = "dr"
rts_dr1 = tstamp()
rts_dr2 = tstamp()
d1 = drone("d1","d1",mk_cr,id_cr,pub_cr,pk_cr,random.randrange(1,curve.n),rts_dr1)
d2 = drone("d2","d2",mk_cr,id_cr,pub_cr,pk_cr,random.randrange(1,curve.n),rts_dr2)

#rid_drs = (hashlib.sha256((id_cr+str(mk_cr)+rts_dr).encode()))
#rid_dr = rid_drs.hexdigest() 
rid_dr1 = d1.rid()
rid_dr2 = d2.rid()
#print(rid_dr)
#tid_dr = "temporal_id"
pr_dr1= d1.priv()#random.randrange(1,curve.n)
pr_dr2= d2.priv()
#print(type(pr_dr))
pub_drt1 = d1.pub(r_cr)#scalar_mult(r_cr, curve.g)
pub_dr1 = str(pub_drt1[0])
pub_drt2 = d2.pub(r_cr)#scalar_mult(r_cr, curve.g)
pub_dr2 = str(pub_drt2[0])

#print(pub_dr)
#cer_dr = hashlib.sha256((str(pub_dr)+str(pub_cr)+str(pk_cr)).encode())
#cert_dr = str(mk_cr)+format((int(cer_dr.hexdigest(),base=16)*r_cr)%curve.n,'x')
cert_dr1 = d1.cert(pub_dr1)
cert_dr2 = d2.cert(pub_dr2)
k_dr_gss_1 = d1.get_private_key("drone1password")
k_dr_gss1 = k_dr_gss_1.decode("utf-8","ignore")
k_dr_gss_2 = d2.get_private_key("drone2password")
k_dr_gss2 = k_dr_gss_2.decode("utf-8","ignore")
#print("the data saved in drone is",  d1.tid_dr  ,  rid_dr1 ,  cert_dr1 ,  k_dr_gss1,  pr_dr1 ,  curve.name)
#print("the data published publicly is",pub_dr1)
id_gss = "gss"
rts_gss = tstamp()#date_time.strftime("%c")
ri_gss = (hashlib.sha256((id_gss+str(mk_cr)+rts_gss).encode()))
rid_gss = ri_gss.hexdigest()
cer_gss = hashlib.sha256((rid_gss+str(pub_cr)+str(pk_cr)).encode())
cert_gss=str(r_cr)+format((int(cer_gss.hexdigest(),base=16)*mk_cr)%curve.n,'x')  #change
print("the data saved in gss is: ",d1.tid_dr,rid_dr1,cert_gss,rid_gss,k_dr_gss1,curve.name)

pr_gss = random.randrange(1,curve.n)
#print(type(pr_gss))

pub_gsst = scalar_mult(pr_gss, curve.g)
pub_gss = str(pub_gsst[0])
print("the data of gss published publicly is ",pub_gss)


l1=acdg1(k_dr_gss1,k_dr_gss_1,cert_dr1,d1.tid_dr,rid_dr1)
l2=acdg2(*l1)
l=[rid_gss,cert_gss,k_dr_gss_1,k_dr_gss1]
l2.extend(l)
l3=acdg3(*l2)
#print(l3[6])
sk_gd = l3[7]
l3.pop(7)
lx = [cert_gss,pub_cr,rid_gss,pk_cr,k_dr_gss1,d1.tid_dr]
l3.extend(lx)
l4 = acdg4(*l3)
l4.append(sk_gd)
l5 = acdg5(*l4)#newtid_dr = acdg5(*l4)
#l5[0] is the one to replace sk_dr_gss after drone to gss connection is established . l5[1] replaces tid_dr in database when drone to gss connection is established
# only one database is created that contains details of drones and their connection status.

l1_1 = [d1.tid_dr,k_dr_gss1,rid_dr1,pr_dr1,pub_dr1,cert_dr1]
l2 = acdd1(*l1_1)
x_dr = l2[7]
l2.pop(7)
l1 = [pub_cr,pk_cr,d2.tid_dr,cert_dr2,pub_dr2,pr_dr2,rid_dr2,k_dr_gss2]
l2.extend(l1)
l3 = acdd2(*l2)
l1 = [pk_cr,pub_dr2,pub_cr,x_dr,d1.tid_dr,cert_dr1]
l3.extend(l1)
l4 = acdd4(*l3)
sk_d1_d2 = acdd5(*l4)#sk_d1_d2 is the one to replace sk_dr_dr after drone to drone connection is established.
