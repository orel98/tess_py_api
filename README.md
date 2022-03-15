# tess_py_api
### Python wrapper around [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) C language API using Python built-in ctypes module.
tess_py_api is much faster than [pytesseract](https://github.com/madmaze/pytesseract) when dealing with more than one image and lets Python developers use all of the Tesseract library functionality using the auto-generated [Python base wrapper](https://github.com/orel98/tess_py_api/TessPyWrap/CpyAPI.py).


## INSTALLATION

```console
me@home:~$ pip install tess_py_api
```
To use this module you need to have Tesseract installed.

For Windows users, Tesseract-OCR executable can be downloaded from [here](https://github.com/UB-Mannheim/tesseract/wiki) (note that you will need to add Tesseract to your path). 

For Linux users, you can compile Tesseract from source or get it via your package manager (note that you will need to add an enviroment variable called TESSDATA_PREFIX pointing to your tessdata directory).

## USAGE

```python
from tess_py_api import Pyapi

api = Pyapi("eng")

image_path = "/path/to/image"
print(api.image_to_string(image_path))
  
```

if you have OpenCV installed you can use it:
```python
import cv2 as cv
from tess_py_api import Pyapi

api = Pyapi("eng")

image = cv.imread("path/to/image")

print(api.image_to_string(image))

```

or you can use python built-in PIL/pillow:

```python

from PIL import Image
from tess_py_api import Pyapi

api = Pyapi("eng")

image = Image.open("path/to/image")

print(api.image_to_string(image)

```
Python context manager is also supported:
```python
from tess_py_api import Pyapi

with Pyapi("eng") as api:
  print(api.image_to_string("/path/to/image"))
```




