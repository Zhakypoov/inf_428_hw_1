import numpy as np


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(departments_data, departments_importance):
    weighted_scores = 0
    total_importance = sum(departments_importance)

    for i, dept_data in enumerate(departments_data):
        dept_mean = np.mean(dept_data)
        dept_importance = departments_importance[i]
        weighted_scores += dept_mean * dept_importance

    aggregated_score = weighted_scores / total_importance
    aggregated_score = np.clip(aggregated_score, 0, 90)

    return aggregated_score


def test_case():
    departments_data = [
        generate_random_data(30, 10, 100),
        generate_random_data(40, 12, 120),
        generate_random_data(35, 8, 110),
        generate_random_data(50, 5, 115),
        generate_random_data(25, 15, 105),
    ]

    departments_importance = [3, 2, 4, 5, 1]

    score = calculate_aggregated_threat_score(departments_data, departments_importance)
    print(f"Итоговая угроза: {score}")


test_case()

import unittest


class TestAggregatedThreatScore(unittest.TestCase):

    def test_aggregated_score(self):
        departments_data = [
            generate_random_data(30, 10, 100),
            generate_random_data(40, 12, 120),
            generate_random_data(35, 8, 110),
            generate_random_data(50, 5, 115),
            generate_random_data(25, 15, 105),
        ]
        departments_importance = [3, 2, 4, 5, 1]
        score = calculate_aggregated_threat_score(departments_data, departments_importance)
        self.assertTrue(0 <= score <= 90)

    def test_equal_importance(self):
        departments_data = [
            generate_random_data(30, 10, 100),
            generate_random_data(30, 10, 100),
            generate_random_data(30, 10, 100),
            generate_random_data(30, 10, 100),
            generate_random_data(30, 10, 100),
        ]
        departments_importance = [1, 1, 1, 1, 1]
        score = calculate_aggregated_threat_score(departments_data, departments_importance)
        self.assertTrue(0 <= score <= 90)

    def test_zero_threat(self):
        departments_data = [
            generate_random_data(0, 0, 100),
            generate_random_data(0, 0, 100),
            generate_random_data(0, 0, 100),
            generate_random_data(0, 0, 100),
            generate_random_data(0, 0, 100),
        ]
        departments_importance = [3, 3, 3, 3, 3]
        score = calculate_aggregated_threat_score(departments_data, departments_importance)
        self.assertEqual(score, 0)

    def test_maximum_threat(self):
        departments_data = [
            generate_random_data(90, 0, 100),
            generate_random_data(90, 0, 100),
            generate_random_data(90, 0, 100),
            generate_random_data(90, 0, 100),
            generate_random_data(90, 0, 100),
        ]
        departments_importance = [5, 5, 5, 5, 5]
        score = calculate_aggregated_threat_score(departments_data, departments_importance)
        self.assertEqual(score, 90)


if __name__ == '__main__':
    unittest.main()
