#!/bin/bash
# This script is to help increase shm size in case of crashes that may happen.

sudo mount -o remount,size=8G /dev/shm