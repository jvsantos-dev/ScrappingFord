from playwright.sync_api import sync_playwright
import time 
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url_principal = "https://www.honda.com.br/automoveis/"
        page.goto(url_principal)   
        selector_button = "button.location-modal__submit.location-modal__button.btn.btn-default"
        locator = page.locator(selector_button).first           
        page.wait_for_selector(selector_button, state="attached", timeout=10000)
        locator.scroll_into_view_if_needed()
        try:
            locator.click()
        except Exception:
            locator.click(force=True)
        time.sleep(5)

        selectors = [
            "h3.card--texts--title",
            "h3 .card--texts--title",
            ".card--texts--title",
            ".card--texts__title",
            "h3"
        ]

        found = False
        for sel in selectors:
            try:
                texts = page.eval_on_selector_all(sel, "nodes => nodes.map(n => n.innerText.trim())")
            except Exception:
                texts = []

            if texts:
                print(f"Selector matched: {sel} ({len(texts)} itens)")
                for t in texts:
                    print("-", t)
                found = True
                break
        
        for t in texts:
            url_carro = url_principal + f"/{t}"
            page.goto(url_carro)
            
            import pdb;pdb.set_trace()   
        if not found:
            print("Nenhum seletor encontrou elementos. Trecho do HTML para debug:")
            print(page.content()[:2000])

# <line data-name="Line" x2="9" y2="9" transform="translate(0.5 0.5)" fill="none" stroke="#3d3d3d" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.667"></line>
if __name__ == "__main__":
    main()