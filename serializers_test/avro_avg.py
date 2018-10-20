import avro.schema
import json

import fastavro

SCHEMA = {
    "namespace": "avg_obj",
    "type": "record",
    "name": "Meme",
    "fields": [
        {"name": "user", "type": {
            "type": "record",
            "name": "PostUser",
            "fields": [
                {"name": "user_id", "type": "string"},
                {"name": "first_name", "type": ["null", "string"], "default": "null"},
                {"name": "last_name", "type": ["null", "string"], "default": "null"},
                {"name": "user_type", "type": ["null",
                                               {"type": "enum",
                                                "name": "UserType",
                                                "symbols": ["FREE", "REGULAR", "PREMIUM"]
                                                }], "default": "null"},
            ]}},

        {"name": "title", "type": ["null", "string"], "default": "null"},
        {"name": "content", "type": ["null", "bytes"], "default": "null"},
        {"name": "top_string", "type": ["null", "string"], "default": "null"},
        {"name": "botom_string", "type": ["null", "string"], "default": "null"},
        {"name": "likes", "type": ["null", "long"], "default": 0},
        {"name": "hates", "type": ["null", "long"], "default": 0},
    ]
}

avro_schema = fastavro.parse_schema(SCHEMA)
