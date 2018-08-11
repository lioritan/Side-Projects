# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_avg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_avg.proto',
  package='avg_obj',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fproto_avg.proto\x12\x07\x61vg_obj\"\xa7\x01\n\x08PostUser\x12\x0f\n\x07user_id\x18\x01 \x02(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x33\n\tuser_type\x18\x04 \x01(\x0e\x32\x1a.avg_obj.PostUser.UserType:\x04\x46REE\".\n\x08UserType\x12\x08\n\x04\x46REE\x10\x00\x12\x0b\n\x07REGULAR\x10\x01\x12\x0b\n\x07PREMIUM\x10\x02\"\xa2\x01\n\tMemeImage\x12\x1f\n\x04user\x18\x01 \x02(\x0b\x32\x11.avg_obj.PostUser\x12\r\n\x05title\x18\x02 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12\x12\n\ntop_string\x18\x04 \x01(\t\x12\x15\n\rbottom_string\x18\x05 \x01(\t\x12\x10\n\x05likes\x18\x06 \x01(\x03:\x01\x30\x12\x10\n\x05hates\x18\x07 \x01(\x03:\x01\x30*\x05\x08\x64\x10\xc8\x01')
)



_POSTUSER_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='avg_obj.PostUser.UserType',
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
  serialized_start=150,
  serialized_end=196,
)
_sym_db.RegisterEnumDescriptor(_POSTUSER_USERTYPE)


_POSTUSER = _descriptor.Descriptor(
  name='PostUser',
  full_name='avg_obj.PostUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='avg_obj.PostUser.user_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='avg_obj.PostUser.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='avg_obj.PostUser.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='avg_obj.PostUser.user_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POSTUSER_USERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=196,
)


_MEMEIMAGE = _descriptor.Descriptor(
  name='MemeImage',
  full_name='avg_obj.MemeImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='avg_obj.MemeImage.user', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='avg_obj.MemeImage.title', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='avg_obj.MemeImage.content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_string', full_name='avg_obj.MemeImage.top_string', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom_string', full_name='avg_obj.MemeImage.bottom_string', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='likes', full_name='avg_obj.MemeImage.likes', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hates', full_name='avg_obj.MemeImage.hates', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 200), ],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=361,
)

_POSTUSER.fields_by_name['user_type'].enum_type = _POSTUSER_USERTYPE
_POSTUSER_USERTYPE.containing_type = _POSTUSER
_MEMEIMAGE.fields_by_name['user'].message_type = _POSTUSER
DESCRIPTOR.message_types_by_name['PostUser'] = _POSTUSER
DESCRIPTOR.message_types_by_name['MemeImage'] = _MEMEIMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostUser = _reflection.GeneratedProtocolMessageType('PostUser', (_message.Message,), dict(
  DESCRIPTOR = _POSTUSER,
  __module__ = 'proto_avg_pb2'
  # @@protoc_insertion_point(class_scope:avg_obj.PostUser)
  ))
_sym_db.RegisterMessage(PostUser)

MemeImage = _reflection.GeneratedProtocolMessageType('MemeImage', (_message.Message,), dict(
  DESCRIPTOR = _MEMEIMAGE,
  __module__ = 'proto_avg_pb2'
  # @@protoc_insertion_point(class_scope:avg_obj.MemeImage)
  ))
_sym_db.RegisterMessage(MemeImage)


# @@protoc_insertion_point(module_scope)
