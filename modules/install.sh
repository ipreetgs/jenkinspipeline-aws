#!/bin/bash

set -e

eval $(ssh-agent)
pip3 install boto3