import openpyxl, pprint
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']
data={}
totpop=0
for row in range(2,sheet.max_row+1):
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
    data.setdefault(state,{})
    data[state].setdefault(county,{'tracts':0,'pop':0})
    data[state][county]['tracts']+=1
    data[state][county]['pop']+=int(pop)
    totpop+=int(pop)
popFile=open('cansus2010.py','w')
popFile.write(pprint.pformat(data))
popFile.close()
print(totpop)
