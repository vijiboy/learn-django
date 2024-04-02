from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class AllUrlsCheck(TestCase):
    validUrlPaths = ["/"]
    validViewNames = ["home"]
    templateViewTuples = [("home.html", "home")]

    def test_urlpaths_exists_at_correct_location(self):
        for urlpath in self.validUrlPaths:
            self.assertEqual(self.client.get(urlpath).status_code, 200)

    def test_urlpath_available_by_viewname(self):
        for viewName in self.validViewNames:
            self.assertEqual(self.client.get(reverse(viewName)).status_code, 200)

    def test_correct_template_used_by_view(self):
        for template, view in self.templateViewTuples:
            self.assertTemplateUsed(self.client.get(reverse(view)), template)


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text="This is a Test")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a Test")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a Test")
