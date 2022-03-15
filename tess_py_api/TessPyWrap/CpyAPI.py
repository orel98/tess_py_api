# DEV
if __name__ == "__main__":
    from capi_types import *
else:
    from .capi_types import *

import os
from ctypes import *


class CpyAPI:
    """This code is auto-generated from "capi.hpp" header file and its not fully tested, use at your own risk"""

    def __init__(self, tess_name: str):
        self.TESSERACT = cdll.LoadLibrary(tess_name)
        self._handle = self.TessBaseAPICreate()

    def TessVersion(self) -> c_char_p:

        self.TESSERACT.TessVersion.restype = c_char_p
        self.TESSERACT.TessVersion.argtypes = []
        return self.TESSERACT.TessVersion()

    def TessDeleteText(self, text: c_char_p) -> None:

        self.TESSERACT.TessDeleteText.restype = None
        self.TESSERACT.TessDeleteText.argtypes = [c_char_p]
        return self.TESSERACT.TessDeleteText(text)

    def TessDeleteTextArray(self, arr: c_void_p) -> None:

        self.TESSERACT.TessDeleteTextArray.restype = None
        self.TESSERACT.TessDeleteTextArray.argtypes = [c_void_p]
        return self.TESSERACT.TessDeleteTextArray(arr)

    def TessDeleteIntArray(self, arr: POINTER(c_int)) -> None:

        self.TESSERACT.TessDeleteIntArray.restype = None
        self.TESSERACT.TessDeleteIntArray.argtypes = [POINTER(c_int)]
        return self.TESSERACT.TessDeleteIntArray(arr)

    def TessTextRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessTextRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessTextRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessTextRendererCreate(outputbase)

    def TessHOcrRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessHOcrRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessHOcrRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessHOcrRendererCreate(outputbase)

    def TessHOcrRendererCreate2(
        self, outputbase: c_char_p, font_info: c_bool
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessHOcrRendererCreate2.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessHOcrRendererCreate2.argtypes = [c_char_p, c_bool]
        return self.TESSERACT.TessHOcrRendererCreate2(outputbase, font_info)

    def TessAltoRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessAltoRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessAltoRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessAltoRendererCreate(outputbase)

    def TessTsvRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessTsvRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessTsvRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessTsvRendererCreate(outputbase)

    def TessPDFRendererCreate(
        self, outputbase: c_char_p, datadir: c_char_p, textonly: c_bool
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessPDFRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessPDFRendererCreate.argtypes = [c_char_p, c_char_p, c_bool]
        return self.TESSERACT.TessPDFRendererCreate(outputbase, datadir, textonly)

    def TessUnlvRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessUnlvRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessUnlvRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessUnlvRendererCreate(outputbase)

    def TessBoxTextRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessBoxTextRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessBoxTextRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessBoxTextRendererCreate(outputbase)

    def TessLSTMBoxRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessLSTMBoxRendererCreate.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessLSTMBoxRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessLSTMBoxRendererCreate(outputbase)

    def TessWordStrBoxRendererCreate(
        self, outputbase: c_char_p
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessWordStrBoxRendererCreate.restype = POINTER(
            TessResultRenderer
        )
        self.TESSERACT.TessWordStrBoxRendererCreate.argtypes = [c_char_p]
        return self.TESSERACT.TessWordStrBoxRendererCreate(outputbase)

    def TessDeleteResultRenderer(self, renderer: POINTER(TessResultRenderer)) -> None:

        self.TESSERACT.TessDeleteResultRenderer.restype = None
        self.TESSERACT.TessDeleteResultRenderer.argtypes = [POINTER(TessResultRenderer)]
        return self.TESSERACT.TessDeleteResultRenderer(renderer)

    def TessResultRendererInsert(
        self, renderer: POINTER(TessResultRenderer), next: POINTER(TessResultRenderer)
    ) -> None:

        self.TESSERACT.TessResultRendererInsert.restype = None
        self.TESSERACT.TessResultRendererInsert.argtypes = [
            POINTER(TessResultRenderer),
            POINTER(TessResultRenderer),
        ]
        return self.TESSERACT.TessResultRendererInsert(renderer, next)

    def TessResultRendererNext(
        self, renderer: POINTER(TessResultRenderer)
    ) -> POINTER(TessResultRenderer):

        self.TESSERACT.TessResultRendererNext.restype = POINTER(TessResultRenderer)
        self.TESSERACT.TessResultRendererNext.argtypes = [POINTER(TessResultRenderer)]
        return self.TESSERACT.TessResultRendererNext(renderer)

    def TessResultRendererBeginDocument(
        self, renderer: POINTER(TessResultRenderer), title: c_char_p
    ) -> c_bool:

        self.TESSERACT.TessResultRendererBeginDocument.restype = c_bool
        self.TESSERACT.TessResultRendererBeginDocument.argtypes = [
            POINTER(TessResultRenderer),
            c_char_p,
        ]
        return self.TESSERACT.TessResultRendererBeginDocument(renderer, title)

    def TessResultRendererAddImage(
        self, renderer: POINTER(TessResultRenderer), api: POINTER(TessBaseAPI)
    ) -> c_bool:

        self.TESSERACT.TessResultRendererAddImage.restype = c_bool
        self.TESSERACT.TessResultRendererAddImage.argtypes = [
            POINTER(TessResultRenderer),
            POINTER(TessBaseAPI),
        ]
        return self.TESSERACT.TessResultRendererAddImage(renderer, api)

    def TessResultRendererEndDocument(
        self, renderer: POINTER(TessResultRenderer)
    ) -> c_bool:

        self.TESSERACT.TessResultRendererEndDocument.restype = c_bool
        self.TESSERACT.TessResultRendererEndDocument.argtypes = [
            POINTER(TessResultRenderer)
        ]
        return self.TESSERACT.TessResultRendererEndDocument(renderer)

    def TessResultRendererExtention(
        self, renderer: POINTER(TessResultRenderer)
    ) -> c_char_p:

        self.TESSERACT.TessResultRendererExtention.restype = c_char_p
        self.TESSERACT.TessResultRendererExtention.argtypes = [
            POINTER(TessResultRenderer)
        ]
        return self.TESSERACT.TessResultRendererExtention(renderer)

    def TessResultRendererTitle(
        self, renderer: POINTER(TessResultRenderer)
    ) -> c_char_p:

        self.TESSERACT.TessResultRendererTitle.restype = c_char_p
        self.TESSERACT.TessResultRendererTitle.argtypes = [POINTER(TessResultRenderer)]
        return self.TESSERACT.TessResultRendererTitle(renderer)

    def TessResultRendererImageNum(
        self, renderer: POINTER(TessResultRenderer)
    ) -> c_int:

        self.TESSERACT.TessResultRendererImageNum.restype = c_int
        self.TESSERACT.TessResultRendererImageNum.argtypes = [
            POINTER(TessResultRenderer)
        ]
        return self.TESSERACT.TessResultRendererImageNum(renderer)

    def TessBaseAPICreate(self) -> POINTER(TessBaseAPI):

        self.TESSERACT.TessBaseAPICreate.restype = POINTER(TessBaseAPI)
        self.TESSERACT.TessBaseAPICreate.argtypes = []
        return self.TESSERACT.TessBaseAPICreate()

    def TessBaseAPIDelete(self) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIDelete.restype = None
        self.TESSERACT.TessBaseAPIDelete.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIDelete(handle)

    def TessBaseAPIGetOpenCLDevice(self, device: POINTER(c_void_p)) -> c_size_t:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetOpenCLDevice.restype = c_size_t
        self.TESSERACT.TessBaseAPIGetOpenCLDevice.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(c_void_p),
        ]
        return self.TESSERACT.TessBaseAPIGetOpenCLDevice(handle, device)

    def TessBaseAPISetInputName(self, name: c_char_p) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetInputName.restype = None
        self.TESSERACT.TessBaseAPISetInputName.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPISetInputName(handle, name)

    def TessBaseAPIGetInputName(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetInputName.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetInputName.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetInputName(handle)

    def TessBaseAPISetInputImage(self, pix: POINTER(Pix)) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetInputImage.restype = None
        self.TESSERACT.TessBaseAPISetInputImage.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(Pix),
        ]
        return self.TESSERACT.TessBaseAPISetInputImage(handle, pix)

    def TessBaseAPIGetInputImage(self) -> POINTER(Pix):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetInputImage.restype = POINTER(Pix)
        self.TESSERACT.TessBaseAPIGetInputImage.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetInputImage(handle)

    def TessBaseAPIGetSourceYResolution(self) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetSourceYResolution.restype = c_int
        self.TESSERACT.TessBaseAPIGetSourceYResolution.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetSourceYResolution(handle)

    def TessBaseAPIGetDatapath(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetDatapath.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetDatapath.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetDatapath(handle)

    def TessBaseAPISetOutputName(self, name: c_char_p) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetOutputName.restype = None
        self.TESSERACT.TessBaseAPISetOutputName.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPISetOutputName(handle, name)

    def TessBaseAPISetVariable(self, name: c_char_p, value: c_char_p) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetVariable.restype = c_bool
        self.TESSERACT.TessBaseAPISetVariable.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPISetVariable(handle, name, value)

    def TessBaseAPISetDebugVariable(self, name: c_char_p, value: c_char_p) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetDebugVariable.restype = c_bool
        self.TESSERACT.TessBaseAPISetDebugVariable.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPISetDebugVariable(handle, name, value)

    def TessBaseAPIGetIntVariable(
        self, name: c_char_p, value: POINTER(c_int)
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetIntVariable.restype = c_bool
        self.TESSERACT.TessBaseAPIGetIntVariable.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            POINTER(c_int),
        ]
        return self.TESSERACT.TessBaseAPIGetIntVariable(handle, name, value)

    def TessBaseAPIGetBoolVariable(
        self, name: c_char_p, value: POINTER(c_bool)
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetBoolVariable.restype = c_bool
        self.TESSERACT.TessBaseAPIGetBoolVariable.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            POINTER(c_bool),
        ]
        return self.TESSERACT.TessBaseAPIGetBoolVariable(handle, name, value)

    def TessBaseAPIGetDoubleVariable(
        self, name: c_char_p, value: POINTER(c_double)
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetDoubleVariable.restype = c_bool
        self.TESSERACT.TessBaseAPIGetDoubleVariable.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            POINTER(c_double),
        ]
        return self.TESSERACT.TessBaseAPIGetDoubleVariable(handle, name, value)

    def TessBaseAPIGetStringVariable(self, name: c_char_p) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetStringVariable.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetStringVariable.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIGetStringVariable(handle, name)

    def TessBaseAPIPrintVariables(self, fp: c_void_p) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIPrintVariables.restype = None
        self.TESSERACT.TessBaseAPIPrintVariables.argtypes = [
            POINTER(TessBaseAPI),
            c_void_p,
        ]
        return self.TESSERACT.TessBaseAPIPrintVariables(handle, fp)

    def TessBaseAPIPrintVariablesToFile(self, filename: c_char_p) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIPrintVariablesToFile.restype = c_bool
        self.TESSERACT.TessBaseAPIPrintVariablesToFile.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIPrintVariablesToFile(handle, filename)

    def TessBaseAPIInit1(
        self,
        datapath: c_char_p,
        language: c_char_p,
        oem: TessOcrEngineMode,
        configs: c_void_p,
        configs_size: c_int,
    ) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIInit1.restype = c_int
        self.TESSERACT.TessBaseAPIInit1.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
            TessOcrEngineMode,
            c_void_p,
            c_int,
        ]
        return self.TESSERACT.TessBaseAPIInit1(
            handle, datapath, language, oem, configs, configs_size
        )

    def TessBaseAPIInit2(
        self, datapath: c_char_p, language: c_char_p, oem: TessOcrEngineMode
    ) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIInit2.restype = c_int
        self.TESSERACT.TessBaseAPIInit2.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
            TessOcrEngineMode,
        ]
        return self.TESSERACT.TessBaseAPIInit2(handle, datapath, language, oem)

    def TessBaseAPIInit3(self, datapath: c_char_p, language: c_char_p) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIInit3.restype = c_int
        self.TESSERACT.TessBaseAPIInit3.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIInit3(handle, datapath, language)

    def TessBaseAPIInit4(
        self,
        datapath: c_char_p,
        language: c_char_p,
        mode: TessOcrEngineMode,
        configs: c_void_p,
        configs_size: c_int,
        vars_vec: c_void_p,
        vars_values: c_void_p,
        vars_vec_size: c_size_t,
        set_only_non_debug_params: c_bool,
    ) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIInit4.restype = c_int
        self.TESSERACT.TessBaseAPIInit4.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
            TessOcrEngineMode,
            c_void_p,
            c_int,
            c_void_p,
            c_void_p,
            c_size_t,
            c_bool,
        ]
        return self.TESSERACT.TessBaseAPIInit4(
            handle,
            datapath,
            language,
            mode,
            configs,
            configs_size,
            vars_vec,
            vars_values,
            vars_vec_size,
            set_only_non_debug_params,
        )

    def TessBaseAPIGetInitLanguagesAsString(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetInitLanguagesAsString.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetInitLanguagesAsString.argtypes = [
            POINTER(TessBaseAPI)
        ]
        return self.TESSERACT.TessBaseAPIGetInitLanguagesAsString(handle)

    def TessBaseAPIGetLoadedLanguagesAsVector(self) -> c_void_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetLoadedLanguagesAsVector.restype = c_void_p
        self.TESSERACT.TessBaseAPIGetLoadedLanguagesAsVector.argtypes = [
            POINTER(TessBaseAPI)
        ]
        return self.TESSERACT.TessBaseAPIGetLoadedLanguagesAsVector(handle)

    def TessBaseAPIGetAvailableLanguagesAsVector(self) -> c_void_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetAvailableLanguagesAsVector.restype = c_void_p
        self.TESSERACT.TessBaseAPIGetAvailableLanguagesAsVector.argtypes = [
            POINTER(TessBaseAPI)
        ]
        return self.TESSERACT.TessBaseAPIGetAvailableLanguagesAsVector(handle)

    def TessBaseAPIInitForAnalysePage(self) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIInitForAnalysePage.restype = None
        self.TESSERACT.TessBaseAPIInitForAnalysePage.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIInitForAnalysePage(handle)

    def TessBaseAPIReadConfigFile(self, filename: c_char_p) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIReadConfigFile.restype = None
        self.TESSERACT.TessBaseAPIReadConfigFile.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIReadConfigFile(handle, filename)

    def TessBaseAPIReadDebugConfigFile(self, filename: c_char_p) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIReadDebugConfigFile.restype = None
        self.TESSERACT.TessBaseAPIReadDebugConfigFile.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIReadDebugConfigFile(handle, filename)

    def TessBaseAPISetPageSegMode(self, mode: TessPageSegMode) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetPageSegMode.restype = None
        self.TESSERACT.TessBaseAPISetPageSegMode.argtypes = [
            POINTER(TessBaseAPI),
            TessPageSegMode,
        ]
        return self.TESSERACT.TessBaseAPISetPageSegMode(handle, mode)

    def TessBaseAPIGetPageSegMode(self) -> TessPageSegMode:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetPageSegMode.restype = TessPageSegMode
        self.TESSERACT.TessBaseAPIGetPageSegMode.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetPageSegMode(handle)

    def TessBaseAPIRect(
        self,
        imagedata: c_void_p,
        bytes_per_pixel: c_int,
        bytes_per_line: c_int,
        left: c_int,
        top: c_int,
        width: c_int,
        height: c_int,
    ) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIRect.restype = c_char_p
        self.TESSERACT.TessBaseAPIRect.argtypes = [
            POINTER(TessBaseAPI),
            c_void_p,
            c_int,
            c_int,
            c_int,
            c_int,
            c_int,
            c_int,
        ]
        return self.TESSERACT.TessBaseAPIRect(
            handle, imagedata, bytes_per_pixel, bytes_per_line, left, top, width, height
        )

    def TessBaseAPIClearAdaptiveClassifier(self) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIClearAdaptiveClassifier.restype = None
        self.TESSERACT.TessBaseAPIClearAdaptiveClassifier.argtypes = [
            POINTER(TessBaseAPI)
        ]
        return self.TESSERACT.TessBaseAPIClearAdaptiveClassifier(handle)

    def TessBaseAPISetImage(
        self,
        imagedata: c_void_p,
        width: c_int,
        height: c_int,
        bytes_per_pixel: c_int,
        bytes_per_line: c_int,
    ) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetImage.restype = None
        self.TESSERACT.TessBaseAPISetImage.argtypes = [
            POINTER(TessBaseAPI),
            c_void_p,
            c_int,
            c_int,
            c_int,
            c_int,
        ]
        return self.TESSERACT.TessBaseAPISetImage(
            handle, imagedata, width, height, bytes_per_pixel, bytes_per_line
        )

    def TessBaseAPISetImage2(self, pix: POINTER(Pix)) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetImage2.restype = None
        self.TESSERACT.TessBaseAPISetImage2.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(Pix),
        ]
        return self.TESSERACT.TessBaseAPISetImage2(handle, pix)

    def TessBaseAPISetSourceResolution(self, ppi: c_int) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetSourceResolution.restype = None
        self.TESSERACT.TessBaseAPISetSourceResolution.argtypes = [
            POINTER(TessBaseAPI),
            c_int,
        ]
        return self.TESSERACT.TessBaseAPISetSourceResolution(handle, ppi)

    def TessBaseAPISetRectangle(
        self, left: c_int, top: c_int, width: c_int, height: c_int
    ) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetRectangle.restype = None
        self.TESSERACT.TessBaseAPISetRectangle.argtypes = [
            POINTER(TessBaseAPI),
            c_int,
            c_int,
            c_int,
            c_int,
        ]
        return self.TESSERACT.TessBaseAPISetRectangle(handle, left, top, width, height)

    def TessBaseAPIGetThresholdedImage(self) -> POINTER(Pix):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetThresholdedImage.restype = POINTER(Pix)
        self.TESSERACT.TessBaseAPIGetThresholdedImage.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetThresholdedImage(handle)

    def TessBaseAPIGetRegions(self, pixa: POINTER(POINTER(Pixa))) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetRegions.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetRegions.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(POINTER(Pixa)),
        ]
        return self.TESSERACT.TessBaseAPIGetRegions(handle, pixa)

    def TessBaseAPIGetTextlines(
        self, pixa: POINTER(POINTER(Pixa)), blockids: "POINTER(POINTER(c_int))"
    ) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetTextlines.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetTextlines.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(POINTER(Pixa)),
            "POINTER(POINTER(c_int))",
        ]
        return self.TESSERACT.TessBaseAPIGetTextlines(handle, pixa, blockids)

    def TessBaseAPIGetTextlines1(
        self,
        raw_image: c_bool,
        raw_padding: c_int,
        pixa: POINTER(POINTER(Pixa)),
        blockids: "POINTER(POINTER(c_int))",
        paraids: "POINTER(POINTER(c_int))",
    ) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetTextlines1.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetTextlines1.argtypes = [
            POINTER(TessBaseAPI),
            c_bool,
            c_int,
            POINTER(POINTER(Pixa)),
            "POINTER(POINTER(c_int))",
            "POINTER(POINTER(c_int))",
        ]
        return self.TESSERACT.TessBaseAPIGetTextlines1(
            handle, raw_image, raw_padding, pixa, blockids, paraids
        )

    def TessBaseAPIGetStrips(
        self, pixa: POINTER(POINTER(Pixa)), blockids: "POINTER(POINTER(c_int))"
    ) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetStrips.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetStrips.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(POINTER(Pixa)),
            "POINTER(POINTER(c_int))",
        ]
        return self.TESSERACT.TessBaseAPIGetStrips(handle, pixa, blockids)

    def TessBaseAPIGetWords(self, pixa: POINTER(POINTER(Pixa))) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetWords.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetWords.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(POINTER(Pixa)),
        ]
        return self.TESSERACT.TessBaseAPIGetWords(handle, pixa)

    def TessBaseAPIGetConnectedComponents(
        self, cc: POINTER(POINTER(Pixa))
    ) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetConnectedComponents.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetConnectedComponents.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(POINTER(Pixa)),
        ]
        return self.TESSERACT.TessBaseAPIGetConnectedComponents(handle, cc)

    def TessBaseAPIGetComponentImages(
        self,
        level: TessPageIteratorLevel,
        text_only: c_bool,
        pixa: POINTER(POINTER(Pixa)),
        blockids: "POINTER(POINTER(c_int))",
    ) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetComponentImages.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetComponentImages.argtypes = [
            POINTER(TessBaseAPI),
            TessPageIteratorLevel,
            c_bool,
            POINTER(POINTER(Pixa)),
            "POINTER(POINTER(c_int))",
        ]
        return self.TESSERACT.TessBaseAPIGetComponentImages(
            handle, level, text_only, pixa, blockids
        )

    def TessBaseAPIGetComponentImages1(
        self,
        level: TessPageIteratorLevel,
        text_only: c_bool,
        raw_image: c_bool,
        raw_padding: c_int,
        pixa: POINTER(POINTER(Pixa)),
        blockids: "POINTER(POINTER(c_int))",
        paraids: "POINTER(POINTER(c_int))",
    ) -> POINTER(Boxa):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetComponentImages1.restype = POINTER(Boxa)
        self.TESSERACT.TessBaseAPIGetComponentImages1.argtypes = [
            POINTER(TessBaseAPI),
            TessPageIteratorLevel,
            c_bool,
            c_bool,
            c_int,
            POINTER(POINTER(Pixa)),
            "POINTER(POINTER(c_int))",
            "POINTER(POINTER(c_int))",
        ]
        return self.TESSERACT.TessBaseAPIGetComponentImages1(
            handle, level, text_only, raw_image, raw_padding, pixa, blockids, paraids
        )

    def TessBaseAPIGetThresholdedImageScaleFactor(self) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetThresholdedImageScaleFactor.restype = c_int
        self.TESSERACT.TessBaseAPIGetThresholdedImageScaleFactor.argtypes = [
            POINTER(TessBaseAPI)
        ]
        return self.TESSERACT.TessBaseAPIGetThresholdedImageScaleFactor(handle)

    def TessBaseAPIAnalyseLayout(self) -> POINTER(TessPageIterator):
        handle = self._handle
        self.TESSERACT.TessBaseAPIAnalyseLayout.restype = POINTER(TessPageIterator)
        self.TESSERACT.TessBaseAPIAnalyseLayout.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIAnalyseLayout(handle)

    def TessBaseAPIRecognize(self, monitor: POINTER(ETEXT_DESC)) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIRecognize.restype = c_int
        self.TESSERACT.TessBaseAPIRecognize.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(ETEXT_DESC),
        ]
        return self.TESSERACT.TessBaseAPIRecognize(handle, monitor)

    def TessBaseAPIProcessPages(
        self,
        filename: c_char_p,
        retry_config: c_char_p,
        timeout_millisec: c_int,
        renderer: POINTER(TessResultRenderer),
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIProcessPages.restype = c_bool
        self.TESSERACT.TessBaseAPIProcessPages.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
            c_char_p,
            c_int,
            POINTER(TessResultRenderer),
        ]
        return self.TESSERACT.TessBaseAPIProcessPages(
            handle, filename, retry_config, timeout_millisec, renderer
        )

    def TessBaseAPIProcessPage(
        self,
        pix: POINTER(Pix),
        page_index: c_int,
        filename: c_char_p,
        retry_config: c_char_p,
        timeout_millisec: c_int,
        renderer: POINTER(TessResultRenderer),
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIProcessPage.restype = c_bool
        self.TESSERACT.TessBaseAPIProcessPage.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(Pix),
            c_int,
            c_char_p,
            c_char_p,
            c_int,
            POINTER(TessResultRenderer),
        ]
        return self.TESSERACT.TessBaseAPIProcessPage(
            handle, pix, page_index, filename, retry_config, timeout_millisec, renderer
        )

    def TessBaseAPIGetIterator(self) -> POINTER(TessResultIterator):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetIterator.restype = POINTER(TessResultIterator)
        self.TESSERACT.TessBaseAPIGetIterator.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetIterator(handle)

    def TessBaseAPIGetMutableIterator(self) -> POINTER(TessMutableIterator):
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetMutableIterator.restype = POINTER(
            TessMutableIterator
        )
        self.TESSERACT.TessBaseAPIGetMutableIterator.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetMutableIterator(handle)

    def TessBaseAPIGetUTF8Text(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetUTF8Text.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetUTF8Text.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetUTF8Text(handle)

    def TessBaseAPIGetHOCRText(self, page_number: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetHOCRText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetHOCRText.argtypes = [POINTER(TessBaseAPI), c_int]
        return self.TESSERACT.TessBaseAPIGetHOCRText(handle, page_number)

    def TessBaseAPIGetAltoText(self, page_number: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetAltoText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetAltoText.argtypes = [POINTER(TessBaseAPI), c_int]
        return self.TESSERACT.TessBaseAPIGetAltoText(handle, page_number)

    def TessBaseAPIGetTsvText(self, page_number: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetTsvText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetTsvText.argtypes = [POINTER(TessBaseAPI), c_int]
        return self.TESSERACT.TessBaseAPIGetTsvText(handle, page_number)

    def TessBaseAPIGetBoxText(self, page_number: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetBoxText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetBoxText.argtypes = [POINTER(TessBaseAPI), c_int]
        return self.TESSERACT.TessBaseAPIGetBoxText(handle, page_number)

    def TessBaseAPIGetLSTMBoxText(self, page_number: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetLSTMBoxText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetLSTMBoxText.argtypes = [
            POINTER(TessBaseAPI),
            c_int,
        ]
        return self.TESSERACT.TessBaseAPIGetLSTMBoxText(handle, page_number)

    def TessBaseAPIGetWordStrBoxText(self, page_number: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetWordStrBoxText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetWordStrBoxText.argtypes = [
            POINTER(TessBaseAPI),
            c_int,
        ]
        return self.TESSERACT.TessBaseAPIGetWordStrBoxText(handle, page_number)

    def TessBaseAPIGetUNLVText(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetUNLVText.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetUNLVText.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIGetUNLVText(handle)

    def TessBaseAPIMeanTextConf(self) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIMeanTextConf.restype = c_int
        self.TESSERACT.TessBaseAPIMeanTextConf.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIMeanTextConf(handle)

    def TessBaseAPIAllWordConfidences(self) -> POINTER(c_int):
        handle = self._handle
        self.TESSERACT.TessBaseAPIAllWordConfidences.restype = POINTER(c_int)
        self.TESSERACT.TessBaseAPIAllWordConfidences.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIAllWordConfidences(handle)

    def TessBaseAPIAdaptToWordStr(
        self, mode: TessPageSegMode, wordstr: c_char_p
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIAdaptToWordStr.restype = c_bool
        self.TESSERACT.TessBaseAPIAdaptToWordStr.argtypes = [
            POINTER(TessBaseAPI),
            TessPageSegMode,
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIAdaptToWordStr(handle, mode, wordstr)

    def TessBaseAPIClear(self) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIClear.restype = None
        self.TESSERACT.TessBaseAPIClear.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIClear(handle)

    def TessBaseAPIEnd(self) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIEnd.restype = None
        self.TESSERACT.TessBaseAPIEnd.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIEnd(handle)

    def TessBaseAPIIsValidWord(self, word: c_char_p) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPIIsValidWord.restype = c_int
        self.TESSERACT.TessBaseAPIIsValidWord.argtypes = [
            POINTER(TessBaseAPI),
            c_char_p,
        ]
        return self.TESSERACT.TessBaseAPIIsValidWord(handle, word)

    def TessBaseAPIGetTextDirection(
        self, out_offset: POINTER(c_int), out_slope: POINTER(c_float)
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetTextDirection.restype = c_bool
        self.TESSERACT.TessBaseAPIGetTextDirection.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(c_int),
            POINTER(c_float),
        ]
        return self.TESSERACT.TessBaseAPIGetTextDirection(handle, out_offset, out_slope)

    def TessBaseAPIGetUnichar(self, unichar_id: c_int) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessBaseAPIGetUnichar.restype = c_char_p
        self.TESSERACT.TessBaseAPIGetUnichar.argtypes = [POINTER(TessBaseAPI), c_int]
        return self.TESSERACT.TessBaseAPIGetUnichar(handle, unichar_id)

    def TessBaseAPIClearPersistentCache(self) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPIClearPersistentCache.restype = None
        self.TESSERACT.TessBaseAPIClearPersistentCache.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIClearPersistentCache(handle)

    def TessBaseAPIDetectOrientationScript(
        self,
        orient_deg: POINTER(c_int),
        orient_conf: POINTER(c_float),
        script_name: POINTER(POINTER(c_char)),
        script_conf: POINTER(c_float),
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessBaseAPIDetectOrientationScript.restype = c_bool
        self.TESSERACT.TessBaseAPIDetectOrientationScript.argtypes = [
            POINTER(TessBaseAPI),
            POINTER(c_int),
            POINTER(c_float),
            POINTER(POINTER(c_char)),
            POINTER(c_float),
        ]
        return self.TESSERACT.TessBaseAPIDetectOrientationScript(
            handle, orient_deg, orient_conf, script_name, script_conf
        )

    def TessBaseAPISetMinOrientationMargin(self, margin: c_double) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseAPISetMinOrientationMargin.restype = None
        self.TESSERACT.TessBaseAPISetMinOrientationMargin.argtypes = [
            POINTER(TessBaseAPI),
            c_double,
        ]
        return self.TESSERACT.TessBaseAPISetMinOrientationMargin(handle, margin)

    def TessBaseAPINumDawgs(self) -> c_int:
        handle = self._handle
        self.TESSERACT.TessBaseAPINumDawgs.restype = c_int
        self.TESSERACT.TessBaseAPINumDawgs.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPINumDawgs(handle)

    def TessBaseAPIOem(self) -> TessOcrEngineMode:
        handle = self._handle
        self.TESSERACT.TessBaseAPIOem.restype = TessOcrEngineMode
        self.TESSERACT.TessBaseAPIOem.argtypes = [POINTER(TessBaseAPI)]
        return self.TESSERACT.TessBaseAPIOem(handle)

    def TessBaseGetBlockTextOrientations(
        self,
        block_orientation: "POINTER(POINTER(c_int))",
        vertical_writing: POINTER(POINTER(c_bool)),
    ) -> None:
        handle = self._handle
        self.TESSERACT.TessBaseGetBlockTextOrientations.restype = None
        self.TESSERACT.TessBaseGetBlockTextOrientations.argtypes = [
            POINTER(TessBaseAPI),
            "POINTER(POINTER(c_int))",
            POINTER(POINTER(c_bool)),
        ]
        return self.TESSERACT.TessBaseGetBlockTextOrientations(
            handle, block_orientation, vertical_writing
        )

    def TessPageIteratorDelete(self) -> None:
        handle = self._handle
        self.TESSERACT.TessPageIteratorDelete.restype = None
        self.TESSERACT.TessPageIteratorDelete.argtypes = [POINTER(TessPageIterator)]
        return self.TESSERACT.TessPageIteratorDelete(handle)

    def TessPageIteratorCopy(self) -> POINTER(TessPageIterator):
        handle = self._handle
        self.TESSERACT.TessPageIteratorCopy.restype = POINTER(TessPageIterator)
        self.TESSERACT.TessPageIteratorCopy.argtypes = [POINTER(TessPageIterator)]
        return self.TESSERACT.TessPageIteratorCopy(handle)

    def TessPageIteratorBegin(self) -> None:
        handle = self._handle
        self.TESSERACT.TessPageIteratorBegin.restype = None
        self.TESSERACT.TessPageIteratorBegin.argtypes = [POINTER(TessPageIterator)]
        return self.TESSERACT.TessPageIteratorBegin(handle)

    def TessPageIteratorNext(self, level: TessPageIteratorLevel) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessPageIteratorNext.restype = c_bool
        self.TESSERACT.TessPageIteratorNext.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessPageIteratorNext(handle, level)

    def TessPageIteratorIsAtBeginningOf(self, level: TessPageIteratorLevel) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessPageIteratorIsAtBeginningOf.restype = c_bool
        self.TESSERACT.TessPageIteratorIsAtBeginningOf.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessPageIteratorIsAtBeginningOf(handle, level)

    def TessPageIteratorIsAtFinalElement(
        self, level: TessPageIteratorLevel, element: TessPageIteratorLevel
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessPageIteratorIsAtFinalElement.restype = c_bool
        self.TESSERACT.TessPageIteratorIsAtFinalElement.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessPageIteratorIsAtFinalElement(handle, level, element)

    def TessPageIteratorBoundingBox(
        self,
        level: TessPageIteratorLevel,
        left: POINTER(c_int),
        top: POINTER(c_int),
        right: POINTER(c_int),
        bottom: POINTER(c_int),
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessPageIteratorBoundingBox.restype = c_bool
        self.TESSERACT.TessPageIteratorBoundingBox.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
        ]
        return self.TESSERACT.TessPageIteratorBoundingBox(
            handle, level, left, top, right, bottom
        )

    def TessPageIteratorBlockType(self) -> TessPolyBlockType:
        handle = self._handle
        self.TESSERACT.TessPageIteratorBlockType.restype = TessPolyBlockType
        self.TESSERACT.TessPageIteratorBlockType.argtypes = [POINTER(TessPageIterator)]
        return self.TESSERACT.TessPageIteratorBlockType(handle)

    def TessPageIteratorGetBinaryImage(
        self, level: TessPageIteratorLevel
    ) -> POINTER(Pix):
        handle = self._handle
        self.TESSERACT.TessPageIteratorGetBinaryImage.restype = POINTER(Pix)
        self.TESSERACT.TessPageIteratorGetBinaryImage.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessPageIteratorGetBinaryImage(handle, level)

    def TessPageIteratorGetImage(
        self,
        level: TessPageIteratorLevel,
        padding: c_int,
        original_image: POINTER(Pix),
        left: POINTER(c_int),
        top: POINTER(c_int),
    ) -> POINTER(Pix):
        handle = self._handle
        self.TESSERACT.TessPageIteratorGetImage.restype = POINTER(Pix)
        self.TESSERACT.TessPageIteratorGetImage.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
            c_int,
            POINTER(Pix),
            POINTER(c_int),
            POINTER(c_int),
        ]
        return self.TESSERACT.TessPageIteratorGetImage(
            handle, level, padding, original_image, left, top
        )

    def TessPageIteratorBaseline(
        self,
        level: TessPageIteratorLevel,
        x1: POINTER(c_int),
        y1: POINTER(c_int),
        x2: POINTER(c_int),
        y2: POINTER(c_int),
    ) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessPageIteratorBaseline.restype = c_bool
        self.TESSERACT.TessPageIteratorBaseline.argtypes = [
            POINTER(TessPageIterator),
            TessPageIteratorLevel,
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
        ]
        return self.TESSERACT.TessPageIteratorBaseline(handle, level, x1, y1, x2, y2)

    def TessPageIteratorOrientation(
        self,
        orientation: POINTER(TessOrientation),
        writing_direction: POINTER(TessWritingDirection),
        textline_order: POINTER(TessTextlineOrder),
        deskew_angle: POINTER(c_float),
    ) -> None:
        handle = self._handle
        self.TESSERACT.TessPageIteratorOrientation.restype = None
        self.TESSERACT.TessPageIteratorOrientation.argtypes = [
            POINTER(TessPageIterator),
            POINTER(TessOrientation),
            POINTER(TessWritingDirection),
            POINTER(TessTextlineOrder),
            POINTER(c_float),
        ]
        return self.TESSERACT.TessPageIteratorOrientation(
            handle, orientation, writing_direction, textline_order, deskew_angle
        )

    def TessPageIteratorParagraphInfo(
        self,
        justification: POINTER(TessParagraphJustification),
        is_list_item: POINTER(c_bool),
        is_crown: POINTER(c_bool),
        first_line_indent: POINTER(c_int),
    ) -> None:
        handle = self._handle
        self.TESSERACT.TessPageIteratorParagraphInfo.restype = None
        self.TESSERACT.TessPageIteratorParagraphInfo.argtypes = [
            POINTER(TessPageIterator),
            POINTER(TessParagraphJustification),
            POINTER(c_bool),
            POINTER(c_bool),
            POINTER(c_int),
        ]
        return self.TESSERACT.TessPageIteratorParagraphInfo(
            handle, justification, is_list_item, is_crown, first_line_indent
        )

    def TessResultIteratorDelete(self) -> None:
        handle = self._handle
        self.TESSERACT.TessResultIteratorDelete.restype = None
        self.TESSERACT.TessResultIteratorDelete.argtypes = [POINTER(TessResultIterator)]
        return self.TESSERACT.TessResultIteratorDelete(handle)

    def TessResultIteratorCopy(self) -> POINTER(TessResultIterator):
        handle = self._handle
        self.TESSERACT.TessResultIteratorCopy.restype = POINTER(TessResultIterator)
        self.TESSERACT.TessResultIteratorCopy.argtypes = [POINTER(TessResultIterator)]
        return self.TESSERACT.TessResultIteratorCopy(handle)

    def TessResultIteratorGetPageIterator(self) -> POINTER(TessPageIterator):
        handle = self._handle
        self.TESSERACT.TessResultIteratorGetPageIterator.restype = POINTER(
            TessPageIterator
        )
        self.TESSERACT.TessResultIteratorGetPageIterator.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorGetPageIterator(handle)

    def TessResultIteratorGetPageIteratorConst(self) -> POINTER(TessPageIterator):
        handle = self._handle
        self.TESSERACT.TessResultIteratorGetPageIteratorConst.restype = POINTER(
            TessPageIterator
        )
        self.TESSERACT.TessResultIteratorGetPageIteratorConst.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorGetPageIteratorConst(handle)

    def TessResultIteratorGetChoiceIterator(self) -> POINTER(TessChoiceIterator):
        handle = self._handle
        self.TESSERACT.TessResultIteratorGetChoiceIterator.restype = POINTER(
            TessChoiceIterator
        )
        self.TESSERACT.TessResultIteratorGetChoiceIterator.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorGetChoiceIterator(handle)

    def TessResultIteratorNext(self, level: TessPageIteratorLevel) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessResultIteratorNext.restype = c_bool
        self.TESSERACT.TessResultIteratorNext.argtypes = [
            POINTER(TessResultIterator),
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessResultIteratorNext(handle, level)

    def TessResultIteratorGetUTF8Text(self, level: TessPageIteratorLevel) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessResultIteratorGetUTF8Text.restype = c_char_p
        self.TESSERACT.TessResultIteratorGetUTF8Text.argtypes = [
            POINTER(TessResultIterator),
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessResultIteratorGetUTF8Text(handle, level)

    def TessResultIteratorConfidence(self, level: TessPageIteratorLevel) -> c_float:
        handle = self._handle
        self.TESSERACT.TessResultIteratorConfidence.restype = c_float
        self.TESSERACT.TessResultIteratorConfidence.argtypes = [
            POINTER(TessResultIterator),
            TessPageIteratorLevel,
        ]
        return self.TESSERACT.TessResultIteratorConfidence(handle, level)

    def TessResultIteratorWordRecognitionLanguage(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessResultIteratorWordRecognitionLanguage.restype = c_char_p
        self.TESSERACT.TessResultIteratorWordRecognitionLanguage.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorWordRecognitionLanguage(handle)

    def TessResultIteratorWordFontAttributes(
        self,
        is_bold: POINTER(c_bool),
        is_italic: POINTER(c_bool),
        is_underlined: POINTER(c_bool),
        is_monospace: POINTER(c_bool),
        is_serif: POINTER(c_bool),
        is_smallcaps: POINTER(c_bool),
        pointsize: POINTER(c_int),
        font_id: POINTER(c_int),
    ) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessResultIteratorWordFontAttributes.restype = c_char_p
        self.TESSERACT.TessResultIteratorWordFontAttributes.argtypes = [
            POINTER(TessResultIterator),
            POINTER(c_bool),
            POINTER(c_bool),
            POINTER(c_bool),
            POINTER(c_bool),
            POINTER(c_bool),
            POINTER(c_bool),
            POINTER(c_int),
            POINTER(c_int),
        ]
        return self.TESSERACT.TessResultIteratorWordFontAttributes(
            handle,
            is_bold,
            is_italic,
            is_underlined,
            is_monospace,
            is_serif,
            is_smallcaps,
            pointsize,
            font_id,
        )

    def TessResultIteratorWordIsFromDictionary(self) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessResultIteratorWordIsFromDictionary.restype = c_bool
        self.TESSERACT.TessResultIteratorWordIsFromDictionary.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorWordIsFromDictionary(handle)

    def TessResultIteratorWordIsNumeric(self) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessResultIteratorWordIsNumeric.restype = c_bool
        self.TESSERACT.TessResultIteratorWordIsNumeric.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorWordIsNumeric(handle)

    def TessResultIteratorSymbolIsSuperscript(self) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessResultIteratorSymbolIsSuperscript.restype = c_bool
        self.TESSERACT.TessResultIteratorSymbolIsSuperscript.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorSymbolIsSuperscript(handle)

    def TessResultIteratorSymbolIsSubscript(self) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessResultIteratorSymbolIsSubscript.restype = c_bool
        self.TESSERACT.TessResultIteratorSymbolIsSubscript.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorSymbolIsSubscript(handle)

    def TessResultIteratorSymbolIsDropcap(self) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessResultIteratorSymbolIsDropcap.restype = c_bool
        self.TESSERACT.TessResultIteratorSymbolIsDropcap.argtypes = [
            POINTER(TessResultIterator)
        ]
        return self.TESSERACT.TessResultIteratorSymbolIsDropcap(handle)

    def TessChoiceIteratorDelete(self) -> None:
        handle = self._handle
        self.TESSERACT.TessChoiceIteratorDelete.restype = None
        self.TESSERACT.TessChoiceIteratorDelete.argtypes = [POINTER(TessChoiceIterator)]
        return self.TESSERACT.TessChoiceIteratorDelete(handle)

    def TessChoiceIteratorNext(self) -> c_bool:
        handle = self._handle
        self.TESSERACT.TessChoiceIteratorNext.restype = c_bool
        self.TESSERACT.TessChoiceIteratorNext.argtypes = [POINTER(TessChoiceIterator)]
        return self.TESSERACT.TessChoiceIteratorNext(handle)

    def TessChoiceIteratorGetUTF8Text(self) -> c_char_p:
        handle = self._handle
        self.TESSERACT.TessChoiceIteratorGetUTF8Text.restype = c_char_p
        self.TESSERACT.TessChoiceIteratorGetUTF8Text.argtypes = [
            POINTER(TessChoiceIterator)
        ]
        return self.TESSERACT.TessChoiceIteratorGetUTF8Text(handle)

    def TessChoiceIteratorConfidence(self) -> c_float:
        handle = self._handle
        self.TESSERACT.TessChoiceIteratorConfidence.restype = c_float
        self.TESSERACT.TessChoiceIteratorConfidence.argtypes = [
            POINTER(TessChoiceIterator)
        ]
        return self.TESSERACT.TessChoiceIteratorConfidence(handle)

    def TessMonitorCreate(self) -> POINTER(ETEXT_DESC):

        self.TESSERACT.TessMonitorCreate.restype = POINTER(ETEXT_DESC)
        self.TESSERACT.TessMonitorCreate.argtypes = []
        return self.TESSERACT.TessMonitorCreate()

    def TessMonitorDelete(self, monitor: POINTER(ETEXT_DESC)) -> None:

        self.TESSERACT.TessMonitorDelete.restype = None
        self.TESSERACT.TessMonitorDelete.argtypes = [POINTER(ETEXT_DESC)]
        return self.TESSERACT.TessMonitorDelete(monitor)

    def TessMonitorSetCancelFunc(
        self, monitor: POINTER(ETEXT_DESC), cancelFunc: TessCancelFunc
    ) -> None:

        self.TESSERACT.TessMonitorSetCancelFunc.restype = None
        self.TESSERACT.TessMonitorSetCancelFunc.argtypes = [
            POINTER(ETEXT_DESC),
            TessCancelFunc,
        ]
        return self.TESSERACT.TessMonitorSetCancelFunc(monitor, cancelFunc)

    def TessMonitorSetCancelThis(
        self, monitor: POINTER(ETEXT_DESC), cancelThis: c_void_p
    ) -> None:

        self.TESSERACT.TessMonitorSetCancelThis.restype = None
        self.TESSERACT.TessMonitorSetCancelThis.argtypes = [
            POINTER(ETEXT_DESC),
            c_void_p,
        ]
        return self.TESSERACT.TessMonitorSetCancelThis(monitor, cancelThis)

    def TessMonitorGetCancelThis(self, monitor: POINTER(ETEXT_DESC)) -> c_void_p:

        self.TESSERACT.TessMonitorGetCancelThis.restype = c_void_p
        self.TESSERACT.TessMonitorGetCancelThis.argtypes = [POINTER(ETEXT_DESC)]
        return self.TESSERACT.TessMonitorGetCancelThis(monitor)

    def TessMonitorSetProgressFunc(
        self, monitor: POINTER(ETEXT_DESC), progressFunc: TessProgressFunc
    ) -> None:

        self.TESSERACT.TessMonitorSetProgressFunc.restype = None
        self.TESSERACT.TessMonitorSetProgressFunc.argtypes = [
            POINTER(ETEXT_DESC),
            TessProgressFunc,
        ]
        return self.TESSERACT.TessMonitorSetProgressFunc(monitor, progressFunc)

    def TessMonitorGetProgress(self, monitor: POINTER(ETEXT_DESC)) -> c_int:

        self.TESSERACT.TessMonitorGetProgress.restype = c_int
        self.TESSERACT.TessMonitorGetProgress.argtypes = [POINTER(ETEXT_DESC)]
        return self.TESSERACT.TessMonitorGetProgress(monitor)

    def TessMonitorSetDeadlineMSecs(
        self, monitor: POINTER(ETEXT_DESC), deadline: c_int
    ) -> None:

        self.TESSERACT.TessMonitorSetDeadlineMSecs.restype = None
        self.TESSERACT.TessMonitorSetDeadlineMSecs.argtypes = [
            POINTER(ETEXT_DESC),
            c_int,
        ]
        return self.TESSERACT.TessMonitorSetDeadlineMSecs(monitor, deadline)
