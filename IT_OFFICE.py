"""*************************************************************************************************
====EXCEL
	OFFICE_merge_csv_to_xls(filename_cut,sheetname_lenth,initial_dir="\\")


====OUTLOOK
	OFFICE_sendemail (Tolist, Cclist, Subject,Sentence1,attachment="Null")
	OFFICE_send_plain_mail (Tolist, Cclist, Subject, Sentence1,attachment="Null")





Last Modified by:
wind.wang@syniverse.com 20181016
*************************************************************************************************"""

"""====EXCEL*************************************************************************************"""

"""*************************************************************************************************
merge_csv_to_xls enable user to merge multiple csv with same name header to one xls file.
f is the number to cut file header from rear
c is the number of charactor from the rear of filename for sheet name
if source file name is ABC20180913.csv,ABC20180914.csv f=-2,c=-4
                       ABC201809
merged filename will be ABC281809,sheet name will be 0913&0914

wind.wang@syniverse.com 20180924
*************************************************************************************************"""
def OFFICE_merge_csv_to_xls(filename_cut,sheetname_lenth,initial_dir="\\"):
	from IT_OS import IT_OS_get_file_path_name
	import xlwt,os,csv
	fpfn= IT_OS_get_file_path_name(initial_dir)
	file_path=fpfn[0]
	file_name=fpfn[1]
	suffix_lenth=len('.csv')
	
	if os.path.splitext(file_name)[1] != '.csv':
		print("Error,only csv file is supported.")
		return()
	file_header=file_name[:filename_cut-suffix_lenth]
	print("file_header")
	print(file_header)
	csv_file_list = []
	files = os.listdir(file_path)  
	for filename in files:  
		if os.path.splitext(filename)[1] == '.csv':
			if file_header in os.path.splitext(filename)[0]:
				csv_file_list.append(filename)

	print (csv_file_list)
	output_file_name=file_header+".xls"
	book = xlwt.Workbook()
	
	for file in csv_file_list:
		f = open(file_path+"\\"+file, 'r')
		csvreader = csv.reader(f)
		final_list = list(csvreader)
		sheet = book.add_sheet(file[(sheetname_lenth-suffix_lenth):-4])
		row = 0
		for entry in final_list:
			column= 0
			for item in entry:
				sheet.write(row,column,item)
				if sheet.col(column).width < (len(item)+1)*256:
					sheet.col(column).width=(len(item)+1)*256
				column+=1
			row+=1
	book.save(file_path+"\\"+output_file_name)
	fp=file_path.replace("/","\\")
	os.system("explorer.exe %s" % fp)
	
#IT_OFFICE_merge_csv_to_xls(-2,-4)

"""*************************************************************************************************
Tansfer decimal number to excel column letter string
can only process less than 701
to be improved in future

wind.wang@syniverse.com 20181114
*************************************************************************************************"""
def OFFICE_transfer_decimal_column_to_excel_letter_column(dec_column):

	if dec_column>701:
		print("can not process more than 701")
		return()
	if dec_column<=26:
		return(chr(digit_column+64))
	if dec_column>26:
		d1=dec_column//26
		d2=dec_column%26
		return(chr(d1+64)+chr(d2+64))



"""====OUTLOOK***********************************************************************************"""

"""*************************************************************************************************
OFFICE_sendemail AND sende_plain_mail utilize Outlook to send email
attachment is an opentional parameter
20181016 greg.zhai@syniverse.com created modified by wind.wang@syniverse.com
*************************************************************************************************"""
def OFFICE_sendemail (Tolist, Cclist, Subject,Sentence1,attachment="Null"):
	#First, install pywin32 by using "python -m pip install pypiwin32" on Windows Command console
	import os
	import win32com.client as win32
	if attachment[0].isalpha()==False:#Not start like c:
		attachment=os.getcwd()+attachment
	outlook = win32.Dispatch('outlook.application') 
	mail = outlook.CreateItem(0)
	mail.To = Tolist
	mail.CC = Cclist
	mail.Subject = Subject
	mail.HTMLBody=Sentence1
	if attachment!="Null":
		mail.Attachments.Add(attachment)
	mail.Display()
	return(0)
	
def OFFICE_send_plain_mail (Tolist, Cclist, Subject, Sentence1,attachment="Null"):
	#First, install pywin32 by using "python -m pip install pypiwin32" on Windows Command console
	import win32com.client as win32
	outlook = win32.Dispatch('outlook.application') 
	mail = outlook.CreateItem(0)
	mail.To = Tolist
	mail.CC = Cclist
	mail.Subject = Subject
	mail.Body=Sentence1
	if attachment!="Null":
		mail.Attachments.Add(attachment)
	mail.Display() 

email_body='''<html><body>
	<p style='font-family:Arial;font-size:13;color:black'>
	Dear Colleagues,<br/><br/>
	Greeting from Syniverse!<br/><br/>
	For historical s6a request to establish LTE roaming relationship between OP_A and OP_B.<br/><br/>
	Please let us know if you are interested in open this route via Syniverse.<br/><br/>
	<strong><font color="#0066CC">OP_A<br/></font></strong>
	<Strong>Realm         :</Strong>REALM_A<br/>
	<strong><font color="#0066CC">OP_B<br/></font></strong>
	<strong>Realm         :</Strong>REALM_B<br/>
	<strong>Peering Point :</Strong><Strong><font color="green">SVR_PEER<==>HUB_PEER</font></Strong><br/><br/>
	B.R.<br/><br/>
	<Strong>Syniverse DSS Team<br/></Strong>
	</p>
	</body></html>'''
email_body=email_body.replace('OP_A',"China Mobile")
email_body=email_body.replace('OP_B',"NTT Docomo")
email_body=email_body.replace('REALM_A',"epc111")
email_body=email_body.replace('REALM_B',"epc222")


#OFFICE_sendemail ('greg.zhai@syniverse.com;','ts-dss@syniverse.com', 'Test Email',email_body,'\IT_OFFICE.py')
#OFFICE_send_plain_mail ('greg.zhai@syniverse.com;jason.qin@syniverse.com;joe.feng@syniverse.com','wind.wang@syniverse.com;ts-dss@syniverse.com', 'Test Email','This Email is sent using Python script')

