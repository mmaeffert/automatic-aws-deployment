### Init terraform
Make sure to execute "terraform init" inside the terraform directory

### Create config
configure your AWS environment inside the terraform/aws-credentials.tfvars file

### Create Bucket and upload
```
python main.py mmaeffert-s3-bucket example.JPG
```

### Destroy bucket
```
python destroy.py mmaeffert-s3-bucket
```