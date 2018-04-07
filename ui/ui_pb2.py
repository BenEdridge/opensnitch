# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ui.proto

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
  name='ui.proto',
  package='protocol',
  syntax='proto3',
  serialized_pb=_b('\n\x08ui.proto\x12\x08protocol\"\xa3\x06\n\nStatistics\x12\x16\n\x0e\x64\x61\x65mon_version\x18\x01 \x01(\t\x12\x0e\n\x06uptime\x18\x02 \x01(\x04\x12\x15\n\rdns_responses\x18\x03 \x01(\x04\x12\x13\n\x0b\x63onnections\x18\x04 \x01(\x04\x12\x0f\n\x07ignored\x18\x05 \x01(\x04\x12\x10\n\x08\x61\x63\x63\x65pted\x18\x06 \x01(\x04\x12\x0f\n\x07\x64ropped\x18\x07 \x01(\x04\x12\x11\n\trule_hits\x18\x08 \x01(\x04\x12\x13\n\x0brule_misses\x18\t \x01(\x04\x12\x33\n\x08\x62y_proto\x18\n \x03(\x0b\x32!.protocol.Statistics.ByProtoEntry\x12\x37\n\nby_address\x18\x0b \x03(\x0b\x32#.protocol.Statistics.ByAddressEntry\x12\x31\n\x07\x62y_host\x18\x0c \x03(\x0b\x32 .protocol.Statistics.ByHostEntry\x12\x31\n\x07\x62y_port\x18\r \x03(\x0b\x32 .protocol.Statistics.ByPortEntry\x12/\n\x06\x62y_uid\x18\x0e \x03(\x0b\x32\x1f.protocol.Statistics.ByUidEntry\x12=\n\rby_executable\x18\x0f \x03(\x0b\x32&.protocol.Statistics.ByExecutableEntry\x1a.\n\x0c\x42yProtoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x30\n\x0e\x42yAddressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a-\n\x0b\x42yHostEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a-\n\x0b\x42yPortEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a,\n\nByUidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\x1a\x33\n\x11\x42yExecutableEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\">\n\x0bPingRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12#\n\x05stats\x18\x02 \x01(\x0b\x32\x14.protocol.Statistics\"\x17\n\tPingReply\x12\n\n\x02id\x18\x01 \x01(\x04\"\xc6\x01\n\x0bRuleRequest\x12\x10\n\x08protocol\x18\x01 \x01(\t\x12\x0e\n\x06src_ip\x18\x02 \x01(\t\x12\x10\n\x08src_port\x18\x03 \x01(\r\x12\x0e\n\x06\x64st_ip\x18\x04 \x01(\t\x12\x10\n\x08\x64st_host\x18\x05 \x01(\t\x12\x10\n\x08\x64st_port\x18\x06 \x01(\r\x12\x0f\n\x07user_id\x18\x07 \x01(\r\x12\x12\n\nprocess_id\x18\x08 \x01(\r\x12\x14\n\x0cprocess_path\x18\t \x01(\t\x12\x14\n\x0cprocess_args\x18\n \x03(\t\";\n\x0cRuleOperator\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07operand\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"e\n\tRuleReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x10\n\x08\x64uration\x18\x03 \x01(\t\x12(\n\x08operator\x18\x04 \x01(\x0b\x32\x16.protocol.RuleOperator2s\n\x02UI\x12\x34\n\x04Ping\x12\x15.protocol.PingRequest\x1a\x13.protocol.PingReply\"\x00\x12\x37\n\x07\x41skRule\x12\x15.protocol.RuleRequest\x1a\x13.protocol.RuleReply\"\x00\x62\x06proto3')
)




_STATISTICS_BYPROTOENTRY = _descriptor.Descriptor(
  name='ByProtoEntry',
  full_name='protocol.Statistics.ByProtoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Statistics.ByProtoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Statistics.ByProtoEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=537,
  serialized_end=583,
)

_STATISTICS_BYADDRESSENTRY = _descriptor.Descriptor(
  name='ByAddressEntry',
  full_name='protocol.Statistics.ByAddressEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Statistics.ByAddressEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Statistics.ByAddressEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=633,
)

_STATISTICS_BYHOSTENTRY = _descriptor.Descriptor(
  name='ByHostEntry',
  full_name='protocol.Statistics.ByHostEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Statistics.ByHostEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Statistics.ByHostEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=680,
)

_STATISTICS_BYPORTENTRY = _descriptor.Descriptor(
  name='ByPortEntry',
  full_name='protocol.Statistics.ByPortEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Statistics.ByPortEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Statistics.ByPortEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=727,
)

_STATISTICS_BYUIDENTRY = _descriptor.Descriptor(
  name='ByUidEntry',
  full_name='protocol.Statistics.ByUidEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Statistics.ByUidEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Statistics.ByUidEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=773,
)

_STATISTICS_BYEXECUTABLEENTRY = _descriptor.Descriptor(
  name='ByExecutableEntry',
  full_name='protocol.Statistics.ByExecutableEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='protocol.Statistics.ByExecutableEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='protocol.Statistics.ByExecutableEntry.value', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=826,
)

_STATISTICS = _descriptor.Descriptor(
  name='Statistics',
  full_name='protocol.Statistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='daemon_version', full_name='protocol.Statistics.daemon_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uptime', full_name='protocol.Statistics.uptime', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dns_responses', full_name='protocol.Statistics.dns_responses', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connections', full_name='protocol.Statistics.connections', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignored', full_name='protocol.Statistics.ignored', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accepted', full_name='protocol.Statistics.accepted', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dropped', full_name='protocol.Statistics.dropped', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_hits', full_name='protocol.Statistics.rule_hits', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule_misses', full_name='protocol.Statistics.rule_misses', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_proto', full_name='protocol.Statistics.by_proto', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_address', full_name='protocol.Statistics.by_address', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_host', full_name='protocol.Statistics.by_host', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_port', full_name='protocol.Statistics.by_port', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_uid', full_name='protocol.Statistics.by_uid', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='by_executable', full_name='protocol.Statistics.by_executable', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATISTICS_BYPROTOENTRY, _STATISTICS_BYADDRESSENTRY, _STATISTICS_BYHOSTENTRY, _STATISTICS_BYPORTENTRY, _STATISTICS_BYUIDENTRY, _STATISTICS_BYEXECUTABLEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=826,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='protocol.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protocol.PingRequest.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='protocol.PingRequest.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=890,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='protocol.PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='protocol.PingReply.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=915,
)


_RULEREQUEST = _descriptor.Descriptor(
  name='RuleRequest',
  full_name='protocol.RuleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='protocol.RuleRequest.protocol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_ip', full_name='protocol.RuleRequest.src_ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_port', full_name='protocol.RuleRequest.src_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_ip', full_name='protocol.RuleRequest.dst_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_host', full_name='protocol.RuleRequest.dst_host', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_port', full_name='protocol.RuleRequest.dst_port', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='protocol.RuleRequest.user_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_id', full_name='protocol.RuleRequest.process_id', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_path', full_name='protocol.RuleRequest.process_path', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='process_args', full_name='protocol.RuleRequest.process_args', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=918,
  serialized_end=1116,
)


_RULEOPERATOR = _descriptor.Descriptor(
  name='RuleOperator',
  full_name='protocol.RuleOperator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.RuleOperator.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operand', full_name='protocol.RuleOperator.operand', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protocol.RuleOperator.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1118,
  serialized_end=1177,
)


_RULEREPLY = _descriptor.Descriptor(
  name='RuleReply',
  full_name='protocol.RuleReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protocol.RuleReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='protocol.RuleReply.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='protocol.RuleReply.duration', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator', full_name='protocol.RuleReply.operator', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1280,
)

_STATISTICS_BYPROTOENTRY.containing_type = _STATISTICS
_STATISTICS_BYADDRESSENTRY.containing_type = _STATISTICS
_STATISTICS_BYHOSTENTRY.containing_type = _STATISTICS
_STATISTICS_BYPORTENTRY.containing_type = _STATISTICS
_STATISTICS_BYUIDENTRY.containing_type = _STATISTICS
_STATISTICS_BYEXECUTABLEENTRY.containing_type = _STATISTICS
_STATISTICS.fields_by_name['by_proto'].message_type = _STATISTICS_BYPROTOENTRY
_STATISTICS.fields_by_name['by_address'].message_type = _STATISTICS_BYADDRESSENTRY
_STATISTICS.fields_by_name['by_host'].message_type = _STATISTICS_BYHOSTENTRY
_STATISTICS.fields_by_name['by_port'].message_type = _STATISTICS_BYPORTENTRY
_STATISTICS.fields_by_name['by_uid'].message_type = _STATISTICS_BYUIDENTRY
_STATISTICS.fields_by_name['by_executable'].message_type = _STATISTICS_BYEXECUTABLEENTRY
_PINGREQUEST.fields_by_name['stats'].message_type = _STATISTICS
_RULEREPLY.fields_by_name['operator'].message_type = _RULEOPERATOR
DESCRIPTOR.message_types_by_name['Statistics'] = _STATISTICS
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
DESCRIPTOR.message_types_by_name['RuleRequest'] = _RULEREQUEST
DESCRIPTOR.message_types_by_name['RuleOperator'] = _RULEOPERATOR
DESCRIPTOR.message_types_by_name['RuleReply'] = _RULEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Statistics = _reflection.GeneratedProtocolMessageType('Statistics', (_message.Message,), dict(

  ByProtoEntry = _reflection.GeneratedProtocolMessageType('ByProtoEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYPROTOENTRY,
    __module__ = 'ui_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Statistics.ByProtoEntry)
    ))
  ,

  ByAddressEntry = _reflection.GeneratedProtocolMessageType('ByAddressEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYADDRESSENTRY,
    __module__ = 'ui_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Statistics.ByAddressEntry)
    ))
  ,

  ByHostEntry = _reflection.GeneratedProtocolMessageType('ByHostEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYHOSTENTRY,
    __module__ = 'ui_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Statistics.ByHostEntry)
    ))
  ,

  ByPortEntry = _reflection.GeneratedProtocolMessageType('ByPortEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYPORTENTRY,
    __module__ = 'ui_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Statistics.ByPortEntry)
    ))
  ,

  ByUidEntry = _reflection.GeneratedProtocolMessageType('ByUidEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYUIDENTRY,
    __module__ = 'ui_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Statistics.ByUidEntry)
    ))
  ,

  ByExecutableEntry = _reflection.GeneratedProtocolMessageType('ByExecutableEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATISTICS_BYEXECUTABLEENTRY,
    __module__ = 'ui_pb2'
    # @@protoc_insertion_point(class_scope:protocol.Statistics.ByExecutableEntry)
    ))
  ,
  DESCRIPTOR = _STATISTICS,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Statistics)
  ))
_sym_db.RegisterMessage(Statistics)
_sym_db.RegisterMessage(Statistics.ByProtoEntry)
_sym_db.RegisterMessage(Statistics.ByAddressEntry)
_sym_db.RegisterMessage(Statistics.ByHostEntry)
_sym_db.RegisterMessage(Statistics.ByPortEntry)
_sym_db.RegisterMessage(Statistics.ByUidEntry)
_sym_db.RegisterMessage(Statistics.ByExecutableEntry)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), dict(
  DESCRIPTOR = _PINGREPLY,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:protocol.PingReply)
  ))
_sym_db.RegisterMessage(PingReply)

RuleRequest = _reflection.GeneratedProtocolMessageType('RuleRequest', (_message.Message,), dict(
  DESCRIPTOR = _RULEREQUEST,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:protocol.RuleRequest)
  ))
_sym_db.RegisterMessage(RuleRequest)

RuleOperator = _reflection.GeneratedProtocolMessageType('RuleOperator', (_message.Message,), dict(
  DESCRIPTOR = _RULEOPERATOR,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:protocol.RuleOperator)
  ))
_sym_db.RegisterMessage(RuleOperator)

RuleReply = _reflection.GeneratedProtocolMessageType('RuleReply', (_message.Message,), dict(
  DESCRIPTOR = _RULEREPLY,
  __module__ = 'ui_pb2'
  # @@protoc_insertion_point(class_scope:protocol.RuleReply)
  ))
_sym_db.RegisterMessage(RuleReply)


_STATISTICS_BYPROTOENTRY.has_options = True
_STATISTICS_BYPROTOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_STATISTICS_BYADDRESSENTRY.has_options = True
_STATISTICS_BYADDRESSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_STATISTICS_BYHOSTENTRY.has_options = True
_STATISTICS_BYHOSTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_STATISTICS_BYPORTENTRY.has_options = True
_STATISTICS_BYPORTENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_STATISTICS_BYUIDENTRY.has_options = True
_STATISTICS_BYUIDENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_STATISTICS_BYEXECUTABLEENTRY.has_options = True
_STATISTICS_BYEXECUTABLEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_UI = _descriptor.ServiceDescriptor(
  name='UI',
  full_name='protocol.UI',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1282,
  serialized_end=1397,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='protocol.UI.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AskRule',
    full_name='protocol.UI.AskRule',
    index=1,
    containing_service=None,
    input_type=_RULEREQUEST,
    output_type=_RULEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UI)

DESCRIPTOR.services_by_name['UI'] = _UI

# @@protoc_insertion_point(module_scope)
