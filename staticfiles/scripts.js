async function get_data(url){
    return  await fetch(url)
            .then(res=>res.json())
            .then(data=>data)
}
async function post_data(url,postData){
    return  await fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(postData)
    })
            .then(res=>res.json())
            .then(data=>data)
}

const get_Categories_all_url = "http://127.0.0.1:8000/api/get_Categories/all"
const get_Conditions_all_url = "http://127.0.0.1:8000/api/get_Conditions/all"
const get_Stores_all_url = "http://127.0.0.1:8000/api/get_Stores/all"
const get_Shoppers_all_url = "http://127.0.0.1:8000/api/get_Shoppers/all"
const get_Sellers_all_url = "http://127.0.0.1:8000/api/get_Sellers/all"
const get_Orders_all_url = "http://127.0.0.1:8000/api/get_Orders/all"
const get_Carts_all_url = "http://127.0.0.1:8000/api/get_Carts/all"
const get_CartItems_all_url = "http://127.0.0.1:8000/api/get_CartItems/all"
const get_Wishlists_all_url = "http://127.0.0.1:8000/api/get_Wishlists/all"


function getPrice(priceStr,discount){
    price = parseFloat(priceStr)
    return price * (1-(discount /100))
}