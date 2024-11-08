from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# Setup Selenium WebDriver (make sure you have ChromeDriver installed)
driver = webdriver.Chrome()

# Base URL to scrape (example: images with pagination)
base_url = "https://esahubble.org/images/archive/category"
picture_type = "stars"
# other picture_type options include:
##
# cosmology, exoplanets, galaxies, jwst, nebulae, blackholes, solarsystem, starclusters
##

base_url = f"{base_url}/{picture_type}/page/"


# Directory to save images
save_dir = "hubble_images/stars"
os.makedirs(save_dir, exist_ok=True)


# Function to download images from a single page
def download_images_from_page():
    # Find all image elements with class 'image-thumb'
    images = driver.find_elements(By.CSS_SELECTOR, "img.image-thumb")

    if not images:
        print("No images found on this page.")
        return

    for img in images:
        img_src = img.get_attribute('src')

        # Download image
        response = requests.get(img_src)
        img_name = os.path.basename(img_src)
        with open(os.path.join(save_dir, img_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {img_name}")


# Loop through all pages
for page_number in range(1, 14):  # Assuming there are 36 pages
    url = base_url + str(page_number) + "/"  # Construct URL for each page
    print(f"Opening page: {url}")
    driver.get(url)
    time.sleep(5)  # Wait for the page to load, adjust time if necessary
    download_images_from_page()

# Close the browser
driver.quit()
