import re
raw1='SELECT T.SWB_CNTRY_ID,T.CNTRY_TYPE_CD,T.DW_EFF_DT,S.DW_AS_OF_DT FROM (SELECT SWB_CNTRY_ID, CNTRY_TYPE_CD, RCV_IN, DW_EFF_DT,MAX(DW_EFF_DT) MAX_EFF_DT FROM IDW_DATA.CNTRY_MULTI_DEF_CD_T WHERE CURR_IN=1 GROUP BY 1,2,3,4) T, (SELECT SWB_CNTRY_ID, CNTRY_SCHEME_CD,DW_AS_OF_DT,DW_ACTN_IND FROM IDW_STAGE.CNTRY_MULTI_DEF_CD_S) S WHERE S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD AND (S.DW_SCTN_IND=‘U’ OR (S.DW_ACTN_IND=‘I’ AND T.RCV_IN=0)) AND S.DW_AS_OF_DT > T.MAX_EFF_DT'
count=0
substrName=set()
s=re.split("FROM",raw1,flags=re.IGNORECASE)[0]
s1=re.split("select",s,flags=re.IGNORECASE)[1]
for st in s1.split(','):
    substrName.add(st.split('.')[0].strip())
print(substrName)
raw=re.search('FROM(.*)Where', raw1,re.IGNORECASE).group(1)
substart,substop=[],[]
for x in range(0,len(raw)):
    if(raw[x]=='('):
        count+=1
        if(count==1):
            substart.append(x)
    elif(raw[x]==')'):
        count-=1
        if(count==0):
            substop.append(x)
print(substart,substop)
print(s1)
for z in s1.split(','):
    for x in range(0,len(substart)):
        find=re.search(z.split('.')[1],raw[substart[x]:substop[x]],re.IGNORECASE)
        print(find)
    

        