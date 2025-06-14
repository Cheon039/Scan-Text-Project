<package.bat 구성요소>
PyQt5 : pip install PyQt5
pytesseract : pip install pytesseract
opencv-python : pip install opencv-python
transformers : pip install transformers
torch : pip install torch
scikit-learn : pip install scikit-learn
langdetect : pip install langdetect
pymupdf : pip install pymupdf
googletrans==4.0.0rc1 : pip install googletrans==4.0.0rc1
httpcore : pip install httpcore==0.9.1
httpx : pip install httpx==0.13.3

<exe>
Tesseract-OCR.exe


0. package 설치 방법 : 
 - TxTScan 폴더 내부 (main.py 있는 곳)에 package.bat 설치
 - tesseract-ocr-w64-setup-5.5.0.20241111.exe 설치 (기본 경로 권장)
 - googletrans와 httpcore, httpx 버전이 맞아야 합니다.
 - 
 - 개발환경 : VSCode

 ⚠ 첫 실행 시 AI 모델 설치 과정이 있어 시간이 걸릴 수 있습니다.

1. 로그인 창 좌측 하단, SignUp

2. 메인메뉴 :
 2-1 : 문서/이미지 업로드 :
  2-1-1. 파일 선택 후 파일 업로드 후, 요약/번역 버튼 클릭

 2-2 : 텍스트 직접 입력
   2-2-1. 텍스트 입력 후, 요약/번역 버튼 클릭
   2-2-2. 초기화 버튼 클릭으로 텍스트 삭제 가능

 2-3 : 최신 결과 보기
  - 마지막으로 업로드 한 결과를 확인할 수 있다.
  - 복사 및 저장이 가능하다.

 2-4 : 결과 저장 목록
  - 저장된 결과를 확인할 수 있다.
  - 저장된 결과 선택 후, 삭제 버튼 클릭 시 저장한 결과를 삭제할 수 있다.

 2-5 : 로그아웃 (우측 상단)