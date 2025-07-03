# My Biodata program

'''
This
is
a
multiple line
comment
print(10)
print("Topu")
print("01629334432")

print("Sabbir Chowdhury \n 01629334432")
print("Sabbir chowdhury \n \t 01629334432")

print("\"Sabbir Chowdhury\"")

#Name with doble quotation

print("\"Sabbir Chowdhury\"")

#Name with single Quotation

print('\'Sabbir Topu\'')'''


#print("\"I will be a successful SQA specialist\"")
'''
print("\"I will do everything If I want to do\"")
'''
'''
print("\'Hello \n My name is Topu\'")
'''


import qrcode

# Data for the QR code
data = "https://yourwebsite.com"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # size of the QR Code (1-40), 1 is smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # about 7% error can be corrected
    box_size=10,  # size of each box in pixels
    border=4,     # thickness of the border (minimum 4 required)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image or show it
img.save("qrcode.png")
img.show()
