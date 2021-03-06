# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_small.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_small.proto',
  package='small_obj',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11proto_small.proto\x12\tsmall_obj\"\xb8\x01\n\x05Tweet\x12\x0f\n\x07user_id\x18\x01 \x02(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x32\n\tuser_type\x18\x04 \x01(\x0e\x32\x19.small_obj.Tweet.UserType:\x04\x46REE\x12\x13\n\x0btweet_chars\x18\x05 \x03(\t\".\n\x08UserType\x12\x08\n\x04\x46REE\x10\x00\x12\x0b\n\x07REGULAR\x10\x01\x12\x0b\n\x07PREMIUM\x10\x02')
)



_TWEET_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='small_obj.Tweet.UserType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FREE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGULAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREMIUM', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=171,
  serialized_end=217,
)
_sym_db.RegisterEnumDescriptor(_TWEET_USERTYPE)


_TWEET = _descriptor.Descriptor(
  name='Tweet',
  full_name='small_obj.Tweet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='small_obj.Tweet.user_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='small_obj.Tweet.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='small_obj.Tweet.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='small_obj.Tweet.user_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tweet_chars', full_name='small_obj.Tweet.tweet_chars', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TWEET_USERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=217,
)

_TWEET.fields_by_name['user_type'].enum_type = _TWEET_USERTYPE
_TWEET_USERTYPE.containing_type = _TWEET
DESCRIPTOR.message_types_by_name['Tweet'] = _TWEET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Tweet = _reflection.GeneratedProtocolMessageType('Tweet', (_message.Message,), dict(
  DESCRIPTOR = _TWEET,
  __module__ = 'proto_small_pb2'
  # @@protoc_insertion_point(class_scope:small_obj.Tweet)
  ))
_sym_db.RegisterMessage(Tweet)


# @@protoc_insertion_point(module_scope)
