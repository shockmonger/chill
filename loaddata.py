#make Dataset
"""Workbook[sheets[values[#messagekeypressID,#messagekeypressID]]]"""

data = pd.DataFrame()

for i in range(0,len(parts),1):
    wb = openpyxl.load_workbook(filename = fil+'indivData/'+parts[i]+'.xlsx')
    sheets = wb.get_sheet_names()
    for j in range(0,3,1):
        name = sheets[j]
        sheet_ranges = wb[name]
        df = pd.DataFrame(sheet_ranges.values)
        df.columns = ['id','ms','time','type','key','lmapped','rmapped']
        newdf = df.sort_values('type')
        locs = newdf.loc[(df['key']=='# Message: UE-keypress C') & (df['type']=='MSG')]
        ids = locs.filter(['id'],axis =1)
        ids['participant'] = i
        ids['song'] = j
        frames = [data,ids]
        data= pd.concat(frames)
        

#Load Dataset
wb = openpyxl.load_workbook(filename = fil+'finalchills.xlsx')
sheets = wb.get_sheet_names()
name = sheets[0]
sheet_ranges = wb[name]
df = pd.DataFrame(sheet_ranges.values)
df.columns = ['id','participant','song','start','end']