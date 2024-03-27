Feature: Book a Flight for Henry, his wife Casey and his daughter from BLR to DEL and vice versa
@part1
  Scenario: Verify the Booking of BLR to DEL flight for 1 Adult and 1 Child
    Given details for from BLR to DEL and number of travellers
    When we submit the details for flight booking we get the list of available flights
    Then book the cheapest non-stop flight and proceed to the payment page



@part2
  Scenario: Verify the Booking of DEL to BLR flight for 2 Adults and 1 Child
    Given details for from DEL to BLR and number of travellers
    When we submit the details for flight booking to get the list of available nonstop flight
    Then book the last available non-stop flight and proceed to the payment page