from fractions import Fraction as F
import unittest

from uniform_game_cleanroom import (
    direct_best_response_candidates,
    profit_a,
    profit_b,
    share_a_direct,
    share_a_piecewise,
    source_uniform_prices,
    x_h_condition,
)


class FrozenRegressionTests(unittest.TestCase):
    def test_piecewise_matches_primitive_at_boundaries(self):
        for x in (F(3, 5), F(7, 10), F(9, 10)):
            for s in (F(1, 10), F(1, 2), F(9, 10)):
                cuts = (-1 - s, 2*x - 1 - s, 2*x - 1 + s, 1 + s)
                for d in cuts:
                    a, b = F(2), F(2) + d
                    self.assertEqual(
                        share_a_direct(a, b, x, s),
                        share_a_piecewise(a, b, x, s),
                    )

    def test_exact_source_counterexample(self):
        x, s = F(3, 5), F(1, 2)
        a, b = source_uniform_prices(s)
        b_dev = F(28, 15)
        self.assertEqual(profit_b(a, b, x, s), F(25, 72))
        self.assertEqual(profit_b(a, b_dev, x, s), F(56, 75))
        self.assertEqual(profit_b(a, b_dev, x, s) - profit_b(a, b, x, s), F(719, 1800))

    def test_exact_equality_boundary_is_singleton_nash(self):
        s, x = F(6, 47), F(67, 94)
        self.assertTrue(x_h_condition(x, s))
        a, b = source_uniform_prices(s)
        best_b, brs_b = direct_best_response_candidates("B", a, x, s)
        self.assertEqual(best_b, profit_b(a, b, x, s))
        kink_b = a + 2*x - 1 + s
        self.assertIn(b, brs_b)
        self.assertIn(kink_b, brs_b)
        best_a_at_kink, _ = direct_best_response_candidates("A", kink_b, x, s)
        self.assertGreater(best_a_at_kink, profit_a(a, kink_b, x, s))

    def test_below_threshold_profitable_deviation(self):
        s, x = F(6, 47), F(66, 94)
        self.assertFalse(x_h_condition(x, s))
        a, b = source_uniform_prices(s)
        best_b, _ = direct_best_response_candidates("B", a, x, s)
        self.assertGreater(best_b, profit_b(a, b, x, s))


if __name__ == "__main__":
    unittest.main()
