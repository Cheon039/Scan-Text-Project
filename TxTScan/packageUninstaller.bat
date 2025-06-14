@echo off
echo ===============================
echo  package uninstall start
echo ===============================

pip uninstall -y PyQt5 pytesseract opencv-python googletrans transformers torch scikit-learn langdetect pymupdf httpcore httpx

echo ===============================
echo  package uninstall complete
echo ===============================
pause