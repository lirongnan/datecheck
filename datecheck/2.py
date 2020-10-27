import os
cmd = 'git diff --name-only Head~ head'
res = os.popen(cmd)
output_str = res.read()   # 获得输出字符串
print(output_str)