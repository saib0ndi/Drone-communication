from project.secp256k1 import curve,scalar_mult
#from aes import * 
from project.ts import * 
import random
import hashlib
def acdd1(tid_dr,k_dr_gss,rid_dr,pr_dr,pub_dr,cert_dr):
 r_d1 = random.randrange(1,curve.n)
 ts_d1= tstamp()#date_time.strftime("%c")
 x_dr = hashlib.sha256((str(r_d1)+tid_dr+k_dr_gss+rid_dr+pr_dr+ts_d1).encode()).hexdigest()
 X_drt = scalar_mult(int(x_dr,16),curve.g)
 X_dr = str(X_drt[0])
 sig_dr = x_dr + format((int(hashlib.sha256((tid_dr+pub_dr+cert_dr+ts_d1).encode()).hexdigest(),16)*int(pr_dr))%curve.n,'x')
 print("the message sent to drone 2 is :",tid_dr,X_dr,cert_dr,ts_d1)
 l1 = [tid_dr,X_dr,cert_dr,ts_d1,sig_dr,pub_dr,rid_dr,x_dr]  #pub_cr,pk_cr
 return l1
def acdd2(tid_dr1,X_dr,cert_dr1,ts_d1,sig_dr1,pub_dr1,rid_dr1,pub_cr,pk_cr,tid_dr2,cert_dr2,pub_dr2,pr_dr2,rid_dr2,k_dr_gss2):
 #if(scalar_mult(int(cert_dr1,16),curve.g) == pk_cr+(hashlib.sha256((pub_dr1+pub_cr+pk_cr).encode()).hexdigest())*int(pub_cr)):
    print("first check")
   #if(scalar_mult(int(sig_dr1,16),curve.g) == X_dr+(hashlib.sha256((tid_dr1+pub_dr1+cert_dr1+ts_d1).encode()).hexdigest()*int(pub_dr1)):
    r_d2 = random.randrange(1,curve.n)
    ts_d2 = tstamp()#date_time.strftime("%c")
    y_dr = hashlib.sha256((str(r_d2)+tid_dr2+k_dr_gss2+rid_dr2+pr_dr2+ts_d2).encode()).hexdigest()
    Y_drt= scalar_mult(int(y_dr,16),curve.g)
    Y_dr = str(Y_drt[0])
    dhk_d2_d1 = str(int(y_dr,16)*int(X_dr))
    sk_d2_d1 = hashlib.sha256((dhk_d2_d1+tid_dr1+tid_dr2+ts_d2+ts_d1).encode()).hexdigest()
    sig_dr2 = y_dr+format((int(hashlib.sha256((sk_d2_d1+cert_dr1+cert_dr2+tid_dr2+Y_dr+ts_d2).encode()).hexdigest(),16)*int(pr_dr2))%curve.n,'x')
    print("the reply from drone 2 sent to drone 1 is:",tid_dr2,Y_dr,cert_dr2,sig_dr2,ts_d2,ts_d1)
    l3 = [tid_dr2,Y_dr,cert_dr2,sig_dr2,ts_d2,ts_d1,sk_d2_d1]
    return l3
def acdd4(tid_dr2,Y_dr,cert_dr2,sig_dr2,ts_d2,ts_d1,sk_d2_d1,pk_cr,pub_dr2,pub_cr,x_dr,tid_dr1,cert_dr1):
 #if(scalar_mult(int(cert_dr2,16),curve.g)==pk_cr+hashlib.sha256((pub_dr2+pub_cr+pk_cr).encode()).hexdigest()*pub_cr):
   dhk_d1_d2 = str(int(x_dr,16)*int(Y_dr))
   sk_d1_d2 = hashlib.sha256((dhk_d1_d2+tid_dr1+tid_dr2+ts_d2+ts_d1).encode()).hexdigest()
  #if(scalar_mult(int(sig_dr2,16),curve.g) == Y_dr+hashlib.sha256((sk_d1_d2+cert_dr1+cert_dr2+tid_dr2+Y_dr+ts_d2).encode()).hexdigest()*pub_dr2):
   ts_d3 = tstamp()#date_time.strftime("%c")
   skv_d1_d2 = hashlib.sha256((sk_d1_d2+ts_d3).encode()).hexdigest()
   print("the acknowledgement message sent by d1 is :",skv_d1_d2,ts_d3)
   l4 = [skv_d1_d2,ts_d3,sk_d2_d1]
   return l4
def acdd5(skv_d1_d2,ts_d3,sk_d2_d1):
 #if(skv_d1_d2 == hashlib.sha256((sk_d2_d1+ts_d3).encode()).hexdigest()):
  print(" the drone to drone access control phase is complete and the common session key is established")
  return sk_d2_d1
 
