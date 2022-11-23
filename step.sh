#!/bin/bash
set -e

#!/bin/bash

THIS_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo '$' "python "$THIS_SCRIPT_DIR/step.py""
python3 "$THIS_SCRIPT_DIR/step.py"
