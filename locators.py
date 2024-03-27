# ------------------------- Locators for Search Flights Page -------------------------#
from_city_locator = "FromTag"
to_city_locator = "ToTag"
depart_calender = "DepartDate"
current_date_xpath = "//a[@class='ui-state-default ui-state-highlight ui-state-active ']"
passenger_adult = "Adults"
passenger_children = "Childrens"
search_btn = '//*[@id="SearchBtn"]'

# ------------------------- Flight Details Page -------------------------#
nonstop_flight = "//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/aside[1]/div[4]/div[2]/div[2]/div[1]/label[1]/div[1]/span[1]"
cheap_flight_price = "//*[@id='root']/div/main/div/div/div[2]/div[2]/div[8]/div[1]/div[1]/div[2]/div[3]/div[2]/p"
price_filter_option = "fs-inherit c-inherit mr-1 fw-500"
book_button = '//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[8]/div[1]/div[1]/div[2]/div[4]/button'
last_flight = "//span[contains(text(),'Departure')]"
last_flight_time = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[2]/div[8]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/p[1]"

# ------------------------- Booking Page -------------------------#
submit_button = '//*[@id="root"]/div/div[2]/div/div[1]/main/div[2]/div/div/div[20]/div[1]/button'
select_standard_fare_price = '/html/body/div[3]/div/div/div[5]/div[1]/div/div[3]/button'
skip_meal = "//button[contains(text(),'Skip this step')]"
contact_details_number = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[8]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"
contact_details_emailid = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[8]/div[1]/div[1]/div[3]/div[1]/div[1]/input[1]"
contact_submit_btn = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[8]/div[1]/div[1]/div[7]/button[1]"

# ----------------------- Add Travel Details ------------------------#
adult_firsname = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/input[1]"
adult_lastname = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/input[1]"
select_male = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]"
gender_dropdown = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/button[1]"
gender_dropdown_return = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/button[1]"

adult2_firsname = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]"
adult2_lastname = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/input[1]"
adult2_gender_dropdown = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[1]/button[1]"
select_female = "//li[contains(text(),'Female')]"

child_firstname = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]"
child_lastname = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/input[1]"
child_gender_dropdown = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[1]/button[1]"
select_child_female = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[2]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]"
child_birthdate = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/input[1]"

child_firstname_return = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/input[1]"
child_lastname_return = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/input[1]"
child_gender_dropdown_return = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[4]/div[2]/div[3]/div[1]/div[1]/button[1]"
child_birthdate_return = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[11]/div[1]/div[1]/div[4]/div[4]/div[1]/div[1]/input[1]"
select_child_female_return = "//div[@class='bg-white br-4 elevation-5 p-1 p-absolute mt-1 z-50 l-0']/ul/li[2]"
submit_travellers_details = "//button[contains(text(),'Continue to payment')]"



# ------------------------- Payment Page -------------------------#

card_number = '//*[@id="cardNumber"]'
expiry_month = "//select[@id='expiryMonth']"
expiry_year = "#expiryYear"
card_holder_name = "//input[@id='name']"
cvv_no = "#cvv"
policy = "div.App.flex.flex-column.cleartripWL main.flex-1:nth-child(2) div.container div.row:nth-child(2) div.col-18 div.row.flex-middle:nth-child(4) div.col-14 label.checkbox.w-100p div.flex.flex-start.p-relative.flex-middle > span.checkbox__mark.bs-border.bc-neutral-500.bw-1.ba"
pay_now = "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[1]/main[1]/div[4]/div[3]/div[1]/div[3]/button[1]"