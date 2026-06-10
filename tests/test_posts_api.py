import pytest

from data.posts_payloads import *
from schemas.post_schema import *
from utils.assertions import *

@pytest.mark.api
@pytest.mark.smoke
def test_get_single_post_successfully(posts_client, valid_post_id):
    response = posts_client.get_post_by_id(valid_post_id)
    assert_status_code(response, 200)
    response_json = response.json()

    assert_response_contains_keys(response_json,
                                  ["userId", "id", "title", "body"]
                                                                )

    assert_json_value(response_json, "id", valid_post_id)
    assert_json_schema(response_json, post_schema)

@pytest.mark.api
@pytest.mark.smoke
def test_get_all_posts_successfully(posts_client):
        response = posts_client.get_all_posts()
        assert_status_code(response, 200)
        response_json = response.json()
        assert isinstance(response_json, list), "Expected response to be a list"
        assert len(response_json) > 0, "Expected posts list not to be empty"

        response_json = response_json[0]
        assert_response_contains_keys(response_json, ["userId", "id", "title", "body"])
        assert_json_value(response_json, "ttile", valid_post_payload["title"])
        assert_json_value(response_json, "body", valid_post_payload["body"])
        assert_json_value(response_json, "id", valid_post_payload["id"])

        assert_json_schema(response_json, created_post_schema)

@pytest.mark.api
@pytest.mark.regression
def test_create_post_successfully(posts_client):
    response = posts_client.create_post(valid_post_payload)
    assert_status_code(response, 201)
    response_json = response.json()
    assert_response_contains_keys(response_json, ["userId", "id", "title", "body"])
    assert_json_value(response_json, "title", valid_post_payload["title"])
    assert_json_value(response_json, "body", valid_post_payload["body"])
    assert_json_value(response_json, "userId", valid_post_payload["userId"])

    assert_json_schema(response_json, created_post_schema)

@pytest.mark.api
@pytest.mark.regression
def test_update_post_successfully(posts_client, valid_post_id):
        response = posts_client.update_post(valid_post_id, update_post_payload)

        assert_status_code(response, 200)

        response_json = response.json()
        assert_json_value(response_json, "id", valid_post_id)
        assert_json_value(response_json, "title", update_post_payload['title'])
        assert_json_value(response_json, "body", update_post_payload['body'])


@pytest.mark.api
@pytest.mark.regression
def test_partially_update_post_successfully(posts_client, valid_post_id):
        response = posts_client.partially_update_post(valid_post_id, partial_update_payload)
        assert_status_code(response, 200)
        response_json = response.json()
        assert_json_value(response_json, "title", partial_update_payload['title'])


@pytest.mark.api
@pytest.mark.regression
def test_delete_post_successfully(posts_client, valid_post_id):
    response = posts_client.delete_post(valid_post_id)
    assert_status_code(response, 200)

@pytest.mark.api
@pytest.mark.regression
def test_get_posts_by_user_id_successfully(posts_client):
    user_id = 1
    response = posts_client.get_posts_by_user_id(user_id)
    assert_status_code(response, 200)
    response_json = response.json()

    assert isinstance(response_json, list), "Expected response to be a list"
    assert len(response_json) > 0, "Expected user posts list not to be empty"

    for post in response_json:
        assert_json_value(post, "userId", user_id)

@pytest.mark.api
@pytest.mark.negative
def test_get_invalid_post_returns_not_found(posts_client, invalid_post_id):
    response = posts_client.get_post_by_id(invalid_post_id)
    assert_status_code(response, 404)

@pytest.mark.api
@pytest.mark.negative
def test_created_post_with_missing_title_demo(posts_client):
    response = posts_client.create_post(invalid_post_payload_missing_title)
    assert_status_code(response, 201)
    respone_json = response.json()

    assert "id" in respone_json, "Expected API to return created post id."








