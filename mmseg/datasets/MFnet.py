from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MFnetDataset(CustomDataset):
    """ADE20K dataset.

    In segmentation map annotation for dataTIR, 0 stands for background, which
    is not included in 150 categories. ``reduce_zero_label`` is fixed to True.
    The ``img_suffix`` is fixed to '.bmp' and ``seg_map_suffix`` is fixed to
    '.png'.
    """
    CLASSES = (
        'unlabeled', 'car', 'person', 'bike', 'curve', 'car_stop', 'guardrail', 'color_cone', 'bump'
        )

    PALETTE = [[120, 120, 120], [180, 120, 120], [6, 230, 230], [80, 50, 50],
               [4, 200, 3], [120, 120, 80], [140, 140, 140], [204, 5, 255], [200,0,200]
               ]

    def __init__(self, **kwargs):
        super(MFnetDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=False,
            **kwargs)