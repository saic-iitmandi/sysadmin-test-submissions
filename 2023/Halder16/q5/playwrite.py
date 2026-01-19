from playwright.sync_api import sync_playwright
import sys

target_url = sys.argv[1]

def crt_wbpg(stuff): #writes the response into a webpage we can see...
    f = open(r'path_to_testing_file/testing.html','w',errors='ignore')
    for i in stuff:
        f.write(i)
    f.close()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        a = context.cookies()
        context.add_cookies(a) # Probably doesnt even need the cooies but im too tired to try that now.. maybe later
        page = context.new_page()

        # Going directly to the required link as im so done
        page.goto(target_url)
        page.wait_for_load_state('domcontentloaded')

        # Fill in the login form
        page.fill('input[name=username]', '***')
        page.fill('input[name=password]', '***')

        # Click the login button
        page.click('button[type=submit]')

        # Wait for the page to load (you may need to adjust the delay)
        page.wait_for_load_state('domcontentloaded')

        page.goto(target_url)

        page.wait_for_timeout(2000)

        # Get the page content
        page_content = page.content()

        # Converting the data into an actual see-able webpage
        crt_wbpg(page_content)

        # Close the browser
        browser.close()

if __name__ == "__main__":
    main()

