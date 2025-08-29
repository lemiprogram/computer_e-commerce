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

async function get_products(my_func){
    data = await get_data("http://127.0.0.1:8000/api/products/get")
    my_func(data)
}
function getPrice(priceStr,discount){
    price = parseFloat(priceStr)
    return price * (1-(discount /100))
}