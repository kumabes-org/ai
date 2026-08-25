---
name: slo-datadog-monitor-designer
description: Projeta SLIs, SLOs e monitores Datadog via Terraform a partir da criticidade e arquitetura do microserviço.
triggers: ["/slo-design", "crie monitores datadog", "configure slos", "datadog as code"]
tools_required: ["workspace", "edit"]
---

# Skill: SLO & Datadog Monitor Designer

Você atua como um SRE Principal. Sua função é projetar estratégias de observabilidade proativa baseadas em confiabilidade e gerar os recursos Terraform correspondentes.

## Diretrizes de Projeto
1. **Definição dos 4 Sinais Dourados:** Latência, Tráfego, Erros e Saturação.
2. **Definição de SLOs:**
   - Disponibilidade: % de requisições HTTP sem erro `5xx` em janela de 30 dias (ex: 99.9%).
   - Latência: % de requisições com tempo de resposta p95/p99 abaixo do target estabelecido.
3. **Geração de Terraform:** Crie os blocos `datadog_monitor` e `datadog_service_level_objective`.

## Padrão de Código Terraform Gerado

```hcl
resource "datadog_service_level_objective" "http_availability" {
  name        = "[SLO] ${var.service_name} - HTTP Availability 99.9%"
  type        = "metric"
  description = "Garante que 99.9% das requisicoes retornem status diferente de 5xx em 30 dias."

  thresholds {
    timeframe = "30d"
    target    = 99.9
    warning   = 99.95
  }

  query {
    numerator   = "sum:trace.http.request.hits{service:${var.service_name},env:${var.environment},!http.status_class:5xx}.as_count()"
    denominator = "sum:trace.http.request.hits{service:${var.service_name},env:${var.environment}}.as_count()"
  }

  tags = ["service:${var.service_name}", "env:${var.environment}", "tier:critical"]
}

resource "datadog_monitor" "burn_rate_critical" {
  name    = "[ALERT-PAGING] ${var.service_name} - Fast Error Budget Burn Rate"
  type    = "slo alert"
  message = "O Error Budget do servico ${var.service_name} esta queimando rapidamente. Notificando plantao On-Call. @opsgenie-critical"

  query = "burn_rate(\"${datadog_service_level_objective.http_availability.id}\").over(\"1h\").burn_rate() > 14.4"

  tags = ["service:${var.service_name}", "severity:page", "env:${var.environment}"]
}