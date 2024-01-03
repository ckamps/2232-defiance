# 2232-defiance

## IaC via Terraform

https://loganmarchione.com/2023/11/deploying-hugo-with-cloudfront-and-s3-for-real-this-time/

```
$ cd infra

$ terraform init

$ terraform apply
```

## Hugo themes


## Publishing Hugo-based content

```
% aws s3 cp public/ s3://defiancehome-com --recursive --profile kampmeier-infra

% aws cloudfront create-invalidation --distribution-id E27WOJ1ENY5GKJ --paths "/*" --profile kampmeier-infra

```