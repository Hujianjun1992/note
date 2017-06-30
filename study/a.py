#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

i_format = struct.Struct('4B')

# middle_str = i_format.pack(0, 0, 144, 64)
# middle_str = i_format.pack(191, 76, 87, 19)
middle_str = i_format.pack(19, 87, 76, 191)

f_format = struct.Struct('f')

value = f_format.unpack(middle_str)

print value[0]

