from io import BytesIO
import fastavro


def serialize_avro_to_string(schema, content):
    bytes_writer = BytesIO()
    fastavro.writer(bytes_writer, schema, content)
    #encoder = avro.io.BinaryEncoder(bytes_writer)
    #datum_writer.write(content, encoder)

    return bytes_writer.getvalue()


def deserialize_string_to_avro(schema, content):
    bytes_reader = BytesIO(content)
    #decoder = avro.io.BinaryDecoder(bytes_reader)
    return fastavro.reader(bytes_reader, schema)

    #return datum_reader.read(decoder)


def serialize_proto_to_string(content):
    return content.SerializeToString()


def deserialize_string_to_proto(content, old_obj):  # use old_obj.Clear() to pre-clean
    old_obj.ParseFromString(content)
