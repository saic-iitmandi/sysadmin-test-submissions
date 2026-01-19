import subprocess

# Define Docker image IDs (replace these with your actual image IDs)
image_ids = ["your_image_id_1", "your_image_id_2"]

# Docker Hub username and password (replace with your credentials)
docker_username = "your_docker_username"
docker_password = "your_docker_password"

# Log in to Docker Hub
login_command = f"docker login -u {docker_username} -p {docker_password}"
subprocess.run(login_command, shell=True)

# Iterate over image IDs and deploy each image
for image_id in image_ids:
    # Pull the Docker image
    pull_command = f"docker pull {image_id}"
    subprocess.run(pull_command, shell=True)

    # Run or deploy your application with the new image
    # Example: run_command = f"docker run -d -p 8080:80 {image_id}"

# Log out from Docker Hub
logout_command = "docker logout"
subprocess.run(logout_command, shell=True)
