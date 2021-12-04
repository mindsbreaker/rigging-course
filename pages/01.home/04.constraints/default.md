---
title: Constraints
media_order: 'MaintainOffset.png,CycleWarning.jpg'
---

With [constraints](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-FA047B7D-41AD-4643-9D10-BB1F3B397B4D), you can drive the position, orientation, and scale of one object with the transformations of another object.  
The object that is driven is called the **`Constrained`** or **`Child`** object, and the driver object is called the **`Target`** or **`Parent`** object.  
When a constraint relationship has more than one target object, weights attributes are used to determine the amount of influence.  

An object with a parent constraint does not behave the same as an object with a point and orient constraint.  
When a [Parent](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-29785337-D109-48C5-AFC4-8A7A1D0C246F) constraint is used, rotating the target object(s) affects the constrained object’s rotation along the **world** axis.  
When a [Point](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-79F8E9DC-72B9-4465-8D77-8A69F61D313A) and [Orient](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-ABED0435-54C5-44BE-9E1B-9A2975133695) constraint are used, rotating the target object(s) affects the constrained object’s rotation along its **local** axis.  

!!! To keep offset in the world between constrained & target objects, check the **Maintain Offset** parameter in the constraint option box.  
!!!  (checked by default) <img src="constraints/MaintainOffset.png" style="float:left;margin:5px 5px">

! An object can't be constrained to one of it's children, otherwise you'd get a cycle.  
! .<img src="constraints/CycleWarning.jpg" style="float:left;margin:5px 0px">