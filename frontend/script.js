async function ask(){

let q = document.getElementById("question").value

let res = await fetch(`http://127.0.0.1:8000/chat?q=${q}`)

let data = await res.json()

document.getElementById("response").innerText = data.response

}