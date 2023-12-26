import requests
import json
import logging
from faker import Faker
import allure
import pytest
import os

fake = Faker()

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.step("Logging step")
def log_step(message):
    logger.info(message)

@allure.step("Assert step")
def log_assert(condition, message):
    assert condition, message

@allure.step("Report Request")
def report_request(response):
    allure.attach("Request URL", response.request.url, allure.attachment_type.TEXT)
    allure.attach("Request Method", response.request.method, allure.attachment_type.TEXT)
    allure.attach("Request Headers", json.dumps(dict(response.request.headers)), allure.attachment_type.JSON)
    allure.attach("Request Body", json.dumps(response.request.body), allure.attachment_type.JSON)
    allure.attach("Response Status Code", str(response.status_code), allure.attachment_type.TEXT)
    allure.attach("Response Headers", json.dumps(dict(response.headers)), allure.attachment_type.JSON)
    allure.attach("Response Body", json.dumps(response.json(), indent=2), allure.attachment_type.JSON)

@allure.step("Report Fake Data")
def report_fake_data(data):
    allure.attach("Fake Data", json.dumps(data, indent=2), allure.attachment_type.JSON)

@allure.epic("JSON Server Tests")
@allure.feature("User Tests")
class TestJsonServer:

    @allure.story("Test Users")
    def test_get_users(self):
        log_step("Getting Users")
        response = requests.get("http://localhost:3000/users")
        log_assert(response.status_code == 200, "Request was successful")
        report_request(response)
        users = response.json()
        report_fake_data(users)
        log_assert(len(users) > 0, "At least one user should be returned")

    @allure.story("Test Posts")
    def test_get_posts(self):
        log_step("Getting Posts")
        response = requests.get("http://localhost:3000/posts")
        log_assert(response.status_code == 200, "Request was successful")
        report_request(response)
        posts = response.json()
        report_fake_data(posts)
        log_assert(len(posts) > 0, "At least one post should be returned")

    @allure.story("Test Comments")
    def test_get_comments(self):
        log_step("Getting Comments")
        response = requests.get("http://localhost:3000/comments")
        log_assert(response.status_code == 200, "Request was successful")
        report_request(response)
        comments = response.json()
        report_fake_data(comments)
        log_assert(len(comments) > 0, "At least one comment should be returned")

    @allure.story("Test Products")
    def test_get_products(self):
        log_step("Getting Products")
        response = requests.get("http://localhost:3000/products")
        log_assert(response.status_code == 200, "Request was successful")
        report_request(response)
        products = response.json()
        report_fake_data(products)
        log_assert(len(products) > 0, "At least one product should be returned")

    @allure.story("Test Orders")
    def test_get_orders(self):
        log_step("Getting Orders")
        response = requests.get("http://localhost:3000/orders")
        log_assert(response.status_code == 200, "Request was successful")
        report_request(response)
        orders = response.json()
        report_fake_data(orders)
        log_assert(len(orders) > 0, "At least one order should be returned")

    @allure.story("Test Orders")
    def test_additional_1(self):
        log_step("Additional Test 1")
        fake_name = fake.name()
        log_assert(len(fake_name) > 0, "Fake name should not be empty")
        allure.attach("Fake Name", fake_name, allure.attachment_type.TEXT)

    @allure.story("Test Additional 2")
    def test_additional_2(self):
        log_step("Additional Test 2")
        fake_email = fake.email()
        log_assert(len(fake_email) > 0, "Fake email should not be empty")
        allure.attach("Fake Email", fake_email, allure.attachment_type.TEXT)

    @allure.story("Test Additional 3")
    def test_additional_3(self):
        log_step("Additional Test 3")
        fake_address = fake.address()
        log_assert(len(fake_address) > 0, "Fake address should not be empty")
        allure.attach("Fake Address", fake_address, allure.attachment_type.TEXT)

    @allure.story("Test Additional 4")
    def test_additional_4(self):
        log_step("Additional Test 4")
        fake_text = fake.text()
        log_assert(len(fake_text) > 0, "Fake text should not be empty")
        allure.attach("Fake Text", fake_text, allure.attachment_type.TEXT)

    @allure.story("Test Additional 5")
    def test_additional_5(self):
        log_step("Additional Test 5")
        fake_number = fake.random_number()
        log_assert(isinstance(fake_number, int), "Fake number should be an integer")
        allure.attach("Fake Number", str(fake_number), allure.attachment_type.TEXT)

    @allure.story("Test Additional 6")
    def test_additional_6(self):
        log_step("Additional Test 6")
        fake_sentence = fake.sentence()
        log_assert(len(fake_sentence) > 0, "Fake sentence should not be empty")
        allure.attach("Fake Sentence", fake_sentence, allure.attachment_type.TEXT)

    @allure.story("Test Additional 7")
    def test_additional_7(self):
        log_step("Additional Test 7")
        fake_url = fake.url()
        log_assert(len(fake_url) > 0, "Fake URL should not be empty")
        allure.attach("Fake URL", fake_url, allure.attachment_type.TEXT)

    @allure.story("Test Additional 8")
    def test_additional_8(self):
        log_step("Additional Test 8")
        fake_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
        log_assert(isinstance(fake_date, str), "Fake date should be a string")
        allure.attach("Fake Date of Birth", fake_date, allure.attachment_type.TEXT)

    @allure.story("Test Additional 9")
    def test_additional_9(self):
        log_step("Additional Test 9")
        fake_country = fake.country()
        log_assert(len(fake_country) > 0, "Fake country should not be empty")
        allure.attach("Fake Country", fake_country, allure.attachment_type.TEXT)

    @allure.story("Test Additional 10")
    def test_additional_10(self):
        log_step("Additional Test 10")
        fake_color = fake.color_name()
        log_assert(len(fake_color) > 0, "Fake color should not be empty")
        allure.attach("Fake Color", fake_color, allure.attachment_type.TEXT)


if __name__ == "__main__":
    pytest.main(["-s", "-v", "--alluredir=./allure-results"])
    os.system("allure serve ./allure-results")
