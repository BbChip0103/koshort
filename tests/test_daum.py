# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from koshort.stream.daum import DaumStreamer
from koshort.constants import DATA_DIR
import glob
import pytest


@pytest.mark.parametrize("is_async", [(True), (False)])
def test_daum_streamer(is_async):
    daum = DaumStreamer(is_async=is_async)
    daum.options.n_limits = 1
    daum.options.display_rank = True
    daum.options.verbose = True
    daum.options.interval = 3
    daum.stream()


def test_result_exists():
    """Check if files are correctly created. """

    items = glob.glob(DATA_DIR+"*trend*")
    assert len(items) > 0
