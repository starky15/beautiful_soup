# fetch_site_data.py

"""
We are attempting to fetch some data from the html file
"""
from bs4 import BeautifulSoup

#Read the html file content
with open('home.html', 'r', encoding='utf-8') as fh:
    content = fh.read()

soup = BeautifulSoup(content, 'lxml')
# used to make site data more easy to read
# print(soup.prettify())

#find fetches single data, whatever it finds first
# course_headers = soup.find('h5')
#find_all fetches single data, whatever it finds first
# course_headers = soup.find_all('h5')
# print(course_headers)
#now we have all the header in the list
# print(course_headers)

# for headings in course_headers:
#     print(headings.text)

# Now we will try to fetch the prices
# for this we need to fetch div with class card
# once we have that, we will fetch data from inside

div_data = soup.find_all('div', class_ = "card")
#Since we have all the data, if in case we wish the
# course detail and price, we can fetch it via
for data in div_data:
    course_name = data.h5.text
    course_price = data.a.text.split()[-1]

    print("Course name is {} and it's price is {}".format(course_name, course_price))
# course_heading = div_data.h5
