"""*************************************************************************************************
====FILE
	OS_get_file_path_name(initial_dir="\\")
	OS_get_user_passwd_with_dialog(credential_dir_filename="")


====DATE TIME
	OS_get_8_digit_GMT_date(delta_day)


====COMMUNICATION PROTOCOL
	OS_SSH(host,port,user,pwd,command)
	OS_sftp_download(host,port,username,password,local,remote)
	OS_sftp_upload(host,port,username,password,local,remote)
	
	
====SHARE POINT
	OS_test_credential_by_sharepoint(user,pwd,test_url='http://central.syniverse.com/Pages/home.aspx')
	OS_fileupdate_from_sharepoint(user,pwd,url,output_file_name_path)

====COMPRESS
OS_un_tgz(source_file_path_name,target_path='')

Last Modified by:
Wind 20181030
*************************************************************************************************"""

"""====FILE**************************************************************************************"""

"""*************************************************************************************************
OS_get_file_path_name enable windows user to locate and select a file in dialog window and return the
full_name (path&file name)file path and file name as a list
initial_dir specified where the system start to browse, it can be eigher absolute director like
"C:\\DATA" or relative directory like "\\DATA"

Wind 20180924
*************************************************************************************************"""
def OS_get_file_path_name(initial_dir="\\"):
	import time,os.path, os,shutil,tkinter.filedialog
	if initial_dir[0].isalpha()==False:#Not start like c:
		initial_dir=os.getcwd()+initial_dir
	root1=tkinter.Tk()
	root1.withdraw()
	full_name=tkinter.filedialog.askopenfilename(title="Choose File",\
	initialdir=(os.path.expanduser(initial_dir)))
	root1.destroy()
	file_path=os.path.split(full_name)[0]
	file_name=os.path.split(full_name)[1]
	return([full_name,file_path,file_name])

#print (OS_get_file_path_name("\\file\\msu_report"))
#print (OS_get_file_path_name("C:\\file\\msu_report"))

"""*************************************************************************************************
OS_listFile return a list of file and dir names under specified directory
file suffix can be specified, is suffix=*, it will return all file and directory name
Wind 20181201
*************************************************************************************************"""
def OS_listFile(directory,suffix='*'): 
	import os
	file_name_list = []
	files = os.listdir(directory)  
	for filename in files:  
		if os.path.splitext(filename)[1] == suffix or suffix=="*":
			file_name_list.append(filename)	
	return file_name_list
	
#print(OS_listFile('.\\','*'))
#print(OS_listFile('c:\\','.ppt'))



"""*************************************************************************************************
OS_get_user_passwd_with_dialog(credential_dir_filename="")
if credential_dir_filename ="" ,it will open dialog and obtain user, pwd if they are not empty
if credential_dir_filename !="":
if credential_dir_filename is valid format, it will return user and pwd read from file
if credential_dir_filename is invalid format or not exist,it will trigger dialog to get user,pwd
return the value and update credential_dir_filename
if path in credential_dir_filename does not exist, it will prompt error and return["",""]

outputformat:[user,pwd]

20181017 Wind
*************************************************************************************************"""
def OS_get_user_passwd_with_dialog(credential_dir_filename=""):
	import os,os.path,tkinter,sys
	import tkinter.messagebox
	global user,pwd
	user=pwd=""
	
	def show_login():#populate global variable user,pwd
		global user
		global pwd
		def login():
			global user
			global pwd
			user=entryName.get()
			pwd=entryPwd.get()
			root.destroy()

		def cancel():
			global user,pwd
			user=pwd=""
			root.destroy()
			sys.exit()

		root = tkinter.Tk()
		root.title("Enter your gid/password")
		root.geometry('330x170+500+200')
	
		labelName = tkinter.Label(root,text='Your Gid:',justify=tkinter.RIGHT,width=100)
		labelName.place(x=40, y=20, width=110, height=20)
	
		varName = tkinter.StringVar(root, value='')
		entryName = tkinter.Entry(root,width=80,textvariable=varName)
		entryName.place(x=170, y=20, width=100, height=20)
	
		labelPwd = tkinter.Label(root,text='Your Lan Password:',justify=tkinter.RIGHT,width=100)
		labelPwd.place(x=40, y=55, width=110, height=20)
	
		varPwd = tkinter.StringVar(root, value='')
		entryPwd = tkinter.Entry(root,show='*',width=80,textvariable=varPwd)
		entryPwd.place(x=170, y=55, width=100, height=20)
	
		buttonOk = tkinter.Button(root,text='Confirm',command=login)
		buttonOk.place(x=80, y=100, width=80, height=20)
	
		buttonCancel = tkinter.Button(root,text='Cancel',command=cancel)
		buttonCancel.place(x=180, y=100, width=80, height=20)
		
		root.mainloop()

	#start
	if credential_dir_filename=="":
		while user=="" or pwd=="":
			show_login()
		return([user,pwd])
	if credential_dir_filename!="":
		if credential_dir_filename[0].isalpha()==False:#Not start like c
			credential_dir_filename=os.getcwd()+credential_dir_filename
			print(credential_dir_filename)
		credential_dir=os.path.split(credential_dir_filename)[0]
		credential_filename=os.path.split(credential_dir_filename)[1]
		if not os.path.exists(credential_dir):
			root1=tkinter.Tk()
			root1.withdraw()
			tkinter.messagebox.showinfo('Credential file path error.',"Path "+credential_dir+" not exist")
			return(["",""])
		if not os.path.exists(credential_dir_filename):
			while user=="" or pwd=="":
				show_login()
			output = open(credential_dir_filename, 'w')
			output.write(user+' '+pwd)
			output.close()
			return([user,pwd])
			
		if os.path.exists(credential_dir_filename):
			input=open(credential_dir_filename)
			info=input.read().split(' ')
			input.close()
			if len(info)==2:
				user=info[0]
				pwd=info[1]
				return([user,pwd])
			if len(info)!=2:
				while user=="" or pwd=="":
					show_login()
				output = open(credential_dir_filename, 'w')
				output.write(user+' '+pwd)
				output.close()
				return([user,pwd])
	
#print (OS_get_user_passwd_with_dialog('C:\\python_work\\userinfo.txt'))
#print (OS_get_user_passwd_with_dialog())
#print (OS_get_user_passwd_with_dialog("\\c.txt"))			

"""====DATE TIME*********************************************************************************"""

"""*************************************************************************************************
OS_get_8_digit_GMT_date returns date in 8 digital format like 20181010
if need local time, replace gmtime with localtime in code
to get today, delta_day=0
to get yesterday, delta_day=-1

Wind 20181010
*************************************************************************************************"""
def OS_get_8_digit_GMT_date(delta_day):
	import time

	year=str(time.gmtime(time.time()+24*60*60*delta_day).tm_year)
	month=str(time.gmtime(time.time()+24*60*60*delta_day).tm_mon)
	if len(month)==1:
		month="0"+month		
	day=str(time.gmtime(time.time()+24*60*60*delta_day).tm_mday)
	if len(day)==1:
		day="0"+day		
	timestamp=year+month+day
	return(timestamp)
	
#print(OS_get_8_digit_GMT_date(-1))


'''***************COMMUNICATION PROTOCOL****************************************************************'''

def OS_SSH(host,port,user,pwd,command):
	import paramiko
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=host,port=port, username=user, password=pwd)
	stdin, stdout, stderr = ssh.exec_command(command)
	res,err = stdout.read(),stderr.read()
	result = res if res else err
	dirresult=result.decode().rstrip().lstrip()
	return(dirresult)
	
#print(OS_SSH('10.162.28.187',22,'g707414','%password','netstat -an'))


"""*******************************************************************************************************
OS_sftp_download(host,port,username,password,local,remote)
OS_sftp_upload(host,port,username,password,local,remote)
#host='10.162.28.182'
#port = 22 
#username='g707414'
#password='XXXXXX'
if local is a directory, then remote must be a directory, in this case ,will download all file from remote
directory to local directory
if local is a file, then remote must be a file,in this case, the remote file will be downloaded to local 
file
#local = 'C:\\sftptest\\'#local direcotry，if local OS is windows"\\" is used
#local = 'C:\\sftptest\\test.xml'#local file，if local OS is windows"\\" is used
#remote = '/home/g707414/'#remove direcotry, use "/" for linux
#remote = '/home/g707414/diameter-dsc.xml'#remote file, use "/" for linux


Version: v1.1 2018.11.27

*******************************************************************************************************"""
def OS_sftp_download(host,port,username,password,local,remote):
	import paramiko,os,platform,stat

	sf = paramiko.Transport((host,port))
	sf.connect(username = username,password = password)
	sftp = paramiko.SFTPClient.from_transport(sf)
	try:
		if os.path.isdir(local):# if variable local is a directory
			for f in sftp.listdir(remote):#get all files in remote direcotry
				print(f)
				sftp.get(os.path.join(remote+f),os.path.join(local+f))#下载目录中文件
				#sftp.get('.kshrc',os.path.join(local+f))#下载目录中文件
		else:
			sftp.get(remote,local)#download
	except Exception as e:
		print('download exception:',e)
	sf.close()
	
def OS_sftp_upload(host,port,username,password,local,remote):
	import paramiko
	import os
	import platform
	import stat
	sf = paramiko.Transport((host,port))
	sf.connect(username = username,password = password)
	sftp = paramiko.SFTPClient.from_transport(sf)
	try:
		if os.path.isdir(local):# if variable local is a directory
			for f in os.listdir(local):#get all files in remote direcotry
				sftp.put(os.path.join(local+f),os.path.join(remote+f))#上传目录中的文件
		else:
			sftp.put(local,remote)#upload
	except Exception as e:
		print('upload exception:',e)
	sf.close()
	
def DEMO_download_a_file():
	host='10.162.28.182'
	port = 22 
	username='g707414'
	password='XXXCXX'
	local = 'C:\\sftptest\\test.xml'
	remote = '/home/g707414/diameter-dsc.xml'
	OS_sftp_download(host,port,username,password,local,remote)

def DEMO_upload_a_file():
	host='10.162.28.182'
	port = 22 
	username='g707414'
	password='#XXXXXX'
	local = 'C:\\sftptest\\test.xml'
	remote = '/home/g707414/diameter-dsc2.xml'
	OS_sftp_upload(host,port,username,password,local,remote)

def DEMO_download_all_file():
	host='10.162.28.182'
	port = 22 
	username='g707414'
	password='XXXXXXX'
	local = 'C:\\sftptest\\'
	remote = '/home/g707414/'
	OS_sftp_download(host,port,username,password,local,remote)
	
#DEMO_download_all_file()

'''***************SHARE POINT **************************************************************************'''



"""*************************************************************************************************
OS_test_credential_by_sharepoint verify username and password by trying to open the test_url 
on sharepoint by HttpNtlAuth.
If user and pwd are correct, it will return True.
If user and pwd are not correct, it will return False.
If other error meet like url error, it will prompt error and exist.
If the result code is unexpected, it will return result code

This function is developed by Greg and updated by Wind

20181017 Greg/Wind
*************************************************************************************************"""


def OS_test_credential_by_sharepoint(user,pwd,test_url='http://central.syniverse.com/Pages/home.aspx'):

	import tkinter,tkinter.messagebox,os,os.path,requests,sys,datetime,time
	from requests_ntlm import HttpNtlmAuth

	try:
		r1=requests.get(test_url,auth=HttpNtlmAuth(user,pwd))
	except requests.exceptions.ConnectionError:
		print ('Connection error, URL address not found, please check URL.\n')
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning', 'Connection error, URL address not found, please check URL.'+test_url)
		sys.exit()
	except requests.exceptions.MissingSchema:
		print ('Invalid URL '+test_url+' : No schema supplied. Perhaps you meant http://'+ test_url+'?\n')
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning', 'Invalid URL '+test_url+' : No schema supplied. Perhaps you meant http://'+ test_url+'?\n')
		sys.exit()
	else:
		res1= r1.status_code
# process different HTTP reponse codes 
	if res1==404:
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning','No file in the URL, please double check URL.')
		print ('No file in the URL, please double check URL.\n\n')
		sys.exit()
		return()
	if res1==401:
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning','User name or password incorrect.')
		root1.destroy()

		return(False)
	if res1==200:
		return(True)
	return(resl)
#print(OS_test_credential_by_sharepoint('g707414','XXXXXXX'))


"""*************************************************************************************************
OS_fileupdate_from_sharepoint download file from sharepoint url if local file does not exist
or local file is older than file on sharepoint.

If user,pwd,url or the directory of output_file_name_path, this function will quit with prompt

This function is developed by Greg and updated by Wind

20181030 Greg/Wind
*************************************************************************************************"""

def OS_fileupdate_from_sharepoint(user,pwd,url,output_file_name_path):
	import tkinter,tkinter.messagebox,os,os.path,requests,sys,datetime,time
	from requests_ntlm import HttpNtlmAuth
	GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
#check if user,pwd,url are valid
	try:
		r1=requests.get(url,auth=HttpNtlmAuth(user,pwd))
	except requests.exceptions.ConnectionError:
		print ('Connection error, URL address not found, please check URL.\n')
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning', 'Connection error, URL address not found, please check URL.')
		sys.exit()
	except requests.exceptions.MissingSchema:
		print ('Invalid URL '+url+' : No schema supplied. Perhaps you meant http://'+ url+'?\n')
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning', 'Invalid URL '+url+' : No schema supplied. Perhaps you meant http://'+ url+'?\n')
		sys.exit()
	else:
		res1= r1.status_code
# process different HTTP reponse codes 
	if res1==404:
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning','No file in the URL, please double check URL.')
		print ('No file in the URL, please double check URL.\n\n')
		sys.exit()
		return()
	if res1==401:
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning','User name or password incorrect.')
		root1.destroy()
		return()
		
	if output_file_name_path[0].isalpha()==False:#Not start like c
		output_file_name_path=os.getcwd()+output_file_name_path
		
	output_file=os.path.split(output_file_name_path)[1]
	output_file_directory=os.path.split(output_file_name_path)[0]

	if not os.path.exists(output_file_directory):
		print ("The directory of "+output_file_directory+" dose not exist. Please double check the file directory name.\n")
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showwarning('Warning',"The directory of " +output_file_directory+" dose not exist. Please double check the file directory name.")
		sys.exit()
		
# get url file modification time
	c1=r1.headers
	time1=datetime.datetime.strptime(c1 ['Last-Modified'], GMT_FORMAT)
	timeArray1 = time.strptime(str(time1), "%Y-%m-%d %H:%M:%S")
	urltimestamp = int(time.mktime(timeArray1))
	
# if the file in target directory does not exit, download file dircetly from url
	if not os.path.exists(output_file_name_path):		
		print (output_file+" dose not exist. Start downloading "+ output_file +" from provided url\n")
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showinfo('Information', output_file+" dose not exist. Start downloading "+ output_file +" from provided URL.")
		with open(output_file_name_path, "wb") as code:
			code.write(r1.content)
		print (output_file+" is downloaded successful\n")
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showinfo('Information', output_file+" is downloaded successful.")
		return (0)

# if file exits, get the local file's modification time
	output_filetimestamp=int(os.path.getmtime(output_file_name_path))

# if local file is older than url file, start updating file
	if output_filetimestamp > urltimestamp:
		print ("The "+output_file +" in your local directory is the lastest version.\n")

	else:
		print ("A new version of " +output_file+" is found. Start downloading the new version of "+ output_file +" from provided URL.\n")
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showinfo('Information', "A new version of " +output_file+" is found. Start downloading the new version of "+ output_file +" from provided URL.")
		with open(output_file_name_path, "wb") as code:
			code.write(r1.content)
		print (output_file+" is updated successful.\n")
		root1=tkinter.Tk()
		root1.withdraw()
		tkinter.messagebox.showinfo('Information', output_file+" is updated successful.")

#OS_fileupdate_from_sharepoint ('g707414','XXXXXX','http://central.syniverse.com/sites/TECH/io/ipxop/ts/Shared%20Documents/DSS/Tools/file/PeeringPolicy.csv','\\PeeringPolicy.csv')


'''***************COMPRESS **************************************************************************'''



"""*************************************************************************************************
OS_un_tgz unzip source file to target path
if target path='', unzip to current directory

20181201 Wind.Wang@syniverse.com
*************************************************************************************************"""
def OS_un_tgz(source_file_path_name,target_path=''):
	import os
	import tarfile
	if target_path=='':
		target_path=os.getcwd()
	tar = tarfile.open(source_file_path_name)
	names = tar.getnames()
	for name in names:
		tar.extract(name,target_path)
	tar.close()
f_name='.\\dsc_msu_report_by_operator.daily.HK1P.20181128.tgz'
#OS_un_tgz(f_name,'..\\')
