from fractions import Fraction as F
import unittest

from uniform_game_cleanroom import (
    direct_best_response_candidates,
    profit_a,
    profit_b,
    share_a_direct,
    share_a_piecewise,
    source_uniform_prices,
    source_eq15_switch_cs,
    source_eq16_printed_cs,
    source_uniform_profile_profits,
    weak_hbp_source_profits,
    hbp_strong_profile_unrestricted,
    hbp_profits_direct,
    hbp_cs_direct,
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


    def test_eq15_source_fidelity_and_eq16_sign(self):
        s, x = F(1, 10), F(7, 10)
        self.assertEqual(source_eq15_switch_cs(x, s), F(221, 720))
        self.assertEqual(source_eq16_printed_cs(x, s), F(-221, 720))
        self.assertEqual(source_eq16_printed_cs(x, s), -source_eq15_switch_cs(x, s))

    def test_weak_profit_no_switch_branch(self):
        s, x = F(1, 2), F(51, 100)
        _, pi_b_d = weak_hbp_source_profits(x, s)
        _, pi_b_u = source_uniform_profile_profits(x, s)
        self.assertEqual(pi_b_d, F(3221, 9000))
        self.assertEqual(pi_b_u, F(49, 120))
        self.assertEqual(pi_b_d - pi_b_u, F(-227, 4500))

    def test_strong_profit_does_not_inherit_weak_ranking(self):
        s, x = F(9, 10), F(19, 20)
        profile = hbp_strong_profile_unrestricted(x, s, F(0))
        _, pi_b_d = hbp_profits_direct(*profile, x, s)
        _, pi_b_u = source_uniform_profile_profits(x, s)
        self.assertEqual(pi_b_d - pi_b_u, F(41, 900))

    def test_empty_segment_prices_are_indeterminate_at_x1(self):
        s, x = F(1, 2), F(1)
        p_a = (2 * x + 1 + s) / 3
        q_b = (4 * x - 1 - s) / 3
        base = (p_a, F(0), 1 + s, q_b)
        alt = (p_a, F(7), F(9), q_b)
        self.assertEqual(hbp_profits_direct(*base, x, s), hbp_profits_direct(*alt, x, s))
        self.assertEqual(hbp_cs_direct(*base, x, s), hbp_cs_direct(*alt, x, s))


if __name__ == "__main__":
    unittest.main()
