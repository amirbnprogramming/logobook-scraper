import random
import time

import requests
from bs4 import BeautifulSoup

from constants import user_agents, logo_collection


def load_proxies(file_path):
    with open(file_path, 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]
    return proxies


proxies = load_proxies("proxies.txt")


def get_request(url):
    retries = 10
    while retries > 0:
        try:
            # Select a random proxy and user agent
            proxy = random.choice(proxies)
            user_agent = random.choice(user_agents)

            # Create a proxies dictionary for the request
            proxy_dict = {
                'http': proxy,
                'https': proxy
            }

            # Create headers with random user agent
            headers = {
                'User-Agent': user_agent
            }

            # Send the request
            response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=5)

            # If the request is successful, return the response
            if response.status_code == 200:
                print(f"Success with proxy {proxy} and user agent {user_agent}")
                encoding = response.encoding

                # If the encoding is not UTF-8, try to correct it
                if encoding.lower() != 'utf-8':
                    print(f"Detected encoding: {encoding}. Switching to UTF-8.")
                    response.encoding = 'utf-8'
                return response

        except requests.RequestException as e:
            print(f"Request failed with proxy {proxy} and user agent {user_agent}, retrying... ({10 - retries + 1}/10)")
            retries -= 1
            time.sleep(1)  # Wait before retrying

    print("Failed after 10 retries.")


res = get_request('http://www.logobook.com/directory')
soup = BeautifulSoup(res.text, 'html.parser')
directories = soup.select('div.container:nth-child(8) a')

for link in directories:
    print(f'{directories.index(link)}th Directory:', link.get('href'))
    res = get_request(link.get('href'))
    logos_link_soup = BeautifulSoup(res.text, 'html.parser')
    target_pages = logos_link_soup.select('.logos a')
    titles = logos_link_soup.select('body > div > div.container.main.clear > section > a > h2')

    for target_page, title in zip(target_pages, titles):
        print('Page:', target_page.get('href'))
        if logo_collection.find_one({'URL': target_page.get('href')}) is None:

            temp_dict = {}
            tag_dict = {}

            final_res = get_request(target_page.get('href'))
            final_soup = BeautifulSoup(final_res.text, 'html.parser')
            content = final_soup.select_one('.single-logo-details')

            headings = content.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])
            tags = content.select('.single-tags a')

            img_url = final_soup.select_one('.single-logo img').get('src')
            url = target_page.get('href')

            for tag in tags:
                tag_dict[tag.text.strip()] = tag.get('href')

            country = headings[1].text.strip()

            temp_dict['Title'] = title.text.strip()
            temp_dict['URL'] = url
            temp_dict['Country'] = country

            for item in headings[2::2]:
                key = item.text.strip().title()
                value = headings[headings.index(item) + 1].text.strip()

                temp_dict[key] = value

            temp_dict['Img_Url'] = img_url
            temp_dict['Tags'] = tag_dict
            print(temp_dict)
            if logo_collection.find_one(
                    {'Title': temp_dict['Title'], 'URL': temp_dict['URL'], 'Img_Url': temp_dict['Img_Url']}) is None:
                logo_collection.insert_one(temp_dict)
            time.sleep(random.randint(1, 3))
        else:
            print('The Item is available.')

