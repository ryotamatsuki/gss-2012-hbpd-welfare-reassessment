from fractions import Fraction as F
import unittest

from uniform_game_cleanroom import (
    direct_best_response_candidates,
    hbp_cs_direct,
    hbp_profits_direct,
    hbp_strong_profile_unrestricted,
    hbp_weak_prices,
    profit_a,
    profit_b,
    share_a_direct,
    share_a_piecewise,
    source_uniform_prices,
    uniform_cs_direct,
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
        self.assertEqual(
            profit_b(a, b_dev, x, s) - profit_b(a, b, x, s),
            F(719, 1800),
        )

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

    def test_eq15_source_fidelity_on_valid_switching_branch(self):
        s, x = F(1, 10), F(7, 10)
        p_a_u, p_b_u = source_uniform_prices(s)
        p_a_d, q_a_d, p_b_d, q_b_d = hbp_weak_prices(x, s)
        direct_gap = (
            hbp_cs_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s)
            - uniform_cs_direct(p_a_u, p_b_u, x, s)
        )
        source_eq15 = (
            -52*x*x + 52*x + 1 + 36*s*x - 34*s + s*s
        ) / 36
        self.assertEqual(direct_gap, F(221, 720))
        self.assertEqual(source_eq15, F(221, 720))
        self.assertEqual(-source_eq15, -F(221, 720))

    def test_weak_profit_uses_realized_no_switch_branch(self):
        s, x = F(1, 2), F(51, 100)
        p_a_u, p_b_u = source_uniform_prices(s)
        p_a_d, q_a_d, p_b_d, q_b_d = hbp_weak_prices(x, s)
        _, pi_b_d = hbp_profits_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s)
        pi_b_u = profit_b(p_a_u, p_b_u, x, s)
        switching_extension = (
            s*s - 12*s*x + 14*s + 20*x*x - 20*x + 1
        ) / 18
        self.assertEqual(pi_b_d, F(3221, 9000))
        self.assertEqual(pi_b_u, F(49, 120))
        self.assertEqual(pi_b_d - pi_b_u, -F(227, 4500))
        self.assertEqual(switching_extension, F(4, 375))
        self.assertLess(pi_b_d - pi_b_u, 0)
        self.assertGreater(switching_extension, 0)

    def test_strong_profit_is_not_weak_profit_claim(self):
        s, x = F(9, 10), F(19, 20)
        self.assertTrue(x_h_condition(x, s))
        p_a_d, q_a_d, p_b_d, q_b_d = hbp_strong_profile_unrestricted(x, s, F(0))
        _, pi_b_d = hbp_profits_direct(p_a_d, q_a_d, p_b_d, q_b_d, x, s)
        p_a_u, p_b_u = source_uniform_prices(s)
        pi_b_u = profit_b(p_a_u, p_b_u, x, s)
        self.assertEqual(pi_b_d - pi_b_u, F(41, 900))
        self.assertGreater(pi_b_d - pi_b_u, 0)


if __name__ == "__main__":
    unittest.main()
