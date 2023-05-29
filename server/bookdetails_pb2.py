# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookdetails.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bookdetails.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x62ookdetails.proto\"@\n\x0f\x42ookDetailsData\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06quotes\x18\x03 \x01(\t\"!\n\x0f\x41uthorsListData\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\"$\n\x12\x42ookDetailsRequest\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\"\x14\n\x12\x41uthorsListRequest\"<\n\x13\x42ookDetailsResponse\x12%\n\x0b\x62ookDetails\x18\x01 \x03(\x0b\x32\x10.BookDetailsData\"<\n\x13\x41uthorsListResponse\x12%\n\x0b\x61uthorsList\x18\x01 \x03(\x0b\x32\x10.AuthorsListData2\x87\x01\n\x0b\x42ookDetails\x12;\n\x0eGetBookDetails\x12\x13.BookDetailsRequest\x1a\x14.BookDetailsResponse\x12;\n\x0eGetAuthorsList\x12\x13.AuthorsListRequest\x1a\x14.AuthorsListResponseb\x06proto3'
)




_BOOKDETAILSDATA = _descriptor.Descriptor(
  name='BookDetailsData',
  full_name='BookDetailsData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='BookDetailsData.author', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='BookDetailsData.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quotes', full_name='BookDetailsData.quotes', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=21,
  serialized_end=85,
)


_AUTHORSLISTDATA = _descriptor.Descriptor(
  name='AuthorsListData',
  full_name='AuthorsListData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='AuthorsListData.author', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=87,
  serialized_end=120,
)


_BOOKDETAILSREQUEST = _descriptor.Descriptor(
  name='BookDetailsRequest',
  full_name='BookDetailsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='BookDetailsRequest.author', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=122,
  serialized_end=158,
)


_AUTHORSLISTREQUEST = _descriptor.Descriptor(
  name='AuthorsListRequest',
  full_name='AuthorsListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=160,
  serialized_end=180,
)


_BOOKDETAILSRESPONSE = _descriptor.Descriptor(
  name='BookDetailsResponse',
  full_name='BookDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookDetails', full_name='BookDetailsResponse.bookDetails', index=0,
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
  serialized_start=182,
  serialized_end=242,
)


_AUTHORSLISTRESPONSE = _descriptor.Descriptor(
  name='AuthorsListResponse',
  full_name='AuthorsListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='authorsList', full_name='AuthorsListResponse.authorsList', index=0,
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
  serialized_start=244,
  serialized_end=304,
)

_BOOKDETAILSRESPONSE.fields_by_name['bookDetails'].message_type = _BOOKDETAILSDATA
_AUTHORSLISTRESPONSE.fields_by_name['authorsList'].message_type = _AUTHORSLISTDATA
DESCRIPTOR.message_types_by_name['BookDetailsData'] = _BOOKDETAILSDATA
DESCRIPTOR.message_types_by_name['AuthorsListData'] = _AUTHORSLISTDATA
DESCRIPTOR.message_types_by_name['BookDetailsRequest'] = _BOOKDETAILSREQUEST
DESCRIPTOR.message_types_by_name['AuthorsListRequest'] = _AUTHORSLISTREQUEST
DESCRIPTOR.message_types_by_name['BookDetailsResponse'] = _BOOKDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['AuthorsListResponse'] = _AUTHORSLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BookDetailsData = _reflection.GeneratedProtocolMessageType('BookDetailsData', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDETAILSDATA,
  '__module__' : 'bookdetails_pb2'
  # @@protoc_insertion_point(class_scope:BookDetailsData)
  })
_sym_db.RegisterMessage(BookDetailsData)

AuthorsListData = _reflection.GeneratedProtocolMessageType('AuthorsListData', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORSLISTDATA,
  '__module__' : 'bookdetails_pb2'
  # @@protoc_insertion_point(class_scope:AuthorsListData)
  })
_sym_db.RegisterMessage(AuthorsListData)

BookDetailsRequest = _reflection.GeneratedProtocolMessageType('BookDetailsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDETAILSREQUEST,
  '__module__' : 'bookdetails_pb2'
  # @@protoc_insertion_point(class_scope:BookDetailsRequest)
  })
_sym_db.RegisterMessage(BookDetailsRequest)

AuthorsListRequest = _reflection.GeneratedProtocolMessageType('AuthorsListRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORSLISTREQUEST,
  '__module__' : 'bookdetails_pb2'
  # @@protoc_insertion_point(class_scope:AuthorsListRequest)
  })
_sym_db.RegisterMessage(AuthorsListRequest)

BookDetailsResponse = _reflection.GeneratedProtocolMessageType('BookDetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDETAILSRESPONSE,
  '__module__' : 'bookdetails_pb2'
  # @@protoc_insertion_point(class_scope:BookDetailsResponse)
  })
_sym_db.RegisterMessage(BookDetailsResponse)

AuthorsListResponse = _reflection.GeneratedProtocolMessageType('AuthorsListResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORSLISTRESPONSE,
  '__module__' : 'bookdetails_pb2'
  # @@protoc_insertion_point(class_scope:AuthorsListResponse)
  })
_sym_db.RegisterMessage(AuthorsListResponse)



_BOOKDETAILS = _descriptor.ServiceDescriptor(
  name='BookDetails',
  full_name='BookDetails',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=307,
  serialized_end=442,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBookDetails',
    full_name='BookDetails.GetBookDetails',
    index=0,
    containing_service=None,
    input_type=_BOOKDETAILSREQUEST,
    output_type=_BOOKDETAILSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAuthorsList',
    full_name='BookDetails.GetAuthorsList',
    index=1,
    containing_service=None,
    input_type=_AUTHORSLISTREQUEST,
    output_type=_AUTHORSLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKDETAILS)

DESCRIPTOR.services_by_name['BookDetails'] = _BOOKDETAILS

# @@protoc_insertion_point(module_scope)