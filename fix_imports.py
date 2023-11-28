# These two find+sed commands prepend "espnet_streaming_decoder" to imports of modules in either espnet or espnet2.
# While all files in this repository are already patched this way, this could be very useful if you are updating files from espnet.

import os
import re

ROOT_DIR = 'espnet_streaming_decoder'

def process_file(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    # Replace import statements with espnet_streaming_decoder prefix
    contents = re.sub(r'from (espnet(\.[^\s]+)*)', r'from espnet_streaming_decoder.\1', contents)
    contents = re.sub(r'import (espnet(\.[^\s]+)*)', r'import espnet_streaming_decoder.\1', contents)
    contents = re.sub(r'from (espnet2(\.[^\s]+)*)', r'from espnet_streaming_decoder.\1', contents)
    contents = re.sub(r'import (espnet2(\.[^\s]+)*)', r'import espnet_streaming_decoder.\1', contents)

    with open(file_path, 'w') as f:
        f.write(contents)

def process_directory(directory_path):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                process_file(file_path)

if __name__ == '__main__':
    process_directory(ROOT_DIR)
