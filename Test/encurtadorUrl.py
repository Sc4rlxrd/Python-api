import pyshorteners

# URL original #
url = "https://mangaplus.shueisha.co.jp/updates"

# Carrega lib #
s = pyshorteners.Shortener()

# Gera URL encurtada #
shortUrl = s.tinyurl.short(url)

# Mostra resultado #
print(f"URL Encurtada: {shortUrl}")
