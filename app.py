from selenium import webdriver


def get_youtube_data(url):
    driver = webdriver.Chrome('/home/amin/Desktop/chromedriver')
    driver.get(f"{url}/about")
    data = {
        'Name':'',
        'Subscribers':'',
        'Joined-date':'',
        'Views':'',
        'Description':'',
        'Location':'',
        'Image' : ''
    }
    data['Name'] = driver.find_elements_by_class_name('ytd-channel-name')[0].text
    data['Subscribers'] = (driver.find_elements_by_id('subscriber-count').text).split(' ')[0]
    data['Joined-date'] = driver.find_element_by_xpath('//*[@id="right-column"]/yt-formatted-string[2]/span[2]').text
    data['Views'] = (driver.find_element_by_xpath('//*[@id="right-column"]/yt-formatted-string[3]').text).split(' ')[0]
    data['Description'] = (driver.find_element_by_xpath('//*[@id="description"]').text)
    data['Location'] = (driver.find_element_by_xpath('//*[@id="details-container"]/table/tbody/tr[2]/td[2]/yt-formatted-string').text).split(' ')[0]
    data['Image'] = driver.find_element_by_xpath('//*[@id="img"]').get_attribute("src")
    driver.close()
    return data

if __name__ == "__main__":
    id = input("Youtube url > ")
    print(get_youtube_data(id))
