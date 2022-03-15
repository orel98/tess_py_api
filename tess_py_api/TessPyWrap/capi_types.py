from enum import Enum
from ctypes import Structure


class TessBaseAPI(Structure):
    ...


class TessResultRenderer(Structure):
    ...


class TessPageSegMode(Enum):
    PSM_OSD_ONLY = 0
    PSM_AUTO_OSD = 1
    PSM_AUTO_ONLY = 2
    PSM_AUTO = 3
    PSM_SINGLE_COLUMN = 4
    PSM_SINGLE_BLOCK_VERT_TEXT = 5
    PSM_SINGLE_BLOCK = 6
    PSM_SINGLE_LINE = 7
    PSM_SINGLE_WORD = 8
    PSM_CIRCLE_WORD = 9
    PSM_SINGLE_CHAR = 10
    PSM_SPARSE_TEXT = 11
    PSM_SPARSE_TEXT_OSD = 12
    PSM_RAW_LINE = 13
    PSM_COUNT = 14

    # ctyps 'Structure' like..
    def from_param(self):
        return self.value


class TessPageIterator(Structure):
    ...


class TessPageIteratorLevel(Structure):
    ...


class TessResultIterator(Structure):
    ...


class TessChoiceIterator(Structure):
    ...


class TessMutableIterator(Structure):
    ...


class TessOcrEngineMode(Enum):
    OEM_TESSERACT_ONLY = 0
    OEM_LSTM_ONLY = 1
    OEM_TESSERACT_LSTM_COMBINED = 2
    OEM_DEFAULT = 3

    def from_param(self):
        return self.value


class ETEXT_DESC(Structure):
    ...


class Boxa(Structure):
    ...


class TessWritingDirection(Structure):
    ...


class TessOrientation(Structure):
    ...


class TessTextlineOrder(Structure):
    ...


class TessParagraphJustification(Structure):
    ...


class TessCancelFunc(Structure):
    ...


class TessProgressFunc(Structure):
    ...


class TessPolyBlockType(Structure):
    ...


class Pix(Structure):
    ...


class Pixa(Structure):
    ...
