import os
from ctypes import *


if os.name == "posix":
    TESSLIB_NAME = "libtesseract.so"
    TESSDATA_PREFIX = str(os.getenv("TESSDATA_PREFIX")).encode()
elif os.name == "nt":

    def find_tess_path():
        _path = os.get_exec_path()
        for p in _path:
            if p.lower().endswith("tesseract-ocr"):
                return p

    if not (TESS_PATH := find_tess_path()):
        print("tesseract_not_found..")
        exit(-1)

    TESSLIB_NAME = TESS_PATH + "\libtesseract-5.dll"
    TESSDATA_PREFIX = (TESS_PATH + r"\tessdata").encode()
else:
    print(f"{os.name} not supported..")
    exit(-1)


from .TessPyWrap.CpyAPI import CpyAPI
from .TessPyWrap import capi_types


_cv = False
try:
    import cv2 as cv
    import numpy as np

    _cv = True
except ModuleNotFoundError as e:
    from .dummy_class import dummy

    np, cv = dummy(), dummy()

_PIL = False
try:
    from PIL import Image
    from PIL.ImageFile import ImageFile

    _PIL = True
except:
    from .dummy_class import dummy

    Image, ImageFile = dummy(), dummy()


class Pyapi(object):

    # to prevent double multiple calls to "TessBaseAPIDelete"
    __del = False

    _TESSLIB_NAME = TESSLIB_NAME
    _TESSDATA_PREFIX = TESSDATA_PREFIX

    def __init__(self, lang=None) -> None:
        self.c_api = CpyAPI(self._TESSLIB_NAME)

        self.c_api.TessBaseAPIInit3(self._TESSDATA_PREFIX, lang.encode())

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.__del__()

    def __del__(self):
        if not self.__del:
            self.c_api.TessBaseAPIDelete()
            self.__del = True

    def tess_version(self) -> str:
        return self.c_api.TessVersion().decode()

    @staticmethod
    def get_image_data(img: str | np.ndarray | ImageFile):
        img_type = type(img)
        if img_type == np.ndarray:

            # image bytes per pixel
            # rgba = 4 [r, g, b, a], rgb/bgr = 3 [r, g, b], grayscale = 1 [0..255 per pixel]
            depth = 1 if len(img.shape) < 3 else img.shape[2]
            return (
                img.ctypes.data_as(c_void_p),
                img.shape[1],
                img.shape[0],
                depth,
                depth * img.shape[1],
            )

        if issubclass(img_type, ImageFile) or issubclass(img_type, Image.Image):
            buffer = create_string_buffer(img.tobytes())
            bytes_per_pixel = len(img.getbands())
            bys = img.tobytes()
            return (
                cast(buffer, c_void_p),
                img.width,
                img.height,
                bytes_per_pixel,
                bytes_per_pixel * img.width,
            )

        # RECORSION
        # load the image to opencv(numpy ndarray) if installed
        # else load as PIL image if installed
        # else return None

        if img_type == str:
            if _cv:
                return Pyapi.get_image_data(cv.imread(img))
            elif _PIL:
                return Pyapi.get_image_data(Image.open(img))
            else:
                return

        raise NotImplementedError(f"type '{img_type.__name__}' not supported..")

    def image_to_string(self, img: np.ndarray | str | ImageFile) -> str | None:
        if data := self.get_image_data(img):
            self.c_api.TessBaseAPISetImage(*data)
            res = self.c_api.TessBaseAPIGetUTF8Text()
            return res.decode()

        else:
            self.c_api.TessBaseAPIProcessPages(img.encode(), None, 0, None)
            res = self.c_api.TessBaseAPIGetUTF8Text()
            return res.decode()
        print("No image data")

    def get_languages(self) -> list[str]:
        res = self.c_api.TessBaseAPIGetAvailableLanguagesAsVector()
        p_c_p = cast(res, POINTER(c_char_p))

        languages = []
        i = 0
        while p_c_p[i]:
            languages.append(p_c_p[i].decode())
            i += 1
        return languages

    def image_to_alto_xml(
        self, img: np.ndarray | str | ImageFile, page_number=1
    ) -> str | None:

        if data := self.get_image_data(img):
            self.c_api.TessBaseAPISetImage(*data)
            return self.c_api.TessBaseAPIGetAltoText(page_number)
        else:
            self.c_api.TessBaseAPIProcessPages(img.encode(), None, 0, None)
            return self.c_api.TessBaseAPIGetAltoText(page_number)
