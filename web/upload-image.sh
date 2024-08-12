#!/bin/bash

readonly DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly VERSION=$(cat "${DIR}"/VERSION.txt)

readonly OWNER="starfoxxy"
readonly IMAGE_NAME="spencers.dev"
readonly IMAGE_PREFIX="${IMAGE_PREFIX:-${OWNER}}"
readonly IMAGE_TAG="${IMAGE_TAG:-"${VERSION}"}"

image=$IMAGE_PREFIX/$IMAGE_NAME:$IMAGE_TAG

docker push $image