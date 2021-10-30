#!/bin/bash
if [[ "$(uname -s)" == "Linux" ]]; then
  sudo apt install -y python3 python3-tk
else # MacOS
  brew install python3 python-tk
fi
pip3 install requests
