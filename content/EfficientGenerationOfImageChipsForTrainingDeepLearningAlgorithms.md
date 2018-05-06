Title: Efficient Generation of Image Chips for Training Deep Learning Algorithms
Date: 2017-03-11 12:00
Modified: 2017-03-11 12:00
Category: Research
Authors: Todd V. Rovito

Abstract: Training deep convolutional networks for satellite or aerial image
analysis often requires a large amount of training data. For a more robust
algorithm, training data need to have variations not only in the background and
target, but also radiometric variations in the image such as shadowing,
illumination changes, atmospheric conditions, and imaging platforms with
different collection geometry. Data augmentation is a commonly used approach to
generating additional training data. However, this approach is often
insufficient in accounting for real world changes in lighting, location or
viewpoint outside of the collection geometry. Alternatively, image simulation
can be an efficient way to augment training data that incorporates all these
variations, such as changing backgrounds, that may be encountered in real data.
The Digital Imaging and Remote Sensing Image Image Generation (DIRSIG) model is
a tool that produces synthetic imagery using a suite of physics-based radiation
propagation modules. DIRSIG can simulate images taken from different sensors
with variation in collection geometry, spectral response, solar elevation and
angle, atmospheric models, target, and background. For our research, we
selected ground vehicles as target objects and incorporated the Simulation of
Urban Mobility (SUMO) model into DIRSIG to generate scenes with vehicle
movement. SUMO is a multi-modal traffic simulation tool that explicitly models
vehicles that move through a given road network. Using the combination of
DIRSIG and SUMO, we can quickly generate hundreds of image chips, with the
target at the center with different backgrounds. The simulations generated
chips with vehicles and helicopters as targets, and corresponding images
without targets. Using parallel computing, 120,000 training images were
generated in about an hour. Some preliminary results show an improvement in the
deep learning algorithm when real image training data are augmented with the
simulated images.


Links to paper:

* [Paper](https://www.dropbox.com/s/7usmxgawfrpxfat/2017SPIEPaperDraft.pdf?dl=0)

