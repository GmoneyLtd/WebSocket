# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-zb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import aruba_iot_zb_types_pb2 as aruba__iot__zb__types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61ruba-iot-nb-zb.proto\x12\x0f\x61ruba_telemetry\x1a\x18\x61ruba-iot-zb-types.proto\"Q\n\nZbNbReport\x12\x0b\n\x03mac\x18\x01 \x01(\x0c\x12%\n\x04\x65\x32pc\x18\x02 \x01(\x0b\x32\x17.aruba_telemetry.ZbE2PC\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"m\n\x07ZbNbAck\x12\r\n\x05reqid\x18\x01 \x01(\t\x12)\n\x06result\x18\x02 \x01(\x0e\x32\x19.aruba_telemetry.ZbResult\x12(\n\x04\x63ode\x18\x03 \x01(\x0e\x32\x1a.aruba_telemetry.ZbAckCode\"\x18\n\x07ZbNbRsp\x12\r\n\x05reqid\x18\x01 \x01(\t\"\x9c\x01\n\x07NbZbMsg\x12\x11\n\tradio_mac\x18\x01 \x01(\x0c\x12+\n\x06report\x18\x02 \x01(\x0b\x32\x1b.aruba_telemetry.ZbNbReport\x12%\n\x03\x61\x63k\x18\x03 \x01(\x0b\x32\x18.aruba_telemetry.ZbNbAck\x12*\n\x08response\x18\x04 \x01(\x0b\x32\x18.aruba_telemetry.ZbNbRsp')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruba_iot_nb_zb_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ZBNBREPORT']._serialized_start=68
  _globals['_ZBNBREPORT']._serialized_end=149
  _globals['_ZBNBACK']._serialized_start=151
  _globals['_ZBNBACK']._serialized_end=260
  _globals['_ZBNBRSP']._serialized_start=262
  _globals['_ZBNBRSP']._serialized_end=286
  _globals['_NBZBMSG']._serialized_start=289
  _globals['_NBZBMSG']._serialized_end=445
# @@protoc_insertion_point(module_scope)
