# coding=utf-8
# Copyright 2022 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np
import torch

from diffusers import DDIMPipeline, DDIMScheduler, UNet2DModel
from diffusers.utils.testing_utils import require_torch_gpu, slow, torch_device

from ...test_pipelines_common import PipelineTesterMixin


torch.backends.cuda.matmul.allow_tf32 = False


class DDIMPipelineFastTests(PipelineTesterMixin, unittest.TestCase):
    @property
    def dummy_uncond_unet(self):
        torch.manual_seed(0)
        model = UNet2DModel(
            block_out_channels=(32, 64),
            layers_per_block=2,
            sample_size=32,
            in_channels=3,
            out_channels=3,
            down_block_types=("DownBlock2D", "AttnDownBlock2D"),
            up_block_types=("AttnUpBlock2D", "UpBlock2D"),
        )
        return model

    def test_inference(self):
        device = "cpu"
        unet = self.dummy_uncond_unet
        scheduler = DDIMScheduler()

        ddpm = DDIMPipeline(unet=unet, scheduler=scheduler)
        ddpm.to(device)
        ddpm.set_progress_bar_config(disable=None)

        generator = torch.Generator(device=device).manual_seed(0)
        image = ddpm(generator=generator, num_inference_steps=2, output_type="numpy").images

        generator = torch.Generator(device=device).manual_seed(0)
        image_from_tuple = ddpm(generator=generator, num_inference_steps=2, output_type="numpy", return_dict=False)[0]

        image_slice = image[0, -3:, -3:, -1]
        image_from_tuple_slice = image_from_tuple[0, -3:, -3:, -1]

        assert image.shape == (1, 32, 32, 3)
        expected_slice = np.array(
            [1.000e00, 5.717e-01, 4.717e-01, 1.000e00, 0.000e00, 1.000e00, 3.000e-04, 0.000e00, 9.000e-04]
        )
        assert np.abs(image_slice.flatten() - expected_slice).max() < 1e-2
        assert np.abs(image_from_tuple_slice.flatten() - expected_slice).max() < 1e-2


@slow
@require_torch_gpu
class DDIMPipelineIntegrationTests(unittest.TestCase):
    def test_inference_ema_bedroom(self):
        model_id = "google/ddpm-ema-bedroom-256"

        unet = UNet2DModel.from_pretrained(model_id)
        scheduler = DDIMScheduler.from_config(model_id)

        ddpm = DDIMPipeline(unet=unet, scheduler=scheduler)
        ddpm.to(torch_device)
        ddpm.set_progress_bar_config(disable=None)

        generator = torch.Generator(device=torch_device).manual_seed(0)
        image = ddpm(generator=generator, output_type="numpy").images

        image_slice = image[0, -3:, -3:, -1]

        assert image.shape == (1, 256, 256, 3)
        expected_slice = np.array([0.1546, 0.1561, 0.1595, 0.1564, 0.1569, 0.1585, 0.1554, 0.1550, 0.1575])
        assert np.abs(image_slice.flatten() - expected_slice).max() < 1e-2

    def test_inference_cifar10(self):
        model_id = "google/ddpm-cifar10-32"

        unet = UNet2DModel.from_pretrained(model_id)
        scheduler = DDIMScheduler()

        ddim = DDIMPipeline(unet=unet, scheduler=scheduler)
        ddim.to(torch_device)
        ddim.set_progress_bar_config(disable=None)

        generator = torch.Generator(device=torch_device).manual_seed(0)
        image = ddim(generator=generator, eta=0.0, output_type="numpy").images

        image_slice = image[0, -3:, -3:, -1]

        assert image.shape == (1, 32, 32, 3)
        expected_slice = np.array([0.2060, 0.2042, 0.2022, 0.2193, 0.2146, 0.2110, 0.2471, 0.2446, 0.2388])
        assert np.abs(image_slice.flatten() - expected_slice).max() < 1e-2
