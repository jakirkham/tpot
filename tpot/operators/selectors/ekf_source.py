# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:37:20 2017

@author: ansohn
"""

from .base import Selector
from .ek_filter import EKF_Source


class TPOTekf(Selector):

    import_hash = {'tpot.operators.selectors.ek_filter': ['EKF_source']}
    sklearn_class = EKF_Source
    arg_types = (list, int, int)

    def __init__(self):
        pass

    def preprocess_args(self, expert_source, ekf_index, k_best):
        expert_source = expert_source
        ekf_index = ekf_index % len(expert_source)
        k_best = k_best % 5

        return {
            'expert_source': expert_source,
            'ekf_index': ekf_index,
            'k_best': k_best
        }
