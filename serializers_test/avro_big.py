import avro.schema
import json

SCHEMA = {
    "namespace": "big_obj",
    "type": "record",
    "name": "DirFolders",
    "fields": [
        {"name": "base_folder", "type": {
            "type": "record",
            "name": "Folder",
            "fields": [
                {"name": "path", "type": "string"},
                {"name": "last_mod", "type": ["null", "string"], "default": "null"},
                {"name": "files", "type": ["null", {"type": "array", "items": {
                    "type": "record",
                    "name": "File",
                    "fields": [
                        {"name": "file_name", "type": "string"},
                        {"name": "content", "type": "bytes"},
                        {"name": "last_mod", "type": ["null", "string"], "default": "null"}
                    ]
                }}], "default": "null"},
                {"name": "folders", "type": ["null",
                                             {"type": "array", "items": "Folder"}], "default":"null"}
            ]}},

        {"name": "details", "type": "string"},
    ]
}

avro_schema = avro.schema.Parse(json.dumps(SCHEMA))
