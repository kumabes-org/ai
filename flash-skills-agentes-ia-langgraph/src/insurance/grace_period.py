from dataclasses import dataclass
from datetime import date, timedelta


@dataclass(frozen=True, slots=True)
class GracePeriodCalculation:
    """Resultado auditável do cálculo de carência de uma apólice residual."""

    elapsed_days: int
    residual_grace_period_days: int
    grace_period_end_date: date
    is_eligible: bool


def calculate_auto_residual_grace_period(
    *,
    start_date: date,
    incident_date: date,
    contracted_grace_period_days: int,
    prior_continuous_coverage_days: int = 0,
) -> GracePeriodCalculation:
    """Calcula a carência restante e a elegibilidade do sinistro auto.

    A cobertura anterior só reduz a carência quando seus dias são informados como
    contínuos. A data do sinistro é elegível no dia em que os dias decorridos
    desde o início atingem a carência residual.
    """
    if contracted_grace_period_days < 0:
        raise ValueError("contracted_grace_period_days must be non-negative")
    if prior_continuous_coverage_days < 0:
        raise ValueError("prior_continuous_coverage_days must be non-negative")
    if incident_date < start_date:
        raise ValueError("incident_date cannot precede start_date")

    residual_days = max(
        contracted_grace_period_days - prior_continuous_coverage_days,
        0,
    )
    elapsed_days = (incident_date - start_date).days
    grace_period_end_date = start_date + timedelta(days=residual_days)

    return GracePeriodCalculation(
        elapsed_days=elapsed_days,
        residual_grace_period_days=residual_days,
        grace_period_end_date=grace_period_end_date,
        is_eligible=elapsed_days >= residual_days,
    )
