var fill_gender = document.getElementById("gender");
var fill_from = document.getElementById("age-from");
var fill_to = document.getElementById("age-to");


function fillter() {
    let xmlhttp = new XMLHttpRequest();
    var response;
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);
            let content = document.getElementById('persons');
            content.innerHTML = '';
            response.forEach(element => {
                content.innerHTML += '<a href="person/' + element['pk'] +'"><article class="person"><header class="person-header">' +
                element['fields']['first_name'] + ' ' + element['fields']['last_name'] +
                '</header> <img src="media/' + element['fields']['photo'] + '"></article ></a>' ;
            });
            
        }
    };
    let params = {};
    if (!gender.value == '') params['gender'] = fill_gender.value;
    if (!fill_from.value == '') params['fill_to'] =  fill_to.value;
    if (!fill_to.value == '') params['fill_from'] =  fill_from.value;
    const parsedParams = formatParams(params);
    console.log(parsedParams)
    console.log(params)
    xmlhttp.open("GET", 'http://localhost:8000/api/get_persons?' + parsedParams, true);
    xmlhttp.send();
    
}

gender.addEventListener('change', fillter);
fill_from.addEventListener('change', fillter);
fill_to.addEventListener('change', fillter);

function formatParams( params ){
  return "?" + Object
        .keys(params)
        .map(function(key){
          return key+"="+encodeURIComponent(params[key])
        })
        .join("&")
}