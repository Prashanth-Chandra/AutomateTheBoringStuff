import webbrowser,pyinputplus
def thank_you():
    print("Thank you for using the program")
    sys.exit()
print("Options")
print("Press 1 For Google Browser")
print("Press 2 For Google Maps")
print("Press 3 For Gmail")
opt=int(input())
if opt==1:
    print("Press 1 To open the webbrowser")
    print("Press 2 To search something in the browser")
    opt2=int(input())
    if(opt2==1):
        webbrowser.open('www.google.com')
    elif(opt2==2):
        opt3=input("What to search : ")
        opt3=opt3.replace(" ","+")
        webbrowser.open("https://www.google.com/search?q="+opt3)
elif opt==2:
    print("Press 1 To open Google Maps")
    print("Press 2 To search a location in google maps")
    opt2=int(input())
    if(opt2==1):
        webbrowser.open("https://www.google.com/maps")
    elif(opt2==2):
        opt3=input("Enter the place to search : ")
        opt3=opt3.replace(" ","+")
        webbrowser.open("https://www.google.com/maps/place/"+opt3)
elif opt==3:
    webbrowser.open("https://myaccount.google.com/intro/signing-in-to-google")
    
    
