#!/usr/bin/env sh

set -e

USERNAME="securevote"
DBNAME="securevote"
echo "Creating user '$USERNAME' ..."
createuser -d $USERNAME
echo "Creating database '$DBNAME' ..."
createdb -O $USERNAME $DBNAME
