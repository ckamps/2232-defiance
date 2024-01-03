provider "aws" {
  region  = "us-east-1"
  profile = var.profile
}

provider "aws" {
  alias   = "us-east-1"
  region  = "us-east-1"
  profile = var.profile
}

#data "aws_caller_identity" "self" {
#  provider = aws
#}

module "static_site_domain_com" {
  source = "github.com/loganmarchione/terraform-aws-static-site?ref=0.1.6"

  providers = {
    aws.us-east-1 = aws.us-east-1
  }

  domain_name = "defiancehome.com"

  # Since this is a static site, we probably don't need versioning, since our source files are stored in git
  bucket_versioning_logs = false
  bucket_versioning_site = false

  cloudfront_compress                     = true
  cloudfront_default_root_object          = "index.html"
  cloudfront_enabled                      = true
  cloudfront_function_create              = true
  cloudfront_function_filename            = "function.js"
  cloudfront_function_name                = "ReWrites"
  cloudfront_http_version                 = "http2and3"
  cloudfront_ipv6                         = true
  cloudfront_price_class                  = "PriceClass_100"
  cloudfront_ssl_minimum_protocol_version = "TLSv1.2_2021"
  cloudfront_ttl_min                      = 3600
  cloudfront_ttl_default                  = 86400
  cloudfront_ttl_max                      = 31536000
  cloudfront_viewer_protocol_policy       = "redirect-to-https"

  iam_policy_site_updating = false

  upload_index  = false
  upload_robots = false
  upload_404    = false
}