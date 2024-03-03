FROM node:21-alpine
WORKDIR /usr/src/app

COPY . /usr/src/app
COPY package*.json ./

RUN npm i

EXPOSE 8080

CMD ["npm", "run", "serve"]

ARG BUILD_DATE
ARG BUILD_VCS_REF
ARG BUILD_VERSION

ENV BUILD_DATE ${BUILD_DATE}
ENV BUILD_VCS_REF ${BUILD_VCS_REF}
ENV BUILD_VERSION ${BUILD_VERSION}

LABEL contact="me@spencers.dev"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.name="starfoxxy/spencers.dev"
LABEL org.label-schema.vcs-url="https://github.com/spencermwoo/spencers.dev"
LABEL org.label-schema.vcs-ref=$BUILD_VCS_REF
LABEL org.label-schema.version=$BUILD_VERSION