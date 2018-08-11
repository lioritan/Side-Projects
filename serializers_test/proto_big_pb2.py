# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_big.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_big.proto',
  package='big_obj',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fproto_big.proto\x12\x07\x62ig_obj\"<\n\x04\x46ile\x12\x11\n\tfile_name\x18\x01 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\x10\n\x08last_mod\x18\x03 \x01(\t\"h\n\x06\x46older\x12\x0c\n\x04path\x18\x01 \x02(\t\x12\x10\n\x08last_mod\x18\x02 \x01(\t\x12\x1c\n\x05\x66iles\x18\x03 \x03(\x0b\x32\r.big_obj.File\x12 \n\x07\x66olders\x18\x04 \x03(\x0b\x32\x0f.big_obj.Folder\"C\n\nDirFolders\x12\x0f\n\x07\x64\x65tails\x18\x01 \x02(\t\x12$\n\x0b\x62\x61se_folder\x18\x02 \x02(\x0b\x32\x0f.big_obj.Folder')
)




_FILE = _descriptor.Descriptor(
  name='File',
  full_name='big_obj.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='big_obj.File.file_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='big_obj.File.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mod', full_name='big_obj.File.last_mod', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=88,
)


_FOLDER = _descriptor.Descriptor(
  name='Folder',
  full_name='big_obj.Folder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='big_obj.Folder.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_mod', full_name='big_obj.Folder.last_mod', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='big_obj.Folder.files', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folders', full_name='big_obj.Folder.folders', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=194,
)


_DIRFOLDERS = _descriptor.Descriptor(
  name='DirFolders',
  full_name='big_obj.DirFolders',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='big_obj.DirFolders.details', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_folder', full_name='big_obj.DirFolders.base_folder', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=263,
)

_FOLDER.fields_by_name['files'].message_type = _FILE
_FOLDER.fields_by_name['folders'].message_type = _FOLDER
_DIRFOLDERS.fields_by_name['base_folder'].message_type = _FOLDER
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Folder'] = _FOLDER
DESCRIPTOR.message_types_by_name['DirFolders'] = _DIRFOLDERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'proto_big_pb2'
  # @@protoc_insertion_point(class_scope:big_obj.File)
  ))
_sym_db.RegisterMessage(File)

Folder = _reflection.GeneratedProtocolMessageType('Folder', (_message.Message,), dict(
  DESCRIPTOR = _FOLDER,
  __module__ = 'proto_big_pb2'
  # @@protoc_insertion_point(class_scope:big_obj.Folder)
  ))
_sym_db.RegisterMessage(Folder)

DirFolders = _reflection.GeneratedProtocolMessageType('DirFolders', (_message.Message,), dict(
  DESCRIPTOR = _DIRFOLDERS,
  __module__ = 'proto_big_pb2'
  # @@protoc_insertion_point(class_scope:big_obj.DirFolders)
  ))
_sym_db.RegisterMessage(DirFolders)


# @@protoc_insertion_point(module_scope)
