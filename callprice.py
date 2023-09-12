import numpy as np
import math
import streamlit as st

def main():

    st.title("N-Period Option Pricing Model")

    # Create a radio button widget with two options
    selected_option = st.radio("Select an option", ["Call Price", "Put Price"])

    # Display the selected option
    if selected_option == "Call Price":
        st.write("")
    else:
        st.write("")

    S=st.number_input("Enter Asset Price",step=0.0001,format="%.4f")
    X=st.number_input("Enter Strike Price",step=0.0001,format="%.4f")
    r=st.number_input("Enter Risk Free Rate of Return",step=0.0001,format="%.4f")/100
    u=st.number_input("Enter Forwarding Factor",step=0.01,format="%.2f")
    d=st.number_input("Enter Backwarding Factor",step=0.01,format="%.2f")
    n=st.number_input("Enter Number of Periods",step=1,)
    if st.button("Calculate"):
        if selected_option == "Call Price":
            result = calculationCall(S,X,r,u,d,n)
            st.success(f"The Call Option Price at T=0 is {result}")
        else:
            result = calculationPut(S,X,r,u,d,n)
            st.success(f"The Put Option Price at T=0 is {result}")

def calculationCall(S,X,r,u,d,n):

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


def calculationPut(S,X,r,u,d,n):

    p = round((1+r-d)/(u-d),4)

    asset_prices = []
    for i in range(n+1):
        prices = []
        for k in range(i+1):
            price = round(S*math.pow(u,i-k)*math.pow(d,k),4)
            prices.append(price)
        asset_prices.append(prices)


    put_prices = []
    price = []
    for i in range(len(asset_prices[-1])):
        price.append(max(0,X-asset_prices[-1][i]))
    put_prices.append(price)

    for i in reversed(range(n)):            
        prices = []
        for j in range(i+1):
            i1 = round(p*put_prices[-1][j],4)
            i2 = round((1-p)*put_prices[-1][j+1],4)
            i3 = round(i1+i2,4)
            i4 = round(i3/(1+r),4)
            i5 = round(i4,4)
            prices.append(i5)
        put_prices.append(prices)

    return put_prices[-1][-1]


if __name__ == "__main__":
    main()


