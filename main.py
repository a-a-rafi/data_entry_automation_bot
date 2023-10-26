import requests
from bs4 import BeautifulSoup
from form_fillup import G_form

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'x-amz-continuous-deployment-state=AYABeIMrI760tbJ8zfZe+vfKN0gAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADKNYdfZSlE4XkA20RwAw6blqefTep8x15B2RQujjBK5YhRHpsik%2FAe+Og0mID25Ynkxu9gMWzoxJMPM7RRPnAgAAAAAMAAQAAAAAAAAAAAAAAAAAAB0BLUH%2FUl92UkMdh+MUt8b%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwGSZUBmqUT5v56OEhVnU%2FBHSKYhKlvHx9+soKy; _pxvid=3b86aea7-712f-11ee-a663-86acf54e7ccf; zguid=24|%24cc1d3115-1630-4b55-91e6-89a2a5ee3389; _ga=GA1.2.237448302.1698015831; _gid=GA1.2.2007264666.1698015831; zjs_anonymous_id=%22cc1d3115-1630-4b55-91e6-89a2a5ee3389%22; zjs_user_id=null; zg_anonymous_id=%22a20f7254-a92d-49ea-905a-6eaec458f39a%22; _gcl_au=1.1.676136261.1698015835; __pdst=05bb7f6427a54d9caf39ba91d3d35a4a; _pin_unauth=dWlkPVl6a3dabVJoTjJNdE5qUTFNUzAwTmpjeUxUazBZV1l0TkdRNU1UZ3dZV0UxT0Rkaw; JSESSIONID=FF6BD083C6EBB1700159CECB98E1F112; zgsession=1|f3fe6410-2a60-475a-8180-40b295db9215; pxcts=1fe2a5de-7185-11ee-8269-02a76689fb30; _px3=55d687007518f7df35aa49408d8749b34d2db7da80bf47a95e60e02f874f54c3:rEcCoTlOBtnx9obb8jxjd8z2T0g/JCSj5sy751fP/2UArOkpPB/Z6q5wyqAeG9QeabhU28depHy2B+VStkARoQ==:1000:ocoDhs+Ii97XROuwTRq+47LO4VSOVWj6YwPsajCtH8InGOVFc7Ktx9YYQtpx3Bw48nNKIiuul4g2xDsNAiSR/rzJZboi/trmrj78jCf+i8Tw37+ToYoaoi1sU4/f6KBcNV+nsei/GZUjTA9dTMOLt00vbXL/7wGmN5wshEsjez/5DjK9mg15HUHA6c7f9ZUmszN6vwnMlgbYI37a8PcRlOcYrMxtKiR5faouRRjuzn8=; AWSALB=bY9ubs8tAf1P6DGlmAKgEcY0Zr1cAHh84ufNJ3rIt3h9TPZwFwHHcYluqEbwA5hXHtMkUOzTQJrNo+bo6MCeeAvsCZEaHLBwZdgxTdA0/KehLd5P1mfLweuEYVjB; AWSALBCORS=bY9ubs8tAf1P6DGlmAKgEcY0Zr1cAHh84ufNJ3rIt3h9TPZwFwHHcYluqEbwA5hXHtMkUOzTQJrNo+bo6MCeeAvsCZEaHLBwZdgxTdA0/KehLd5P1mfLweuEYVjB; search=6|1700644709286%7Crect%3D38.036427902194085%2C-122.0103553671875%2C37.51322936117928%2C-122.8563026328125%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D0%26listPriceActive%3D1%26beds%3D1-%26price%3D0-872627%26mp%3D0-3000%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%09%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; x-amz-continuous-deployment-state=AYABeG2vnbmBLOC45jfIk6n0AZEAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADJeiQ9hochur1N++TgAwnQE2QynH8RJLgm2D3moFgy4e9YGdVEOkjc+TpuySfaq4IX6EidRpKmH57lLiZzayAgAAAAAMAAQAAAAAAAAAAAAAAAAAAFhLeAk%2FZyU257ZeGx5XR+b%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxt%2FebvyWKHwlki+wt+SWxwaHxXYQdxz%2Fz4A20A; DoubleClickSession=true; _uetsid=4637bb50712f11ee8f1def356f2448d7; _uetvid=46381220712f11eeab22f1d5fc36c56c; _clck=1gxew1y|2|fg3|0|1390; _clsk=1gmv9ih|1698052804419|1|0|x.clarity.ms/collect; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

zillow_url = input('Provide the link with all the filters applied - ')
response = requests.get(zillow_url, headers=header)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)
# good_soup = soup.prettify()
# print(good_soup)
# soup = BeautifulSoup(good_soup, 'html.parser')
# print(soup.css.select('span[data-test="property-card-price"]'))
prices = soup.find_all(attrs={'data-test': "property-card-price"})
print(len(prices))
# for i in prices:
#     print(i.getText())

addresses = soup.find_all(attrs={'data-test': "property-card-addr"})
# for a in addresses:
#     print(a.getText())

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


form = G_form()

for index in range(0, 9):
    form.input_price(prices[index])
    form.input_address(addresses[index])
    form.input_link(cleaned_urls[index])
    form.submit()
    form.return_to_form()

