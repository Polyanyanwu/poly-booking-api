"""
Depending on how the API is used, you may receive Python objects that were
deserialized from JSON or some other structured data format, or you may receive
a string representation of JSON data. This gets tricky to handle on serializers

To get around this, I created a function.py module with a function to handle
the payload. It will attempt to deserialize JSON, returning the raw input
if it isn’t a string representation of JSON. That way, no matter what
is sent to the API, we can work with the data.

This code also ensures that the data type being returned is the one specified.
That is, if you expect a string, the function will raise an exception
if you don’t get a string.
https://corgibytes.com/blog/2022/06/14/model-relationships-django-rest-framework/
"""

import json


def attempt_json_deserialize(data, expect_type=None):
    try:
        data = json.loads(data)
    except (TypeError, json.decoder.JSONDecodeError):
        pass

    if expect_type is not None and not isinstance(data, expect_type):
        raise ValueError(f"Got {type(data)} but expected {expect_type}.")

    return data
