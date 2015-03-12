#!/bin/bash

# change this to be right for your own setup
CS_DIR=/home/user/bin/counting_sequences

BIN_DIR=$CS_DIR/bin
LIB_DIR=$CS_DIR/lib

if [ "$LOGNAME" != "pvh" -a "$CS_DIR" == "/home/user/bin/counting_sequences" ] ; then
  echo "Please change the CS_DIR variable setting so that it is correct for your own setup" >&2
else
  if [[ ":$PATH:" != *":$BIN_DIR:"* ]] ; then
    PATH=$PATH:$BIN_DIR
    export PATH
  fi

  if [ -z "$PYTHONPATH" ] ; then
    PYTHONPATH=$LIB_DIR
  elif [[ ":$PYTHONPATH:" != *":$LIB_DIR:"* ]] ; then
    PYTHONPATH=$PYTHONPATH:$LIB_DIR
  fi
  export PYTHONPATH
fi
