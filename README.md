# mini-project-calc
## Start docker and jenkins
"sudo systemctl start docker.sock"
"sudo systemctl start jenkins"

## Setup Ngrok
Run following command
"ngrok http 8080"
After this you will get https link.

## Setup Webhook
Copy the https link, and paste it in webhook section of repository.
NOTE: The link should be copied in <your_https_link>/git-webhook/
Example https://de4d-103-156-19-229.in.ngrok.io/git-webhook.
Also add the secret text that you are using as GIT_CREDENTIAL in Jenkins.

## Jenkins Build using GitSCM or Manual
-Dont forget to manage global credentials.

