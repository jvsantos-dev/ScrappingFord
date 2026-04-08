from playwright.sync_api import sync_playwright

veiculos = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ford.com.br/todos-os-veiculos/")
    
    elements = page.locator("[data-nameplate-key]")

    count = elements.count()

    for i in range(count):
        value = elements.nth(i).get_attribute("data-nameplate-key")
        veiculos.append(value)
        
    browser.close()
# Sol#47Marte!Rio