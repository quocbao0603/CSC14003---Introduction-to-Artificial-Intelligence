import utils

def unify(x, y, theta):
   if theta is False:
      return False
   if x == y:
      return theta
   if utils.is_variable(x):
      return unify_var(x, y, theta)
   if utils.is_variable(y):
      return unify_var(y, x, theta)
   if utils.is_compound(x) and utils.is_compound(y):
      return unify(x.get_arguments(), y.get_arguments(), unify(x.get_functor(), y.get_functor(), theta))
   if utils.is_list(x) and utils.is_list(y) and len(x) == len(y):
      return unify(x[1:], y[1:], unify(x[0], y[0], theta))
   return False

def unify_var(var, x, theta):
   if theta.contains(var):
      return unify(theta.substitute_of(var), x, theta)
   if theta.contains(x):
      return unify(var, theta.substitute_of(x), theta)
   theta.add(var, x)
   return theta

