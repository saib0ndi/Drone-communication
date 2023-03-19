from project.secp256k1 import curve,scalar_mult
from project.aes import * 
from project.ts import * 
import random
import hashlib
import base64
def acdg1(k_dr_gss,k_dr_gss_,cert_dr,tid_dr,rid_dr):
 ts1 = tstamp()#date_time.strftime("%c")
 r1 = random.randrange(1,curve.n)
 D1_ = hashlib.sha256((tid_dr+rid_dr+str(r1)+k_dr_gss+ts1).encode())
 D1 = D1_.hexdigest()#format(int(D1_.hexdigest(),base=16),'x')
 iv_ = hashlib.sha256((k_dr_gss+ts1).encode())
 iv_1 = (iv_.hexdigest())
 iv = iv_1[:16]
 D2_1 = encrypt(D1,k_dr_gss_,iv)
 D2 = D2_1.decode("utf-8","ignore")
 D3_1 = str(hashlib.sha256((D2+cert_dr+tid_dr+rid_dr+k_dr_gss+ts1).encode()).hexdigest())
 print("the following details are sent to gss via open channel:",tid_dr,D2,D3_1,cert_dr,ts1)
 #print(D1)
 #print(type(D2_1))
 l1 = [tid_dr,D2,D2_1,D3_1,cert_dr,ts1,rid_dr,k_dr_gss_,k_dr_gss,iv]
 return l1
def acdg2(tid_dr,D2,D2_1,D3_1,cert_dr,ts1,rid_dr,k_dr_gss_,k_dr_gss,iv):
 #D2_1=D2.decode("utf-8","ignore")
 D3=str(hashlib.sha256((D2+cert_dr+tid_dr+rid_dr+k_dr_gss+ts1).encode()).hexdigest()) #D2_1
 if(D3 == D3_1):
  D1=decrypt(D2_1,k_dr_gss_,iv) #,D2_1
 l2 = [D1,rid_dr,tid_dr,ts1]
 return l2
def acdg3(D1,rid_dr,tid_dr,ts1,rid_gss,cert_gss,k_dr_gss_,k_dr_gss):
 r2=random.randrange(1,curve.n)
 ts2 = tstamp()#date_time.strftime("%c")
 tid_new_1="gss and drone 1".encode('utf-8')
 tid_new = tid_new_1.hex()
 G1 = hashlib.sha256((rid_gss+rid_dr+str(r2)+k_dr_gss+ts2).encode()).hexdigest()
 iv_ = hashlib.sha256((k_dr_gss+ts2).encode())
 iv_1 = (iv_.hexdigest())
 iv = iv_1[:16]
 #D1_3 = bytes(D1,'utf-8') 
 D1_3 = D1.decode("utf-8","ignore")
 G2_1 = encrypt(G1,k_dr_gss_,iv)            #D1_3,k_dr_gss_,iv
 G2 = G2_1.decode("utf-8","ignore")
 sk_gd = hashlib.sha256((tid_new+D1_3+G1+ts1+ts2).encode()).hexdigest()
 new = hashlib.sha256((rid_gss+tid_dr+k_dr_gss+ts2).encode())
 Tid_dr = hex((int(tid_new,base=16)^int(new.hexdigest(),base=16)))
 G3 = hashlib.sha256((Tid_dr+G1+cert_gss+rid_gss+ts2).encode()).hexdigest()
 print("the reply from gss is",Tid_dr,rid_gss,G2,G3,cert_gss,ts2)
 l3 = [Tid_dr,G2_1,G3,ts2,D1_3,ts1,k_dr_gss_,sk_gd]
 return l3
def acdg4(Tid_dr,G2_1,G3,ts2,D1_3,ts1,k_dr_gss_,cert_gss,pub_cr,rid_gss,pk_cr,k_dr_gss,tid_dr):
 #if(scalar_mult(int(cert_gss,base=16), curve.g)==pub_cr+(hashlib.sha256((rid_gss+pub_cr+pk_cr).encode()).hexdigest())*pk_cr):
  iv_ = hashlib.sha256((k_dr_gss+ts2).encode())
  iv_1 = (iv_.hexdigest())
  iv = iv_1[:16]
  G1 = decrypt(G2_1,k_dr_gss_,iv)
  G1_4 = G1.decode("utf-8","ignore")
  G3_ = hashlib.sha256((Tid_dr+G1_4+cert_gss+rid_gss+ts2).encode()).hexdigest()
  if(G3_==G3):
   tid_new= hex(int(Tid_dr,16)^int(hashlib.sha256((rid_gss+tid_dr+k_dr_gss+ts2).encode()).hexdigest(),16))
   sk_dg= hashlib.sha256((tid_new+D1_3+G1_4+ts1+ts2).encode()).hexdigest()
   ts3 = tstamp()#date_time.strftime("%c")
   skv_dg=hashlib.sha256((sk_dg+ts3).encode()).hexdigest()
   print("the message sent by drone is :",skv_dg,ts3)
   l4 = [skv_dg,ts3,tid_new]
   return l4
def acdg5(skv_dg,ts3,tid_new,sk_gd):
 #if(skv_dg==hashlib.sha256((sk_gd+ts3).encode()).hexdigest()):
  tid_dr = tid_new
  print("the session key is established and the drone to gss access control phase is complete")
  l5 = [sk_gd,tid_dr]
  return l5#tid_dr

 
