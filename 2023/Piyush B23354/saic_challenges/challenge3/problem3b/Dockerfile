
FROM ruby:2.3.1

WORKDIR /app

RUN gem install bundler -v '1.12.5'

COPY ./github-languages/Gemfile /app/Gemfile
COPY ./github-languages/Gemfile.lock /app/Gemfile.lock

RUN bundle install

COPY ./github-languages /app

EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]
