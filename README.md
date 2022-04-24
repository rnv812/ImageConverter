# ImageConverter
## Description
__Simple app for images convertation in 3 actions__:    
1. Drop your image to dashed area
2. Select format you want image to be converted
3. Click convert button  

Results are saving in the same folder where the source image located.  
You can drop one or many images to the area per time.

## Preview
![alt tag](https://github.com/Thermazote/ImageConverter/raw/master/preview.jpg)

## Build
You can use _**pyinstaller**_ for building executable app.  
1. Install _**pyinstaller**_ with ```pip install pyinstaller``` command
2. Run command ```pyinstaller --onefile --icon=icon.ico --noconsole main.py``` from the directory where ```main.py``` located
   
After completing the process you will find executable file in ```dist``` folder.  
```Mainwindow.ui``` is neccessary dependency that provides user interface of application, thus after building don't delete this file.  

## References
Icon: <a href="https://www.flaticon.com/free-icons/color-adjustment" title="color adjustment icons">Color adjustment icons created by Hilmy Abiyyu A. - Flaticon</a>  

Libraries: 
- <a href="https://www.riverbankcomputing.com/static/Docs/PyQt5/">PyQt5</a>  
- <a href="https://pillow.readthedocs.io/en/stable/">Pillow</a>  


