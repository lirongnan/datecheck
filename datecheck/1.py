
import subprocess
import os

filePath = 'environment.txt'
filePath2 = 'projectlist.txt'
f = open(filePath,'w+',encoding='utf-8')


cmds = [['git rev-parse HEAD','GIT_COMMITID'],
        ['git diff --name-only HEAD~ HEAD','GIT_COMMITIDQW'],
        ['git name-rev --name-only HEAD','GIT_BRANCH'],
        ['git log --pretty=format:"%s" -1','GIT_MESSAGE'],
        ['git log --pretty=format:"%an" -1','GIT_CREATEBY']]

for cmd in cmds:
  p = subprocess.Popen(cmd[0],  stdout=subprocess.PIPE, universal_newlines=True)
  p.wait()

  result_lines = p.stdout.readlines()

  lines = ''
  for line in result_lines:
    lines+=line + ','
f.writelines(cmd[1] + '=' + lines + '\n')
f.close()  
#f2 = open(filePath2,'w+',encoding='gbk')
#paths = [['NTFox.Lib\\NTFox.Framework','NTFox.Framework.csproj'] 
#,['NTFox.Lib\\NTFox.DbHelper','NTFox.DbHelper.csproj']
#,['NTFox.CLX\\NTFox.Log' ,'NTFox.Log.csproj']
#,['NTFox.Item\\NTFox.Item.Comm\\NTFox.Comm','NTFox.Comm.csproj']
#,['NTFox.SDK\\NTFox.SppSDK' ,'NTFox.SppSDK.csproj']
#,['NTFox.SDK\\NTFox.CommSDK','NTFox.CommSDK.csproj']
#,['NTFox.SDK\\NTFox.InsuranceSDK','NTFox.InsuranceSDK.csproj']
#,['NTFox.SDK\\NTFox.JiangTaiInsuranceSDK','NTFox.JiangTaiInsuranceSDK.csproj']
#,['NTFox.Lib\\NTFox.VSBG' ,'NTFox.VSBG.csproj']
#,['NTFox.Lib\\NTFox.IM','NTFox.IM.csproj']
#,['NTFox.Lib\\NTFox.FetchResource' ,'NTFox.FetchResource.csproj']
#,['NTFox.CLX\\NTFox.MongoDb' ,'NTFox.MongoDb.csproj']
#,['NTFox.CLX\\NTFox.RabbitMQ' ,'NTFox.MQ.csproj']
#,['NTFox.Service\\NTFox.ABCsI' ,'NTFox.ABCsI.csproj']
#,['NTFox.Item\\NTFox.Item.Omp\\NTFox.Omp.Model' ,'NTFox.Omp.Model.csproj']
#,['NTFox.CLX\\NTFox.ES' ,'NTFox.ES.csproj']
#,['NTFox.Lib\\NTFox.OnLineUser','NTFox.OnLineUser.csproj']]

#p = subprocess.Popen('git diff --name-only Head~ head',stdout=subprocess.PIPE, universal_newlines=True)
#p.wait()
#result_lines = p.stdout.readlines()

#for path in paths:
#    flag = False
#    for line in result_lines:
#        if path[0] in line:
#            flag = True
#            break
#    if flag:
#        str = path[0] + ',' + path[1] + '\n'
#        f2.writelines(str)
#f2.writelines('')
#f2.close()
