from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def select_city_from_dropdown(driver, city_element_locator, city_name):
    city_selection = driver.find_element_by_id(city_element_locator)  # fetching the locator from locators.py
    city_selection.send_keys(city_name)
    sleep(1)
    city_selection.send_keys(Keys.ENTER)
    assert city_name in city_selection.get_attribute("value")


def select_date_from_calendar(driver, calendar_locator, days_from_today):
    driver.find_element_by_id(calendar_locator).click()
    todays_date = driver.find_element_by_xpath(current_date_xpath)  # fetching the locator from locators.py
    date = int(todays_date.text)  # converting string to int to perform addition
    date_to_be_selected = date + days_from_today
    date_to_be_selected = str(date_to_be_selected)  # link text requires string and not int
    driver.find_element_by_link_text(date_to_be_selected).click()


def select_number_of_passengers(driver, category_locator, no_of_pax):
    select_dropdown = Select(driver.find_element_by_id(category_locator))
    select_dropdown.select_by_value(str(no_of_pax))
    sleep(5)


def scroll_page_height(driver):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(6)


def button_click_submit_details(driver, button_locator):
    driver.find_element_by_xpath(button_locator).click()
    sleep(6)


def select_cheapest_non_stop_flight(driver, non_stop_filter_locator, price_filter_locator):
    driver.find_element_by_xpath(non_stop_filter_locator).click()
    cheapest_flight = driver.find_element_by_xpath(price_filter_locator)
    print("Cheapest Flight: ", cheapest_flight.text)
    driver.find_element_by_xpath(book_button).click()


def select_last_non_stop_flight(driver, non_stop_filter_locator, last_flight_filter_locator):
    driver.find_element_by_xpath(non_stop_filter_locator).click()
    last_flight_details = driver.find_element_by_xpath(last_flight_filter_locator)
    last_flight_details.click()
    sleep(2)
    last_flight_details.click()
    timing_for_last_flight = driver.find_element_by_xpath(last_flight_time)
    print("Last Flight Timing: ", timing_for_last_flight.text)
    driver.find_element_by_xpath(book_button).click()


def review_itinerary_and_proceed(driver):
    sleep(5)
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        if driver.title == '#1 Site for Booking Flights, Hotels, Packages, Trains & Local activities.':
            wait = WebDriverWait(driver, 15)
            wait.until(EC.presence_of_element_located((By.XPATH, submit_button)))
            submit_btn = driver.find_element_by_xpath(submit_button)
            driver.execute_script('arguments[0].click();', submit_btn)


def select_fare_type_and_skip_meal(driver, fare_type_locator):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.XPATH, fare_type_locator)))
    driver.find_element_by_xpath(fare_type_locator).click()
    sleep(5)
    button_click_submit_details(driver, button_locator=skip_meal)


def add_contact_details(driver, contact_number, email_id):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, contact_details_number)))
    driver.find_element_by_xpath(contact_details_number).send_keys(contact_number)
    wait.until(EC.presence_of_element_located((By.XPATH, contact_details_emailid)))
    driver.find_element_by_xpath(contact_details_emailid).send_keys(email_id)
    sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, contact_submit_btn)))
    driver.find_element_by_xpath(contact_submit_btn).click()


def enter_adult_pax_details(driver, first_name_locator, first_name_value, last_name_locator, last_name_value, gender_select, gender_value):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.XPATH, first_name_locator)))
    driver.find_element_by_xpath(first_name_locator).send_keys(first_name_value)
    driver.find_element_by_xpath(last_name_locator).send_keys(last_name_value)
    sleep(2)
    driver.find_element_by_xpath(gender_select).click()
    sleep(2)
    driver.find_element_by_xpath(gender_value).click()
    sleep(2)


def enter_child_pax_details(driver, first_name_locator, first_name_value, last_name_locator, last_name_value, gender_select, gender_value, dob_locator, dob):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.XPATH, first_name_locator)))
    driver.find_element_by_xpath(first_name_locator).send_keys(first_name_value)
    driver.find_element_by_xpath(last_name_locator).send_keys(last_name_value)
    sleep(4)
    driver.find_element_by_xpath(gender_select).click()
    driver.find_element_by_xpath(gender_value).click()
    sleep(3)
    driver.find_element_by_xpath(dob_locator).send_keys(dob)


def submit_details_js_click(driver, button_locator):
    sleep(2)
    submit_travel_details = driver.find_element_by_xpath(button_locator)
    driver.execute_script('arguments[0].click();', submit_travel_details)
    sleep(5)


def enter_card_number(driver, card_number_locator, card_number_value):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, card_number_locator)))
    driver.find_element_by_xpath(card_number_locator).send_keys(card_number_value)
    sleep(3)


def enter_card_expiry_month(driver, expiry_month_element_locator, expiry_month_value_locator):
    driver.find_element_by_xpath(expiry_month_element_locator).click()
    driver.find_element_by_xpath(expiry_month_value_locator).click()
    sleep(3)


def select_card_expiry_year(driver, expiry_year_locator, value_to_select):
    card_expiry_year = Select(driver.find_element_by_css_selector(expiry_year_locator))
    card_expiry_year.select_by_visible_text(value_to_select)


def enter_card_holder_name(driver, name_locator, name_value):
    driver.find_element_by_xpath(name_locator).send_keys(name_value)


def enter_cvv_number(driver, cvv_no_locator, cvv_value):
    driver.find_element_by_css_selector(cvv_no_locator).send_keys(cvv_value)
    sleep(2)