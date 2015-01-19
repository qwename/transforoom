# Copyright 2015 Yixin Zhang
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import zlib
import argparse
import os
from StringIO import StringIO

def decompressSWF(f):
   if type(f) is str:
      f = StringIO(f)
   f.seek(0, 0)
   magic = f.read(3)
   if magic == "CWS":
      return "FWS" + f.read(5) + zlib.decompress(f.read())
   else:
      return None

def compressSWF(f):
   if type(f) is str:
      f = StringIO(f)
   f.seek(0, 0)
   magic = f.read(3)
   if magic == "FWS":
      return "CWS" + f.read(5) + zlib.compress(f.read())
   else:
      return None

def main(arg1):
    try:
        Type = int(arg1[0])
    except:
        print "Error! Input not a number."
        os._exit(1)
    if Type==1:
        data = decompressSWF(file('In.swf', 'rb').read())
    else:
        data = compressSWF(file('In.swf', 'rb').read())
    if data:
        f=open('Out.swf', 'wb')
        f.write(data)
        f.close()
        print "Wrote %d bytes." % (len(data))
    else:
        print "An error occured when compessing/decompressing the file. Check file type?"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='SWF Compressor/Decompressor', epilog="Example usage:\nSWFCompression.py -i 1")
    parser.add_argument('-i', type=str, nargs="+", required=True, help='Type. 1=Decompress. 2=Compress.\n\nInput file must be named "In.swf"\nOutput file will be named "Out.swf"')
    args = parser.parse_args()
    arg1=args.i
    main(arg1)