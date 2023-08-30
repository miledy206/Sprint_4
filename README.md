# Scooter for several days

#### The project was created for studying of Python auto test.
#### This project covers UI tests for site https://qa-scooter.praktikum-services.ru/
#### There was used the pytest lib and selenium WebDriver lib for creating and running auto-tests and allure for results

### List of pages are covered by test (not fully):
* **order of scooter** - 2 block of test sets for ordering of scooter
* **questions on the main page** - questions about rent

#### The following tests were created to cover the UI functionality

### List of tests (tests folder):
* **test_order_page** - this class is for the ordering of scooter
  * **test_success_order_of_scooter** - this method checks a success order with 2 sets of test data, including steps with clicking on the site logo and the Ya logo 
* **test_question_block** - this class is for the questions on the main page
  * **test_answer_on_question** - this method find the question one-by-one and check an answer on each on the main page


*the test coverage is not 100%, only some main functionality*