from PIL import Image
from PIL import ImageEnhance

image_file = input("Enter the name of the Image to be manipulated: ")
p = -1
while(p == -1):
    case = input("Enter Your Choice:\n 'a': Load Image\n 'b': Resize Image\n 'c': Crop Image\n 'd': Rotate/Flip Image\n 'e': Change Mode\n 'f': Enhance Image\n 'g': Exit\n \n")
    im = Image.open(image_file)

    if case == 'a':
        im.show()

    elif case == 'b':
        choice = input("'1': Manual Resize\n'2': Lock Aspect Ratio\n\n")
        if choice == '1':
            x = input("Enter width: ")
            a = int(x)
            y = input("Enter length: ")
            b = int(y)
            resized = im.resize((a, b))
            resized.show()
            resized.save("new_image.jpg")
        elif choice == '2':
            z = input("Enter size: ")
            c = int(z)
            im.thumbnail((c, c))
            im.show()
            im.save("new_image.jpg")

    elif case == 'c':
        w = input("Enter left: ")
        a = int(w)
        x = input("Enter upper: ")
        b = int(x)
        y = input("Enter right: ")
        c = int(y)
        z = input("Enter lower: ")
        d = int(z)
        box = (a, b, c, d)
        crop = im.crop(box)
        crop.show()
        crop.save("new_image.jpg")

    elif case == 'd':
        choice = input("'1': Rotate 90\n'2': Rotate 180\n'3': Rotate 270\n'4': Flip Horizontal\n'5': Flip vertical\n'6': Transpose\n'7': Transverse\n\n")
        if choice == '1':
            image_r90 = im.transpose(Image.ROTATE_90)
            image_r90.show()
            image_r90.save("new_image.jpg")
        elif choice == '2':
            image_r180 = im.transpose(Image.FROTATE_180)
            image_r180.show()
            image_r180.save("new_image.jpg")
        elif choice == '3':
            image_r270 = im.transpose(Image.ROTATE_270)
            image_r270.show()
            image_r270.save("new_image.jpg")
        elif choice == '4':
            image_fliph = im.transpose(Image.FLIP_LEFT_RIGHT)
            image_fliph.show()
            image_fliph.save("new_image.jpg")
        elif choice == '5':
            image_flipv = im.transpose(Image.FLIP_TOP_BOTTOM)
            image_flipv.show()
            image_flipv.save("new_image.jpg")
        elif choice == '6':
            image_transp = im.transpose(Image.TRANSPOSE)
            image_transp.show()
            image_transp.save("new_image.jpg")
        elif choice == '7':
            image_transv = im.transpose(Image.TRANSVERSE)
            image_transv.show()
            image_transv.save("new_image.jpg")
            
    elif case == 'e':
        choice = input("'1': Grayscale\n'2': RGB\n'3': CMYK\n\n")
        if choice == '1':
            grayscale = im.convert("L")
            grayscale.show()
            grayscale.save("new_image.jpg")
        elif choice == '2':
            grayscale = im.convert("RGB")
            grayscale.show()
            grayscale.save("new_image.jpg")
        elif choice == '3':
            grayscale = im.convert("CMYK")
            grayscale.show()
            grayscale.save("new_image.jpg")

    elif case == 'f':
        choice = input("'1': Adjust Contrast\n'2': Adjust Color\n'3': Adjust Brightness\n'4': Adjust Sharpness\n\n")
        if choice == '1':
            x = input("Enter factor (0.0-2.0): ")
            a = int(x)
            contrast = ImageEnhance.Contrast(im)
            contrast.enhance(a).show()
            contrast.enhance(a).save("new_image.jpg")
        elif choice == '2':
            x = input("Enter factor (0.0-2.0): ")
            a = int(x)
            color = ImageEnhance.Color(im)
            color.enhance(a).show()
            color.enhance(a).save("new_image.jpg")
        elif choice == '3':
            x = input("Enter factor (0.0-2.0): ")
            a = int(x)
            brightness = ImageEnhance.Brightness(im)
            brightness.enhance(a).show()
            brightness.enhance(a).save("new_image.jpg")
        elif choice == '4':
            x = input("Enter factor (0.0-2.0): ")
            a = int(x)
            sharpness = ImageEnhance.Sharpness(im)
            sharpness.enhance(a).show()
            sharpness.enhance(a).save("new_image.jpg")

    elif case == 'g':
        p = 0