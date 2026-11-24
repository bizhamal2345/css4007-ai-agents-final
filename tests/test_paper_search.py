import pytest
import requests

from unittest.mock import Mock, patch

from src.paper_search import (
    reconstruct_abstract,
    parse_paper,
    search_papers
)


SAMPLE_PAPER = {
    "id": "https://openalex.org/W123",
    "title": "Sample mathematics research",
    "publication_year": 2024,
    "doi": "https://doi.org/10.0000/test",
    "cited_by_count": 10,
    "authorships": [
        {
            "author": {
                "display_name": "Test Author"
            }
        }
    ],
    "abstract_inverted_index": {
        "Machine": [0],
        "learning": [1],
        "research": [2]
    },
    "primary_location": {
        "landing_page_url": "https://example.com"
    }
}


# Test 1: Abstract reconstruction

def test_reconstruct_abstract():

    data = {
        "Machine": [0],
        "learning": [1]
    }

    assert reconstruct_abstract(data) == "Machine learning"


# Test 2: Missing abstract

def test_missing_abstract():

    assert reconstruct_abstract(None) is None


# Test 3: Paper metadata parsing

def test_parse_paper():

    paper = parse_paper(SAMPLE_PAPER)

    assert paper.title == "Sample mathematics research"
    assert paper.publication_year == 2024
    assert paper.authors == ["Test Author"]
    assert paper.cited_by_count == 10


# Test 4: Empty search query

def test_empty_query():

    with pytest.raises(ValueError):

        search_papers("", 5)


# Test 5: Invalid paper count

def test_invalid_paper_count():

    with pytest.raises(ValueError):

        search_papers("Machine learning", 0)


# Test 6: Successful API response

@patch("src.paper_search.requests.get")
def test_successful_search(mock_get):

    response = Mock()

    response.json.return_value = {
        "results": [SAMPLE_PAPER]
    }

    mock_get.return_value = response

    result = search_papers("Mathematics", 5)

    assert len(result) == 1
    assert result[0].title == SAMPLE_PAPER["title"]


# Test 7: Duplicate paper removal

@patch("src.paper_search.requests.get")
def test_duplicate_papers(mock_get):

    response = Mock()

    response.json.return_value = {
        "results": [
            SAMPLE_PAPER,
            SAMPLE_PAPER
        ]
    }

    mock_get.return_value = response

    result = search_papers("Mathematics", 5)

    assert len(result) == 1


# Test 8: API failure handling

@patch("src.paper_search.requests.get")
def test_api_failure(mock_get):

    mock_get.side_effect = requests.Timeout(
        "API timeout"
    )

    with pytest.raises(RuntimeError):

        search_papers("Machine learning", 5)
