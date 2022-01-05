import PyPDF2 as pdf
pdfReader=pdf.PdfFileReader(open('meetingminutes.pdf','rb'))
pdfWriter=pdf.PdfFileWriter()
for i in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(i))
pdfWriter.encrypt('ABSTRACTLY')
finalPdf=open('encryptedminutes.pdf','wb')
pdfWriter.write(finalPdf)
finalPdf.close()
print("Done")
