
Was able to do the SAIC website but not the ROR app

When attempting the ROR app i ran into many issues regarding the version of ruby.
using ruby:2.3.1 as the base image does not let me run `apt-get update` as ubuntu jessie is no longer supported resulting in 404 errora
Meanwhile trying the later version of ruby after updating it on the gemfile caused many issues in the bundling process.

I will be including the dockerfile for SAIC website and the latest attempt at a dockerfile for github-languages
