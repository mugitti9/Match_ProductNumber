import pandas as pd
import numpy as np
import os,tkinter,tkinter.filedialog,tkinter.messagebox

root=tkinter.Tk()
root.withdraw()
fTyp=[("","*")]
tkinter.messagebox.showinfo("一致確認プログラム","読み込むファイルを選んでください")
fileA=tkinter.filedialog.askopenfilename(filetypes=fTyp)
tkinter.messagebox.showinfo("一致確認プログラム","保存先を選んでください")
file_path=tkinter.filedialog.askdirectory()

df_A = pd.read_excel(fileA,sheet_name ="A")
df_A.set_axis(["職場","品番","品名","支給先","発行ＮＯ","日付","数量","親品番","親品名","型式","発行","日付2","削除"],axis='columns', inplace=True)
df_C = pd.read_excel(fileA,sheet_name ="C",header=2)
OutNum=list(df_C.発行NO)

OutDate=[];
for i in range(len(df_A)):
    OutDate.append(df_C.指示日[OutNum.index(df_A.発行[i])])
    
OutDate_DataFrame=pd.DataFrame(OutDate)
OutDate_DataFrame.set_axis(["指示日"],axis='columns', inplace=True)
Number2=pd.DataFrame(df_A.削除)
df_A.drop("削除", axis=1,inplace=True)
df_A=df_A.join(OutDate_DataFrame)
Number2.set_axis(["数量2"],axis='columns', inplace=True)
df_A=df_A.join(Number2)


df_B=df_A.sort_values("品番")

Before_Word=""
Change_List=[]
for i in range(len(df_B)):
    if df_B.品番[i]!=Before_Word:
        Change_List.append(i)
    Before_Word=df_B.品番[i]
    
List_Add=[];
List_Add_Before=[];
for i in range(len(df_B)):
    if i in Change_List:
        if i!=len(df_B):
            List_Add.append(List_Add_Before)
            List_Add_Before=[]
            i=i+1
        else:
            List_Add.extend(List_Add_Before)
            List_Add_Before=[]
    else:
        List_Add_Before.append(df_B.発行[i])
        List_Add_Before.append(df_B.日付2[i])
        List_Add_Before.append(df_B.指示日[i])
        List_Add_Before.append(df_B.数量2[i])
        
Data_Print=[]
for i in range(len(df_B)-1):
    if i in Change_List:
        Data_Print.append(List_Add[Change_List.index(i)+1])
    else:
        Data_Print.append([])
        
Data_Print.append([])   
DataFrame_Add=pd.DataFrame(Data_Print)
df_Out=df_B.join(DataFrame_Add)
df_D=df_Out.sort_index()

for i in range(len(df_D)):
    if df_D.iat[i, 14]==None:
        df_D.iat[i, 12]=None
        
file_path=file_path+"/Result.csv"
df_D.to_csv(file_path,encoding="utf_8_sig",index=False)