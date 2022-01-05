import PyPDF2 as pdf
import sys
import time
file=input("Enter the file without any spellling mistakes : ")
t0=time.time()
#print("cp1")
passwords=open('dictionary.txt').readlines()
#print("CP2")
pdfReader=pdf.PdfFileReader(open(file+".pdf",'rb'))
#print("CP3")
for i in passwords:
    print("Trying with key : ",i)
    if(pdfReader.decrypt(i.upper().strip())==1 or pdfReader.decrypt(i.lower().strip())==1):
        print("The password is : ",i)
        print("It took",time.time()-t0,"seconds for my potato pc to crack the password")
        sys.exit()
print("You have a strong password and I was not able to find it")
