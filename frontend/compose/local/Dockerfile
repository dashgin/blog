ARG NODE_VERSION=16-alpine3.11
ARG REACT_APP_BACKEND_URL=http://127.0.0.0:8000

FROM node:${NODE_VERSION}

WORKDIR /app/frontend

COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn install

COPY ./frontend/compose/local/start /start
RUN chmod +x /start

COPY frontend .
# COPY .env /app/.env
# RUN npm start

