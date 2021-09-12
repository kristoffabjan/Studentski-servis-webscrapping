from bs4 import BeautifulSoup
import requests
import time


print('Enter desired technology(str): ')
programming_language = input('>')
print('Filtering out desired jobs...')
print()

def find_jobs():
    html_text = requests.get(
        'https://www.studentski-servis.com/studenti/prosta-dela/?kljb=&page=1&isci=1&sort=&skD%5B%5D=004&skD%5B%5D=A832&skD%5B%5D=A210&skD%5B%5D=A055&skD%5B%5D=A078&skD%5B%5D=A090&skD%5B%5D=A095&hourly_rate=4.98%3B21').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('article', class_='job-item')
    my_jobs = []

    for index, job in enumerate(jobs):
        job_name = job.find('h3').text
        job_location_list = job.find('ul', class_='job-attributes').text. \
            replace(' ', '').split()
        job_location = job_location_list[0]
        job_code = job.find('span', class_='job-code mb-0').strong.text
        price_list = job.find('li', class_='job-payment')
        price_string = price_list.find('a').text.split()
        try:
            price = float(price_string[0])
        except ValueError:
            price_string = 'Po dogovoru'

        description = job.find('p', class_='description').text
        description_as_list1 = description.split()
        description_as_list = [x.lower() for x in description_as_list1 ]
        if ((programming_language in description_as_list) and price > 6.00):
            my_jobs.append(job)
            with open(f'jobs/{programming_language}_job{index}.txt', 'w') as f:
                f.write(f'{job_name}, {price}€/h v {job_location} \n')
                f.write(f'Širfra dela: {job_code}\n')
                f.write(description)
                print("Job saved")

if __name__ == '__main__':
     find_jobs()
    # time_between_scrapping = 259200
    # print(f'Another scraping will be done in {time_between_scrapping/86400} days')
    # time.sleep(time_between_scrapping)

