---
title: Skeleton
---

Building a [skeleton](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-906B71D3-C153-4880-A8EF-F9A6D1AE4AD5) is the process of placing and orienting joints to create a system with which you can pose a deformable object.  
If you are creating a skeleton for a human biped, you would place joints at all the major points of articulation in its model. (shoulders, knees, elbows, spine and so on)  
The [skeleton hierarchy](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-DC88B9A7-593B-427E-9BED-4D7822B0E0B6) is composed of a series of joints and joints chains with hierarchical relationships.  

___
### Joints

[Joints](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-1B59334F-2605-44C3-B584-A55B239A2CBE) are the building blocks of skeletons and their points of articulation. Each joint can have one or more bone attached to it, and more than one child joint.  
Bones are only visual cues that illustrate the relationships between joints.  

!!! Joints are specific nodes without shape, they can't be rendered but are displayed in the viewport by the bones (visual helpers).  

A [joint chain](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-267B988F-4E21-4963-BF6A-478E5F6FEF81) is any group of joints and their bones connected in a series.  
The joint chain begins at the highest joint in the chain’s hierarchy, and its bones are drawn pointing down the chain.  

! You can't create a mirrored duplicate of a joint chain with a scale of -1. Instead, use the mirror joint tool in the main menu **Skeleton** -> **Mirror Joint**.  

___
### Solvers


