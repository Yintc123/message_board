with open('.env', mode='w', encoding='utf-8') as file:
    file.write("# mode\nMODE='production'\n\n")
    file.write("# aws s3\naccess_key='AKIAW27V5MCNSDJ6JHUS'\nsecret_access_key='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'\n\n")
    file.write("# aws RDS\nRDS_host='test.clw8df14vxhi.ap-northeast-1.rds.amazonaws.com'\nuser='admin'\npassword='abc123456'\nport='3306'\n")
    

with open('.env.develop', mode='w', encoding='utf-8') as file:
    file.write("# app\napp_host='127.0.0.1'\n\n")
    file.write("# static\nhome_url='http://127.0.0.1:3000/'\n")
    file.write("# aws s3\naccess_key='AKIAW27V5MCNSDJ6JHUS'\nsecret_access_key='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'\n\n")
    file.write("# aws RDS\nRDS_host='test.clw8df14vxhi.ap-northeast-1.rds.amazonaws.com'\nuser='admin'\npassword='abc123456'\nport='3306'\n") 
  
with open('.env.production', mode='w', encoding='utf-8') as file:
    file.write("# app\napp_host='0.0.0.0'\n\n")
    file.write("# static\nhome_url='http://3.115.234.130:3000/'\n")
    file.write("# aws s3\naccess_key='AKIAW27V5MCNSDJ6JHUS'\nsecret_access_key='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'\n\n")
    file.write("# aws RDS\nRDS_host='test.clw8df14vxhi.ap-northeast-1.rds.amazonaws.com'\nuser='admin'\npassword='abc123456'\nport='3306'\n")
