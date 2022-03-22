# Home Insurance Quote App

## Description

A Flask application that takes in requests containing customer home insurance data and returns quote premiums. The Quote API supports both JSON format and URL-Encoded form data.

## Requirements

- Flask >= 2.0.2
- NumPy

## How to run the application

Build a docker image using the provided dockerfile or run the app inside a virtual environment using the provided "flaskup" script.

## Screenshots

![screenshot 1](/screen1.png)

![screenshot 2](/screen2.png)

## JSON Example

**Request**:

```
{
    "CustomerID": 1,
    "DwellingCoverage": 300200,
    "HomeAge": 108,
    "RoofType": "Tin",
    "NumberOfUnits": 4,
    "PartnerDiscount": "Y"
}
```

**Response**:

```
{
    "FinalQuotedPremiumAmount": 1393
}
```
