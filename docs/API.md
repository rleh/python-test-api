# Test Api Documentation

## Resources

### Api Info

Get api info

    GET /info


#### Parameters

| Name  | Type    | Description |
|-------|---------|-------------|
| None   |  |  |


#### Response

Status `200 OK`

```
{
  "author": "Raphael Lehmann",
  "info": "This ist the ApiInfo from api"
}
```


### The Answer

Get answer to life, the universe and everything

    GET /answer


#### Parameters

*None*


#### Response

Status `200 OK`

```
{
  "answer": 42
}
```
