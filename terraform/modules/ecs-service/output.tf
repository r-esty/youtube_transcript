output "ecs_service_arn" {
  value = aws_ecs_service.ecs_service.arn
}

output "ecs_task_definition_arn" {
  value = aws_ecs_task_definition.service.arn
}