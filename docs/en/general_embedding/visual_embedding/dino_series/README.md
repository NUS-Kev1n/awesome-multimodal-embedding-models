[EN](README.md)|[ZH](../../../../zh/general_embedding/visual_embedding/dino_series/README.md)

# DINO Series

## dinov2 series

### dinov2-small

Model: facebook/dinov2-small

Output embedding dimension:
- CLS feature: 384
- Patch feature: (256,384)

Hugging Face: [facebook/dinov2-small](https://huggingface.co/facebook/dinov2-small)

GitHub: [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) ![](https://img.shields.io/github/stars/facebookresearch/dinov2.svg?style=social)

Code: [test_dinov2-small.py](../../../../../code/general_embedding/visual_embedding/dino_series/test_dinov2-small.py)

Output:
```
Feature extraction time: 1.9590 seconds
GPU memory usage: 93.21 MB
CLS features shape: torch.Size([1, 384])
Patch features shape: torch.Size([1, 256, 384])
Features extracted successfully
```

---

### dinov2-base

Model: facebook/dinov2-base

Output embedding dimension:
- CLS feature: 768
- Patch feature: (256,768)

Hugging Face: [facebook/dinov2-base](https://huggingface.co/facebook/dinov2-base)

GitHub: [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) ![](https://img.shields.io/github/stars/facebookresearch/dinov2.svg?style=social)

Code: [test_dinov2-base.py](../../../../../code/general_embedding/visual_embedding/dino_series/test_dinov2-base.py)

Output:
```
Feature extraction time: 2.0362 seconds
GPU memory usage: 340.49 MB
CLS features shape: torch.Size([1, 768])
Patch features shape: torch.Size([1, 256, 768])
Features extracted successfully
```

---

### dinov2-large

Model: facebook/dinov2-large

Output embedding dimension:
- CLS feature: 1024
- Patch feature: (256,1024)

Hugging Face: [facebook/dinov2-large](https://huggingface.co/facebook/dinov2-large)

GitHub: [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) ![](https://img.shields.io/github/stars/facebookresearch/dinov2.svg?style=social)

---

### dinov2-giant

Model: facebook/dinov2-giant

Output embedding dimension:
- CLS feature: 1536
- Patch feature: (256,1536)

Hugging Face: [facebook/dinov2-giant](https://huggingface.co/facebook/dinov2-giant)

GitHub: [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) ![](https://img.shields.io/github/stars/facebookresearch/dinov2.svg?style=social)

---

## webssl-dino series

### webssl-dino1b-full2b-224

Model: facebook/webssl-dino1b-full2b-224

Output embedding dimension:
- CLS feature: 1536
- Patch feature: (256,1536)

Hugging Face: [facebook/webssl-dino1b-full2b-224](https://huggingface.co/facebook/webssl-dino1b-full2b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino2b-full2b-224

Model: facebook/webssl-dino2b-full2b-224

Output embedding dimension:
- CLS feature: 2688
- Patch feature: (256,2688)

Hugging Face: [facebook/webssl-dino2b-full2b-224](https://huggingface.co/facebook/webssl-dino2b-full2b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino2b-light2b-224

Model: facebook/webssl-dino2b-light2b-224

Output embedding dimension:
- CLS feature: 2688
- Patch feature: (256,2688)

Hugging Face: [facebook/webssl-dino2b-light2b-224](https://huggingface.co/facebook/webssl-dino2b-light2b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino2b-heavy2b-224

Model: facebook/webssl-dino2b-heavy2b-224

Output embedding dimension:
- CLS feature: 2688
- Patch feature: (256,2688)

Hugging Face: [facebook/webssl-dino2b-heavy2b-224](https://huggingface.co/facebook/webssl-dino2b-heavy2b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino3b-light2b-224

Model: facebook/webssl-dino3b-light2b-224

Output embedding dimension:
- CLS feature: 3072
- Patch feature: (256,3072)

Hugging Face: [facebook/webssl-dino3b-light2b-224](https://huggingface.co/facebook/webssl-dino3b-light2b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino3b-heavy2b-224

Model: facebook/webssl-dino3b-heavy2b-224

Output embedding dimension:
- CLS feature: 3072
- Patch feature: (256,3072)

Hugging Face: [facebook/webssl-dino3b-heavy2b-224](https://huggingface.co/facebook/webssl-dino3b-heavy2b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino7b-full8b-224

Model: facebook/webssl-dino7b-full8b-224

Output embedding dimension:
- CLS feature: 4096
- Patch feature: (256,4096)

Hugging Face: [facebook/webssl-dino7b-full8b-224](https://huggingface.co/facebook/webssl-dino7b-full8b-224)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino7b-full8b-378

Model: facebook/webssl-dino7b-full8b-378

Output embedding dimension:
- CLS feature: 4096
- Patch feature: (729,4096)

Hugging Face: [facebook/webssl-dino7b-full8b-378](https://huggingface.co/facebook/webssl-dino7b-full8b-378)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social)

---

### webssl-dino7b-full8b-518

Model: facebook/webssl-dino7b-full8b-518

Output embedding dimension:
- CLS feature: 4096
- Patch feature: (1369,4096)

Hugging Face: [facebook/webssl-dino7b-full8b-518](https://huggingface.co/facebook/webssl-dino7b-full8b-518)

GitHub: [facebookresearch/webssl](https://github.com/facebookresearch/webssl) ![](https://img.shields.io/github/stars/facebookresearch/webssl.svg?style=social) 