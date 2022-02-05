//const { default: axios } = require("axios");
//import axios from "axios";
function input() {
    var p_name = document.getElementById("prodname").value;
    localStorage.setItem("Pname",p_name);

    var qnt = document.getElementById("quant").value;
    localStorage.setItem("Quan",qnt)
    
    var man = document.getElementById("manufact").value;
    localStorage.setItem("manuf",man)

    var supli = document.getElementById("supp").value;
    localStorage.setItem("suppl",supli)

    var amunt = document.getElementById("price").value;
    localStorage.setItem("amnt",amunt)
     
     var details = {'Product_name': p_name, 'Quantity': qnt, 'Manufacturer': man, 'Supplier': supli, 'Amount': amunt}
     console.log(details)
    // axios.get('https://127.0.0.1:5000/chain').then(response => {
    //     console.log(response.data);
    // }).catch(error => console.error(error));
}