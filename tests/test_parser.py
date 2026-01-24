from src.parser import get_status_code_from_response

def test_get_status_code_from_response(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    assert get_status_code_from_response(mock_response) == 200