
## Computer Vision Status
Image Classification with TF = ![](https://geps.dev/progress/99)
- [x] Getting started with Tensorflow
- [x] Neural Network Regression with Tensorflow
- [x] Neural Network Classification with Tensorflow
- [x] Convolution Neural Networks & Computer Vision with Tensorflow
- [x] Transfer Learning
  - Very very important
  - Getting to good enough accuracy immediately
- [ ] Image Classification: Kaggle Competition

### Annoying Things
1. Tensorflow 2.15 & Keras 3.0 conflicts of installation. Had to use Colab
2. Tensorflow attempting advanced/fancy features, but incoherent & incosistent. Pytorch is coherent & simple, despite not having advanced feature goals. (Einstein: Genius of Simplicity)
3. Code can be succint, easy to read & understand & write, if using Keras. (Advantage)
4. Time Consuming
   1. Dataset downloading. (Colab needs redownload)
   2. Dataset processing
   3. Writing glue code for many small things. (Dataset download, process, visualize | Model etc...)
   4. Model training time. Time to train 1 batch, time to train entire dataset

### Best Practices Discovered
1. Simplify code, reduce glue code / boilderplate code
2. **Aim for experiment running via one script execution**
3. Get the end to end experiment working first
4. Rename variables for clear understanding. (only after end to end pipeline is running not before)
5. TODO: Upload Dataset & Model & Trained model on **Huggingface**
6. Use Weights & Biases for experiment tracking.

### **Remaining**
- [ ] NN visualizations & interpretability
- [ ] Going beyond Image Classification. Localization, Detection, Segmentation, Generation
- [ ] Trying Different Computer Vision Competitions
- [ ] Vision Classic Research Papers