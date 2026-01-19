#!/bin/bash
source="pathtothevolumedata"
location="pathtobackuplocation"
cd "$source"
zip -r "$location/backup.zip"