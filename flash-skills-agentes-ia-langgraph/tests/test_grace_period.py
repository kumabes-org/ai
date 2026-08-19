import unittest
from datetime import date

from src.insurance.grace_period import calculate_auto_residual_grace_period


class CalculateAutoResidualGracePeriodTests(unittest.TestCase):
    def test_claim_is_rejected_until_contractual_grace_period_elapses(self) -> None:
        before_end = calculate_auto_residual_grace_period(
            start_date=date(2026, 8, 1),
            incident_date=date(2026, 8, 30),
            contracted_grace_period_days=30,
        )
        at_end = calculate_auto_residual_grace_period(
            start_date=date(2026, 8, 1),
            incident_date=date(2026, 8, 31),
            contracted_grace_period_days=30,
        )

        self.assertFalse(before_end.is_eligible)
        self.assertEqual(before_end.residual_grace_period_days, 30)
        self.assertTrue(at_end.is_eligible)
        self.assertEqual(at_end.grace_period_end_date, date(2026, 8, 31))

    def test_previous_continuous_coverage_reduces_residual_grace_period(self) -> None:
        calculation = calculate_auto_residual_grace_period(
            start_date=date(2026, 8, 1),
            incident_date=date(2026, 8, 10),
            contracted_grace_period_days=30,
            prior_continuous_coverage_days=20,
        )

        self.assertFalse(calculation.is_eligible)
        self.assertEqual(calculation.residual_grace_period_days, 10)
        self.assertEqual(calculation.grace_period_end_date, date(2026, 8, 11))

    def test_sufficient_previous_coverage_removes_grace_period(self) -> None:
        calculation = calculate_auto_residual_grace_period(
            start_date=date(2026, 8, 1),
            incident_date=date(2026, 8, 1),
            contracted_grace_period_days=30,
            prior_continuous_coverage_days=30,
        )

        self.assertTrue(calculation.is_eligible)
        self.assertEqual(calculation.residual_grace_period_days, 0)
        self.assertEqual(calculation.grace_period_end_date, date(2026, 8, 1))

    def test_invalid_values_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            calculate_auto_residual_grace_period(
                start_date=date(2026, 8, 2),
                incident_date=date(2026, 8, 1),
                contracted_grace_period_days=30,
            )

        with self.assertRaises(ValueError):
            calculate_auto_residual_grace_period(
                start_date=date(2026, 8, 1),
                incident_date=date(2026, 8, 1),
                contracted_grace_period_days=-1,
            )
