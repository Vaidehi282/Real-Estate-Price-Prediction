const URL = 'http://127.0.0.1:5001/'
const dropdown_location = document.querySelector('.location')
const submit_button = document.querySelector('form button')
const bhk_field = document.getElementsByName("bhk")
const bath_field = document.getElementsByName("bath")
const price = document.querySelector(".estimated-price")

func_dropdown = async () => {
    try {
        const location_url = URL + 'get_locations'
        let response = await fetch(location_url)
        if (!response.ok) {
            console.log("HTTP error")
        }
        let data = await response.json()
        dropdown_location.innerText = ""
        for (let loc of data.locations) {
            let newOption = document.createElement("option");
            newOption.innerText = loc
            newOption.value = loc
            dropdown_location.append(newOption)
        }
    }
    catch (e) {
        console.log("Error: ", e)
    }

}
func_dropdown()


const getBath = () => {
    for (let i in bath_field) {
        if (bath_field[i].checked) {
            return parseInt(i) + 1
        }
    }
    return -1
}
const getBhk = () => {
    for (let i in bhk_field) {
        if (bhk_field[i].checked) {
            return parseInt(i) + 1
        }
    }
    return -1
}

const predictPrice = async () => {
    let sqft = document.querySelector("#area").value
    let bhk = getBhk()
    let bath = getBath()
    let location = dropdown_location.value

    const data = {
        total_sqft: parseFloat(sqft),
        location: location,
        bhk: bhk,
        bath: bath
    };
    const price_url = URL + 'predict_home_price'
    let response = await fetch(price_url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        console.log("HTTP error")
    }
    const result = await response.json()
    console.log(result)
    price.innerHTML = '<h2>' + result.price + " Lakh" + '</h2>'
}

submit_button.addEventListener('click', (e) => {
    e.preventDefault()
    predictPrice()
})