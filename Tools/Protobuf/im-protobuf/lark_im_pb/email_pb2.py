# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: email.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import entities_pb2 as entities__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='email.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0b\x65mail.proto\x1a\x0e\x65ntities.proto\"v\n\x06Member\x12\n\n\x02id\x18\x01 \x02(\t\x12\x1a\n\x04type\x18\x02 \x02(\x0e\x32\x0c.Member.Type\x12\x12\n\ninviter_id\x18\x03 \x01(\t\x12\x11\n\tjoin_time\x18\x04 \x01(\x03\"\x1d\n\x04Type\x12\x0b\n\x07\x43HATTER\x10\x01\x12\x08\n\x04\x43HAT\x10\x02\"y\n\x0fPutEmailRequest\x12\x13\n\x02to\x18\x01 \x03(\x0b\x32\x07.Member\x12\x13\n\x02\x63\x63\x18\x02 \x03(\x0b\x32\x07.Member\x12\x1e\n\x07\x63ontent\x18\x03 \x01(\x0b\x32\r.EmailContent\x12\x0f\n\x07root_id\x18\x04 \x01(\t\x12\x0b\n\x03\x63id\x18\x05 \x01(\t\"W\n\x10PutEmailResponse\x12\x19\n\x07message\x18\x01 \x01(\x0b\x32\x08.Message\x12\x13\n\x02to\x18\x02 \x03(\x0b\x32\x07.Member\x12\x13\n\x02\x63\x63\x18\x03 \x03(\x0b\x32\x07.Member\"+\n\x17PullEmailMembersRequest\x12\x10\n\x08\x65mail_id\x18\x01 \x01(\t\"D\n\x18PullEmailMembersResponse\x12\x13\n\x02to\x18\x01 \x03(\x0b\x32\x07.Member\x12\x13\n\x02\x63\x63\x18\x02 \x03(\x0b\x32\x07.Member\"u\n\x18PatchEmailMembersRequest\x12\x10\n\x08\x65mail_id\x18\x01 \x01(\t\x12\x1d\n\toperation\x18\x02 \x01(\x0e\x32\n.Operation\x12\x13\n\x02to\x18\x03 \x03(\x0b\x32\x07.Member\x12\x13\n\x02\x63\x63\x18\x04 \x03(\x0b\x32\x07.Member\"\x1b\n\x19PatchEmailMembersResponse\"\x9e\x01\n\x17PushEmailMembersRequest\x12\x10\n\x08\x65mail_id\x18\x01 \x01(\t\x12\x13\n\x0boperator_id\x18\x02 \x01(\t\x12\x1d\n\toperation\x18\x03 \x01(\x0e\x32\n.Operation\x12\x13\n\x02to\x18\x04 \x03(\x0b\x32\x07.Member\x12\x13\n\x02\x63\x63\x18\x05 \x03(\x0b\x32\x07.Member\x12\x13\n\x0bupdate_time\x18\x06 \x01(\x03*0\n\tOperation\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x12\x0e\n\nCHANGED_TO\x10\x03\x42I\n\x16\x63om.ss.android.lark.pbZ/git.byted.org/ee/lark/im-protobuf/improto/email')
  ,
  dependencies=[entities__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANGED_TO', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=787,
  serialized_end=835,
)
_sym_db.RegisterEnumDescriptor(_OPERATION)

Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
ADD = 1
DELETE = 2
CHANGED_TO = 3


_MEMBER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Member.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHATTER', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAT', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=120,
  serialized_end=149,
)
_sym_db.RegisterEnumDescriptor(_MEMBER_TYPE)


_MEMBER = _descriptor.Descriptor(
  name='Member',
  full_name='Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Member.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Member.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_id', full_name='Member.inviter_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='join_time', full_name='Member.join_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEMBER_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=149,
)


_PUTEMAILREQUEST = _descriptor.Descriptor(
  name='PutEmailRequest',
  full_name='PutEmailRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='PutEmailRequest.to', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc', full_name='PutEmailRequest.cc', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='PutEmailRequest.content', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_id', full_name='PutEmailRequest.root_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cid', full_name='PutEmailRequest.cid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=151,
  serialized_end=272,
)


_PUTEMAILRESPONSE = _descriptor.Descriptor(
  name='PutEmailResponse',
  full_name='PutEmailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='PutEmailResponse.message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='PutEmailResponse.to', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc', full_name='PutEmailResponse.cc', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=274,
  serialized_end=361,
)


_PULLEMAILMEMBERSREQUEST = _descriptor.Descriptor(
  name='PullEmailMembersRequest',
  full_name='PullEmailMembersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email_id', full_name='PullEmailMembersRequest.email_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=363,
  serialized_end=406,
)


_PULLEMAILMEMBERSRESPONSE = _descriptor.Descriptor(
  name='PullEmailMembersResponse',
  full_name='PullEmailMembersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='PullEmailMembersResponse.to', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc', full_name='PullEmailMembersResponse.cc', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=408,
  serialized_end=476,
)


_PATCHEMAILMEMBERSREQUEST = _descriptor.Descriptor(
  name='PatchEmailMembersRequest',
  full_name='PatchEmailMembersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email_id', full_name='PatchEmailMembersRequest.email_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='PatchEmailMembersRequest.operation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='PatchEmailMembersRequest.to', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc', full_name='PatchEmailMembersRequest.cc', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=478,
  serialized_end=595,
)


_PATCHEMAILMEMBERSRESPONSE = _descriptor.Descriptor(
  name='PatchEmailMembersResponse',
  full_name='PatchEmailMembersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=597,
  serialized_end=624,
)


_PUSHEMAILMEMBERSREQUEST = _descriptor.Descriptor(
  name='PushEmailMembersRequest',
  full_name='PushEmailMembersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email_id', full_name='PushEmailMembersRequest.email_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator_id', full_name='PushEmailMembersRequest.operator_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='PushEmailMembersRequest.operation', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to', full_name='PushEmailMembersRequest.to', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc', full_name='PushEmailMembersRequest.cc', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='PushEmailMembersRequest.update_time', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=627,
  serialized_end=785,
)

_MEMBER.fields_by_name['type'].enum_type = _MEMBER_TYPE
_MEMBER_TYPE.containing_type = _MEMBER
_PUTEMAILREQUEST.fields_by_name['to'].message_type = _MEMBER
_PUTEMAILREQUEST.fields_by_name['cc'].message_type = _MEMBER
_PUTEMAILREQUEST.fields_by_name['content'].message_type = entities__pb2._EMAILCONTENT
_PUTEMAILRESPONSE.fields_by_name['message'].message_type = entities__pb2._MESSAGE
_PUTEMAILRESPONSE.fields_by_name['to'].message_type = _MEMBER
_PUTEMAILRESPONSE.fields_by_name['cc'].message_type = _MEMBER
_PULLEMAILMEMBERSRESPONSE.fields_by_name['to'].message_type = _MEMBER
_PULLEMAILMEMBERSRESPONSE.fields_by_name['cc'].message_type = _MEMBER
_PATCHEMAILMEMBERSREQUEST.fields_by_name['operation'].enum_type = _OPERATION
_PATCHEMAILMEMBERSREQUEST.fields_by_name['to'].message_type = _MEMBER
_PATCHEMAILMEMBERSREQUEST.fields_by_name['cc'].message_type = _MEMBER
_PUSHEMAILMEMBERSREQUEST.fields_by_name['operation'].enum_type = _OPERATION
_PUSHEMAILMEMBERSREQUEST.fields_by_name['to'].message_type = _MEMBER
_PUSHEMAILMEMBERSREQUEST.fields_by_name['cc'].message_type = _MEMBER
DESCRIPTOR.message_types_by_name['Member'] = _MEMBER
DESCRIPTOR.message_types_by_name['PutEmailRequest'] = _PUTEMAILREQUEST
DESCRIPTOR.message_types_by_name['PutEmailResponse'] = _PUTEMAILRESPONSE
DESCRIPTOR.message_types_by_name['PullEmailMembersRequest'] = _PULLEMAILMEMBERSREQUEST
DESCRIPTOR.message_types_by_name['PullEmailMembersResponse'] = _PULLEMAILMEMBERSRESPONSE
DESCRIPTOR.message_types_by_name['PatchEmailMembersRequest'] = _PATCHEMAILMEMBERSREQUEST
DESCRIPTOR.message_types_by_name['PatchEmailMembersResponse'] = _PATCHEMAILMEMBERSRESPONSE
DESCRIPTOR.message_types_by_name['PushEmailMembersRequest'] = _PUSHEMAILMEMBERSREQUEST
DESCRIPTOR.enum_types_by_name['Operation'] = _OPERATION

Member = _reflection.GeneratedProtocolMessageType('Member', (_message.Message,), dict(
  DESCRIPTOR = _MEMBER,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:Member)
  ))
_sym_db.RegisterMessage(Member)

PutEmailRequest = _reflection.GeneratedProtocolMessageType('PutEmailRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUTEMAILREQUEST,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PutEmailRequest)
  ))
_sym_db.RegisterMessage(PutEmailRequest)

PutEmailResponse = _reflection.GeneratedProtocolMessageType('PutEmailResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUTEMAILRESPONSE,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PutEmailResponse)
  ))
_sym_db.RegisterMessage(PutEmailResponse)

PullEmailMembersRequest = _reflection.GeneratedProtocolMessageType('PullEmailMembersRequest', (_message.Message,), dict(
  DESCRIPTOR = _PULLEMAILMEMBERSREQUEST,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PullEmailMembersRequest)
  ))
_sym_db.RegisterMessage(PullEmailMembersRequest)

PullEmailMembersResponse = _reflection.GeneratedProtocolMessageType('PullEmailMembersResponse', (_message.Message,), dict(
  DESCRIPTOR = _PULLEMAILMEMBERSRESPONSE,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PullEmailMembersResponse)
  ))
_sym_db.RegisterMessage(PullEmailMembersResponse)

PatchEmailMembersRequest = _reflection.GeneratedProtocolMessageType('PatchEmailMembersRequest', (_message.Message,), dict(
  DESCRIPTOR = _PATCHEMAILMEMBERSREQUEST,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PatchEmailMembersRequest)
  ))
_sym_db.RegisterMessage(PatchEmailMembersRequest)

PatchEmailMembersResponse = _reflection.GeneratedProtocolMessageType('PatchEmailMembersResponse', (_message.Message,), dict(
  DESCRIPTOR = _PATCHEMAILMEMBERSRESPONSE,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PatchEmailMembersResponse)
  ))
_sym_db.RegisterMessage(PatchEmailMembersResponse)

PushEmailMembersRequest = _reflection.GeneratedProtocolMessageType('PushEmailMembersRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUSHEMAILMEMBERSREQUEST,
  __module__ = 'email_pb2'
  # @@protoc_insertion_point(class_scope:PushEmailMembersRequest)
  ))
_sym_db.RegisterMessage(PushEmailMembersRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.ss.android.lark.pbZ/git.byted.org/ee/lark/im-protobuf/improto/email'))
# @@protoc_insertion_point(module_scope)
