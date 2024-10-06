import requests
from bs4 import BeautifulSoup as bs


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content
    soup = bs(requests.get(url).content, 'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxies


test_url = "http://www.logobook.com/logo/assembly/"
raw_proxies = get_free_proxies()
proxies = []
for i in range(len(raw_proxies)):
    # printing req number
    print("Request Number : " + str(i + 1))
    raw_proxy = raw_proxies[i]
    try:
        response = requests.get(test_url, proxies={"http": raw_proxy, "https": raw_proxy})
        if response.status_code == 200:
            proxies.append(raw_proxy)
            with open("proxies.txt", "a") as f:
                f.write(raw_proxy + "\n")
            print("http:", raw_proxy, "https:", raw_proxy)
    except:
        # if the proxy Ip is pre occupied
        print("Not Available")

print(proxies)
