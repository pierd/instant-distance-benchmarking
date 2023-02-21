#!/bin/zsh

BENCH=$1
shift

function bench() {
    echo $1
    ln -f -s builds/instant_distance.so.$1 instant_distance.so
    PYTHONPATH=instant_distance.so ${BENCH}
}

if [ -z "$1" ]; then
    # no builds selected - run all
    for b in builds/*; do
        name=$(basename $b | cut -d. -f3)
        bench $name
    done
else
    # builds selected - run them
    while [ -n "$1" ]; do
        bench $1
        shift
    done
fi
