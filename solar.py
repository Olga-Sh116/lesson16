assert "Википедия" in browser.title
time.sleep(5)
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_element(By.LINK_TEXT, "Солнечная система")

a.click()