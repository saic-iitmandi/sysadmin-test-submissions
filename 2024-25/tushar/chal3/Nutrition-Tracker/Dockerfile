# Use official Ruby image from the Docker Hub
FROM ruby:3.0

# Install dependencies
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

# Set up the working directory
WORKDIR /app

# Install bundler
RUN gem install bundler

# Copy the Gemfile and Gemfile.lock into the container
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock

# Install Ruby dependencies (gems)
RUN bundle install

# Copy the rest of the application code into the container
COPY . /app

# Expose the port the app will run on
EXPOSE 3000

# Run the Rails server when the container starts
CMD ["rails", "server", "-b", "0.0.0.0"]
