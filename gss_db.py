import mysql.connector
def insert_db(id_dr,tid_dr,rid_dr,cert_dr,k_dr_gss,pr_dr,connection_status,sk_dr_gss,sk_dr1_dr2):
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 #print(conn)
 mycursor = conn.cursor()
 
 sql = "INSERT INTO drone_data (id_dr,tid_dr,rid_dr,cert_dr,k_dr_gss,pr_dr,connection_status,sk_dr_gss,sk_dr1_dr2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
 
 val = (id_dr,tid_dr,rid_dr,cert_dr,k_dr_gss,pr_dr,connection_status,sk_dr_gss,sk_dr1_dr2)
 mycursor.execute(sql,val)
 
 conn.commit()

 conn.close()
def d2g_complete(key_dr1,gss_dr1,id_dr):
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 
 mycursor = conn.cursor()
 
 sql = "UPDATE drone_data SET tid_dr = %s WHERE id_dr = %s"
 val = (gss_dr1,id_dr)
 mycursor.execute(sql,val)
 conn.commit()
 
 sql = "UPDATE drone_data SET sk_dr_gss = %s WHERE id_dr = %s"
 val = (key_dr1,id_dr)
 mycursor.execute(sql,val)
 conn.commit()
 
 sql = "UPDATE drone_data SET connection_status = %s WHERE id_dr = %s"
 val = (1,id_dr)
 mycursor.execute(sql,val)
 conn.commit()
 conn.close()
def d2d_complete(k_dr1_dr2,id_dr1,id_dr2):
 conn = mysql.connector.connect(user = "root",
                                host = "127.0.0.1",
                                password = "{Poorna@01}",
                                database = "gss_db",
                                auth_plugin = 'mysql_native_password')
 
 mycursor = conn.cursor()
 
 sql = "UPDATE drone_data SET sk_dr1_dr2 = %s WHERE id_dr = %s"
 val = (k_dr1_dr2,id_dr1)
 mycursor.execute(sql,val)
 conn.commit()
 
 sql = "UPDATE drone_data SET sk_dr1_dr2 = %s WHERE id_dr = %s"
 val = (k_dr1_dr2,id_dr2)
 mycursor.execute(sql,val)
 conn.commit()
 
 sql = "UPDATE drone_data SET connection_status = %s WHERE id_dr = %s"
 val = [(1,id_dr1),(1,id_dr2)]
 mycursor.executemany(sql,val)
 conn.commit()
 
 conn.close()
#insert_db("tid_dr1","rid_dr1","cert_dr1","k_dr_gss1","pr_dr1",0,"not set","not set")
#d2g_complete()
