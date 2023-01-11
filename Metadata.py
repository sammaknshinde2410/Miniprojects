# # Image metadata
# # Metadata extraction
# # gps tracing on browser
# # metadata editing
# # metadata scrubbing
# # Excel file for image(s) metadata


# # IPTC International Press Telecommunications Council
# # EXIF exchangeable image format
# # XMP extensible Metadata format developed by adobe
# # Resource : ngtvspc/EXIF_remover.py
# # Resource : Pillow documentation
# # Resource : Image module documentation

# supporting imports
import os
import smtplib
import sys
from PIL import Image as im, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import csv
import pandas as pd
from email.mime.multipart  import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase

import webbrowser
import gmplot

# declaring Global Variables
c_file = None               # c_file will store the filename
c_image = None              # object of Image class containing the image
cpath = None                # cpath stores the current working directory path
tag_dic = {}             # stores the final dictionary of tags (as keys) and data values
gps_dic = {}              # stores the dictionary associated with tag 'GPSInfo' in tag_dic
# latlong = None              # stores the formatted values of GPS co-ordinates
clean_image = None          # object of Image class that stores the scrubbed Image
i = 0

    # Option - 1 [Changing the directory]
    # Current working directory (cwd)
    # helps to fetch the file from file-path defined by user
    # checks if the user defined filepath exists
    # if TRUE then change the cwd to user defined path
    # cpath -> Current Path defined by user
    # working in cwd gives user a convenience of not requiring to enter the file_path

def menu():
    '''Displays main menu and accepts user inputs for the flow in program'''
    global i
    if i < 1:                       # print this intro only once
        print("-"*40)
        print("Main purpose of this python project is to extract EXIF data from Image (JPG) file\nOther features include:\n* Scrubbing the metadata\n* Extracting and reformatting GPS co-ordinates\n* Creating/updating .xlsx and .csv log file for all images processed")
        print("-"*40)
        i += 1
    else:
        pass

    print("*"*12, "Main Menu", "*"*12)
    option = int(input("1: Change Current working Directory Address\n2: Upload Image File\n3: Extract Image Metadata\n4: Create a clean copy (without metadata)\n5: Location where the image is clicked on Google map\n6 : Creating a thumbnail of the image\n7: Watermark Image\n8: Bulk Mail\n9: Exit\nEnter the option number :  "))
    
    if option == 1:          # to change cwd
        print()
        change_cwd()

    elif option == 2:       # to upload an image
        print()
        import_image()

    elif option == 3:       # to extract metadata from image
        if c_image is None: # if image is not uploaded yet
            print("Upload image first.")
            import_image()
        else:
            meta_extraction()       # initialize extraction process if image already uploaded

    elif option == 4:               # creating a clean copy of the image by scrubbing the metadata
        if c_image is None:
            print("Please upload the image first.")
            import_image()
        else:
            create_copy()           # if image is already uploaded by the user

    elif option == 5:               # option to pin the location in google maps
        if c_file is None:
            print("Please upload the image first.")
            import_image()
        elif bool(tag_dic)==0:
            print("Try again after extraction of metadata.\nInitializing extraction...")
            meta_extraction()
        else:
            gmap()                  # if metadata already extracted then open map and pin the location

    elif option == 6:               # option to create a thumbnail from the Scrubbed image if available
        if c_file is None:          # or original image uploaded by the user
            print("Please upload the image first.")
            import_image()
        elif clean_image is None:
            print("Your original uploaded image is used to create the thumbnail.")
            create_thumbnail(clean_image=c_image, c_file=c_file)
        else:
            create_thumbnail()

    elif option == 9:           # exit
        confirm = input("Are you sure you want to exit? (answer y or n) : ").upper()
        if confirm == "Y":
            stop()
        else:
            menu()

    elif option == 7:   #watermark image
        watermark(c_image=c_image, c_file=c_file, clean_image = clean_image)

    elif option == 8:   #bulk email
        send_mail()




def change_cwd():
    '''Changes the current working directory for the convenience of user to upload the file'''

    print(12 * "-", "Changing CWD", 12 * "-")
    print("Current working directory : ", os.getcwd())    # getcwd() returns the path of cwd
    global cpath
    cpath=input("Enter the directory address where you want program's cwd in the format given below\n[/home/user/Desktop/folder_1/folder_4/folder_2/ ]\n: ")      # dir path

    if os.path.exists(cpath):   # returns a boolean value 'TRUE' if the directory path exists
        os.chdir(cpath)         # change cwd to the directory defined by user
        print("Current Working Directory updated to : ", os.getcwd())
        print("Returning to Main Menu")
        print()
        menu()
    else:
        print("invalid directory. CWD is unchanged.\nCurrent Working Directory : ",os.getcwd())
        print("Restarting the module!")
        print()
        change_cwd()



# closing the program
def stop():
    '''Terminates the program'''
    print("Have a good day!")
    sys.exit()  # terminates the program


# importing data
# Option - 2 - [Importing the image file]
def import_image():
    '''To import the image file'''
    print(12 * "-", "Select an Image file", 12 * "-")

    global c_file
    global c_image



    if (c_file is None) :       # checks if c_file is already created or not
                                # if not then the whole function is executed
                                # if yes then user input for c_file is skipped

        print("Your current working directory (cwd) is  : ", os.getcwd())

        userchk_cwd= input("Check the cwd above and confirm if target image file is in the same directory.\nAnswer y or n : ").upper()

        if userchk_cwd == "Y":    # if cwd is same as image directory then no need for directory path
            print("Great! Now you just have to enter the filename.")
            c_file = input("Enter the name of the Image file : ")  # user input -> name of the image file
            if ".jpg" not in c_file:
                c_file += ".jpg"
            # c_file = "DSCN0010.jpg"     # name of the image file
            c_image = im.open(c_file)     # Creating Image object and accessing the file using the specified path
            im._show(c_image)             # displaying the image uploaded to the user

        elif userchk_cwd == "N":
            c_file = input("No Problem! Just enter the complete directory path "
                           "of the image file including file name in the following format :.\n"
                           "/home/user/Desktop/folder_1/folder_4/folder_2/Image_Metadata.jpg\n")
            c_image = im.open(c_file)  # Creating Image object and accessing the file using the specified path
            im._show(c_image)          # displaying the image uploaded to the user

    else:
        pass

    # asking user to confirm the image file
    userchk_image = input(f"Is this the image file you have uploaded for metadata extraction (file_name: {c_file}?\nEnter 'Y' for yes or 'N' for no : ").upper()

    if userchk_image == "Y":
        print("Image uploaded Successfully. ")
        print()
        menu()

    elif userchk_image == "N":
        print("Restarting Image upload Module...")
        c_file = None
        print()
        import_image()

    else:
        print("Invalid option!")
        print()
        import_image()




# metadata extraction
# option - 3
def meta_extraction():
    '''Extraction of Data and writing it in .csv and .xlsx files'''
    print(12 * "-", "Extracting Metadata ", 12 * "-")
    global tag_dic
    global gps_dic
    global latlong
    global c_image

    # tag_dic = {}          # tag_dic will be extracted EXIF tags and values
    # gps_dic = {}          # gps_dic will store the inner nedictionary assigned to the value w.r.t key tag_dic["GPSInfo"]

   # for those that match value from TAGS is

    print("TAGS:",TAGS)
    print("GPSTAGS : ",GPSTAGS)
    print(c_image._getexif())
    for tag, value in c_image._getexif().items():      # iterating over the values (exif tags/metadata) returned by getexif() from

        if tag in TAGS:                               # cross-referencing keys in tag_dic to that with the keys in TAGS dictionary
            # print("TAGS[tag] : ",TAGS[tag])
            tag_dic[TAGS[tag]] = value

        else:
            pass
    for key, value in tag_dic["GPSInfo"].items():       # Replacing numerical tags of values in GPSInfo
        gps_dic[GPSTAGS[key]] = value                   # with corresponding standard GPSTAGS

    print("tag_dic : ", tag_dic)
    # GPSInfo values derived above are in DMS (Degree Minutes Seconds) format
    # Reformatting the DMS values in Decimal Degree (DD) format
    print("Gps_dic", gps_dic)
    # print("Gps: ", gps_dic["GPSLatitude"][0])
    # latlong = "{0} {1} {2} {3}, {4} {5} {6} {7}".format(gps_dic["GPSLatitude"][0][0],
    #                                               gps_dic["GPSLatitude"][1][0],
    #                                               round(gps_dic["GPSLatitude"][2][0] / gps_dic["GPSLatitude"][2][1],2),
    #                                               gps_dic["GPSLatitudeRef"],
    #                                               gps_dic["GPSLongitude"][0][0],
    #                                               gps_dic["GPSLongitude"][1][0],
    #                                               round(gps_dic["GPSLongitude"][2][0] / gps_dic["GPSLongitude"][2][1],2),
    #                                               gps_dic["GPSLongitudeRef"])
    #
    # tag_dic["GPSInfo"] = latlong        # replacing gps values in DMS format with DD format in tag_dic

    print("Data has been successfully extracted")

    features = list(tag_dic.keys())                                    # creating a list of all the keys in tag_dic
    metadata = open("exif_records.csv", "a")                           # creating file object with filename as "exif_records.csv"
    record_write = csv.DictWriter(metadata, fieldnames=features)       # creating object of Dictwriter and setting column names
    record_write.writerow(tag_dic)                                     # writing the extracted metadata as a row in the file
    metadata.close()                                                   # closing file
    print("exif_records.csv file updated")


    ## creating and updating excel file

    df = pd.read_csv("exif_records.csv", names=features)              # using Pandas to create a data frame from the csv file
    df.to_excel('EXIF_records.xlsx', columns=features, index=False) # using to_excel method to update the xlsx file

    print("The metadata has been stored successfully in the Excel file(.xlsx format) successfully.")
    menu()



# # # creating a copy of the image without EXIF data
# # option - 4
def create_copy():
    '''Creates a copy of the image without metadata'''
    print(12 * "-", "Scrubbing the metadata and creating a new image file with no metadata ", 12 * "-")
    global c_image
    global c_file
    global clean_image

    image_data = list(c_image.getdata())                # returns pixel value of the image data as a sequence
    clean_image = im.new(c_image.mode, c_image.size)    # creates a new image with the given mode and size of original image
    clean_image.putdata(image_data)                     # copies pixel data to clean_image
    clean_image.save(f"clean_{c_file}")                 # saves the image with the given filename

    print(f"A clean copy of the image {c_file} without tags has been created Successfully.")
    print("Feel free to share the cleaned image over internet.")
    print("We enable anonymity.")
    print()
    menu()



# # creating a thumbnail of the image
def create_thumbnail(clean_image,c_file):
    '''creates thumbnail of the scrubbed image or the original image if not scrubbed '''

    clean_image.thumbnail((100,100))        # creates a thumbnail of the image specified
    clean_image.save(f"cleanthmb_{c_file}")
    im._show(clean_image)                   # displays the image
    print()
    menu()                                  # return to main menu

def gmap():
    # '''opens the extracted latitude ang longitude gps coordinates using google maps url '''
    # print(12 * "-", "Locating where the Image was taken", 12 * "-")
    # # global latlong
    # # print("LatLOng : ", latlong)
    #
    # # gpsco_list = latlong.split(",", 2)          # splitting the values and saving in a list
    # # gpsco_list[0] = gpsco_list[0].strip(" ")    # striping the values of space character
    # # gpsco_list[1] = gpsco_list[1].strip(" ")
    #
    # # lat = gpsco_list[0].split(" ")              # splitting the string in degrees minutes and seconds
    # # lon = gpsco_list[1].split(" ")
    #
    # # lat = list(gps_dic["GPSLatitude"])
    # # lon = list(gps_dic["GPSLongitude"])
    #
    # # print("Latitude  : ", lat)
    # # print("Longitude : ", lon)
    #
    # # building the url using values and .format
    # url = f'''https://www.google.com/maps/place/{int(gps_dic['GPSLatitude'][0])}°{int(gps_dic['GPSLatitude'][1])}'{round(float(gps_dic['GPSLatitude'][2]),2)}"{gps_dic['GPSLatitudeRef']}+{int(gps_dic["GPSLongitude"][0])}°{int(gps_dic["GPSLongitude"][1])}'{round(float(gps_dic["GPSLongitude"][2]),2)}"{gps_dic["GPSLongitudeRef"]}'''
    # print("url : ", url)
    # webbrowser.open(url)        # opens the url in default web browser
    # print()
    # menu()

    # new code for gmplot
    gpsddlat = float(gps_dic['GPSLatitude'][0]) + (float(gps_dic['GPSLatitude'][1]))/60 + float(int(gps_dic['GPSLatitude'][2]))/(60*60)
    gpsddlon = float(gps_dic['GPSLongitude'][0]) + (float(gps_dic['GPSLongitude'][1]))/60 + (float(gps_dic['GPSLongitude'][2]))/(60*60)

    if gps_dic['GPSLatitudeRef']=='N':
        gpsddlat *= -1
    if gps_dic['GPSLongitudeRef'] == 'E':
        gpsddlon *= -1

    gmap = gmplot.GoogleMapPlotter(gpsddlat, gpsddlon, 12)
    gmap.draw("/home/eshan/Desktop/1/4/2/image_meta.html")


def watermark(c_image = None, clean_image = None, c_file = None):

    '''Watermarks the uploaded image'''

    if c_image is None:
        print("You are required to upload the image before watermarking it!")
        print("Initializing Upload process..")
        import_image()
    else:
        usrinput = input(f" Original Upload detected! Do you wish to continue with {c_file}\Enter 'y' or 'n'").upper()
        if usrinput == "Y":
            pos = (10, 10)
            text = input("Enter the watermark text here : ")
            text_color = "red"
            drawing = ImageDraw.Draw(c_image)
            font = ImageFont.truetype("arial.ttf", size=100)  # ttf = True Type Format
            drawing.text(pos, text, text_color, font)
            c_image.show()
            c_image.save(f"watermarked_{c_file}")
            menu()



            # watermark_text= input("Enter the watermark text : ")
            # width, height = c_image.size
            # draw = ImageDraw.Draw(c_image)
            # font = ImageFont.truetype(font="arial.ttf", size=30)
            # textwidth, textheight = draw.textsize(watermark_text, font)
            # margin = 20
            # draw.text(font="arial.ttf", xy=(30, 30), text=watermark_text)
            # c_image.show

        else:
            print("Initialising Image upload Module.....")
            import_image()
            # result_image.save()


def send_mail():
    df = pd.read_csv(input("Enter the csv file name : "))
    names = df['Names']
    emails = df['Emails']

    # sender details this can also be taken from user using input and validate with validate_email module
    sender_id = input("Enter your email address : ")
    sender_p = input("Enter your password : ")

    # create smtp object and define the smtp server (and its port)
    smtpObj = smtplib.SMTP(host="smtp.gmail.com", port=587, local_hostname=None)

    # start tls and login with authentication credentials of the user
    smtpObj.starttls()

    smtpObj.login(sender_id, sender_p)


    for i in range(0, len(names)):
        message = MIMEMultipart("digest")  # multipart/digest is a simple way to send multiple text messages
        message["Subject"] = "Thought for today"
        message["From"] = sender_id
        message["To"] = emails[i]
        # write the plain text part
        text = """\
        Hi, """ + names[i] + '''
        Thought for today is:
        “The secret of getting ahead is getting started.”
        ~ Mark Twain'''

        # convert text to MIMEText object and add them to the MIMEMultipart message
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        smtpObj.sendmail(sender_id, emails[i], message.as_string())
        print('Successfully sent mail to ', names[i])

    # Close the endpoint
    smtpObj.quit()
    menu()









menu()
