import streamlit as st
import requests

# Retrieve query parameters for 'domain' and 'VIN'
query_params = st.experimental_get_query_params()
domain = query_params.get("domain", [""])[0]
vin = query_params.get("vin", [""])[0]

if domain and vin:
    # Construct the URL using the domain and VIN from query parameters
    url = f"https://{domain}.com/catcher.esl?vin={vin}"

    try:
        # Make the HTTP request
        response = requests.get(url)

        # Check if the response contains the specific string
        if "redirectFromMissingVDP=true" in response.text:
            st.error("ERROR!")
        else:
            st.success("Success")
    except Exception as e:
        st.error(f"Failed to make request: {e}")
else:
    st.write("Please provide both domain and VIN in the query parameters.")

