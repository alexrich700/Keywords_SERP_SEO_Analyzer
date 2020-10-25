from selenium.webdriver.common.keys import Keys

def googleSearch(driver, searchQuery):
    # Open Google
    driver.get("https://google.com")

    # Preform a search
    search = driver.find_element_by_name("q")
    search.send_keys(searchQuery)
    search.send_keys(Keys.RETURN)