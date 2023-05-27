from django.test import TestCase
from django.urls import reverse


class TestPlace(TestCase):

    def test_create_place(self):
        response = self.client.post(reverse('add_place'),
                                    data=
                                    {
                                        'title': 'Заголовок',
                                        'description': 'Описание',
                                        'location': '55.85643,37.99974'
                                     }
                                    )

        self.assertEqual(response.status_code, 201)
