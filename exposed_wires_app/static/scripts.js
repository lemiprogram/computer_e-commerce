function fetch_data(url){
    return  fetch(url)
            .then(res=>res)
}

async function get_products(){
    res = await fetch_data("http://127.0.0.1:8000/api/products/get")
    data = await res.then(data=>data)
    return data
}
console.log(get_products())