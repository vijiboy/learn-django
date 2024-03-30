from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class AllUrlsCheck(SimpleTestCase):
    validUrlPaths = ["/", "/about/"]
    validViewNames = ["home", "about"]
    templateViewTuples = [("home.html", "home"), ("about.html", "about")]

    def test_urlpaths_exists_at_correct_location(self):
        for urlpath in self.validUrlPaths:
            self.assertEqual(self.client.get(urlpath).status_code, 200)

    def test_urlpath_available_by_viewname(self):
        for viewName in self.validViewNames:
            self.assertEqual(self.client.get(reverse(viewName)).status_code, 200)

    def test_correct_template_used_by_view(self):
        for template, view in self.templateViewTuples:
            self.assertTemplateUsed(self.client.get(reverse(view)), template)


class HomePageTests(SimpleTestCase):
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Home Page</h1>")


class AboutPageTests(SimpleTestCase):
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")
