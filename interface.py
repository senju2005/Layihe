import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver(request):
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def wait(driver):
    return WebDriverWait(driver, 10)

def test_logo_size(driver, wait):
    driver.get("https://en.wikipedia.org/wiki/NASA")
    eleLogo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.mw-wiki-logo')))
    width = eleLogo.size['width']
    height = eleLogo.size['height']
    assert 150 <= width <= 170, f"Expected width to be between 150 and 170, but got {width}"
    assert 150 <= height <= 170, f"Expected height to be between 150 and 170, but got {height}"

def test_featured_color(driver, wait):
    eleFeaturedDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.central-featured')))
    background_color = eleFeaturedDiv.value_of_css_property("background-color")
    assert "rgba(0, 0, 0, 1)" in background_color, f"Expected color rgba(0, 0, 0, 1), but got {background_color}"

def test_table(driver, wait):
    eleTable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.infobox.vcard')))
    box_sizing = eleTable.value_of_css_property("box-sizing")
    assert box_sizing == "border-box", f"Expected box-sizing to be 'border-box', but got {box_sizing}"

def test_font(driver, wait):
    eleFont = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'cite.citation.web.cs1')))
    font_family = eleFont.value_of_css_property("font-family")
    font_size = eleFont.value_of_css_property("font-size")
    assert font_family == "sans-serif", f"Expected 'sans-serif' font, but got {font_family}"
    assert font_size == "12.6px", f"Expected font-size 12.6px, but got {font_size}"
