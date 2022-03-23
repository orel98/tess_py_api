#!/usr/bin/python
from xml.dom import NotSupportedErr
from tess_py_api import Pyapi
import cv2 as cv
import numpy as np
from PIL import Image


from ctypes import *

# import pytest

pyapi = Pyapi("eng")

OCR_EXPECTED_RESULTS = """This is a lot of 12 point text to test the
ocr code and see if it works on all types
of file format.

The quick brown dog jumped over the
lazy fox. The quick brown dog jumped
over the lazy fox. The quick brown dog
jumped over the lazy fox. The quick
brown dog jumped over the lazy fox.
"""


def test_cv_v_pil_v_string_to_string():
    api = pyapi.image_to_string
    path = "test_images/testocr.png"
    assert api(path) == api(cv.imread(path)) == api(Image.open(path))


def test_cv_v_pil_v_string_to_xml():
    api = pyapi.image_to_alto_xml
    path = "test_images/testocr.png"
    assert api(path) == api(cv.imread(path)) == api(Image.open(path))


def test_image_to_string_results():
    api = pyapi.image_to_string
    path = "test_images/testocr.png"
    assert (
        api(path)
        == api(cv.imread(path))
        == api(Image.open(path))
        == OCR_EXPECTED_RESULTS
    )


def test_get_image_data():
    api = pyapi.get_image_data
    try:
        api(1)
    except NotImplementedError:
        assert True
    else:
        assert False
