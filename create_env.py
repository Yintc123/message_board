with open('.env', mode='w', encoding='utf-8') as file:
    file.write("# mode\nMODE='production'\n\n")
    file.write("# aws\naccess_key='AKIAW27V5MCNSDJ6JHUS'\nsecret_access_key='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'\n")
    
with open('.env.develop', mode='w', encoding='utf-8') as file:
    file.write("# app\napp_host='127.0.0.1'\n\n")
    file.write("# mysql\nmysql_password='abc123456'\nmysql_port='3400'\n\n")
    file.write("# static\nhome_url='http://127.0.0.1:3000/'\n")
  
with open('.env.production', mode='w', encoding='utf-8') as file:
    file.write("# app\napp_host='0.0.0.0'\n\n")
    file.write("# mysql\nmysql_password='AbC123456'\nmysql_port='3306'\n\n")
    file.write("# static\nhome_url='http://3.115.234.130:3000/'\n")
  