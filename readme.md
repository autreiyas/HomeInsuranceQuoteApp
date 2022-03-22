# Online Home Insurance Quote App

## Description

A Flask application that takes in customer requests containing customer home insurance request data and returns quote premiums. The Quote API supports both JSON format and URL-Encoded form data.

**Screenshots:**

![screenshot 1](../screen1.png)

![screenshot 2](../screen2.png)

# Example

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
    "result": "1393"
}
```
