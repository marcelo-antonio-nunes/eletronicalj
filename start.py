import webbrowser

# webbrowser.get('chrome').open("http://127.0.0.1:5000")

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = "http://127.0.0.1:5000"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)