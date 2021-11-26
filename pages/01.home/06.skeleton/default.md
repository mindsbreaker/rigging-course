---
title: Skeleton
---

Building a [skeleton](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-906B71D3-C153-4880-A8EF-F9A6D1AE4AD5) is the process of placing and orienting joints to create a system with which you can pose a deformable object.  
If you are creating a skeleton for a human biped, you would place joints at all the major points of articulation in its model.  
(shoulders, knees, elbows, spine and so on)
The [skeleton hierarchy](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-DC88B9A7-593B-427E-9BED-4D7822B0E0B6) is composed of a series of joints and joints chains with hierarchical relationships.  

### Joints and bones

[Joints](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-1B59334F-2605-44C3-B584-A55B239A2CBE) are the building blocks of skeletons and their points of articulation.  
Each joint can have one or more bone attached to it, and more than one child joint.  
Bones are only visual cues that illustrate the relationships between joints.  

> :information_source: **Note:**  Joints are specific nodes without shape, they can't be rendered but are displayed in the viewport by  the bones.  

A [joint chain](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-267B988F-4E21-4963-BF6A-478E5F6FEF81) is any group of joints and their bones connected in a series.  
The joint chain begins at the highest joint in the chain’s hierarchy, and its bones are drawn pointing down the chain.  


> :warning: **Warn:**  You can't create a mirrored duplicate of a joint chain with a scale of -1. Use *Skeleton -> Mirror Joint* instead.  

---

<br>

## *Deformations*

### Skinning

[Skinning](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-EFE68C08-9ADA-4355-8203-5D1D109DCC82) is the process of binding a modeled surface to a skeleton.  
You can bind any model to its skeleton using a [skinCluster](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2E292C8A-388A-4E77-B42D-165F1C9E1E5F) node.  
And the model will follow or react to the transformations of the skeleton’s joints and bones.  

### Smooth Skinning

Smooth deformations are provided by enabling several joints to influence the same deformable object points.  
The smoothing effects around joints are automatically set up when you [bind skin](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8DBA9E62-3854-4348-A0AD-1F981ECEA54F).  
Maya offers three [methods](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-630C335C-B63E-4F2E-A4A4-AEA1DD00B0D6) to smooth skin a model:  

- Classic Linear
- Dual Quaternion
- Weight Blended (blend of both methods).


> :information_source: **Note:**  The *Dual Quaternion* method has better deformation and keep model's volume.  

### Edit Weights

You can directly modify the values of individual skin point weights using the [Component Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-B698CC5D-2771-488E-98E8-2D4E31DB3B2D).  
The *Component Editor* lets you easily set specific skin point weights to particular values.

If you want to shape the deformation directly and are not concerned with specific values,  
you can instead paint weights with the [Paint Skin Weights Tool](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-99189E9D-237F-471E-A02C-BE6593B4828B).

---

<br>