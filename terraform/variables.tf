variable "bucket_name" {
  description = "Description of the input variable"
  type = string  
  default = "mmaeffert-s3"  
  nullable = false
}

variable "force_destroy" {}
variable "access_key" {}
variable "secret_key" {}

