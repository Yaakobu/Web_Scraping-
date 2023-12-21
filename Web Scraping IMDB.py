from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-3f724978-0 enKyEL cli-parent')

csv_filename = "movies_data1.csv"


with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    # Write the header row
    header = ['Movie_Name', 'Sl_no', 'Year_of_release', 'duration_of_the_movie', 'rating, rated_type']
    writer.writerow(header)

    for movie in movies:
          Movie_Name = movie.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title').a.text.split('.')[1]
          Sl_no = movie.find('div', class_='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title').a.text.split('.')[0]
          Year_of_release = movie.find('div', class_='sc-43986a27-7 dBkaPT cli-title-metadata').span.text
          duration_of_the_movie = movie.find('div', class_='sc-43986a27-7 dBkaPT cli-title-metadata').text
          rating= movie.find('div', class_='sc-e3e7b191-0 jlKVfJ sc-43986a27-2 bvCMEK cli-ratings-container').span.text
          rated_type = movie.find('div', class_='sc-43986a27-7 dBkaPT cli-title-metadata').span.text       

          writer.writerow([Movie_Name, Sl_no, Year_of_release, duration_of_the_movie, rating, rated_type])

print("Data has been written to the CSV file:", csv_filename)