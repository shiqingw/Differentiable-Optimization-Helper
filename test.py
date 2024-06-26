import numpy as np
import diffOptHelper as doh

# a = np.array([1., 2., 3.])
# b = np.array([4., 5., 6.])

# print(doh.getDualVariable(a,b))

h = np.array([1., 2., 3.])
rho = 10.0
F, F_dh, F_dhdh = doh.getSmoothMinimumLocalDerivatives(rho, h)
h_dx = np.random.rand(len(h),6)
h_dxdx = np.random.rand(len(h),6,6)
h_dxdx = np.transpose(h_dxdx, (0,2,1)) + h_dxdx

F, F_dx, F_dxdx = doh.getSmoothMinimumGradientAndHessian(rho, h, h_dx, h_dxdx)
print(F_dx - F_dh @ h_dx)
print(F_dxdx - (np.einsum('i,ijk->jk', F_dh, h_dxdx) + h_dx.T @ F_dhdh @ h_dx))
