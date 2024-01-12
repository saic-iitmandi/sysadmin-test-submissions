#!/bin/bash

perform_backup() {
    backup_folder="./backups"
    mkdir -p "$backup_folder"

    docker container cp name_of_the_firstConatiner:/path/to/mapped/data "$backup_folder/html_css_js_$(date '+%Y-%m-%d').zip"

    docker container cp name_of_the_secondContainer:/path/to/mapped/data "$backup_folder/ruby_on_rails_$(date '+%Y-%m-%d').zip"
}
