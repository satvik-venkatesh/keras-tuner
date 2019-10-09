# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kerastuner/protos/kerastuner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kerastuner/protos/kerastuner.proto',
  package='kerastuner',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"kerastuner/protos/kerastuner.proto\x12\nkerastuner\"l\n\x05Value\x12\x13\n\tint_value\x18\x01 \x01(\x12H\x00\x12\x15\n\x0b\x66loat_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x17\n\rboolean_value\x18\x04 \x01(\x08H\x00\x42\x06\n\x04kind\"\x82\x01\n\x05\x46loat\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x01\x12\x11\n\tmax_value\x18\x03 \x01(\x01\x12\x0c\n\x04step\x18\x04 \x01(\x01\x12&\n\x08sampling\x18\x05 \x01(\x0e\x32\x14.kerastuner.Sampling\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\x01\"\x80\x01\n\x03Int\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tmin_value\x18\x02 \x01(\x12\x12\x11\n\tmax_value\x18\x03 \x01(\x12\x12\x0c\n\x04step\x18\x04 \x01(\x12\x12&\n\x08sampling\x18\x05 \x01(\x0e\x32\x14.kerastuner.Sampling\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x06 \x01(\x12\"n\n\x06\x43hoice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x06values\x18\x02 \x03(\x0b\x32\x11.kerastuner.Value\x12\"\n\x07\x64\x65\x66\x61ult\x18\x03 \x01(\x0b\x32\x11.kerastuner.Value\x12\x0f\n\x07ordered\x18\x04 \x01(\x08\"(\n\x07\x42oolean\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x08\"\xea\x02\n\x0fHyperParameters\x12\x30\n\x05space\x18\x01 \x01(\x0b\x32!.kerastuner.HyperParameters.Space\x12\x37\n\x06values\x18\x02 \x03(\x0b\x32\'.kerastuner.HyperParameters.ValuesEntry\x1a\xa9\x01\n\x05Space\x12&\n\x0b\x66loat_space\x18\x01 \x03(\x0b\x32\x11.kerastuner.Float\x12\"\n\tint_space\x18\x02 \x03(\x0b\x32\x0f.kerastuner.Int\x12(\n\x0c\x63hoice_space\x18\x03 \x03(\x0b\x32\x12.kerastuner.Choice\x12*\n\rboolean_space\x18\x04 \x03(\x0b\x32\x13.kerastuner.Boolean\x1a@\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.kerastuner.Value:\x02\x38\x01\"0\n\x11MetricObservation\x12\r\n\x05value\x18\x01 \x03(\x02\x12\x0c\n\x04step\x18\x02 \x01(\x03\"V\n\rMetricHistory\x12\x33\n\x0cobservations\x18\x01 \x03(\x0b\x32\x1d.kerastuner.MetricObservation\x12\x10\n\x08maximize\x18\x02 \x01(\x08\"\x95\x01\n\x0eMetricsTracker\x12\x38\n\x07metrics\x18\x01 \x03(\x0b\x32\'.kerastuner.MetricsTracker.MetricsEntry\x1aI\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.kerastuner.MetricHistory:\x02\x38\x01\"\xf3\x01\n\x05Trial\x12\x34\n\x0fhyperparameters\x18\x01 \x01(\x0b\x32\x1b.kerastuner.HyperParameters\x12\x10\n\x08trial_id\x18\x02 \x01(\t\x12\'\n\x06status\x18\x03 \x01(\x0e\x32\x17.kerastuner.TrialStatus\x12+\n\x07metrics\x18\x04 \x01(\x0b\x32\x1a.kerastuner.MetricsTracker\x12&\n\x05score\x18\x05 \x01(\x0b\x32\x17.kerastuner.Trial.Score\x1a$\n\x05Score\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x0c\n\x04step\x18\x02 \x01(\x03*:\n\x08Sampling\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\x07\n\x03LOG\x10\x02\x12\x0f\n\x0bREVERSE_LOG\x10\x03*Z\n\x0bTrialStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x08\n\x04IDLE\x10\x02\x12\x0b\n\x07INVALID\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\r\n\tCOMPLETED\x10\x05\x62\x06proto3')
)

_SAMPLING = _descriptor.EnumDescriptor(
  name='Sampling',
  full_name='kerastuner.Sampling',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE_LOG', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1479,
  serialized_end=1537,
)
_sym_db.RegisterEnumDescriptor(_SAMPLING)

Sampling = enum_type_wrapper.EnumTypeWrapper(_SAMPLING)
_TRIALSTATUS = _descriptor.EnumDescriptor(
  name='TrialStatus',
  full_name='kerastuner.TrialStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1539,
  serialized_end=1629,
)
_sym_db.RegisterEnumDescriptor(_TRIALSTATUS)

TrialStatus = enum_type_wrapper.EnumTypeWrapper(_TRIALSTATUS)
NONE = 0
LINEAR = 1
LOG = 2
REVERSE_LOG = 3
UNKNOWN = 0
RUNNING = 1
IDLE = 2
INVALID = 3
STOPPED = 4
COMPLETED = 5



_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='kerastuner.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_value', full_name='kerastuner.Value.int_value', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='kerastuner.Value.float_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='kerastuner.Value.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='kerastuner.Value.boolean_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='kerastuner.Value.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=50,
  serialized_end=158,
)


_FLOAT = _descriptor.Descriptor(
  name='Float',
  full_name='kerastuner.Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Float.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='kerastuner.Float.min_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='kerastuner.Float.max_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.Float.step', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='kerastuner.Float.sampling', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Float.default', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=291,
)


_INT = _descriptor.Descriptor(
  name='Int',
  full_name='kerastuner.Int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Int.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_value', full_name='kerastuner.Int.min_value', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_value', full_name='kerastuner.Int.max_value', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.Int.step', index=3,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='kerastuner.Int.sampling', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Int.default', index=5,
      number=6, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=422,
)


_CHOICE = _descriptor.Descriptor(
  name='Choice',
  full_name='kerastuner.Choice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Choice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='kerastuner.Choice.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Choice.default', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ordered', full_name='kerastuner.Choice.ordered', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=534,
)


_BOOLEAN = _descriptor.Descriptor(
  name='Boolean',
  full_name='kerastuner.Boolean',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='kerastuner.Boolean.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default', full_name='kerastuner.Boolean.default', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=576,
)


_HYPERPARAMETERS_SPACE = _descriptor.Descriptor(
  name='Space',
  full_name='kerastuner.HyperParameters.Space',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_space', full_name='kerastuner.HyperParameters.Space.float_space', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_space', full_name='kerastuner.HyperParameters.Space.int_space', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='choice_space', full_name='kerastuner.HyperParameters.Space.choice_space', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean_space', full_name='kerastuner.HyperParameters.Space.boolean_space', index=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=706,
  serialized_end=875,
)

_HYPERPARAMETERS_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='kerastuner.HyperParameters.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.HyperParameters.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.HyperParameters.ValuesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=877,
  serialized_end=941,
)

_HYPERPARAMETERS = _descriptor.Descriptor(
  name='HyperParameters',
  full_name='kerastuner.HyperParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='space', full_name='kerastuner.HyperParameters.space', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='kerastuner.HyperParameters.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HYPERPARAMETERS_SPACE, _HYPERPARAMETERS_VALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=941,
)


_METRICOBSERVATION = _descriptor.Descriptor(
  name='MetricObservation',
  full_name='kerastuner.MetricObservation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.MetricObservation.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.MetricObservation.step', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=943,
  serialized_end=991,
)


_METRICHISTORY = _descriptor.Descriptor(
  name='MetricHistory',
  full_name='kerastuner.MetricHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observations', full_name='kerastuner.MetricHistory.observations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximize', full_name='kerastuner.MetricHistory.maximize', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1079,
)


_METRICSTRACKER_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='kerastuner.MetricsTracker.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kerastuner.MetricsTracker.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.MetricsTracker.MetricsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1158,
  serialized_end=1231,
)

_METRICSTRACKER = _descriptor.Descriptor(
  name='MetricsTracker',
  full_name='kerastuner.MetricsTracker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='kerastuner.MetricsTracker.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METRICSTRACKER_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1082,
  serialized_end=1231,
)


_TRIAL_SCORE = _descriptor.Descriptor(
  name='Score',
  full_name='kerastuner.Trial.Score',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='kerastuner.Trial.Score.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='step', full_name='kerastuner.Trial.Score.step', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1441,
  serialized_end=1477,
)

_TRIAL = _descriptor.Descriptor(
  name='Trial',
  full_name='kerastuner.Trial',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hyperparameters', full_name='kerastuner.Trial.hyperparameters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trial_id', full_name='kerastuner.Trial.trial_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='kerastuner.Trial.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='kerastuner.Trial.metrics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='kerastuner.Trial.score', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRIAL_SCORE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1234,
  serialized_end=1477,
)

_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['int_value'])
_VALUE.fields_by_name['int_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['float_value'])
_VALUE.fields_by_name['float_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['string_value'])
_VALUE.fields_by_name['string_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_VALUE.oneofs_by_name['kind'].fields.append(
  _VALUE.fields_by_name['boolean_value'])
_VALUE.fields_by_name['boolean_value'].containing_oneof = _VALUE.oneofs_by_name['kind']
_FLOAT.fields_by_name['sampling'].enum_type = _SAMPLING
_INT.fields_by_name['sampling'].enum_type = _SAMPLING
_CHOICE.fields_by_name['values'].message_type = _VALUE
_CHOICE.fields_by_name['default'].message_type = _VALUE
_HYPERPARAMETERS_SPACE.fields_by_name['float_space'].message_type = _FLOAT
_HYPERPARAMETERS_SPACE.fields_by_name['int_space'].message_type = _INT
_HYPERPARAMETERS_SPACE.fields_by_name['choice_space'].message_type = _CHOICE
_HYPERPARAMETERS_SPACE.fields_by_name['boolean_space'].message_type = _BOOLEAN
_HYPERPARAMETERS_SPACE.containing_type = _HYPERPARAMETERS
_HYPERPARAMETERS_VALUESENTRY.fields_by_name['value'].message_type = _VALUE
_HYPERPARAMETERS_VALUESENTRY.containing_type = _HYPERPARAMETERS
_HYPERPARAMETERS.fields_by_name['space'].message_type = _HYPERPARAMETERS_SPACE
_HYPERPARAMETERS.fields_by_name['values'].message_type = _HYPERPARAMETERS_VALUESENTRY
_METRICHISTORY.fields_by_name['observations'].message_type = _METRICOBSERVATION
_METRICSTRACKER_METRICSENTRY.fields_by_name['value'].message_type = _METRICHISTORY
_METRICSTRACKER_METRICSENTRY.containing_type = _METRICSTRACKER
_METRICSTRACKER.fields_by_name['metrics'].message_type = _METRICSTRACKER_METRICSENTRY
_TRIAL_SCORE.containing_type = _TRIAL
_TRIAL.fields_by_name['hyperparameters'].message_type = _HYPERPARAMETERS
_TRIAL.fields_by_name['status'].enum_type = _TRIALSTATUS
_TRIAL.fields_by_name['metrics'].message_type = _METRICSTRACKER
_TRIAL.fields_by_name['score'].message_type = _TRIAL_SCORE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Float'] = _FLOAT
DESCRIPTOR.message_types_by_name['Int'] = _INT
DESCRIPTOR.message_types_by_name['Choice'] = _CHOICE
DESCRIPTOR.message_types_by_name['Boolean'] = _BOOLEAN
DESCRIPTOR.message_types_by_name['HyperParameters'] = _HYPERPARAMETERS
DESCRIPTOR.message_types_by_name['MetricObservation'] = _METRICOBSERVATION
DESCRIPTOR.message_types_by_name['MetricHistory'] = _METRICHISTORY
DESCRIPTOR.message_types_by_name['MetricsTracker'] = _METRICSTRACKER
DESCRIPTOR.message_types_by_name['Trial'] = _TRIAL
DESCRIPTOR.enum_types_by_name['Sampling'] = _SAMPLING
DESCRIPTOR.enum_types_by_name['TrialStatus'] = _TRIALSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Value)
  })
_sym_db.RegisterMessage(Value)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Float)
  })
_sym_db.RegisterMessage(Float)

Int = _reflection.GeneratedProtocolMessageType('Int', (_message.Message,), {
  'DESCRIPTOR' : _INT,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Int)
  })
_sym_db.RegisterMessage(Int)

Choice = _reflection.GeneratedProtocolMessageType('Choice', (_message.Message,), {
  'DESCRIPTOR' : _CHOICE,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Choice)
  })
_sym_db.RegisterMessage(Choice)

Boolean = _reflection.GeneratedProtocolMessageType('Boolean', (_message.Message,), {
  'DESCRIPTOR' : _BOOLEAN,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Boolean)
  })
_sym_db.RegisterMessage(Boolean)

HyperParameters = _reflection.GeneratedProtocolMessageType('HyperParameters', (_message.Message,), {

  'Space' : _reflection.GeneratedProtocolMessageType('Space', (_message.Message,), {
    'DESCRIPTOR' : _HYPERPARAMETERS_SPACE,
    '__module__' : 'kerastuner.protos.kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters.Space)
    })
  ,

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HYPERPARAMETERS_VALUESENTRY,
    '__module__' : 'kerastuner.protos.kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _HYPERPARAMETERS,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.HyperParameters)
  })
_sym_db.RegisterMessage(HyperParameters)
_sym_db.RegisterMessage(HyperParameters.Space)
_sym_db.RegisterMessage(HyperParameters.ValuesEntry)

MetricObservation = _reflection.GeneratedProtocolMessageType('MetricObservation', (_message.Message,), {
  'DESCRIPTOR' : _METRICOBSERVATION,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.MetricObservation)
  })
_sym_db.RegisterMessage(MetricObservation)

MetricHistory = _reflection.GeneratedProtocolMessageType('MetricHistory', (_message.Message,), {
  'DESCRIPTOR' : _METRICHISTORY,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.MetricHistory)
  })
_sym_db.RegisterMessage(MetricHistory)

MetricsTracker = _reflection.GeneratedProtocolMessageType('MetricsTracker', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _METRICSTRACKER_METRICSENTRY,
    '__module__' : 'kerastuner.protos.kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.MetricsTracker.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _METRICSTRACKER,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.MetricsTracker)
  })
_sym_db.RegisterMessage(MetricsTracker)
_sym_db.RegisterMessage(MetricsTracker.MetricsEntry)

Trial = _reflection.GeneratedProtocolMessageType('Trial', (_message.Message,), {

  'Score' : _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), {
    'DESCRIPTOR' : _TRIAL_SCORE,
    '__module__' : 'kerastuner.protos.kerastuner_pb2'
    # @@protoc_insertion_point(class_scope:kerastuner.Trial.Score)
    })
  ,
  'DESCRIPTOR' : _TRIAL,
  '__module__' : 'kerastuner.protos.kerastuner_pb2'
  # @@protoc_insertion_point(class_scope:kerastuner.Trial)
  })
_sym_db.RegisterMessage(Trial)
_sym_db.RegisterMessage(Trial.Score)


_HYPERPARAMETERS_VALUESENTRY._options = None
_METRICSTRACKER_METRICSENTRY._options = None
# @@protoc_insertion_point(module_scope)
