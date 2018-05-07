Title: Physics Accurate Layered Sensing Model
Date: 2011-07-01 12:00
Modified: 2015-12-25 12:00
Category: Research
Authors: Todd V. Rovito
Summary: Learn how to build a layered sensing model with open source software

Abstract: This paper will look at using open source tools (Blender [1],
LuxRender [2], Open CV [3], SUMO [4], and Python [5]) to build an image
processing model for exploring combinations of sensors/platforms for any given
image resolution. The model produces camera position, camera attitude, and
synthetic camera data that can be used for exploitation purposes. We focus on
electro-optical (EO) visible sensors to simplify the rendering but this work
could be extended to use other rendering tools that support different
modalities. Open Computer Vision (Open CV) is used to generate a camera model
for the intrinsics of the virtual camera. This camera model is then used to geo-
project the images from pixel space into a world coordinate system storing the
output in National Imagery Transmission Format (NITF) for display with standard
Intelligence Analysis (IA) tools such as RYA’s Pursuer [6]. We also demonstrate
Simulation of Urban Mobility (SUMO) software to simulate complex traffic
patterns. The key idea of the paper is to provide an architecture for layered
sensing simulation which is modular in design and constructed on open-source
off-the-shelf software yielding a physics accurate virtual model of the world.
This architecture shows how leveraging existing open-source software allows for
practical layered sensing modeling to be rapidly assimilated and utilized in
real-world applications. In this paper we demonstrate our model output is
automatically exploitable by using generated data with an innovative geo-
registration algorithm and real time display.

* [Paper](https://drive.google.com/uc?id=1QwYS7jOVuKRAbV4BbpaCxrw4BHV-fi56)
* [Presentation](https://drive.google.com/uc?id=1-HbP96RIicmjOk2LXBh43HsmfFPbSk5Y)
* [Blender Camera Animation](https://drive.google.com/uc?id=13Z__K5z0GDeK3CycJ1_dGINmTfV2Usj5)
* [SUMO Animation](https://drive.google.com/uc?id=1Ghg715obdFkE67dedvqkzrcejEYFFzeB)
* [Sadr City Car Animation Wire Frame](https://drive.google.com/uc?id=1MSfBBnPeviGvULip6PSwg8iPo6TzLegx)
* [Building Camera Animation](https://drive.google.com/uc?id=1WWTkWZya8_-yEPSjyPSSSDUa7YUq63Jr)
* [Synthetic NITF in Pursuer Animation](https://drive.google.com/uc?id=15iIPhWcxeMPjmdeWH9gJFKkB7dh-lux6)

