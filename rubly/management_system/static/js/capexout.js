const searchField = document.querySelector(".search_input");
const mytable=document.getElementById("mytable");
display()
console.log(sessionStorage.length)
console.log(searchField);
searchField.addEventListener("keyup", (event) => {
  const search = event.target.value;
  const table = document.querySelector(".ul-table");
  table.innerHTML = "";
  console.log(search);
  if (search != " " && search.length > 0) {
    fetch("/capexout", {
      method: "POST",
      body: JSON.stringify({ sku: search }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        console.log(data["search"]);
        skus = data["search"].length;
        table.innerHTML = "";
        const drop = document.querySelector(".rowadrop");
        drop.style.display = "flex";
        myElement=document.getElementById("hidden");
        for (let i = 0; i < skus; i++) {
          myElement.style.display="flex";
          let sku = data["search"][i];
          console.log(JSON.stringify(sku.Description));
          var id = sku.id;
          table.innerHTML +=
            '<li class = "list-table"onclick="myfunc(' +
            id +
            ')">' +
            sku.Description +
            "</li>";
        }

        // const table = document.querySelector('.capexout-table');
        // for (let i = 0; i < data.length; i++)
        //     table.innerHTML = '<p>${data.sku}</p>';
      });
  }
  else{
    myElement=document.getElementById("hidden");
    myElement.style.display="none";
  }
});
function myfunc(id) {
  var url = "dashboard?search=" + encodeURIComponent(id);
  window.location.href = url;
}
function myfunc1() {
  var url = "dashboard?search1=" + encodeURIComponent(searchField.value);
  window.location.href = url;
}
function myfunc2(id,des,max) {
  var amount=document.getElementById(id).value;
  if(amount<1){
    alert("Please enter a Valid amount");
    return false;
  }
  else if(parseInt(amount)>parseInt(max)){
    alert("The amount exceeds available amount");
    return false;
  }
// Function to add elements to session storage

  // Retrieve the existing data from session storage
  const existingData = sessionStorage.getItem(id);
  if(existingData){
    sessionStorage.removeItem(id);
  }

  // Parse the existing data (if any) as an array or create an empty array if no data exists
  const dataArray = [];

  // Append the new value to the array
  dataArray.push(id,amount,des);

  // Convert the updated array back to a JSON string and store it in session storage
  sessionStorage.setItem(id, dataArray);
  mytable.innerHTML='';
  display();

  // Function to get all data from session storage

 // Return the object containing all session storage data
}
 function display(){
  // Iterate over each key in sessionStorage
  for (let i = 0; i < sessionStorage.length; i++) {
    const key = sessionStorage.key(i);
    const array = sessionStorage.getItem(key);
    const value=array.split(",");
    var myrow=document.createElement('tr');
    mytable.appendChild(myrow);
    var des=value[2];
    var d=document.createElement('td');
    d.textContent = des;
    myrow.appendChild(d);
    var a=document.createElement('td');
    a.textContent=value[1];
    myrow.appendChild(a);
    var b=document.createElement('td');
    myrow.appendChild(b)
    var bu=document.createElement('button');
    bu.textContent="delete";
    bu.addEventListener('click', function() {
      var arg1 = key; // Replace this with your desired argument
      myfunc3(arg1);
    });
    b.appendChild(bu);
        }
    }
    function myfunc3(key){
      sessionStorage.removeItem(key);
      mytable.innerHTML='';
      display()
    } 
    function clearall(){
      sessionStorage.clear();
      mytable.innerHTML='';
    }
    function checkout(){
      const myarray=[];
      for(let i=0;i<sessionStorage.length;i++){
        var key=sessionStorage.key(i);
        var array=sessionStorage.getItem(key);
        const value=array.split(",");
        value.pop()
        myarray.push(value[0],value[1]);
      }
      var capex=document.getElementById('capex').value;
      if(capex!=''){
      var url = 'order/?array='+encodeURIComponent(myarray)+'&capex=' + encodeURIComponent(capex);

      var xhr = new XMLHttpRequest();
      xhr.open('GET', url, true);
      xhr.onload = function() {
        if (xhr.status === 200) {
          var options = JSON.parse(xhr.responseText);
          console.log(options);
          if(options.date==="Successfull") {
            clearall();
            var url = "dashboard" ;
            window.location.href = url;
          }
          else if(options.date==="Capex not found"){
            alert(options.date);
          }         
        }
      };
    
      xhr.send();
    }
    else{
     
      var url = 'order/?array='+encodeURIComponent(myarray);

      var xhr = new XMLHttpRequest();
      xhr.open('GET', url, true);
      xhr.onload = function() {
        if (xhr.status === 200) {
          var options = JSON.parse(xhr.responseText);
          if(options.date==="Successfull") {
            clearall();
            var url = "dashboard" ;
            window.location.href = url;
          } 
          else {
            alert("An Error Occured")
          }    
        }
      };
    
      xhr.send();
    }
  }
  function hide(){
    var elem = document.getElementById("hide");
    elem.remove();
    var elem2=document.getElementById("layout-navbar");
    elem2.remove();
  }
  





