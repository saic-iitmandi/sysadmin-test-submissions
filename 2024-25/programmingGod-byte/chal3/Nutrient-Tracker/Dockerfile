FROM ruby:2.7-alpine

ENV RAILS_ENV=development
ENV RACK_ENV=development

RUN apk update && apk add --no-cache \
  build-base \
  nodejs \
  sqlite-dev \
  tzdata \
  yarn

RUN gem install bundler -v 1.16.0

WORKDIR /app

COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY . .

RUN chmod +x bin/*

RUN bundle exec rake assets:precompile
RUN bundle update devise

EXPOSE 3000


CMD ["sh", "-c", "bundle exec rails db:migrate RAILS_ENV=development && bundle exec puma -C config/puma.rb"]
