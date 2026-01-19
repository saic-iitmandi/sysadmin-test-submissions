FROM ruby:2.3.1

WORKDIR /usr/src/app
COPY . .
COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v "1.12.5" 
RUN bundle install


EXPOSE 3000

CMD ["bundle", "exec", "puma","-C","config/puma.rb"]
