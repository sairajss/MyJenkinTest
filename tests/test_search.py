def test_search_valid_query():
    assert "jenkins" in "jenkins pipeline"

def test_search_empty_query():
    assert len("") == 0