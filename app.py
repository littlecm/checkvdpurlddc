import streamlit as st
import requests
from urllib.parse import urlparse

# Function to check if the response has a redirect indicating a missing page
def has_redirect_to_missing_vdp(response):
    if response.history:
        for resp in response.history:
            if "redirectFromMissingVDP=true" in urlparse(resp.url).query:
                return True
    return "redirectFromMissingVDP=true" in urlparse(response.url).query

# Retrieve query parameters for 'domain' and 'VIN'
query_params = st.experimental_get_query_params()
domain = query_params.get("domain", [""])[0]
vin = query_params.get("vin", [""])[0]

if domain and vin:
    # Construct the URL using the domain and VIN from query parameters
    url = f"https://{domain}.com/catcher.esl?vin={vin}"

    try:
        # Make the HTTP request while allowing redirects
        response = requests.get(url, allow_redirects=True)

        # Check if the response has a redirect to a missing page
        if has_redirect_to_missing_vdp(response):
            st.error("ERROR: Redirected to a missing page.")
        else:
            st.success("Success: No redirect to a missing page detected.")
    except Exception as e:
        st.error(f"Failed to make request: {e}")
else:
    st.write("Please provide both domain and VIN in the query parameters.")
