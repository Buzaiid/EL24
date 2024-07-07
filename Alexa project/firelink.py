import webbrowser

fb = 'https://www.facebook.com'
linkedin='https://www.linkedin.com'
youtube='https://youtube.com'
google='https://www.google.com'
spotify='https://spotify.com'


def firefox(url):
    webbrowser.get('firefox').open(url)

def links():
    return {'fb':fb,'linkedin':linkedin,'google':google}
