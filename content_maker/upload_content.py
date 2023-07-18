import requests

def upload_ukranian_letters():
    """
    https://talkukrainian.com/ukrainian-alphabet/
    """
    urls = ['a', 'b', 'v', 'h',  'g', 'd',  'e', 'je',  'zh', 'z',  'y', 'i',  'ji', 'j',  'k', 'l',  'm', 'n',  'o', 'p',
            'r', 's',  't', 'u',  'f', 'kh',  'ts', 'ch',  'sh', 'shch',  'mjakyj_znak', 'ju', 'ja' ]
    url_template = "https://talkukrainian.com/audio//ogg/ukrainian-alphabet/{letter}.ogg"
    urls = [url_template.format(letter=x) for x in urls]

    for i, url in enumerate(urls):
        res = requests.get(url, allow_redirects=True)
        f = str(i + 1)
        if i + 1 < 10:
            f = "0" + f
        with open(f'output/{f}.mp3', 'wb') as f:
            f.write(res.content)

upload_ukranian_letters()