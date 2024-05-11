# 2232-defiance

## IaC via Terraform

https://loganmarchione.com/2023/11/deploying-hugo-with-cloudfront-and-s3-for-real-this-time/

```
$ cd infra

$ terraform init

$ terraform apply
```

## Hinode Hugo Theme

https://myrthos.net/blog/modifications/


## Publishing Hugo-based content

### Automate via GitHub Actions

See `.github/workflows/`

https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/

### Manual from dev client

```
$ hugo
```
Followed by either:

$ hugo deploy
```
Or:

```
% aws s3 cp public/ s3://defiancehome-com --recursive --profile kampmeier-infra

% aws cloudfront create-invalidation --distribution-id E27WOJ1ENY5GKJ --paths "/*" --profile kampmeier-infra

```
## River data

https://waterdata.usgs.gov/nwis/dv?cb_00065=on&format=rdb&site_no=06935450&legacy=&referred_module=sw&period=&begin_date=2008-09-04&end_date=2024-05-04


curl "https://waterdata.usgs.gov/nwis/dv?cb_00065=on&format=rdb&site_no=06935450&legacy=&referred_module=sw&period=&begin_date=2008-09-04&end_date=2024-05-04" -o out.rdb

