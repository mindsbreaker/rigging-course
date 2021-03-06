---
title: Constraints
media_order: 'MaintainOffset.png,CycleWarning.jpg'
---

With [constraints](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-FA047B7D-41AD-4643-9D10-BB1F3B397B4D), you can drive the position, orientation, and scale of one object with the transformations of another object.  
The object that is driven is called the **`Constrained`** or **`Child`** object, and the driver object is called the **`Target`** or **`Parent`** object.  
When a constraint relationship has more than one target object, weights attributes are used to determine the amount of influence.  

!!! To keep offset in the world between constrained & target objects, check the **Maintain Offset** parameter in the constraint option box.  
!!!  (checked by default) <img src="constraints/MaintainOffset.png" style="float:left;margin:5px 5px">

! An object can't be constrained to one of it's children, otherwise you'd get a cycle.  
! .<img src="constraints/CycleWarning.jpg" style="float:left;margin:5px 0px">

___
### Main Constraints

- **Point** --> Point constraints limit and control only the translation channels of the constrained object.
- **Orient** --> Orient constraints limit and control only the rotation channels of the constrained object.
- **Parent** --> Parent constraints cause the constrained object to inherit the transformations and global orientation of its target objects, mimicking a parent-child relationship.
- **Scale** --> Scale constraints limit and control the scaling channels of the constrained object. 
- **Aim** --> Aim constraints limit and control the rotation channels and aim vector of the constrained object.

!!! An object with a [**Parent**](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-29785337-D109-48C5-AFC4-8A7A1D0C246F) constraint does not behave the same as an object with a [**Point**](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-79F8E9DC-72B9-4465-8D77-8A69F61D313A) and [**Orient**](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=GUID-ABED0435-54C5-44BE-9E1B-9A2975133695) constraints.  

___
### Pin Constraints
- **Proximity Pin** --> The proximityPin node outputs positions by calculating the closest point on a surface to a given world position.
- **UV Pin** --> Similar to proximityPin, but uses input UV coordinates to calculate and output positions.
- **Rivet** --> Rivet is a command that quickly creates uvPin node using common settings.