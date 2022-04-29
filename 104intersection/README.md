# 104intersection

To create synthesis images (when doing ray tracing, for example), potential intersection points betweenlight rays and scene objects (here cylinders, spheres and cones) must be computed.

This algorithm allow you to compute those points for a sphere, a cylinder and a cone.

- USAGE :
    * ./104intersection opt xp yp zp xv yv zv p

- DESCRIPTION :
    * opt surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone
    * (xp, yp, zp) coordinates of a point by which the light ray passes through
    * (xv, yv, zv) coordinates of a vector parallel to the light ray
    * parameter: radius of the sphere, radius of the cylinder, or angle formed by the cone and the Z-axis


## Testing the algorithm

In order to test the algorithm please use  
> sh test.sh