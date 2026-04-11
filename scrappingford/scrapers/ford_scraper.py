from playwright.sync_api import sync_playwright

class ScrappingWright:
    def __init__(self):
        ...
veiculos = []
nada2 = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ford.com.br/todos-os-veiculos/")
    
    elements = page.locator("[data-nameplate-key]")
    modelos = page.locator('h2 span.font-medium')
    textos = modelos.all_inner_texts()

    for i in textos:
        if i not in nada2:
            nada2.append(i)
        else: 
            pass
    count = elements.count()

    for i in range(count):
        value = elements.nth(i).get_attribute("data-nameplate-key")
        veiculos.append(value)
    classe = 'common-richtext fds-richtext desktop-h1-48 mobile-h1-30'
    browser.close()
for i in nada2:
    try:
        url = "https://www.ford.com.br/picapes/ranger/"

# '<span class="font-medium">Picapes</span>'
# Sol#47Marte!Rio