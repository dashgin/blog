ARG VERSION=16-alpine3.11

FROM node:${VERSION} as builder

ARG REACT_APP_BACKEND_URL

WORKDIR /app

COPY . /app/
RUN yarn install --check-files \
 && yarn build


FROM node:${VERSION} as final

WORKDIR /app
COPY --from=builder /app/build /app

RUN yarn global add serve