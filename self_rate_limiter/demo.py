from rate_limiter import rate_limited_multiprocessing

### Please replace demo_func with your scraping function (or any functions you want to rate limit)
def demo_func(e):
    print(e)


### Please assign the list of items you want to pass to the function as inputList
if __name__ == "__main__":
    inputList = [{'a': i, 'b': i+1} for i in range(100)]
    rate_limited_multiprocessing(demo_func, inputList, rate_limit_per_second=10)