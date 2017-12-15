from bs4 import BeautifulSoup
import ctypes
import requests
import time

while True:
    data = requests.get('https://in.bookmyshow.com/buytickets/star-wars-the-last-jedi-hyderabad/movie-hyd-ET00066915-MT/20171216')
    
    soup = BeautifulSoup(data.text)
    
    cinemaCount = len(soup.select('#venuelist')[0].select('li.list'))
    print(cinemaCount)
    
    if (cinemaCount > 8):
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'A new cinema is available', 'New Cinema Available!', 0)
    
    time.sleep(60)
