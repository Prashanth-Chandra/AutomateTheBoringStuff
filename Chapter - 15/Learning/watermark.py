import PyPDF2 as pdf
pdfReader=pdf.PdfFileReader(open('meetingminutes.pdf','rb'))
pdfWaterReader=pdf.PdfFileReader(open('watermark.pdf','rb'))
watermarkObj=pdfWaterReader.getPage(0)
pdfWriter=pdf.PdfFileWriter()
for i in range(pdfReader.numPages):
    print(i)
    pageObj=pdfReader.getPage(i)
    pageObj.mergePage(watermarkObj)
    pdfWriter.addPage(pageObj)
finalPdf=open('watermarkCover.pdf','wb')
pdfWriter.write(finalPdf)

finalPdf.close()
print("Done")
