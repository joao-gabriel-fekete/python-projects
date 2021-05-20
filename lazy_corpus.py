import pandas as pd #Pandas is the module used for working with DataFrames
import re #Best way to work with RegEx
import os #usado pelo shutil e glob (operating system)
import shutil # for high-level file and directory handling
import glob #encontra paths através de padrões

metadados = pd.read_excel(r'C:\Users\conta\Documents\metadados_lazy_corpus.xlsx') #Planilha deve estar em .xlsx e a última parte corresponder ao nome do arquivo | lembre-se de alterar o path para encontrar o seus "Documents".

metadados["codigo_limpo"] = metadados["Código"]

for l,w in metadados.iterrows():
    line = w["codigo_limpo"]
    line = re.sub(r'<', "", line)
    w["codigo_limpo"] = re.sub(r'>', "", line)

st_metadado = metadados[["Código", "Copie e cole seu texto logo abaixo:", "codigo_limpo"]] #Seleciona apenas as colunas necessárias para continuar o processo

path = r'C:\Users\conta\Documents'
#Creating a folder for texts
os.makedirs(path+'\Textos-CorIFA')

# Creating txt
for i, j in st_metadado.iterrows():
    code = j["codigo_limpo"] + '.txt'
    f = open("C:/Users/conta/Documents/Textos-CorIFA/"+code, "w", encoding="utf-8")
    f.writelines([j["Código"], "\n"])
    f.writelines(j["Copie e cole seu texto logo abaixo:"])
    f.close()

dest = path+ r"\Textos-CorIFA"

#Creating Directories
for i in range(1,9):
    os.mkdir(dest+r'\Batch_'+str(i))
    batches = glob.glob(dest+r'\Batch_[0-9]')
        
txt = glob.glob(dest+'\*[0-9].txt')

#Dividing per Batch
for i in txt:
    if re.match(r'.+Ne.Abs.*\.txt', i):
        shutil.move(i, batches[0])
    elif re.match(r'.+E.Abs.*\.txt', i):
        shutil.move(i, batches[1])
    elif re.match(r'.+Ne.SoP.*\.txt', i):
        shutil.move(i, batches[2])
    elif re.match(r'.+E.SoP.*\.txt', i):
        shutil.move(i, batches[3])
    elif re.match(r'.+Ne.AEss.*\.txt', i):
        shutil.move(i, batches[4])
    elif re.match(r'.+E.AEss.*\.txt', i):
        shutil.move(i, batches[5])
    elif re.match(r'.+Ne.LiR.*\.txt', i):
        shutil.move(i, batches[6])
    else :
        shutil.move(i, batches[7])
