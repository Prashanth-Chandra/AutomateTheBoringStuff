import os,pathlib,sys
import PyPDF2
path=pathlib.Path('G:\\Automate The Boring Stuff\\Chapter - 15\\Encrypted')
for folder,subfolder,files in os.walk(path):
    for filenames in files:
        if(filenames.endswith('.pdf')):
            print(filenames)
            #print("CP2")
            x=open(os.path.join(folder,filenames),'rb')
            pdfReader=PyPDF2.PdfFileReader(x)
            #print("CP1")
            if(pdfReader.isEncrypted==False):
                pdfWriter=PyPDF2.PdfFileWriter()
                for pgno in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pgno))
                pdfWriter.encrypt('chandu')
                name=str(filenames)+str("_encrypted")
                repPdf=open(filenames,'wb')
                pdfWriter.write(repPdf)
                repPdf.close()
                print("Encrypted PDF ",filenames)
