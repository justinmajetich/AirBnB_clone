#!/usr/bin/env bash
find . -type f -name "*.py" -exec sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' {} \;
