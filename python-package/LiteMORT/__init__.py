# coding: utf-8
"""LiteMORT, Light Gradient Boosting Machine.

__author__ = 'Yingshi Chen'
"""
from __future__ import absolute_import
import os


try:
    #from .LiteMORT_problems import Mort_Problems
    from .LiteMORT import LiteMORT,LiteMORT_profile
    from .LiteMORT_preprocess import Mort_Preprocess,Mort_PickSamples
    from .LiteMORT_hyppo import MORT_feat_select_
except ImportError:
    pass
'''
try:
    from .plotting import plot_importance, plot_metric, plot_tree, create_tree_digraph
except ImportError:
    pass
'''

dir_path = os.path.dirname(os.path.realpath(__file__))

if os.path.isfile(os.path.join(dir_path, 'VERSION.txt')):
    __version__ = open(os.path.join(dir_path, 'VERSION.txt')).read().strip()

__all__ = ['LiteMORT','LiteMORT_profile','Mort_Preprocess','Mort_PickSamples','MORT_feat_select_']


