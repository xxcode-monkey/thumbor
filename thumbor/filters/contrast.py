#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.filters import BaseFilter
from thumbor.ext.filters import _contrast

class Filter(BaseFilter):
    regex = r'(?:contrast\((?P<value>[-]?[\d]+)\))'

    def run_filter(self):
        imgdata = _contrast.apply(self.engine.get_image_mode(), int(self.params['value']), self.engine.get_image_data())
        self.engine.set_image_data(imgdata)