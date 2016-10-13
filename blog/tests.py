from blog.models import PostAuthor, PostEntry
from category.models import Category
from django.test import TestCase


class PostModelsCreateTest(TestCase):

    def create_post_author(self):
        return PostAuthor.objects.create(
            name="Author",
            email="author@mail.com",
            description="I'm a Author of this Post.",
        )

    def create_post_entry(self):
        return PostEntry.objects.create(
            title="My title.",
            author=PostAuthor.objects.create(
                name="Author",
            ),
            category=Category.objects.create(
                name="Category",
            ),
            content="My content.",
            height=400,
            width=300,
            views=1,
            draft=True,
            slug="my-title.",
        )

    def test_create_post_author(self):
        self.post_author = self.create_post_author()
        self.assertTrue(isinstance(self.post_author, PostAuthor))
        self.assertEqual(self.post_author.__str__(), self.post_author.name)

    def test_create_post_entry(self):

        self.post_entry = self.create_post_entry()
        self.assertTrue(isinstance(self.post_entry, PostEntry))
        self.assertEqual(self.post_entry.__str__(), self.post_entry.title+' - '+self.post_entry.author.name)

