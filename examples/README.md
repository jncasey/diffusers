<!---
Copyright 2022 The HuggingFace Team. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# 🧨 Diffusers Examples

Diffusers examples are a collection of best-practices on how to use the `diffusers` library.

**Note**: If you are looking for **official** examples on how to use `diffusers` for inference, 
please have a look at [src/diffusers/pipelines](https://github.com/huggingface/diffusers/tree/main/src/diffusers/pipelines)

Our examples aspire to be **self-contained**, **easy-to-tweak**, **beginner-friendly** and for **one-purpose-only**.
More specifically, this means:

- **Self-contained**: An example script shall only depend on "pip-install-able" Python packages that can be found in a `requirements.txt` file. Example scripts shall **not** depend on any local files. This means that one can simply download an example script, *e.g.* [train_unconditional.py](https://github.com/huggingface/diffusers/blob/main/examples/unconditional_image_generation/train_unconditional.py), install the required dependencies, *e.g.* [requirements.txt](https://github.com/huggingface/diffusers/blob/main/examples/unconditional_image_generation/requirements) and execute the example script.
- **Easy-to-tweak**: While we strive to present as many use cases as possible, the example scripts are just that - examples. It is expected that they won't work out-of-the box on your specific problem and that you will be required to change a few lines of code to adapt them to your needs. To help you with that, most of the examples fully expose the preprocessing of the data and the training loop to allow you to tweak and edit them as required.
- **Beginner-friendly**: We do not aim for providing state-of-the-art training scripts for the newest models, but rather examples that can be used as a way to better understand Diffusion models and how to use them with the `diffusers` library. We often purposefully leave out certain state-of-the-art methods if we consider them too complex for beginners.
- **One-purpose-only**: Examples should show one task and one task only. Even if a task is from a modeling 
point of view very similar, *e.g.* image super-resolution and image modification tend to use the same model and training method, we want examples to showcase only one task to keep them as readable and easy-to-understand as possible.

We provide **official** examples that cover the most popular tasks of diffusion models.
*Official* examples are **actively** maintained by the `diffusers` maintainers and we try to rigorously follow our example philosophy as defined above. 
If you feel like an important examples, we are more than happy to welcome a [Feature Request](https://github.com/huggingface/diffusers/issues/new?assignees=&labels=&template=feature_request.md&title=) or directly a [Pull Request](https://github.com/huggingface/diffusers/compare) from you 🤗.

Training examples show how to pretrain or fine-tune diffusion models for a variety of tasks. Currently we support:

| Task | 🤗 Accelerate | 🤗 Datasets | Colab
|---|---|:---:|:---:|:---:|:---:|
| [**Unconditional Image Generation**](https://github.com/huggingface/transformers/tree/main/examples/training/train_unconditional.py) | ✅ | ✅ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/training_example.ipynb)

## Community

In additon, we provide **community** examples, which are examples added and maintained by our community.
Community examples can consists of both *training* examples and *inference* pipelines.
For such examples, we are more lenient regarding the philosophy defined above and also cannot guarantee to provide maintenance for every issue.
Examples that we deem not (yet) popular/important enough to go into the [official training examples]( ) or [official pipelines](https://github.com/huggingface/diffusers/tree/main/src/diffusers/pipelines), or that don't fully following the philosophy defined above, should go into the [community examples](https://github.com/huggingface/diffusers/tree/main/examples/community) folder. The community folder therefore includes training examples and inference pipelines.
**Note**: Community examples can be a [great first contribution](https://github.com/huggingface/diffusers/compare) to show to the community how you like to use `diffusers` 🪄.

## Important note

To make sure you can successfully run the latest versions of the example scripts, you have to **install the library from source** and install some example-specific requirements. To do this, execute the following steps in a new virtual environment:
```bash
git clone https://github.com/huggingface/transformers
cd transformers
pip install .
```
Then cd in the example folder of your choice and run
```bash
pip install -r requirements.txt
```