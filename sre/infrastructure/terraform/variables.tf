variable "cluster_name" {
  description = "The kind cluster name."
  default     = "economic"
  type        = string
}

variable "kind_version" {
  description = "The kind version of kubernetes."
  default     = "v1.31.0"
  type        = string
}

variable "install_ingress_nginx" {
  description = "Whether to install the nginx Helm chart"
  type        = bool
  default     = false
}