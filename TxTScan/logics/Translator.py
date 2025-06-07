from googletrans import Translator as GoogleTranslator

class Translator:
    def __init__(self, defaultTargetLang="en"):
        self.beforeLanguage = "auto"  # 자동 감지
        self.afterLanguage = defaultTargetLang  # 번역 결과 언어
        self.translatorAPI = GoogleTranslator()

    def setLanguage(self, targetLang):
        """
        번역 결과 언어 설정 (예: 'en', 'ko', 'ja', 'zh-cn')
        """
        self.afterLanguage = targetLang

    def getLanguage(self):
        return (self.beforeLanguage, self.afterLanguage)

    def translate(self, text):
        try:
            result = self.translatorAPI.translate(text, src=self.beforeLanguage, dest=self.afterLanguage)
            if hasattr(result, "text"):
                print(f"[DEBUG] 번역된 텍스트: {result.text} (type: {type(result.text)})")
                return result.text
            else:
                print("[ERROR] result 객체에 .text 없음:", result)
                return "[번역 실패]"
        except Exception as e:
            print(f"[EXCEPTION] 번역 오류 발생: {e}")
            return "[번역 실패]"