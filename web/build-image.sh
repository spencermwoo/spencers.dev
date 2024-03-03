#!/bin/bash

set -o errexit

readonly BUILD_DATE="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
readonly BUILD_VCS_REF="$(git rev-parse --verify HEAD)"
readonly DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

readonly VERSION=$(cat "${DIR}"/VERSION.txt)

readonly OWNER="starfoxxy"
readonly IMAGE_NAME="spencers.dev"
readonly IMAGE_PREFIX="${IMAGE_PREFIX:-${OWNER}}"
readonly IMAGE_TAG="${IMAGE_TAG:-"${VERSION}"}"

main() {
  build_image "$@"
}

build_image() {
  local image=$IMAGE_PREFIX/$IMAGE_NAME:$IMAGE_TAG

  echo -e "\nBuilding image: $image"

  echo -e "\nDocker build args:
    --build-arg BUILD_DATE=\"${BUILD_DATE}\"
    --build-arg BUILD_VCS_REF=\"${BUILD_VCS_REF}\"
    --build-arg BUILD_VERSION=\"${IMAGE_TAG}\"\n"

  docker build \
    --build-arg BUILD_DATE="${BUILD_DATE}" \
    --build-arg BUILD_VCS_REF="${BUILD_VCS_REF}" \
    --build-arg BUILD_VERSION="$IMAGE_TAG" \
    --tag "${image}" \
    --tag "${IMAGE_PREFIX}/${IMAGE_NAME}:local" \
    "$DIR" \
    "$@"

  echo -e "\nSuccessfully built $image"
}

main "$@"

# docker run -p 8080:8080 starfoxxy/spencers.dev:local
# docker push starfoxxy/spencers.dev:3.1.2