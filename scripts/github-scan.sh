#!/usr/bin/env bash

mkdir -p knowledge/repositories

URL=$1

if [ -z "$URL" ]; then
    echo "usage:"
    echo "./scripts/github-scan.sh https://github.com/owner/repo"
    exit
fi

NAME=$(basename "$URL")

cat > knowledge/repositories/${NAME}.yaml <<EOF
name: ${NAME}
repository: ${URL}

status: pending

license: unknown

architecture: unknown

cli: unknown

plugin: unknown

memory: unknown

workflow: unknown

compare: pending
EOF

echo "registered ${NAME}"
