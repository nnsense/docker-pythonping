#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tcping import Ping
import os
hostname = os.environ["WP_HOSTNAME"]
print("PING " + hostname)

ping = Ping(hostname, 80, 60)

while True:
  ping.ping()

