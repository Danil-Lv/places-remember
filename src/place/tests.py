from django.test import TestCase
from django.urls import reverse

from .models import Place
from ..user.models import User


class TestPlace(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_create_place_not_auth_user(self):
        self.client.logout()
        response = self.client.post(reverse('add_place'),
                                    data=
                                    {
                                        'title': 'Заголовок',
                                        'description': 'Описание',
                                        'location': '55.85643,37.99974'
                                    }
                                    )

        self.assertRedirects(response, '/?next=/place/add/')

    def test_create_place_auth_user(self):
        response = self.client.post(reverse('add_place'),
                                    data=
                                    {
                                        'title': 'Заголовок',
                                        'description': 'Описание',
                                        'location': '55.85643,37.99974'
                                    }
                                    )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

    def test_read_only_author(self):
        user2 = User.objects.create_user(username='user2', password='12345', email='email@bk.ru')
        place = Place.objects.create(user=user2, title='title', description='desc', location='55.85643,37.99974',
                                     slug='title-1')

        response = self.client.get(reverse('show_place', kwargs={'slug': place.slug}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

    def test_read_place(self):
        user = User.objects.get(id=1)
        place = Place.objects.create(user=user, title='title', description='desc', location='55.85643,37.99974',
                                     slug='title1')

        response = self.client.get(reverse('show_place', kwargs={'slug': place.slug}))

        self.assertEqual(response.status_code, 200)
