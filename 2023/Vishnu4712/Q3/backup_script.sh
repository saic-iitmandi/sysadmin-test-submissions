#!/bin/bash


docker run --rm -v html_css_js_website_data:/data -v $(pwd)/backups:/backup alpine \
  tar czvf /backup/html_css_js_website_backup_$(date +"%Y%m%d%H%M%S").tar.gz -C /data .


docker run --rm -v ruby_on_rails_website_data:/data -v $(pwd)/backups:/backup alpine \
  tar czvf /backup/ruby_on_rails_website_backup_$(date +"%Y%m%d%H%M%S").tar.gz -C /data .

