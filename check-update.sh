#!/bin/sh
curl -s -L 'https://www.libraw.org/download' |grep -E 'LibRaw-[0-9\.]*'\.tar |sed -e 's,.*data/,,;s,>.*,,;s,LibRaw-,,;s,\.tar.*,,' |sort -V |tail -n1
