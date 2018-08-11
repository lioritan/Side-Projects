from io import BytesIO
import avro.io


def serialize_avro_to_string(datum_writer, content):
    bytes_writer = BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    datum_writer.write(content, encoder)

    return bytes_writer.getvalue()


def deserialize_string_to_avro(datum_reader, content):
    bytes_reader = BytesIO(content)
    decoder = avro.io.BinaryDecoder(bytes_reader)

    return datum_reader.read(decoder)


def serialize_proto_to_string(content):
    return content.SerializeToString()


def deserialize_string_to_proto(content, old_obj):  # use old_obj.Clear() to pre-clean
    old_obj.ParseFromString(content)
