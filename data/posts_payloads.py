
valid_post_payload = {
    "title": "API Automation Framework",
    "body" : "Learning API automation using python and pytest",
    "userId" : 1
}

update_post_payload = {
    "id" : 1,
    "title" : "Updated API Automation Title",
    "body" : "Updated body content",
    "userId" : 1
    }

partial_update_payload = {
    "title" : "Partially Updated Title"
    }

invalid_post_payload_missing_title = {
    "body": "This payload is missing title",
    "userId" : 1
}