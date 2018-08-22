#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/8/22
"""This module implements DISTMULT model.
References:
    Embedding Entities and Relations for Learning and Inference in Knowledge Bases, 2014
"""
import tensorflow as tf

from kge.model import BaseModel


class DISTMULT(BaseModel):

    def _score_func(self, h, r, t):
        """f_r(h, t) = h * W_r * t."""
        with tf.name_scope('score'):
            self.W_r = tf.get_variable("W", [self.k, self.k])
            h = tf.expand_dims(h, axis=1)  # (b, k) -> (b, 1, k)
            W_r = tf.tile(tf.expand_dims(self.W_r, 0), [self.b, 1, 1])
            t = tf.expand_dims(t, axis=2)
            score = tf.matmul(tf.matmul(h, W_r), t)

        return score

