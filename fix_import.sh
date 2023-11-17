# These two find+sed commands prepend "espnet_streaming_decoder" to imports of modules in either espnet or espnet2.
# While all files in this repository are already patched this way, this could be very useful if you are updating files from espnet.

find /path/to/project -name "*.py" -exec sed -i 's/from \(espnet\.\)/from espnet_streaming_decoder.\1/gI; s/import \(espnet\.\)/import espnet_streaming_decoder.\1/gI' {} +
find /path/to/project -name "*.py" -exec sed -i 's/from \(espnet2\.\)/from espnet_streaming_decoder.\1/gI; s/import \(espnet2\.\)/import espnet_streaming_decoder.\1/gI' {} +
