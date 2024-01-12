# Get the current date in the required format
$dateSuffix = Get-Date -Format "yyyyMMdd"

# Set the source and destination paths for SAIC IIT Mandi
$saicSourcePath = "C:\Users\Dell\Desktop\SAIC-Website"  # Update this path to the actual path of SAIC-Website
$saicDestinationPath = "C:\Users\Dell\Desktop\Backup"

# Set the source and destination paths for GitHub Languages
$githubSourcePath = "C:\Users\Dell\Desktop\github-languages"  # Update this path to the actual path of github-languages
$githubDestinationPath = "C:\Users\Dell\Desktop\Backup"

# Create a zip file with the current date suffix for SAIC IIT Mandi
$saicZipFileName = "saic-iit-mandi-$dateSuffix.zip"
$saicZipFilePath = Join-Path -Path $saicDestinationPath -ChildPath $saicZipFileName

# Create a zip file with the current date suffix for GitHub Languages
$githubZipFileName = "github-languages-$dateSuffix.zip"
$githubZipFilePath = Join-Path -Path $githubDestinationPath -ChildPath $githubZipFileName

# Compress the source folders to zip files
Compress-Archive -Path $saicSourcePath -DestinationPath $saicZipFilePath
Compress-Archive -Path $githubSourcePath -DestinationPath $githubZipFilePath

Write-Host "Backup completed for SAIC IIT Mandi: $saicZipFilePath"
Write-Host "Backup completed for GitHub Languages: $githubZipFilePath"
