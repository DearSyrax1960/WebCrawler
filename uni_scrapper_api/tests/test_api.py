from rest_framework import status


class TestAccessLevel:

    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.get('')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, api_client):
        authenticate(is_staff=True)

        response = api_client.get('/university/yorku/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_user_is_not_staff_returns_403(self, authenticate, api_client):
        authenticate()

        response = api_client.get('/university/')

        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestData:
    def test_if_given_name_is_invalid_returns_400(self, authenticate, api_client):
        authenticate(is_superuser=True)
        wrong_name = 'wrongName'
        response = api_client.get(f'/university/{wrong_name}/')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
