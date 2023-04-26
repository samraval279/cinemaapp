from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from movie.models import Movie
from movie.serializer import MovieSerializer


class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie_url = reverse('movie-list')
        self.movie_data = {
            'name': 'Mission Impossible',
            'protagonists': 'Tom Cruise',
            'poster': SimpleUploadedFile("download.jpg", b"file_content", content_type="image/png"),
            'start_date': '2023-24-27',
            'status': 'running',
            'ranking': 9
        }

    def test_create_movie(self):
        response = self.client.post(self.movie_url, self.movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)