import PyPDF2 as pdf
import os,pprint
pdfWriter=pdf.PdfFileWriter()
pdfs=[]
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        pdfs.append(file)
pdfs.sort()
pprint.pprint(pdfs)
for i in range(len(pdfs)):
    pdfFile=pdfs[i]
    pdfReader=pdf.PdfFileReader(open(pdfFile,'rb'))
    print("Woring on file :",pdfFile)
    if(pdfReader.isEncrypted):
        continue
    for j in range(1,pdfReader.numPages):
        pageObj=pdfReader.getPage(j)
        pdfWriter.addPage(pageObj)
finalPdf=open("CombSelPages.pdf",'wb')
pdfWriter.write(finalPdf)
finalPdf.close()
print("Done")
