#!/usr/bin/env python3
from logistic_regression import MyLogisticRegression
import unittest
import numpy as np

class TestMyLogisticRegression(unittest.TestCase):

	def test_basic_play_game_1(self):
		classifier = MyLogisticRegression('2')
		[accuracy, precision, recall, f1, support] = classifier.model_predict_linear()

		ans = accuracy >=0.35 and precision[0] >= 0.52 and recall[0] >= 0.20 \
            	and f1[0] >= 0.24 and support[0] >=19 \
                and precision[1] >= 0.30 and recall[1] >= 0.68 \
            	and f1[1] >= 0.43 and support[1] >=11
		print('\nexpected results:')
		print('Accuracy: 0.90')
		print('class 0 | p r f1 sup = 0.83, 0.91, 0.87, 11.00')
		print('class 1 | p r f1 sup = 0.94, 0.89, 0.92, 19.00')
		print('Your results:')
		print('Accuracy: {}'.format(accuracy))
		print('class 0 | p r f1 sup = {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(precision[0], recall[0], f1[0], support[0]))
		print('class 1 | p r f1 sup = {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(precision[1], recall[1], f1[1], support[1]))
		self.assertTrue(ans)

if __name__ == '__main__':
    unittest.main()