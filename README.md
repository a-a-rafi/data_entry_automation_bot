# data_entry_automation_bot
Scrapes real estate data from the website zillow, entries the data on a pre-made google form. Made with BeautifulSoup and Selenium.


In this project, we will try to find apartments in San Francisco, CA. 
We will find apartments that fit our criteria from Zillow.
We will scrape all the information of the apartment from the website using BeautifulSoup.
We will input the data into a pre-made Google form using Selenium, 
so when the program is done running, we can export all the information into a spreadsheet.

Steps - 

1. Go to Zillow, (the link that contains all the required filters). The user can use his/her own link for this too.
2. Scrape the following for each result -
   1. Property Name
   2. Property Address
   3. Contact
   4. Url of the result
3. Save the information into a dictionary
4. Go to the google form. User should have his/her own Google form ready with three fields - 
   1. Property Name
   2. Property Address
   3. Contact
   4. Url of the result
5. Input the data into the Google form
6. Click submit
7. Loop the process for all the instances

***1. Go to Zillow, (the link that contains all the required filters). The user can use his/her own link for this too.***

Initially tried with this simple script - 
```python
import requests

zillow_url = input('Provide the link with all the filters applied - ')
response = requests.get(zillow_url, headers=header)
print(response.status_code)
```
```
403
```

A google search revealed that - 

*Error code 403 in Python is a response that indicates the web server understood the request but refused to 
fulfill it due to insufficient permissions or bot detection.*

There were a number of solutions posted in stack overflow, one of them was to add headers.
Initially added one, "User-Agent".
Didn't work.
Kept adding more parameters to the headers, until it worked.

How to find the headers?

Chrome > Go to the link provided (zillow) > Developer Tools > Network > Reload the page > Click on the search query >
The headers will be shown on a tab on the right. Pick and add to your header.

Finally, this worked - 

```python
import requests

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control':'max-age=0',
    'Cookie': 'x-amz-continuous-deployment-state=AYABeIMrI760tbJ8zfZe+vfKN0gAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADKNYdfZSlE4XkA20RwAw6blqefTep8x15B2RQujjBK5YhRHpsik%2FAe+Og0mID25Ynkxu9gMWzoxJMPM7RRPnAgAAAAAMAAQAAAAAAAAAAAAAAAAAAB0BLUH%2FUl92UkMdh+MUt8b%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwGSZUBmqUT5v56OEhVnU%2FBHSKYhKlvHx9+soKy; _pxvid=3b86aea7-712f-11ee-a663-86acf54e7ccf; zguid=24|%24cc1d3115-1630-4b55-91e6-89a2a5ee3389; _ga=GA1.2.237448302.1698015831; _gid=GA1.2.2007264666.1698015831; zjs_anonymous_id=%22cc1d3115-1630-4b55-91e6-89a2a5ee3389%22; zjs_user_id=null; zg_anonymous_id=%22a20f7254-a92d-49ea-905a-6eaec458f39a%22; _gcl_au=1.1.676136261.1698015835; __pdst=05bb7f6427a54d9caf39ba91d3d35a4a; _pin_unauth=dWlkPVl6a3dabVJoTjJNdE5qUTFNUzAwTmpjeUxUazBZV1l0TkdRNU1UZ3dZV0UxT0Rkaw; JSESSIONID=FF6BD083C6EBB1700159CECB98E1F112; zgsession=1|f3fe6410-2a60-475a-8180-40b295db9215; pxcts=1fe2a5de-7185-11ee-8269-02a76689fb30; _px3=55d687007518f7df35aa49408d8749b34d2db7da80bf47a95e60e02f874f54c3:rEcCoTlOBtnx9obb8jxjd8z2T0g/JCSj5sy751fP/2UArOkpPB/Z6q5wyqAeG9QeabhU28depHy2B+VStkARoQ==:1000:ocoDhs+Ii97XROuwTRq+47LO4VSOVWj6YwPsajCtH8InGOVFc7Ktx9YYQtpx3Bw48nNKIiuul4g2xDsNAiSR/rzJZboi/trmrj78jCf+i8Tw37+ToYoaoi1sU4/f6KBcNV+nsei/GZUjTA9dTMOLt00vbXL/7wGmN5wshEsjez/5DjK9mg15HUHA6c7f9ZUmszN6vwnMlgbYI37a8PcRlOcYrMxtKiR5faouRRjuzn8=; AWSALB=bY9ubs8tAf1P6DGlmAKgEcY0Zr1cAHh84ufNJ3rIt3h9TPZwFwHHcYluqEbwA5hXHtMkUOzTQJrNo+bo6MCeeAvsCZEaHLBwZdgxTdA0/KehLd5P1mfLweuEYVjB; AWSALBCORS=bY9ubs8tAf1P6DGlmAKgEcY0Zr1cAHh84ufNJ3rIt3h9TPZwFwHHcYluqEbwA5hXHtMkUOzTQJrNo+bo6MCeeAvsCZEaHLBwZdgxTdA0/KehLd5P1mfLweuEYVjB; search=6|1700644709286%7Crect%3D38.036427902194085%2C-122.0103553671875%2C37.51322936117928%2C-122.8563026328125%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D0%26listPriceActive%3D1%26beds%3D1-%26price%3D0-872627%26mp%3D0-3000%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%09%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; x-amz-continuous-deployment-state=AYABeG2vnbmBLOC45jfIk6n0AZEAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADJeiQ9hochur1N++TgAwnQE2QynH8RJLgm2D3moFgy4e9YGdVEOkjc+TpuySfaq4IX6EidRpKmH57lLiZzayAgAAAAAMAAQAAAAAAAAAAAAAAAAAAFhLeAk%2FZyU257ZeGx5XR+b%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxt%2FebvyWKHwlki+wt+SWxwaHxXYQdxz%2Fz4A20A; DoubleClickSession=true; _uetsid=4637bb50712f11ee8f1def356f2448d7; _uetvid=46381220712f11eeab22f1d5fc36c56c; _clck=1gxew1y|2|fg3|0|1390; _clsk=1gmv9ih|1698052804419|1|0|x.clarity.ms/collect; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

zillow_url = input('Provide the link with all the filters applied - ')
response = requests.get(zillow_url, headers=header)
print(response.status_code)
```

***2. Scrape the following for each result -***

   ***1. Property Name***

   ***2. Property Address***

   ***3. Contact***
   
   ***4. Url of the result***

It is probably a dynamically generated webpage. Which is why it only captures 09 results.

```python
prices = soup.find_all(attrs={'data-test': "property-card-price"})
print(len(prices))
for i in prices:
    print(i.getText())
```
```
9
$2,095+ 1 bd
$2,540+ 1 bd
$2,810+ 1 bd
$3,000/mo
$2,825/mo
$2,461+ 1 bd
$2,404+ 1 bd
$2,151+ 1 bd
$2,496+ 1 bd
```

```python
addresses = soup.find_all(attrs={'data-test': "property-card-addr"})
for a in addresses:
    print(a.getText())
```
```
777 Broadway | 777 Broadway, Oakland, CA
Vespr | 312 24th St, Oakland, CA
Parkmerced | 3711 19th Ave, San Francisco, CA
Tahoe Terrace Apartments, 2522 35th Ave #2530-07, Oakland, CA 94601
AVE Emeryville at Bay Street, 5684 Bay St APT 735, Emeryville, CA 94608
MacArthur Commons | 540 39th St, Oakland, CA
Eleven Fifty Clay | 1150 Clay St, Oakland, CA
Hanover Northgate | 2450 Valdez St, Oakland, CA
19th and Harrison | 1889 Harrison St, Oakland, CA
```

```python
urls = soup.find_all(attrs={'data-test': "property-card-link", 'tabindex': "0"})
cleaned_urls = []
for a in urls:
    link = a.get('href')
    if link.startswith('https'):
        cleaned_urls.append(link)
        pass
    else:
        link = f'https://www.zillow.com{link}'
        cleaned_urls.append(link)
print(cleaned_urls)
```

```
https://www.zillow.com/apartments/oakland-ca/777-broadway/BKvyNv/
https://www.zillow.com/apartments/oakland-ca/vespr/C4MNc7/
https://www.zillow.com/apartments/san-francisco-ca/parkmerced/5XjKHx/
https://www.zillow.com/apartments/oakland-ca/tahoe-terrace-apartments/9k9v5R/
https://www.zillow.com/apartments/emeryville-ca/ave-emeryville-at-bay-street/5XjVfH/
https://www.zillow.com/apartments/oakland-ca/macarthur-commons/BG4Hxg/
https://www.zillow.com/apartments/oakland-ca/eleven-fifty-clay/BMMnBZ/
https://www.zillow.com/apartments/oakland-ca/hanover-northgate/BMVS8N/
https://www.zillow.com/apartments/oakland-ca/19th-and-harrison/BPPyPZ/
```

From **geeksforgeeks.org** -

To scrape content from a static page, we use BeautifulSoup as our package for scraping, and it works flawlessly for static pages. We use requests to load page into our python script. Now, if the page we are trying to load is dynamic in nature and we request this page by requests library, it would send the JS code to be executed locally. Requests package does not execute this JS code and just gives it as the page source.

BeautifulSoup does not catch the interactions with DOM via Java Script. Let’s suppose, if you have a table that is generated by JS. BeautifulSoup will not be able to capture it, while Selenium can.

If there was just a need to scrape static websites, we would’ve used just bs4. But, for dynamically generated webpages, we use selenium.

***3. Save the information into a dictionary***
***4. Go to the google form. User should have his/her own Google form ready with three fields -*** 
   ***1. Property Name***
   ***2. Property Address***
   ***3. Contact***
   ***4. Url of the result***

Not saving the information in dictionary because do not need it anymore.

Create a separate module named form_fillup, having the class G_form

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class G_form:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=Service(ChromeDriverManager().install()))
        self.driver.get("https://forms.gle/XNYg119TM5q6QNKWA")
        self.driver.maximize_window()

    def input_price(self, price_data):
        self.price_field = self.driver.find_element(By.XPATH,
                                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.price_field.click()
        self.price_field.send_keys(price_data)

    def input_address(self, address_data):
        self.address_field = self.driver.find_element(By.XPATH,
                                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
        self.address_field.click()
        self.address_field.send_keys(address_data)

    def input_link(self, link_data):
        self.link_field = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.link_field.click()
        self.link_field.send_keys(link_data)

    def submit(self):
        self.submit_button = self.driver.find_element(By.XPATH,
                                                      '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        self.submit_button.click()

    def return_to_form(self):
        self.return_link = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        self.return_link.click()
```

***5. Input the data into the Google form***
***6. Click submit***
***7. Loop the process for all the instances***

```python
form = G_form()

for index in range(0, 9):
    form.input_price(prices[index])
    form.input_address(addresses[index])
    form.input_link(cleaned_urls[index])
    form.submit()
    form.return_to_form()
```

fin
