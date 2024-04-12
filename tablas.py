from tabula import read_pdf 
from tabulate import tabulate 

#reads the table from pdf file 

df = read_pdf("sample.pdf",pages="all") #address of pdf file
print(tabulate(df))
