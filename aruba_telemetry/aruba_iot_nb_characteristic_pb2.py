# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruba-iot-nb-characteristic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!aruba-iot-nb-characteristic.proto\x12\x0f\x61ruba_telemetry\"\xab\x01\n\x0e\x43haracteristic\x12\x11\n\tdeviceMac\x18\x01 \x01(\x0c\x12\x13\n\x0bserviceUuid\x18\x02 \x01(\x0c\x12\x1a\n\x12\x63haracteristicUuid\x18\x03 \x01(\x0c\x12\r\n\x05value\x18\x04 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x31\n\nproperties\x18\x06 \x03(\x0e\x32\x1d.aruba_telemetry.CharProperty*\xa4\x01\n\x0c\x43harProperty\x12\r\n\tbroadcast\x10\x00\x12\x08\n\x04read\x10\x01\x12\x18\n\x14writeWithoutResponse\x10\x02\x12\x15\n\x11writeWithResponse\x10\x03\x12\n\n\x06notify\x10\x04\x12\x0c\n\x08indicate\x10\x05\x12\x0f\n\x0bsignedWrite\x10\x06\x12\x11\n\rwriteReliable\x10\x07\x12\x0c\n\x08writeAux\x10\x08')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruba_iot_nb_characteristic_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHARPROPERTY']._serialized_start=229
  _globals['_CHARPROPERTY']._serialized_end=393
  _globals['_CHARACTERISTIC']._serialized_start=55
  _globals['_CHARACTERISTIC']._serialized_end=226
# @@protoc_insertion_point(module_scope)
