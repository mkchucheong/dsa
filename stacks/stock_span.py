'''
problem:
The stock span problem is a financial problem where 
we have a series of n daily price quotes for a stock
and we need to calculate the span of stocks price 
for all n days. 

The span Si of the stocks price on a given day i is 
defined as the maximum number of consecutive days just
before the given day, for which the price of the stock
on the current day is less than or equal to its price
on the given day.

For example, if an array of 7 days prices is given as 
{100, 80, 60, 70, 60, 75, 85}, then the span values 
for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.

approach:
can use a stack here. why?
- just need to maintain a sense of "at what index is an 
earlier price higher than my current price?"
- so we dont need to maintain a full array
- this way we can simplify calculations and keep it O(n)


'''

def stock_span(prices):
    span = [0]
    out_arr = [1]

    for i in range(1, len(prices)):

        while (len(span)>0) and (prices[i] >= prices[span[-1]]):
            span.pop()
        
        if len(span) > 0:
            out_arr.append(i - span[-1])
        else:
            out_arr.append(i+1)
        span.append(i)
    
    return out_arr

if __name__ == "__main__":
    stock_prices = [100, 80, 60, 70, 60, 75, 85]
    print(stock_span(stock_prices))

    stock_prices = [100, 100, 100]
    print(stock_span(stock_prices))