
![](https://geps.dev/progress/40)
- [x] Getting started with Tensorflow
- [x] Neural Network Regression with Tensorflow
- [x] Neural Network Classification with Tensorflow
- [ ] Convolution Neural Networks & Computer Vision with Tensorflow
- [ ] Transfer Learning
- [ ] Image Classification: Kaggle Competition

### Why Tensorflow is worse than Pytorch
   1. Tensorflow 2.15 & Keras 3.0 conflicts of installation. Pytorch doesn't have that problem.
   2. Lots of inconsistent & incoherent features. Pytorch is coherent in features. 
   3. **Annoying to make some things work, in Tensorflow**
2. Conclusion
    1. Use Pytorch for training loop, if you want to use tensorflow, use it just for model architecture.
    2. Future: Using Jax or Tensorflow for speedup. Then use keras 3.0, same api, and multiple backends. No need to learn different libraries. 

### Best Practices Discovered
1. **Aim for experiment running via one script execution**
2. Get the end to end experiment working first
3. Rename variables for clear understanding

### Checklist

- [x] downloading **datasets** & starting training.
  - -> ans: huggingface datasets. standard way of uploading dataset. dataset to dataloader in pytorch & in tensorflow via huggingface
- [ ] **model**. 
  - sequential is easy but can't debug properly -> ans: extending model. (2 ways)
- [ ] **training** loop from that dataset. training loop 