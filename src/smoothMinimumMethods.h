#include <tuple>
#include <xtensor/xarray.hpp>

std::tuple<double, xt::xarray<double>, xt::xarray<double>>
getSmoothMinimumLocalDerivatives(const double rho, const xt::xarray<double>& h);

std::tuple<double, xt::xarray<double>, xt::xarray<double>> 
getSmoothMinimumGradientAndHessian(const double rho, const xt::xarray<double>& h,
const xt::xarray<double>& h_dx, const xt::xarray<double>& h_dxdx);