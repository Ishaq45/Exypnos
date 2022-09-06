#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:49:54 2021

@author: acer
"""


from pydantic import BaseModel

# Class which describes the input for the x values in the function y = 2 * x + 1
# Providing the base model to our defined class provides the input with additional helpful functionality
# more can be read about the bonus functionality can be found on the pydantic website 
# for instance, it alerts us if string values are provided for 'x'
class InputModel(BaseModel):
    xValue : float
    #input_2 : datatype
