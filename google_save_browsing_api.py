
import requests


class GoogleSaveBrowsing():
    __private_API_KEY = "AIzaSyA01TyRfuGCtCjil93vczc5sfNWshjjf2E"
    __URL_Google = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=' + __private_API_KEY
    UrlToCheck = None
    response = None
    
    def CheckUrl(self, url):
        
        payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]}}
        try:
            self.response = requests.post(self.__URL_Google, json= payload)
            return self.response
        except:
            return None
    def CheckResponse(self):
        try:
            if self.response.status_code == 200:
                threats = self.response.json()
                if "matches" in threats:
                    return "Небезопасно"
                else:
                    return "Безопасно"   
        except:
            return f"Ошибка"
        
class UrlCheckerGoogle(GoogleSaveBrowsing):
    
    def UrlInfo(self,url):
        self.CheckUrl(url)
        isSaveUrl = self.CheckResponse()
        return isSaveUrl
        
            
   
if __name__ == "__main__":
    url_to_check = "http://testsafebrowsing.appspot.com/s/malware.html"
    isSave = UrlCheckerGoogle().UrlInfo(url_to_check)
    print(isSave)

