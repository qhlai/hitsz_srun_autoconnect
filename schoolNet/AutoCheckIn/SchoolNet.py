import encode_srun_md5 
import encode_srun_sha1
import encode_srun_base64 
import encode_srun_xencode 
#import NetReady
import requests
import re
import time
import numpy as np
#封装头信息，伪装成浏览器
#Win10 火狐
header={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
}
jQuery="0"
ip="0"
get_ip_api="http://10.248.98.2/cgi-bin/rad_user_info"
get_challenge_api="http://10.248.98.2/cgi-bin/get_challenge"
srun_portal_api="http://10.248.98.2/cgi-bin/srun_portal"
srun_dm_api="http://10.248.98.2/cgi-bin/rad_user_dm"

username="33318********"
password="********"
n = '200'
type = '1'
ac_id='1'
enc = "srun_bx1"

def get_uniform_random_number(low, high):
	"""
	:param low: 均匀分布的下界
	:param high: 均匀分布的上界
	:return: 从均匀分布中产生的随机数
	"""
	# 均匀分布的随机数生成
	number = np.random.uniform(low, high)
	# 返回值
	return number
def produce_jQuery():
	global jQuery
	strnum=""
	for i in range(21):
		strnum=strnum+str(int(get_uniform_random_number(0, 9)))
	jQuery="jQuery"+strnum+"_"
	print("jQuery:"+jQuery)

def get_chkstr():
	chkstr = token+username
	chkstr += token+hmd5
	chkstr += token+ac_id
	chkstr += token+ip
	chkstr += token+n
	chkstr += token+type
	chkstr += token+i
	return chkstr
def get_info():
	info_temp={
		"username":username,
		"password":password,
		"ip":ip,
		"acid":ac_id,
		"enc_ver":enc
	}
	i=re.sub("'",'"',str(info_temp))
	i=re.sub(" ",'',i)
	return i
def init_getip():
	global ip
	global callback
	callback=jQuery+str(int(time.time()*1000))
	get_ip_params={
		"callback": callback,
		"_":int(time.time()*1000),
	}
	get_ip_res=requests.get(get_ip_api,params=get_ip_params,headers=header)
	#init_res=requests.get(init_url,headers=header)
	print("初始化获取ip")
	print(get_ip_res.content)
	print(get_ip_res.content[10])
	ip=re.search('online_ip":"(.*?)"',str(get_ip_res.content)).group()[12:-1]
	#ip=ip[12:-1]
	#print(ip[12:-1])
	#print(re.search(r'"online_ip":"(.*?)"',str(get_ip_res.content)))
	#ip=re.search('id="client_ip" value="(.*?)"',get_ip_res.content).group(3)
	#ip=re.search('id="user_ip" value="(.*?)"',get_challenge_res).group(1)
	print("ip:"+ip)
def get_token():
	# print("获取token")
	global token
	get_challenge_params={
		"callback": callback,
		"username":username,
		"ip":ip,
		"_":int(time.time()*1000),
	}
	get_challenge_res=requests.get(get_challenge_api,params=get_challenge_params,headers=header)
	token=re.search('"challenge":"(.*?)"',get_challenge_res.text).group(1)
	print(get_challenge_res.text)
	print("token为:"+token)
def data_encode():
	global i,hmd5,chkstr_final
	i=get_info()
	i="{SRBX1}"+encode_srun_base64._encode(encode_srun_xencode._encode(i,token))
	hmd5=encode_srun_md5._encode(password,token)
	chkstr_final=encode_srun_sha1._encode(get_chkstr())
	print("所有加密工作已完成")

def login():
	produce_jQuery()
	init_getip()
	get_token()
	data_encode()
	
	srun_portal_params={
	'callback': callback,
	'action':'login',
	'username':username,
	'password':'{MD5}'+hmd5,
	'ac_id':ac_id,
	'ip':ip,
	'chksum':chkstr_final,
	'info':i,
	'n':n,
	'type':type,
	'os':'Windows+10',
	'name':'Windows',
	'double_stack':'0',
	'_':int(time.time()*1000)
	}
	# print(srun_portal_params)
	srun_portal_res=requests.get(srun_portal_api,params=srun_portal_params,headers=header)
	print(srun_portal_res.text)
	return srun_portal_res.text
def logout():
	if jQuery=="0":
		 produce_jQuery()
		 init_getip()

	t=int(time.time()*1000)
	srun_portal_params= {
	'callback': jQuery+str(int(time.time()*1000)),
    'ip':ip,
    'username':username,
    'time': str(t),
    'unbind': '0',
    'sign': encode_srun_sha1._encode(str(t) + username + ip + '0' + str(t))
     }
	srun_dm_res=requests.get(srun_dm_api,params=srun_portal_params,headers=header)
	print(srun_dm_res.text)
	return srun_dm_res.text
	