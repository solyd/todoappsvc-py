# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='todoapp',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\x07todoapp\"2\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08\x63ontents\x18\x02 \x01(\t\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\"%\n\x06\x43reate\x12\x1b\n\x04task\x18\x01 \x01(\x0b\x32\r.todoapp.Task\"\x16\n\x08\x43reateOk\x12\n\n\x02id\x18\x01 \x01(\x03\"%\n\x05GetOk\x12\x1c\n\x05tasks\x18\x01 \x03(\x0b\x32\r.todoapp.Task\"\x17\n\x08MarkDone\x12\x0b\n\x03ids\x18\x01 \x03(\x03\"\x19\n\nMarkDoneOk\x12\x0b\n\x03ids\x18\x01 \x03(\x03\"\x15\n\x06\x44\x65lete\x12\x0b\n\x03ids\x18\x01 \x03(\x03\"\x17\n\x08\x44\x65leteOk\x12\x0b\n\x03ids\x18\x01 \x03(\x03\"$\n\x06\x41piErr\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t*)\n\nApiErrCode\x12\x0f\n\x0b\x45RR_UNKNOWN\x10\x00\x12\n\n\x06\x45RR_DB\x10\x01\x62\x06proto3'
)

_APIERRCODE = _descriptor.EnumDescriptor(
  name='ApiErrCode',
  full_name='todoapp.ApiErrCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERR_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERR_DB', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=314,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_APIERRCODE)

ApiErrCode = enum_type_wrapper.EnumTypeWrapper(_APIERRCODE)
ERR_UNKNOWN = 0
ERR_DB = 1



_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='todoapp.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todoapp.Task.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contents', full_name='todoapp.Task.contents', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='done', full_name='todoapp.Task.done', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=72,
)


_CREATE = _descriptor.Descriptor(
  name='Create',
  full_name='todoapp.Create',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='todoapp.Create.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=111,
)


_CREATEOK = _descriptor.Descriptor(
  name='CreateOk',
  full_name='todoapp.CreateOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todoapp.CreateOk.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=135,
)


_GETOK = _descriptor.Descriptor(
  name='GetOk',
  full_name='todoapp.GetOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='todoapp.GetOk.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=174,
)


_MARKDONE = _descriptor.Descriptor(
  name='MarkDone',
  full_name='todoapp.MarkDone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='todoapp.MarkDone.ids', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=199,
)


_MARKDONEOK = _descriptor.Descriptor(
  name='MarkDoneOk',
  full_name='todoapp.MarkDoneOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='todoapp.MarkDoneOk.ids', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=226,
)


_DELETE = _descriptor.Descriptor(
  name='Delete',
  full_name='todoapp.Delete',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='todoapp.Delete.ids', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=249,
)


_DELETEOK = _descriptor.Descriptor(
  name='DeleteOk',
  full_name='todoapp.DeleteOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='todoapp.DeleteOk.ids', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=274,
)


_APIERR = _descriptor.Descriptor(
  name='ApiErr',
  full_name='todoapp.ApiErr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='todoapp.ApiErr.code', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='todoapp.ApiErr.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=312,
)

_CREATE.fields_by_name['task'].message_type = _TASK
_GETOK.fields_by_name['tasks'].message_type = _TASK
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Create'] = _CREATE
DESCRIPTOR.message_types_by_name['CreateOk'] = _CREATEOK
DESCRIPTOR.message_types_by_name['GetOk'] = _GETOK
DESCRIPTOR.message_types_by_name['MarkDone'] = _MARKDONE
DESCRIPTOR.message_types_by_name['MarkDoneOk'] = _MARKDONEOK
DESCRIPTOR.message_types_by_name['Delete'] = _DELETE
DESCRIPTOR.message_types_by_name['DeleteOk'] = _DELETEOK
DESCRIPTOR.message_types_by_name['ApiErr'] = _APIERR
DESCRIPTOR.enum_types_by_name['ApiErrCode'] = _APIERRCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.Task)
  })
_sym_db.RegisterMessage(Task)

Create = _reflection.GeneratedProtocolMessageType('Create', (_message.Message,), {
  'DESCRIPTOR' : _CREATE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.Create)
  })
_sym_db.RegisterMessage(Create)

CreateOk = _reflection.GeneratedProtocolMessageType('CreateOk', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOK,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.CreateOk)
  })
_sym_db.RegisterMessage(CreateOk)

GetOk = _reflection.GeneratedProtocolMessageType('GetOk', (_message.Message,), {
  'DESCRIPTOR' : _GETOK,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.GetOk)
  })
_sym_db.RegisterMessage(GetOk)

MarkDone = _reflection.GeneratedProtocolMessageType('MarkDone', (_message.Message,), {
  'DESCRIPTOR' : _MARKDONE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.MarkDone)
  })
_sym_db.RegisterMessage(MarkDone)

MarkDoneOk = _reflection.GeneratedProtocolMessageType('MarkDoneOk', (_message.Message,), {
  'DESCRIPTOR' : _MARKDONEOK,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.MarkDoneOk)
  })
_sym_db.RegisterMessage(MarkDoneOk)

Delete = _reflection.GeneratedProtocolMessageType('Delete', (_message.Message,), {
  'DESCRIPTOR' : _DELETE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.Delete)
  })
_sym_db.RegisterMessage(Delete)

DeleteOk = _reflection.GeneratedProtocolMessageType('DeleteOk', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOK,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.DeleteOk)
  })
_sym_db.RegisterMessage(DeleteOk)

ApiErr = _reflection.GeneratedProtocolMessageType('ApiErr', (_message.Message,), {
  'DESCRIPTOR' : _APIERR,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:todoapp.ApiErr)
  })
_sym_db.RegisterMessage(ApiErr)


# @@protoc_insertion_point(module_scope)
