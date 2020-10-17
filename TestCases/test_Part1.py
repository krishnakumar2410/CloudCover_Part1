from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from Utilities.CustomeLogger import LogGen

#chromeBrowserPath = "C:\Data\LnD\Browsers\chromedriver.exe" #Incase of physical path for driver
url = "https://stackoverflow.com/"

def test_get_maxquestioncount_tagname():
    logger = LogGen.loggen()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome(chromeBrowserPath) #Incase of physical path for driver
    logger.info("******* Test Case Part1 started ********")
    driver.get(url)
    driver.maximize_window()
    browse_question_xpath = "//a[@class='d-inline-block fc-white p-bg-purple d:bg-blue-600 py12 px24 bar-sm js-gps-track' " \
                            "and contains(text(),'Browse questions')] "
    element = driver.find_element_by_xpath(browse_question_xpath)
    driver.execute_script("arguments[0].click();", element)
    driver.find_element_by_id("nav-tags").click()
    time.sleep(2)
    driver.find_element_by_css_selector("[title='tags in alphabetical order']").click()

    question_count = driver.find_elements_by_xpath("//div[@class='grid--cell' and contains(text(),'question')]")
    tag_name = driver.find_elements_by_xpath("//a[@class='post-tag']")
    logger.info("******* Storing the tag and questions count in list ********")
    tag_list = []
    for i in tag_name:
        tag_list.append(i.text.partition(".")[2])
    que_list = []
    for i in question_count:
        que_list.append(int(i.text.partition(" ")[0]))
    logger.info("******* Getting the max values of questions from question list ********")
    max_que_count = max(que_list)
    logger.info("******* Creating the dictionary from the two list created ********")
    tag_que = {}
    for tagname in tag_list:
        for quecount in que_list:
            tag_que[tagname] = quecount
            que_list.remove(quecount)
            break
    for key, value in tag_que.items():
        if value == max_que_count:
            print("Tag Name :", key, "-->", "QuestionCount :", max_que_count)
    driver.close()
    logger.info("******* Test Case part1 finished! ********")