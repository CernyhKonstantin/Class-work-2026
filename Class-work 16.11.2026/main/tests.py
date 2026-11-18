from django.test import TestCase
from .models import Card, Tag
class ManyToManyTests(TestCase):
    def test_card_has_multiple_tags(self):
        card = Card.objects.create(title="Django homework")
        one = Tag.objects.create(name="Python")
        two = Tag.objects.create(name="Django")
        card.tags.add(one, two)
        self.assertEqual(card.tags.count(), 2)
        self.assertIn(card, one.cards.all())
    def test_tag_is_shared_by_cards(self):
        tag = Tag.objects.create(name="Backend")
        first = Card.objects.create(title="First")
        second = Card.objects.create(title="Second")
        first.tags.add(tag)
        second.tags.add(tag)
        self.assertEqual(tag.cards.count(), 2)
