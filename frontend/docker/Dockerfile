# pull official base image
FROM node:21-alpine3.18

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY yarn.lock ./
RUN yarn install --frozen-lockfile

# start app
CMD ["yarn", "start"]
