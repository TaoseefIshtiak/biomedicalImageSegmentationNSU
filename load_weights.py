from segmentation_models import Unet, Nestnet, Xnet
model = Xnet(backbone_name='resnet50', encoder_weights='imagenet', decoder_block_type='transpose') # build UNet++
# model = Unet(backbone_name='resnet50', encoder_weights='imagenet', decoder_block_type='transpose') # build U-Net
# model = NestNet(backbone_name='resnet50', encoder_weights='imagenet', decoder_block_type='transpose') # build DLA

model.compile('Adam', 'binary_crossentropy', ['binary_accuracy'])
