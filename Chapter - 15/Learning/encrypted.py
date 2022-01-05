import PyPDF2
pdfFileObj=open('encrypted.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.isEncrypted)
if(pdfReader.isEncrypted):
    pdfReader.decrypt('rosebud')
pageObj=pdfReader.getPage(0)
print(pageObj.extractText())
