## OCR-Streamlit-App
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![python](https://img.shields.io/badge/Python-14354C?logo=python&logoColor=white)
![numpy](https://img.shields.io/badge/Numpy-777BB4?logo=numpy&logoColor=white)
![pytorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=PyTorch&logoColor=white)
![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?&logo=streamlit&logoColor=white)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?&logo=Windows%20terminal&logoColor=white)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?&logo=visual%20studio%20code&logoColor=white)

- OCR Streamlit App is used to extract text from images using python's easyocr, pytorch and streamlit packages
- OCR app gets an image and detection language from the user using streamlit's file uploader and selectbox functions.
- If the image is not uploaded then the app will display a info message to the user.
- If the image is uploaded then the app displays the extracted text to the user.

### Installation :- 
To install all necessary requirement packages for the app 👇
```
pip install -r requirements.txt
```
Then, Run the app 👇
```
streamlit run app.py
```

### Packages Imported :- 
```python
import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np
```

### Demo GIF Image 👇:- 
![output_image](images/demo.gif)
