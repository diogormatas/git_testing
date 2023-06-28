import pytest
import requests
from unittest.mock import patch
from deploy_script import deploy_to_environment


def test_deploy_to_environment(capsys):
    connection_string = "test_connection_string"

    with patch("requests.get") as mock_get:
        deploy_to_environment(connection_string)

        captured = capsys.readouterr()
        assert "Deploying to environment with connection string: test_connection_string" in captured.out
        assert "Hello, World from development branch -> merged to main!" in captured.out

        mock_get.assert_called_with("https://www.example.com")


def test_deploy_to_environment_failure(capsys):
    connection_string = "test_connection_string"

    with patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Error")

        deploy_to_environment(connection_string)

        captured = capsys.readouterr()
        assert "Deploying to environment with connection string: test_connection_string" in captured.out
        assert "Hello, World from development branch -> merged to main!" in captured.out
        assert "Error" in captured.out


if __name__ == "__main__":
    pytest.main()
