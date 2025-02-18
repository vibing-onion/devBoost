### DevBoost
It is a collection of helper modules that I frequently use during development. Feel free to take reference from any of them.

Modules:
[self_rate_limiter](https://github.com/vibing-onion/devBoost/tree/master#self_rate_limiter)

### self_rate_limiter
function:
* rate_limited_multiprocessing(func, feed, rate_limit_per_second = 1)
  * func : the function you want to run concurrently
  * feed : a list of dictionary, where each dictionary is the **ONLY** function parameter
  * rate_limit_per_second : (theoretically) the maximum rate of the concurrency, the actual one should be lower. Default : 1 time per second
