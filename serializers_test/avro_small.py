#import avro.schema
import fastavro
import json

SCHEMA = {
    "namespace": "small_obj",
    "type": "record",
    "name": "Tweet",
    "fields": [
        {"name": "user_id", "type":"string"},
        {"name": "first_name", "type":["null", "string"], "default":"null"},
        {"name": "last_name", "type":["null", "string"], "default":"null"},
        {"name": "user_type", "type":["null",
                {"type":"enum",
                 "name":"UserType",
                 "symbols": ["FREE", "REGULAR", "PREMIUM"]
                 }], "default":"null"},
        {"name": "tweet_chars", "type": ["null",{"type": "array", "items": "string"}], "default":"null"}
    ]
}

avro_schema = fastavro.parse_schema(SCHEMA)