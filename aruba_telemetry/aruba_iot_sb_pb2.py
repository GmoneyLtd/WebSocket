# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-sb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aruba_iot_types_pb2
import aruba_iot_sb_action_pb2
import aruba_iot_sb_config_pb2
import aruba_iot_sb_status_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aruba-iot-sb.proto',
  package='aruba_telemetry',
  serialized_pb=_b('\n\x12\x61ruba-iot-sb.proto\x12\x0f\x61ruba_telemetry\x1a\x15\x61ruba-iot-types.proto\x1a\x19\x61ruba-iot-sb-action.proto\x1a\x19\x61ruba-iot-sb-config.proto\x1a\x19\x61ruba-iot-sb-status.proto\"&\n\x08Receiver\x12\x0b\n\x03\x61ll\x18\x01 \x01(\x08\x12\r\n\x05\x61pMac\x18\x02 \x01(\x0c\"\xec\x01\n\x0cIotSbMessage\x12#\n\x04meta\x18\x01 \x02(\x0b\x32\x15.aruba_telemetry.Meta\x12+\n\x08receiver\x18\x02 \x01(\x0b\x32\x19.aruba_telemetry.Receiver\x12(\n\x07\x61\x63tions\x18\x03 \x03(\x0b\x32\x17.aruba_telemetry.Action\x12\x30\n\x06\x63onfig\x18\x04 \x01(\x0b\x32 .aruba_telemetry.TransportConfig\x12.\n\x06status\x18\x05 \x01(\x0b\x32\x1e.aruba_telemetry.ConnectStatus')
  ,
  dependencies=[aruba_iot_types_pb2.DESCRIPTOR,aruba_iot_sb_action_pb2.DESCRIPTOR,aruba_iot_sb_config_pb2.DESCRIPTOR,aruba_iot_sb_status_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RECEIVER = _descriptor.Descriptor(
  name='Receiver',
  full_name='aruba_telemetry.Receiver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all', full_name='aruba_telemetry.Receiver.all', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apMac', full_name='aruba_telemetry.Receiver.apMac', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=181,
)


_IOTSBMESSAGE = _descriptor.Descriptor(
  name='IotSbMessage',
  full_name='aruba_telemetry.IotSbMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='aruba_telemetry.IotSbMessage.meta', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='aruba_telemetry.IotSbMessage.receiver', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actions', full_name='aruba_telemetry.IotSbMessage.actions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config', full_name='aruba_telemetry.IotSbMessage.config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='aruba_telemetry.IotSbMessage.status', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=420,
)

_IOTSBMESSAGE.fields_by_name['meta'].message_type = aruba_iot_types_pb2._META
_IOTSBMESSAGE.fields_by_name['receiver'].message_type = _RECEIVER
_IOTSBMESSAGE.fields_by_name['actions'].message_type = aruba_iot_sb_action_pb2._ACTION
_IOTSBMESSAGE.fields_by_name['config'].message_type = aruba_iot_sb_config_pb2._TRANSPORTCONFIG
_IOTSBMESSAGE.fields_by_name['status'].message_type = aruba_iot_sb_status_pb2._CONNECTSTATUS
DESCRIPTOR.message_types_by_name['Receiver'] = _RECEIVER
DESCRIPTOR.message_types_by_name['IotSbMessage'] = _IOTSBMESSAGE

Receiver = _reflection.GeneratedProtocolMessageType('Receiver', (_message.Message,), dict(
  DESCRIPTOR = _RECEIVER,
  __module__ = 'aruba_iot_sb_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.Receiver)
  ))
_sym_db.RegisterMessage(Receiver)

IotSbMessage = _reflection.GeneratedProtocolMessageType('IotSbMessage', (_message.Message,), dict(
  DESCRIPTOR = _IOTSBMESSAGE,
  __module__ = 'aruba_iot_sb_pb2'
  # @@protoc_insertion_point(class_scope:aruba_telemetry.IotSbMessage)
  ))
_sym_db.RegisterMessage(IotSbMessage)


# @@protoc_insertion_point(module_scope)
