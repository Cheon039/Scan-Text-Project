PyQt5
pytesseract
opencv-python
googletrans==4.0.0rc1
transformers
torch

1. LoginView → SignUpView → Authentication → main.py → MainMenuView
2. InputTextView → TextProcessor → Summarizer + Translator → ResultView
3. UploadView → OCRProcessor → TextProcessor (재사용)
4. ResultManager → SaveResultView

TXTScan/
├── main.py
├── views/
│   ├── LoginView.py
│   ├── SignUpView.py
│   ├── MainMenuView.py
│   ├── InputTextView.py
│   ├── UploadView.py
│   ├── ResultView.py
│   └── SaveResultView.py
├── logic/
│   ├── Authentication.py
│   ├── OCRProcessor.py
│   ├── Summarizer.py
│   ├── Translator.py
│   ├── TextProcessor.py
│   └── ResultManager.py
├── assets/
│   └── example_img.png
├── user_data/
│   └── user_credential.json
└── requirements.txt

1단계 – 인증과 화면 전환의 뼈대
① views/LoginView.py	로그인 화면 구성 -> # 위치 이동 필요 (중심으로)
② views/SignUpView.py	계정 등록 화면 (로컬 저장용)	
③ logic/Authentication.py	ID/PW 저장 및 검증 로직	
④ main.py	여러 화면 전환을 제어하는 중앙 허브	
⑤ views/MainMenuView.py	텍스트 입력, 업로드, 결과 보기 진입 메뉴

2단계 – 텍스트 입력 → 요약/번역 → 결과 출력
⑥ views/InputTextView.py	텍스트 입력창 UI + 처리 버튼	
⑦ logic/TextProcessor.py	텍스트 받아 Summarizer + Translator 호출	
⑧ logic/Summarizer.py	텍스트 요약 기능 (dummy or transformers)	
⑨ logic/Translator.py	번역 기능 (googletrans 사용)	
⑩ views/ResultView.py	결과 텍스트를 보여주는 화면

3단계 – 업로드 + OCR 연동
⑪ views/UploadView.py	이미지 업로드 UI	
⑫ logic/OCRProcessor.py	이미지에서 텍스트 추출 (pytesseract)	
⑬ (재사용) TextProcessor → Summarizer, Translator	앞에서 만든 것과 흐름 공유

4단계 – 결과 저장 / 저장 목록 보기
⑭ logic/ResultManager.py	결과 저장 (JSON or 메모리)	
⑮ views/SaveResultView.py	저장된 결과 목록 + 상세보기 UI	
⑯ assets/	테스트 이미지나 아이콘 리소스 등	
⑰ user_data/	계정 정보 및 결과 저장 파일 위치	