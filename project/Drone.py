from project.secp256k1 import* #curve,scalar_mult
from datetime import datetime
from project.aes import *  
from project.ts import * 
import random
import hashlib
#import base64
class drone:
 def __init__(self,id_dr,tid_dr,mk_cr,id_cr,pub_cr,pk_cr,r_cr,rts_dr):
  self.id_dr = id_dr
  self.tid_dr = tid_dr
  self.mk_cr= mk_cr
  self.id_cr = id_cr
  self.pub_cr = pub_cr
  self.pk_cr = pk_cr
  self.r_cr = r_cr
  self.rts_dr = rts_dr

 def rid(self):
  rid_drs = (hashlib.sha256((self.id_cr+str(self.mk_cr)+self.rts_dr).encode()))
  rid_dr = format(int(rid_drs.hexdigest(),base=16),'x')
  return rid_dr
 def priv(self):
  pr_dr= random.randrange(1,curve.n)
  return str(pr_dr)
 def pub(self,r_cr):
  #r_cr = self.r_cr
  pub_dr = scalar_mult(r_cr,curve.g)
  return pub_dr
  #print(type(pub_dr))
 def cert(self,pub_dr):
  cer_dr = hashlib.sha256((str(pub_dr)+str(self.pub_cr)+str(self.pk_cr)).encode())
  cert_dr = str(self.mk_cr)+format((int(cer_dr.hexdigest(),base=16)*self.r_cr)%curve.n,'x')
  return cert_dr
 def get_private_key(self,password):
  salt = b"this is a salt"
  kdf = PBKDF2(password, salt, 64, 1000)
  key = kdf[:16]
  return key
'''obj = Drone("drone","d1","mk_cr","id_cr","pub_cr","pk_cr",random.randrange(1,curve.n))
pub_dr=obj.pub(obj.r_cr)
#pub_dr = obj.pub()
ret = obj.cert(pub_dr)
print(ret)'''
