FROM ruby:2.3.1-alpine
WORKDIR /app

RUN apk --no-cache add \
    build-base \
    libcurl \
    curl-dev \
    nodejs \
    postgresql-dev \
    tzdata

RUN gem install bundler -v '1.17.3'
COPY Gemfile Gemfile.lock /app/

RUN bundle install

COPY . /app

EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]

