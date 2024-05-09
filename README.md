# Image to Turtle Code

This project turns an image of any size into a turtle code. Where if you run the turtle code it will draw the image out pixel by pixel. It is pretty slow if the color have too much detail. It took around an hour to finish a 200x200 pixel image so I think I will improve it later.

# Dependency

This project uses Pillow and Numpy. If you didn't have these library you can run below command on your terminal to install it.

```
pip install numpy pillow
```

# Usage

Open the main.py, change the filename and its format to the specified image. And then run the main.py, it will generate a new file called "filename".py. You can run this file to see your image being draw with turtle.

Make sure the image is on the same directory with the python. Or you can change the code to have the open filepath into your image path.

You can also specify how big is each pixel, just change the "pix" variable.

# Demonstration

![Demonstration of umbreon drawn by turtle](/Assets/umbreonTurtle.png)

# Afterwords

That's it basically, I did this project just for fun and I hope it is useful for someone!
