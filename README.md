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

## Installation
### Building executable file
You can use _**pyinstaller**_ for building executable app.  
1. Install _**pyinstaller**_ with ```pip install pyinstaller``` command
2. Run command ```pyinstaller --onefile --icon=icon.ico --noconsole main.py``` from the directory where ```main.py``` is located  

After completing the process you will find executable file in ```dist``` folder.  
```Mainwindow.ui``` is neccessary dependency that provides user interface of application, thus after building don't delete this file.  

### Using original package
If you don't need executable file and you want to run program rigth with python interpreter you have to install neccessary packages in global or local environment.
Use these commands to install neccessary packages:
- ```pip install pillow```
- ```pip install pillow-avif-plugin```
- ```pip install pyqt5```  

Note: Change extension of package from ```.py``` to ```.pyw``` for hiding console when script is running.

## References
Icon: <a href="https://www.flaticon.com/free-icons/color-adjustment" title="color adjustment icons">Color adjustment icons created by Hilmy Abiyyu A. - Flaticon</a>  

Libraries: 
- <a href="https://www.riverbankcomputing.com/static/Docs/PyQt5/">PyQt5</a>  
- <a href="https://pillow.readthedocs.io/en/stable/">Pillow</a>  


