#!/bin/bash

cat config.json.cluster > config.json
sparse submit -o supervisor.worker.timeout.secs=3600 -o topology.tick.tuple.freq.secs=1 -w=2
