### DevBoost
It is a collection of helper modules that I frequently use during development. Feel free to take reference from any of them.

Modules:
* [self_rate_limiter](https://github.com/vibing-onion/devBoost/tree/master#self_rate_limiter)
* [alt_yfinance](https://github.com/vibing-onion/devBoost/tree/master#alt_yfinance)

### self_rate_limiter
A rate-limit control during parallel programming with multiprocessing. The purpose is to optimize concurrency without violating rate-limit policies of API which might result in banning of IP.

function:
* rate_limited_multiprocessing(func, feed, rate_limit_per_second = 1)
  * func : the function you want to run concurrently
  * feed : a list of dictionary, where each dictionary is the **ONLY** function parameter
  * rate_limit_per_second : (theoretically) the maximum rate of the concurrency, the actual one should be lower. Default : 1 time per second

### alt_yfinance
A replacement module of yfinance, due to occasional breakdown of the library (currently only available for historical single ticker price)

function(s):
* yf_download_alt(ticker, start, end, column = ['Close'])
  * ticker : the ticker / symbol of the stock used by yahoo finance
  * start : starting date in string, in the format of YYYY-MM-DD
  * end : ending date in string, in the format of YYYY-MM-DD
  * column : the features to be returned, including (Open, High, Low, Close, Volume). Default : Only Close