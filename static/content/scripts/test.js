function dmm_print(data){
  console.log(data);
  console.log("Does this work?");
  document.getElementById("red").textContent = data.fetch;
}

function dmm_fetch(){
  fetch('/inst/dmm/fetch.json')
    .then((response) => response.json())
    .then((data) => dmm_print(data))
    .catch(Document.getElementById("red").textContent = "");
}

setInterval(dmm_fetch,2500)
