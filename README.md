# deploy
* serverless deploy --aws-profile {aws-profile} --aws-region {aws-region} --stage dev --region {region}

# deploy function
* serverless deploy function -f {function-name} --aws-profile {aws-profile} --aws-region {aws-region} --stage dev --region {region}

# deploy config changes
* serverless deploy function -f {function-name} --update-config --aws-profile {aws-profile} --aws-region {aws-region} --stage dev --region {region}

# remove
* serverless remove --aws-profile {aws-profile} --aws-region {aws-region} --stage dev --region {region}

# debug offline
* serverless offline
