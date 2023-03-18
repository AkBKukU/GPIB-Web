function dmm_print(datad){
  console.log(datad);
  console.log("Does this work?");
  document.getElementById("red").textContent = datad.fetch;
}

function dmm_fetch(){
  fetch('/inst/dmm/fetch.json')
    .then((response) => response.json())
    .then((data) => dmm_print(data))
    .catch(Document.getElementById("red").textContent = "");
}

setInterval(dmm_fetch,2500)

startup_time="something"

function refresh_check(datar){
     if (startup_time == "something")
     {
       startup_time=datar.fetch
       return
     }

     if (startup_time != datar.fetch)
     {
       window.location.reload()
     }
}

function refresh_fetch(){
  fetch('/refresh/fetch.json')
    .then((response) => response.json())
    .then((data) => refresh_check(data))
}

setInterval(refresh_fetch,2500)
