import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_db"]
logo_collection = db["your_collection"]

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/18.18363",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4085.122 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
]

replacements = {
    'Ã¡': 'á',  # a with acute (á)
    'Ã©': 'é',  # e with acute (é)
    'Ã­': 'í',  # i with acute (í)
    'Ã³': 'ó',  # o with acute (ó)
    'Ãº': 'ú',  # u with acute (ú)
    'Ã±': 'ñ',  # n with tilde (ñ)
    'Ã¼': 'ü',  # u with diaeresis (ü)
    'Ã€': 'À',  # A with grave (À)
    'Ã': 'Á',  # A with acute (Á)
    'Ã‚': 'Â',  # A with circumflex (Â)
    'Ã„': 'Ä',  # A with diaeresis (Ä)
    'Ã†': 'Æ',  # AE ligature (Æ)
    'Ã‡': 'Ç',  # C with cedilla (Ç)
    'Ãˆ': 'È',  # E with grave (È)
    'Ã‰': 'É',  # E with acute (É)
    'ÃŠ': 'Ê',  # E with circumflex (Ê)
    'Ã‹': 'Ë',  # E with diaeresis (Ë)
    'ÃŒ': 'Ì',  # I with grave (Ì)
    'Ã': 'Í',  # I with acute (Í)
    'ÃŽ': 'Î',  # I with circumflex (Î)
    'Ã': 'Ï',  # I with diaeresis (Ï)
    'Ã’': 'Ò',  # O with grave (Ò)
    'Ã“': 'Ó',  # O with acute (Ó)
    'Ã”': 'Ô',  # O with circumflex (Ô)
    'Ã–': 'Ö',  # O with diaeresis (Ö)
    'Ã™': 'Ù',  # U with grave (Ù)
    'Ãš': 'Ú',  # U with acute (Ú)
    'Ã›': 'Û',  # U with circumflex (Û)
    'Ãœ': 'Ü',  # U with diaeresis (Ü)
    'ÃŸ': 'ß',  # sharp s (ß)
    'Ã¡': 'á',  # a with acute (á)
    'â‚¬': '€',  # euro symbol (â‚¬)
    'Ã¢': 'â',  # a with circumflex (â)
    'Ã£': 'ã',  # a with tilde (ã)
    'Ã¤': 'ä',  # a with diaeresis (ä)
    'Ã¥': 'å',  # a with ring above (å)
    'Ã¦': 'æ',  # ae ligature (æ)
    'Ã§': 'ç',  # c with cedilla (ç)
    'Ã¨': 'è',  # e with grave (è)
    'Ãª': 'ê',  # e with circumflex (ê)
    'Ã«': 'ë',  # e with diaeresis (ë)
    'Ã¬': 'ì',  # i with grave (ì)
    'Ã®': 'î',  # i with circumflex (î)
    'Ã¯': 'ï',  # i with diaeresis (ï)
    'Ã°': 'ð',  # eth (ð)
    'Ã±': 'ñ',  # n with tilde (ñ)
    'Ã²': 'ò',  # o with grave (ò)
    'Ã´': 'ô',  # o with circumflex (ô)
    'Ãµ': 'õ',  # o with tilde (õ)
    'Ã¶': 'ö',  # o with diaeresis (ö)
    'Ã¸': 'ø',  # o with stroke (ø)
    'Ã¹': 'ù',  # u with grave (ù)
    'Ã»': 'û',  # u with circumflex (û)
    'Ã½': 'ý',  # y with acute (ý)
    'Ã¾': 'þ',  # thorn (þ)
    'Ã¿': 'ÿ',  # y with diaeresis (ÿ)
    'â€™': '’',  # right single quote (’)
    'â€œ': '“',  # left double quote (“)
    'â€�': '”',  # right double quote (”)
    'â€“': '–',  # en dash (–)
    'â€”': '—',  # em dash (—)
    'â€¦': '…',  # ellipsis (…)
    'â€˜': '‘',  # left single quote (‘)
}
