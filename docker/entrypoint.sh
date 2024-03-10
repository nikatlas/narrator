#!/bin/bash
set -euo pipefail

echo Running with environment variables:
env | sort | sed 's/^/  /'

urlencode() {
    local s="$1"
    local len=${#s}
    for (( i=0; i<len; i++ )); do
        local c=${s:i:1}
        case "$c" in
            [a-zA-Z0-9.~_-]) printf "$c" ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done
}

poetry run django-admin collectstatic --noinput --clear -v0

encoded_password=$(urlencode "$DJANGO_DB_PASSWORD")
holdup --verbose "pg://$DJANGO_DB_USER:$encoded_password@$DJANGO_DB_HOST:5432/$DJANGO_DB_NAME"
poetry run django-admin migrate --noinput --fake-initial


set -x
exec "$@"
