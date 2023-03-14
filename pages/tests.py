from django.test import TestCase, SimpleTestCase

# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


class RenderingTests(TestCase):
    def test_supreme_court_cases_status_code(self):
        response = self.client.get("/supreme_court_judgements/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_about_page_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")

    def test_supreme_court_cases_template(self):
        response = self.client.get("/supreme_court_judgements/")
        self.assertTemplateUsed(response, "judgements_list.html")
