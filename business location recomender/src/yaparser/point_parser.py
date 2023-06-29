from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import LINKS
from soup_parser import SoupContentParser


class Parser:

    def __init__(self, driver):
        self.driver = driver
        self.soup_parser = SoupContentParser()

    def parse_city(self, city):
        # todo
        pass

    def points_from_link(self, map_link: str):
        self.driver.maximize_window()
        self.driver.get(map_link)
        sleep(3)
        if self.open_all_slidebar_view():
            scroll_list = self.driver.find_element(By.CLASS_NAME, "search-list-view__list")
            li_elements = scroll_list.find_elements(By.CLASS_NAME, "search-snippet-view")
            points = [BeautifulSoup(point.get_attribute('innerHTML'), features="html.parser")
                      for point in li_elements]
            return self.soup_parser.get_info(points)

    def open_all_slidebar_view(self):
        scroll_list = self.driver.find_element(By.CLASS_NAME, "search-list-view__list")
        li_elements = scroll_list.find_elements(By.CLASS_NAME, "search-snippet-view")
        while True:
            li_elements[-1].location_once_scrolled_into_view
            li_elements = scroll_list.find_elements(By.CLASS_NAME, "search-snippet-view")
            li_size_now = len(li_elements)
            sleep(1.5)
            list_size = len(
                list(BeautifulSoup(scroll_list.get_attribute('innerHTML'), features="html.parser").children))
            if list_size == li_size_now:
                return True


if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    parser = Parser(driver)
    for link in LINKS:
        info = parser.points_from_link(link)
        pd.DataFrame(info).to_csv(link.split("/")[7] + ".csv", index=False)
    driver.close()
