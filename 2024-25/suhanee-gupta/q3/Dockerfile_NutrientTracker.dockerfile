#project uses ruby
FROM ruby:3.2

WORKDIR /app

RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

#gemfiles copy
COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY . .

RUN bundle exec rails assets:precompile

#port
EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]