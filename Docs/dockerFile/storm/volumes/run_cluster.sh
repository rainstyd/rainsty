#!/bin/bash

cat config.json.cluster > config.json
sparse submit -n wordcount -o supervisor.worker.timeout.secs=600 -o topology.tick.tuple.freq.secs=600