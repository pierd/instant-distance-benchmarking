#!/bin/zsh

set -e

# sanity check
if [ -e builds/instant_distance.so.$1 ]; then
    echo "$1 already exists!"
    exit 1
fi


pushd ../instant-distance
RUSTFLAGS="-C target-cpu=native" cargo build --release
popd

mkdir -p builds
if [ -f ../instant-distance/target/release/libinstant_distance.so ]; then
    cp ../instant-distance/target/release/libinstant_distance.so builds/instant_distance.so.$1
elif [ -f ../instant-distance/target/release/libinstant_distance_py.so ]; then
    cp ../instant-distance/target/release/libinstant_distance_py.so builds/instant_distance.so.$1
fi
