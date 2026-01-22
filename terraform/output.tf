output "alb_dns" {

  value = module.alb.alb_dns_name

}

output "ecr_repository_url" {
  value       = module.ecr.repository_url
  description = "ECR repository URL"
}