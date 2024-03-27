from behave import *
from Features.functions import *


@given('details for from BLR to DEL and number of travellers')
def step_impl(context):
    ##################################################################################################
    #                       Select From and To City, Passengers and Date                             #
    ##################################################################################################
    select_city_from_dropdown(context.driver, from_city_locator, 'Bangalore')
    select_city_from_dropdown(context.driver, to_city_locator, 'Delhi')
    select_date_from_calendar(context.driver, depart_calender, days_from_today=13)
    select_number_of_passengers(context.driver, passenger_adult, no_of_pax=1)
    select_number_of_passengers(context.driver, passenger_children, no_of_pax=1)
    scroll_page_height(context.driver)
    button_click_submit_details(context.driver, search_btn)


@when('we submit the details for flight booking we get the list of available flights')
def step_impl(context):
    # ----------------------- Selecting Non-Stop and Cheapest Flights ------------------------#
    select_cheapest_non_stop_flight(context.driver, non_stop_filter_locator=nonstop_flight, price_filter_locator=cheap_flight_price)


@then('book the cheapest non-stop flight and proceed to the payment page')
def step_impl(context):
    # ----------------------- Booking Page ------------------------#
    review_itinerary_and_proceed(context.driver)
    select_fare_type_and_skip_meal(context.driver, fare_type_locator=select_standard_fare_price)
    add_contact_details(context.driver, 92345678923, 'shivani@gmail.com')
    enter_adult_pax_details(context.driver, adult_firsname, 'Henry', adult_lastname, 'D', gender_dropdown, select_male)
    enter_child_pax_details(context.driver, child_firstname, 'Henrys Daughter', child_lastname, 'D', child_gender_dropdown, select_child_female, child_birthdate, '02012011')
    submit_details_js_click(context.driver, button_locator=submit_travellers_details)

    ##################################################################################################
    #                             Payment Page to Pay for booking                                    #
    ##################################################################################################
    enter_card_number(context.driver, card_number, '7834 9230 2323 2345')
    enter_card_expiry_month(context.driver, expiry_month, '//*[@id="expiryMonth"]/option[6]')
    select_card_expiry_year(context.driver, expiry_year, '2025')
    enter_card_holder_name(context.driver, card_holder_name, 'Henry D')
    enter_cvv_number(context.driver, cvv_no, "456")
    button_click_submit_details(context.driver, pay_now)


@given('details for from DEL to BLR and number of travellers')
def step_impl(context):
    ##################################################################################################
    #                       Select From and To City, Passengers and Date                             #
    ##################################################################################################
    select_city_from_dropdown(context.driver, from_city_locator, 'Delhi')
    select_city_from_dropdown(context.driver, to_city_locator, 'Bangalore')
    select_date_from_calendar(context.driver, depart_calender, days_from_today=14)
    select_number_of_passengers(context.driver, category_locator=passenger_adult, no_of_pax=2)
    select_number_of_passengers(context.driver, category_locator=passenger_children, no_of_pax=1)
    scroll_page_height(context.driver)
    button_click_submit_details(context.driver, search_btn)


@when('we submit the details for flight booking to get the list of available nonstop flight')
def step_impl(context):
    # ----------------------- Selecting Last Non-Stop ------------------------#
    select_last_non_stop_flight(context.driver, non_stop_filter_locator=nonstop_flight, last_flight_filter_locator=last_flight)


@then('book the last available non-stop flight and proceed to the payment page')
def step_impl(context):
    # ----------------------- Booking Page ------------------------#
    review_itinerary_and_proceed(context.driver)
    select_fare_type_and_skip_meal(context.driver, fare_type_locator=select_standard_fare_price)
    add_contact_details(context.driver, 92345678923, 'shivani@gmail.com')
    enter_adult_pax_details(context.driver, adult_firsname, 'Henry', adult_lastname, 'D', gender_dropdown, select_male)
    enter_adult_pax_details(context.driver, adult2_firsname, 'Casey', adult2_lastname, 'D', adult2_gender_dropdown, select_female)
    enter_child_pax_details(context.driver, child_firstname_return, 'Henrys Daughter', child_lastname_return, 'D',child_gender_dropdown_return, select_child_female_return, child_birthdate_return,'02012011')
    submit_details_js_click(context.driver, button_locator=submit_travellers_details)

    ##################################################################################################
    #                             Payment Page to Pay for booking                                    #
    ##################################################################################################
    enter_card_number(context.driver, card_number, '7834 9230 2323 2345')
    enter_card_expiry_month(context.driver, expiry_month, '//*[@id="expiryMonth"]/option[6]')
    select_card_expiry_year(context.driver, expiry_year, '2025')
    enter_card_holder_name(context.driver, card_holder_name, 'Henry D')
    enter_cvv_number(context.driver, cvv_no, "456")
    button_click_submit_details(context.driver, pay_now)
