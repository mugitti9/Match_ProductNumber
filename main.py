import pandas 
df_A = pandas.read_excel('/Users/mugikura/Desktop/12月2旬時間納入タロンB/SheetA.xls', sheet_name=0)
df_B = pandas.read_excel('/Users/mugikura/Desktop/12月2旬時間納入タロンB/SheetB.xlsx', sheet_name=0)

Match_List=set(df_A.親品番)&set(df_B.品目番号)
Error_Vec=[]

for i in range(len(df_B)):
    if (df_B.品目番号[i] in Match_List):
        Error_Vec.append(i)

Error_Add=[];
for i in range(len(df_B)):
    if (i in Error_Vec):
        Error_Add.append("○")
    else:
        Error_Add.append("×")

df_B["一致"]=Error_Add
df_B.to_csv("/Users/mugikura/Desktop/12月2旬時間納入タロンB/Keep.csv",encoding='utf-8-sig')