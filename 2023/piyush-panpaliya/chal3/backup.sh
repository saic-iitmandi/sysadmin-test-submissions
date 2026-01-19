#!/bin/bash

tar czf backup/saic_$(date +%Y%m%d%H%M%S).tar.gz -C SAIC-Website/data .
tar czf backup/ruby_$(date +%Y%m%d%H%M%S).tar.gz  -C  github-languages/data .
