"""*************************************************************************************************

	DATA_PROCESS_str_transform_2_2d_list(string,seg_mark_1,seg_mark_2,min_len)
	DATA_PROCESS_sort_list_of_list(list_of_list,position,trend="down")


Last Modified by:
Wind.WANG@SYNIVERSE.COM 20181110
*************************************************************************************************"""




"""*************************************************************************************************
DATA_PROCESS_STR_transform_str_2_2d_list transform string list into a list of list
typically, seg_mark_1 shall be "\n",seg_mark_2 shal be " "
if seg_mark_2 !=" ",items in level2 list will be stripped
after splited by seg_mark_1, if the len of str is less than min_len, it will be ignored

Wind.Wang@syniverse.com 20180924
*************************************************************************************************"""
def DATA_PROCESS_str_transform_2_2d_list(string,seg_mark_1,seg_mark_2,min_len):
	list_split_by_seg1=[]
	list_level_1=[]
	list_remove_blank=[]
	output=[]
	list_split_by_seg1=string.split(seg_mark_1)
	
	for row in list_split_by_seg1:
		if len(row)>min_len:
			list_level_1.append(row)
			
	for row in list_level_1:
		items_in_row=row.split(seg_mark_2)
		list_level_2=[]
		if seg_mark_2==" ":
			for item in items_in_row:
				if item.strip()!="":
					list_level_2.append(item)
			output.append(list_level_2)
		else:
			for item in items_in_row:
				list_level_2.append(item.strip())
			output.append(list_level_2)
	return(output)
	
a="""sctp       0      0 173.209.220.115:17167       223.224.117.114:3868        ESTABLISHED 
sctp       0      0 173.209.220.115:3868        112.215.136.74:7170         ESTABLISHED 
sctp       0    712 173.209.220.115:3868        112.215.136.34:6144         ESTABLISHED 

sctp       0      0 173.209.220.115:3868        103.2.216.243:35662         ESTABLISHED 
sctp       0      0 173.209.220.115:3868        223.224.146.41:48861        ESTABLISHED """
b="""362 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6818#Radiomovil-TELCEL        |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
    265 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6566#Bell-Mobility            |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
    265 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6121#Telus-Mobility           |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
    186 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6937#Jersey-Telecom           |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
    144 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6497#Rogers-Wireless          |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
    126 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6585#China-Mobile             |Fw-Ans-RstCode:null|Fw-Ans-ExpRstCode:5004|Fw-Ans-ErrMsg:null            
    112 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6623#TM-Mexico                |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
     88 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:7319#Claro-Puerto-Rico        |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
     75 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6639#Claro-Brazil             |Fw-Ans-RstCode:null|Fw-Ans-ExpRstCode:5004|Fw-Ans-ErrMsg:null            
     70 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6895#BTC-Bahamas              |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
     68 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:null                          |Fw-Ans-RstCode:null|Fw-Ans-ExpRstCode:5004|Fw-Ans-ErrMsg:null            
     57 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6514#NTT-DoCoMo               |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
     55 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:7011#TM-Peru                  |Fw-Ans-RstCode:null|Fw-Ans-ExpRstCode:5004|Fw-Ans-ErrMsg:null            
     54 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6684#China-Unicom             |Fw-Ans-RstCode:2001|Fw-Ans-ExpRstCode:null|Fw-Ans-ErrMsg:null            
     53 |Req-O-OP:6538#Verizon-Wireless         |Req-D-OP:6912#Compania-Dominicana      |Fw-Ans-RstCode:null|Fw-Ans-ExpRstCode:5004|Fw-Ans-ErrMsg:null"""

#print(DATA_PROCESS_str_transform_2_2d_list(a,"\n"," ",5))
#print(DATA_PROCESS_str_transform_2_2d_list(b,"\n","|",5))


"""*************************************************************************************************
DATA_PROCESS_sort_list_of_list sort sub list in list of list by value of interger in speicifed 
position in each sub list.
the position starts from 0(0 indicates sort by the first item in sub list).
trend = "down" or "up", which means sort by big to small or small to bigger in value

Greg.Zhai@syniverse.com 20181109
*************************************************************************************************"""

def DATA_PROCESS_sort_list_of_list(list_of_list,position,trend="down"):
	def swap(listA,i,j):
		temp=listA[i]
		listA[i]=listA[j]
		listA[j]=temp
		
	length=len(list_of_list)
	for i in range(length):
		max_or_min=i
		for j in range(i+1, length):
			if int(list_of_list[max_or_min][position])<int(list_of_list[j][position]) and trend=="down":
				max_or_min=j
			if int(list_of_list[max_or_min][position])>int(list_of_list[j][position]) and trend=="up":
				max_or_min=j
		if i!=max_or_min:
			swap(list_of_list,i,max_or_min)
	return(list_of_list)
#LOL=[[2,3,1],[3,4,2],[1,2,5]]
#print(DATA_PROCESS_sort_list_of_list(LOL,0,"up"))

