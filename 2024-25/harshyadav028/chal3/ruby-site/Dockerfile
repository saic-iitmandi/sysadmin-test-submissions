# Use the official Ruby image with a compatible version
# Use the official Ruby image with a compatible version
FROM ruby:2.7

# Install dependencies
RUN apt-get update -qq && apt-get install -y \
    build-essential \
    libpq-dev \
    nodejs \
    yarn \
    sqlite3

# Set the working directory in the container
WORKDIR /app

# Copy the Gemfile and Gemfile.lock
COPY Gemfile Gemfile.lock ./

# Install Bundler version 1.16.0
RUN gem install bundler -v 1.16.0

# Install the necessary gems
RUN bundle install

# Copy the entire application code
COPY . .

# Expose port 3000 for the Rails app
EXPOSE 3000

# Set the entrypoint to run the Rails server
CMD ["rails", "server", "-b", "0.0.0.0"]
