from PIL import Image
import numpy as np

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b).upper()

def img2turtlecode(filepath="null!",filename="null!",format="png",pix=2):

    w = 0
    h = 0
    pixels = np.zeros((1,1,3))
    outputFilename = ""
    
    if(filepath == "null!"):
        with Image.open(f"{filename}.{format}") as im:
            pixels = np.array(list(im.getdata()),dtype='uint8').reshape(im.size[1],im.size[0],3)
            w = im.size[0]
            h = im.size[1]
        outputFilename = filename.split(".")[0]

    elif(filename == "null!"):
        if("\\" in filepath):
            filepath = filepath.replace("\\","/")
        with Image.open(f"{filepath}") as im:
            pixels = np.array(list(im.getdata()),dtype='uint8').reshape(im.size[1],im.size[0],3)
            w = im.size[0]
            h = im.size[1]
        outputFilename = filepath.split("/")[-1].split(".")[0]
    f = open(f"{outputFilename}.py","w")
    init = f'''import turtle 
p = turtle.Pen()
p.speed('fastest')
p.up()
p.setpos(-500,325)
p.down()
def draw_pixel(color,length):
    p.color(color)
    p.begin_fill()
    for i in range(1,5):
        p.fd({pix}*(i%2)*(length-1)+{pix})
        p.rt(90)
    p.end_fill()
'''
    f.write(init)

    for i in range(h):
        cur = np.array([-1,-1,-1])
        num = 1
        for j in range(w):
            if(np.array_equal(cur,[-1,-1,-1])):
                cur = pixels[i,j]
            if(j == w-1 or not np.array_equal(cur,pixels[i,j+1])):
                hxcol = rgb2hex(*pixels[i,j])
                f.write(f"draw_pixel(\"{hxcol}\",{num})\np.fd({pix*num})\n") 
                num = 1
                cur = np.array([-1,-1,-1])
            else:
                num += 1
        pos = w*pix
        f.write("\np.up()\n")
        f.write(f"p.rt(180)\np.fd({pos})\np.lt(90)\np.fd({pix})\np.lt(90)\n")
        f.write("p.down()\n")

    f.write("#turtle.update()\nturtle.done()")
    return f"{outputFilename}.py"

if __name__ == "__main__":
    print("Run default or Manual input?")
    print("1. Default\n2. Manual\n3.Exit")
    choice = int(input("->"))
    if(choice == 1):
        outputFilename = img2turtlecode(filename = "umbreon",format = "jpg", pix = 1)
        print(f"Program ended, your output file is {outputFilename}")
    elif(choice == 2):
        filepath = ""
        filename = ""
        format  = ""
        pix = 0
        opt = 0
        while(1):   
            filename = input("Input your image file path :")
            if("/" in filename or "\\" in filename):
                filepath = filename
                opt = 0
            else:
                format = input("Input your image format (eg. jpg, png, jpeg) :")
                opt = 1
            pix = int(input("Input how many pixels per block :"))

            if(opt):
                print(f'''\nPlease confirm the following information:
Filepath : {filepath}
Format : {format}''')
            else:
                print(f'''\nPlease confirm the following information:
Filepath : {filepath}''')
            print(f"Pixels per block : {pix}")

            confirm = input("Is the above information correct? (y/n) : ").lower()
            if( 'y' in confirm):
                break
            else:
                print("Please re-enter the information\n")
        if(opt):  
            outputFilename = img2turtlecode(filename = filename, format = format , pix = pix)
        else:
            outputFilename = img2turtlecode(filepath = filepath, pix = pix)
        print(f"Program ended, your output file is {outputFilename}")
    print("Thanks for using this program!")
    


