
from datetime import datetime
from project.Drone import drone
from project.acdg import *
from project.aes import * 
from project.ts import *
from project.acdd import * 
from project.secp256k1 import curve,scalar_mult
from gss_db import *
import time
import random
import hashlib
import mysql.connector
#import base64
id_cr = "cr"
#print("Basepoint:\t", curve.g)
mk_cr= random.randrange(1,curve.n)
r_cr= random.randrange(1,curve.n)
pk_crt  = scalar_mult(mk_cr, curve.g)
pk_cr = str(pk_crt[0])
pub_crt = scalar_mult(r_cr, curve.g)
pub_cr = str(pub_crt[0])
dr_list=[]
l_dr = []
gss_list=[]
#print("the public parameters are",curve.name,curve.g,pk_cr,pub_cr)
#id_dr = "dr"
def dr_reg(id_dr):#,mk_cr,id_cr,pub_cr,pk_cr):
 print("the drone registration phase begins ")
 rts_dr = tstamp()
 dr = drone(id_dr,id_dr,mk_cr,id_cr,pub_cr,pk_cr,random.randrange(1,curve.n),rts_dr)
 dr_list.append(dr)
 rid_dr = dr_list[-1].rid()
 pr_dr= dr_list[-1].priv()
 pub_drt = dr_list[-1].pub(int(pr_dr))
 pub_dr = str(pub_drt[1])
 cert_dr = dr_list[-1].cert(pub_dr)
 k_dr_gss_ = dr_list[-1].get_private_key(id_dr+"passwordforgss")
 k_dr_gss = k_dr_gss_.decode("utf-8","ignore")
 insert_db(id_dr,id_dr,rid_dr,cert_dr,k_dr_gss,pr_dr,0,"not_set","not_set")
 time.sleep(11)
 print("the drone registration phase ends\n")
 l = ( k_dr_gss,k_dr_gss_,id_dr,rid_dr,cert_dr,pr_dr,pub_dr)
 l_dr.append(l)
 return True
 #print(l_dr[0][1])

def gss_reg(id_gss):#mk_cr,pub_cr,pk_cr,r_cr):
 print("the gss registration phase begins\n")
#  id_gss = "gss"
 rts_gss = tstamp()
 ri_gss = (hashlib.sha256((id_gss+str(mk_cr)+rts_gss).encode()))
 rid_gss = ri_gss.hexdigest()
 cer_gss = hashlib.sha256((rid_gss+str(pub_cr)+str(pk_cr)).encode())
 cert_gss=str(r_cr)+format((int(cer_gss.hexdigest(),base=16)*mk_cr)%curve.n,'x')  #change
 #print("the data saved in gss is: \n",d1.tid_dr,rid_dr1,cert_gss,rid_gss,k_dr_gss1,curve.name)
 pr_gss = random.randrange(1,curve.n)
 pub_gsst = scalar_mult(pr_gss, curve.g)
 pub_gss = str(pub_gsst[0])
 print("the data of gss published publicly is \n",pub_gss)
 print("the gss registration phase ends\n")
 gss_list.append(rid_gss)
 gss_list.append(cert_gss)
 gss_list.append(pub_gss)#,pr_gss,pub_gss]
 print("the drone to gss access control phase begins\n")
 return gss_list,pub_gss

def ret_drone():
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 
 mycursor = conn.cursor()
 sql = "SELECT id_dr FROM drone_data "
 mycursor.execute(sql)
 myresult = mycursor.fetchall()
 return myresult
 

def d2g (i_dr):
 x=0
 for each in l_dr :
  x=x+1
  if(each[2]==i_dr):
   break
 i = x#int(i_dr[-1])
 rid_gss = gss_list[0]
 cert_gss = gss_list[1]
 k_dr_gss = l_dr[i-1][0]
 k_dr_gss_ = l_dr[i-1][1]
 tid_dr = l_dr[i-1][2]
 rid_dr = l_dr[i-1][3]
 cert_dr = l_dr[i-1][4]
 l1=acdg1(k_dr_gss,k_dr_gss_,cert_dr,tid_dr,rid_dr)
 l2=acdg2(*l1)
 l=[rid_gss,cert_gss,k_dr_gss_,k_dr_gss]
 l2.extend(l)
 l3=acdg3(*l2)
 #print(l3[6])
 sk_gd = l3[7]
 l3.pop(7)
 lx = [cert_gss,pub_cr,rid_gss,pk_cr,k_dr_gss,tid_dr]
 l3.extend(lx)
 l4 = acdg4(*l3)
 l4.append(sk_gd)
 l5 = acdg5(*l4)
 d2g_complete(*l5,dr_list[i-1].id_dr)
 q = list(l_dr[i-1])
 q[2] = l5[1]
 l_dr[i-1] = tuple(q)
#l5[0] is the one to replace sk_dr_gss after drone to gss connection is established . l5[1] replaces tid_dr in database when drone to gss connection is established
# only one database is created that contains details of drones and their connection status.
def d2d (i_dr,j_dr):
 x=0
 y=0
 for each in l_dr :
  x=x+1
  if(each[2]==i_dr):
   break
  #else:
   #continue
 for each in l_dr :
  y=y+1
  if(each[2]==j_dr):
   break
  #else:
   #continue
 i = x#int(i_dr[-1])
 j = y#int(j_dr[-1])
 k_dr_gss1 = l_dr[i-1][0]
 tid_dr1 = l_dr[i-1][2]
 rid_dr1 = l_dr[i-1][3]
 cert_dr1 = l_dr[i-1][4]
 pr_dr1 = l_dr[i-1][5]
 pub_dr1 = l_dr[i-1][6]
 k_dr_gss2 = l_dr[j-1][0]
 tid_dr2 = l_dr[j-1][2]
 rid_dr2 = l_dr[j-1][3]
 cert_dr2 = l_dr[j-1][4]
 pr_dr2 = l_dr[j-1][5]
 pub_dr2 = l_dr[j-1][6]
 print("the drone to drone access control phase begins\n")
 l1_1 = [tid_dr1,k_dr_gss1,rid_dr1,pr_dr1,pub_dr1,cert_dr1]
 l2 = acdd1(*l1_1)
 x_dr = l2[7]
 l2.pop(7)
 l1 = [pub_cr,pk_cr,tid_dr2,cert_dr2,pub_dr2,pr_dr2,rid_dr2,k_dr_gss2]
 l2.extend(l1)
 l3 = acdd2(*l2)
 l1 = [pk_cr,pub_dr2,pub_cr,x_dr,tid_dr1,cert_dr1]
 l3.extend(l1)
 l4 = acdd4(*l3)
 sk_d1_d2 = acdd5(*l4)#sk_d1_d2 is the one to replace sk_dr_dr after drone to drone connection is established.
 d2d_complete(sk_d1_d2,dr_list[i-1].id_dr,dr_list[j-1].id_dr)
 return sk_d1_d2
'''dr_reg("d1")
dr_reg("d2")#,mk_cr,id_cr,pub_cr,pk_cr)
#print("going")
#print("going")
#dr_reg("d2")#,mk_cr,id_cr,pub_cr,pk_cr)
#print(dr_list)
gss_list = gss_reg()
d2g(1,*gss_list)
d2d(1,2)'''
#print(dr_list[0].cert((dr_list[0].pub(r_cr))[0]))
def end_conn_gss(id_dr):
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 
 mycursor = conn.cursor()
 
 sql = "UPDATE drone_data SET sk_dr_gss = %s WHERE id_dr = %s"
 val = ("not set",id_dr)
 mycursor.execute(sql,val)
 conn.commit()
 
 sql = "UPDATE drone_data SET connection_status = %s WHERE id_dr = %s"
 val = (0,id_dr)
 mycursor.execute(sql,val)
 conn.commit()
 conn.close()
def end_conn_drone(id_dr):
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 
 mycursor = conn.cursor()
 sql = "SELECT sk_dr1_dr2 FROM drone_data WHERE id_dr = %s"
 val = (id_dr,)
 mycursor.execute(sql,val)
 myresult = mycursor.fetchall()
 #print(type(myresult))
 sk_dr_dr = myresult[0][0]
 if(sk_dr_dr == "not set") :
  sql = "UPDATE drone_data SET sk_dr_gss = %s WHERE id_dr = %s"
  val = ("not set",id_dr)
  mycursor.execute(sql,val)
  conn.commit()
 
  sql = "UPDATE drone_data SET connection_status = %s WHERE id_dr = %s"
  val = (0,id_dr)
  mycursor.execute(sql,val)
  conn.commit()
 else:
  sql = "UPDATE drone_data SET connection_status = %s WHERE sk_dr1_dr2 = %s"
  val = (0,sk_dr_dr)
  mycursor.execute(sql,val)
  conn.commit()
  sql = "UPDATE drone_data SET sk_dr1_dr2 = %s WHERE sk_dr1_dr2 = %s"
  val = ("not set",sk_dr_dr)
  mycursor.execute(sql,val)
  conn.commit()
 conn.close()
def check_conn_stat(id_dr):
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 
 mycursor = conn.cursor()
 sql = "SELECT connection_status FROM drone_data WHERE id_dr = %s"
 val = (id_dr,)
 mycursor.execute(sql,val)
 myresult = mycursor.fetchall()
 #print(type(myresult))
 c_stat = myresult[0][0]
 conn.close() 
 if c_stat == 0:
  return True
 else:
  return False
 
#check_conn_stat("d1")
#check_conn_stat("d2")
#end_conn_gss("d1")
#end_conn_drone("d2")
