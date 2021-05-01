# camera_calibration

The process of estimating the parameters of a camera is called camera calibration

This means we have all the information (parameters or coefficients) about the camera required to determine an accurate relationship between a 3D point in the real world and its corresponding 2D projection (pixel) in the image captured by that calibrated camera.

The equations that relate 3D point <img src="https://render.githubusercontent.com/render/math?math=(X_w, Y_w, Z_w)">
 in world coordinates to its projection (u, v) in the image coordinates are shown below:
 



<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}u'  \\v' \\z'  \end{bmatrix}= P "><img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix} X_{w} \\ Y_w \\ Z_w \\ 1 \end{bmatrix}">


<img src="https://render.githubusercontent.com/render/math?math=u=\frac{u'}{w'} \, \,\, \, , \,\, v=\frac{v'}{w'} ">

<img src="https://render.githubusercontent.com/render/math?math=P=K\, \, \times \,\,[R\,|\,t]">

Distortioncoefficients=(k1 , k2 , p1 , p2 , k3)


and k is 3*3 calibration matrix .

Inputs : A collection of images with points whose 2D image coordinates and 3D world coordinates are known.

Outputs: The 3×3 camera calibration matrix , radial distortion coefficients of the lens


