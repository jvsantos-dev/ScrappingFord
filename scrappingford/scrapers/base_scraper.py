from playwright.sync_api import sync_playwright


class ScrappingWright:
    def __init__(self, open_window: bool = True):
        with sync_playwright() as p:
            if open_window:
                self.browser = p.chromium.launch(headless=False)
            else:
                self.browser = p.chromium.launch()
            self.page = self.browser.new_page()
    
    def open_page(self, url: str):
        self.page.goto(url)
    
    def get_element(self, element: str):
        found = self.page.locator(element)
        return found.text_
        
    
    def event_handler(request_event):
        response = request_event.response()
        print(request_event.url) 
        print(response.status)