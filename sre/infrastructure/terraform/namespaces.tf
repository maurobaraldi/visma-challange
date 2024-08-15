resource "kubernetes_namespace" "visma-assessment" {
  metadata {
    labels = {
      environment = "stagging",
      region      = "local"
    }

    name = "visma"
  }
}