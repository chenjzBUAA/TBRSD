_base_ = [
    '../../configs/_base_/datasets/TBRSD_repeat.py',
    '../../configs/_base_/default_runtime.py',
    '../../configs/_base_/schedules/schedule_240k_adamw.py'
]

# model settings
norm_cfg = dict(type='SyncBN', requires_grad=True)
find_unused_parameters = True
model = dict(
    type='EncoderDecoder',
    pretrained='pretrained/mit_b5.pth',
    # pretrained=None,
    backbone=dict(
        type='TINNet',#这里就是encoder的结构
        style='pytorch'),
    decode_head=dict(
        type='TINNHead',
        in_channels=[64, 64, 128, 320, 512],
        in_index=[0, 1, 2, 3, 4],
        feature_strides=[4, 8, 16, 32, 64],
        channels=128,
        dropout_ratio=0.1,
        num_classes=2,
        norm_cfg=norm_cfg,
        align_corners=False,
        decoder_params=dict(embed_dim=768),
        loss_decode=dict(type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
    # model training and testing settings
    train_cfg=dict(),
    # test_cfg=dict(mode='whole'))
    test_cfg=dict(mode='slide', crop_size=(512,512), stride=(168,168)))

# data
data = dict(samples_per_gpu=2)
evaluation = dict(interval=20000, metric='mIoU')

# optimizer
optimizer = dict(_delete_=True, type='AdamW', lr=0.00006, betas=(0.9, 0.999), weight_decay=0.01,
                 paramwise_cfg=dict(custom_keys={'pos_block': dict(decay_mult=0.),
                                                 'norm': dict(decay_mult=0.),
                                                 'head': dict(lr_mult=10.)
                                                 }))

lr_config = dict(_delete_=True, policy='poly',
                 warmup='linear',
                 warmup_iters=1500,
                 warmup_ratio=1e-6,
                 power=1.0, min_lr=0.0, by_epoch=False)


