from googletrans import Translator as GoogleTranslator

class Translator:
    def __init__(self, defaultLang="en"):
        self.beforeLanguage = "auto"
        self.afterLanguage = defaultLang
        self.translatorAPI = GoogleTranslator()

    # 번역 목표 언어 변경 가능하게 함
    def setLanguage(self, changeLang):
        self.afterLanguage = changeLang

    # 현재 번역 언어 상태 반환
    def getLanguage(self):
        return (self.beforeLanguage, self.afterLanguage)

    # 실제로 번역을 실행함
    def translate(self, text):
        try:
            result = self.translatorAPI.translate(text, src=self.beforeLanguage, dest=self.afterLanguage)
            if hasattr(result, "text"):
                #print(f"번역된 텍스트: {result.text} (type: {type(result.text)})")
                return result.text
            else:
                #print("result 객체에 .text 없음:", result)
                return "[번역 실패]"
        except Exception as e:
            #print(f"번역 오류 발생: {e}")
            return "[번역 실패]"