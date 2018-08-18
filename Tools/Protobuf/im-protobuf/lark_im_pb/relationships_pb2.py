# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relationships.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='relationships.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x13relationships.proto\"\xac\x01\n\x0b\x43hatUserRef\x12\x35\n\rchat2user_ids\x18\x01 \x03(\x0b\x32\x1e.ChatUserRef.Chat2userIdsEntry\x1a\x1b\n\x07UserIds\x12\x10\n\x08user_ids\x18\x01 \x03(\t\x1aI\n\x11\x43hat2userIdsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.ChatUserRef.UserIds:\x02\x38\x01\x42Q\n\x16\x63om.ss.android.lark.pbZ7git.byted.org/ee/lark/im-protobuf/improto/relationships')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHATUSERREF_USERIDS = _descriptor.Descriptor(
  name='UserIds',
  full_name='ChatUserRef.UserIds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_ids', full_name='ChatUserRef.UserIds.user_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=121,
)

_CHATUSERREF_CHAT2USERIDSENTRY = _descriptor.Descriptor(
  name='Chat2userIdsEntry',
  full_name='ChatUserRef.Chat2userIdsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ChatUserRef.Chat2userIdsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ChatUserRef.Chat2userIdsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=196,
)

_CHATUSERREF = _descriptor.Descriptor(
  name='ChatUserRef',
  full_name='ChatUserRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chat2user_ids', full_name='ChatUserRef.chat2user_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CHATUSERREF_USERIDS, _CHATUSERREF_CHAT2USERIDSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=196,
)

_CHATUSERREF_USERIDS.containing_type = _CHATUSERREF
_CHATUSERREF_CHAT2USERIDSENTRY.fields_by_name['value'].message_type = _CHATUSERREF_USERIDS
_CHATUSERREF_CHAT2USERIDSENTRY.containing_type = _CHATUSERREF
_CHATUSERREF.fields_by_name['chat2user_ids'].message_type = _CHATUSERREF_CHAT2USERIDSENTRY
DESCRIPTOR.message_types_by_name['ChatUserRef'] = _CHATUSERREF

ChatUserRef = _reflection.GeneratedProtocolMessageType('ChatUserRef', (_message.Message,), dict(

  UserIds = _reflection.GeneratedProtocolMessageType('UserIds', (_message.Message,), dict(
    DESCRIPTOR = _CHATUSERREF_USERIDS,
    __module__ = 'relationships_pb2'
    # @@protoc_insertion_point(class_scope:ChatUserRef.UserIds)
    ))
  ,

  Chat2userIdsEntry = _reflection.GeneratedProtocolMessageType('Chat2userIdsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CHATUSERREF_CHAT2USERIDSENTRY,
    __module__ = 'relationships_pb2'
    # @@protoc_insertion_point(class_scope:ChatUserRef.Chat2userIdsEntry)
    ))
  ,
  DESCRIPTOR = _CHATUSERREF,
  __module__ = 'relationships_pb2'
  # @@protoc_insertion_point(class_scope:ChatUserRef)
  ))
_sym_db.RegisterMessage(ChatUserRef)
_sym_db.RegisterMessage(ChatUserRef.UserIds)
_sym_db.RegisterMessage(ChatUserRef.Chat2userIdsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.ss.android.lark.pbZ7git.byted.org/ee/lark/im-protobuf/improto/relationships'))
_CHATUSERREF_CHAT2USERIDSENTRY.has_options = True
_CHATUSERREF_CHAT2USERIDSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
