import pytest
from tool_setup import deploy_to_environment

# comentario dummy
def test_deploy_to_environment(capsys):
    connection_string = "test_connection_string"

    deploy_to_environment(connection_string)

    captured = capsys.readouterr()
    assert "Deploying to environment with connection string: test_connection_string" in captured.out
    # assert "Hello, World from development branch -> merged to main!" in captured.out
    # Modificando a expectativa para uma frase diferente
    assert "This is an intentionally failing test" in captured.out

if __name__ == "__main__":
    pytest.main()
