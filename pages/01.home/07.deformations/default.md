---
title: Deformations
---

The [deformation effects](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2016/ENU/Maya/files/GUID-B1AB118B-D620-4A74-88AA-11E8569D0E60-htm.html) are only aply on the shape node. When you apply a deformer, Maya makes a copy of the shape (tagged as an *"original”* or *"intermediate"*).  
This duplicated shape **"Orig"** is connected to the deformer, and the result is plugged into the shape node.  

There are many different types of deformers, each to apply a different effect, but probably the most common one is the *skinCluster*.  
This is used when you skin a character to a joint hierarchy. In the skinCluster node, weights are applied to the vertexes corresponding to which joints influence it.  

___
### Skinning

[Skinning](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-EFE68C08-9ADA-4355-8203-5D1D109DCC82) is the process of binding a modeled surface to a skeleton. You can bind any model to its skeleton using a [skinCluster](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-2E292C8A-388A-4E77-B42D-165F1C9E1E5F) node.  
And the model will follow or react to the transformations of the skeleton’s joints and bones.  

#### Smooth Skinning

Smooth deformations are provided by enabling several joints to influence the same deformable object points.  
The smoothing effects around joints are automatically set up when you [bind skin](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-8DBA9E62-3854-4348-A0AD-1F981ECEA54F).  
Maya offers three [methods](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-630C335C-B63E-4F2E-A4A4-AEA1DD00B0D6) to smooth skin a model:  

- Classic Linear
- Dual Quaternion
- Weight Blended (blend of both methods).

!!! The **Dual Quaternion** method better preserves the volume of the model when a joint is oriented.  

#### Edit Weights

You can precisly modify the values of individual vertices weights using the [Component Editor](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-B698CC5D-2771-488E-98E8-2D4E31DB3B2D).  
If you want to shape the deformation directly you can instead paint weights with the [Paint Skin Weights Tool](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-99189E9D-237F-471E-A02C-BE6593B4828B).