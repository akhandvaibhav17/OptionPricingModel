import numpy as np
import math
import streamlit as st

def main():

    st.title("N-Period Option Pricing Model")

    S=st.number_input("Enter Asset Price",step=0.01)
    X=st.number_input("Enter Strike Price",step=0.01)
    r=st.number_input("Enter Risk Free Rate of Return",step=0.01)/100
    u=st.number_input("Enter Forwarding Factor",step=0.01)
    d=st.number_input("Enter Backwarding Factor",step=0.01)
    n=st.number_input("Enter Numbe of Periods",step=1)
    if st.button("Calculate"):
        result = calculation(S,X,r,u,d,n)
        st.success(f"The Call Option Price at T=0 is {result}")

def calculation(S,X,r,u,d,n):

    p = round((1+r-d)/(u-d),4)

    asset_prices = []
    for i in range(n+1):
        prices = []
        for k in range(i+1):
            price = round(S*math.pow(u,i-k)*math.pow(d,k),4)
            prices.append(price)
        asset_prices.append(prices)


    call_prices = []
    price = []
    for i in range(len(asset_prices[-1])):
        price.append(max(0,asset_prices[-1][i]-X))
    call_prices.append(price)

    for i in reversed(range(n)):
        prices = []
        for j in range(i+1):
            i1 = round(p*call_prices[-1][j],4)
            i2 = round((1-p)*call_prices[-1][j+1],4)
            i3 = round(i1+i2,4)
            i4 = round(i3/(1+r),4)
            i5 = round(i4,4)
            prices.append(i5)
        call_prices.append(prices)

    return call_prices[-1][-1]
    

if __name__ == "__main__":
    main()


