# PyTessy2 - Enhancements to Pytessy

This module is based off of 'pytessy' by [hyperrixel](https://github.com/hyperrixel). The original module is excellent for faster OCR, and is much faster than pytesseract, the mainstream package for tesseract in python. However the original version lacked some of the usability features of pytesseract. Specifically, this features the ability to configure page segmentation and OCR engine mode. This allows all the functionality of 'pytesseract', the speed of 'pytessy', as well as more flexibility than other similar style wrappers like 'tesserocr', since you can easily use your own version of tesseract and/or .traineddata models. This is also compatible with both openCV and PIL (examples in repo [here](https://github.com/raghavm243512/pytessy/blob/master/example.py))

## Why and when is it so fast?

PyTessy(2) uses direct library-level access to Tesseract-OCR's core library. Therefore it is fast when the image is already in the memory or when the image need to be processed before scanning with Tesseract-OCR. In case of reading and scanning existing files, the gain in speed is still there, although less noticeable Tesseract-OCR Python wrappers.

## Requirements

### Operating system

PyTessy(2) is operating system independent if you set the exact location of your Tesseract-OCR library since presently library search process is implemented on Windows only. For windows users, library and model search will work only if you installed at the default directory. It should work on tesseract 4.0, and it has been tested on v5 alpha successfully.

### Python modules

PyTessy(2) uses only modules from the Standard Library only. Python version must be ` >= 3.6 `.

### External requirements

You have to have installed or portable version of Tesseract-OCR (at least a working library and ` tessdata `).

You can download Tesseract-OCR from [here](https://tesseract-ocr.github.io/tessdoc/Downloads).

NOTE: At the time of writing, the .traineddata files which come with the v5 alpha installation did not work. However, replacing the .traineddata files with the ones from [here](https://github.com/tesseract-ocr/tessdata) worked.

## Installation

pip installation coming soon, for now the pytessy.py file will work by just downloading and importing it.
